#!/usr/bin/env python3
"""
Scraper du guide de démo "Cisco Catalyst Center Instant Demo 3.2"
(https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/)
pour en faire une base de connaissances Markdown.

Le site est un MkDocs statique (thème windmill). Le script :
  1. crawle toutes les pages internes à partir de la page d'accueil (+ sitemap) ;
  2. extrait le contenu de l'article, le convertit en Markdown propre ;
  3. télécharge les images (optionnel) et réécrit les liens en local ;
  4. inventorie tous les liens (internes, externes, dCloud, images) ;
  5. produit :
       output/pages/<section>/<page>.md   une page = un fichier, avec front-matter
       output/knowledge_base.md           tout le guide dans un seul fichier, ordonné
       output/chunks.jsonl                découpage par section (h2) pour RAG / embeddings
       output/links.csv                   inventaire de tous les liens trouvés
       output/index.md                    sommaire
       output/images/...                  captures d'écran (si --images)

Usage :
  .venv/bin/python scrape.py                 # texte + liens
  .venv/bin/python scrape.py --images        # + téléchargement des captures
  .venv/bin/python scrape.py --out autre_dir --delay 0.2
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import time
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urljoin, urldefrag, urlparse

import requests
import truststore
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

BASE_URL = "https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/"
USER_AGENT = "Mozilla/5.0 (KB scraper; demo-guide archival)"
truststore.inject_into_ssl()  # utilise le trousseau macOS/Windows (proxy d'entreprise)

ASSET_DIRS = ("css/", "js/", "img/", "fonts/", "assets/", "search/")


@dataclass
class Page:
    url: str
    rel: str  # chemin relatif au BASE_URL, ex. "assurance/ai-issues/"
    title: str = ""
    section: str = ""
    markdown: str = ""
    headings: list[tuple[int, str, str]] = field(default_factory=list)  # (niveau, texte, ancre)
    links: list[dict] = field(default_factory=list)
    images: list[str] = field(default_factory=list)


# --------------------------------------------------------------------------- utils

def session() -> requests.Session:
    s = requests.Session()
    s.headers["User-Agent"] = USER_AGENT
    return s


def get(s: requests.Session, url: str, delay: float, retries: int = 3) -> requests.Response | None:
    for attempt in range(retries):
        try:
            r = s.get(url, timeout=30)
            time.sleep(delay)
            if r.status_code == 200:
                r.encoding = "utf-8"  # le serveur n'annonce pas le charset
                return r
            if r.status_code == 404:
                return None
        except requests.RequestException as e:
            print(f"  ! {url}: {e}")
        time.sleep(1 + attempt * 2)
    return None


def is_internal_page(url: str) -> bool:
    if not url.startswith(BASE_URL):
        return False
    rel = url[len(BASE_URL):]
    if rel.startswith(ASSET_DIRS):
        return False
    last = rel.rstrip("/").rsplit("/", 1)[-1]
    # pages MkDocs = dossiers "xxx/" ou .html ; on ignore les fichiers binaires
    return rel == "" or rel.endswith("/") or rel.endswith(".html") or "." not in last


def normalize(url: str) -> str:
    url, _ = urldefrag(url)
    url = url.split("?")[0]
    if url.endswith("index.html"):
        url = url[: -len("index.html")]
    return url


def classify(href: str) -> str:
    host = urlparse(href).netloc
    if href.startswith("mailto:"):
        return "mailto"
    if href.startswith(BASE_URL):
        return "internal"
    if "dcloud" in host and "cisco.com" in host:
        return "dcloud-demo-ui"  # liens directs vers l'UI Catalyst Center de la démo
    if host.endswith("cisco.com"):
        return "cisco"
    return "external"


def slug_path(rel: str) -> Path:
    rel = rel.strip("/")
    if not rel:
        return Path("index.md")
    if rel.endswith(".html"):
        rel = rel[:-5]
    return Path(rel + ".md")


# ------------------------------------------------------------------ html -> markdown

class KBConverter(MarkdownConverter):
    """Markdownify avec gestion des admonitions MkDocs et des blocs de code."""

    def convert_div(self, el, text, *args, **kwargs):
        classes = el.get("class") or []
        if "admonition" in classes:
            kind = next((c for c in classes if c != "admonition"), "note")
            body = "\n".join(f"> {line}" if line else ">" for line in text.strip().splitlines())
            return f"\n\n> **[{kind.upper()}]**\n{body}\n\n"
        return text

    def convert_p(self, el, text, *args, **kwargs):
        if "admonition-title" in (el.get("class") or []):
            return f"**{text.strip()}**\n\n"
        return super().convert_p(el, text, *args, **kwargs)


def to_markdown(html: str) -> str:
    md = KBConverter(heading_style="ATX", bullets="-", code_language_callback=lambda el: (
        next((c.replace("language-", "") for c in (el.get("class") or []) if c.startswith("language-")), "")
    )).convert(html)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


# ---------------------------------------------------------------------- extraction

def extract(page: Page, html: str) -> list[str]:
    """Remplit `page` et renvoie les URLs internes découvertes."""
    soup = BeautifulSoup(html, "html.parser")
    discovered: list[str] = []

    # Navigation latérale : sert à la découverte ET à connaître la section
    for a in soup.select("a[href]"):
        absu = normalize(urljoin(page.url, a["href"]))
        if is_internal_page(absu):
            discovered.append(absu)

    content = soup.select_one("div.wm-page-content")
    if content is None:
        content = soup.body or soup
    # retire les boutons Précédent / Suivant et les ancres ¶
    for n in content.select(".wm-article-nav-buttons, a.headerlink, script, style"):
        n.decompose()

    h1 = content.find("h1")
    page.title = h1.get_text(strip=True) if h1 else (soup.title.get_text(strip=True) if soup.title else page.rel)
    page.title = re.sub(r"\s+-\s+Cisco Catalyst Center Instant Demo.*$", "", page.title)
    page.section = page.rel.split("/")[0] if "/" in page.rel.strip("/") else "home"

    for h in content.find_all(re.compile(r"^h[1-6]$")):
        page.headings.append((int(h.name[1]), h.get_text(" ", strip=True), h.get("id", "")))

    # liens et images, avec URL absolue
    for a in content.find_all("a", href=True):
        href = a["href"]
        if href.startswith("#"):
            continue
        absu = urljoin(page.url, href)
        page.links.append({
            "page": page.url,
            "page_title": page.title,
            "text": a.get_text(" ", strip=True),
            "url": absu,
            "type": classify(absu),
        })
        a["href"] = absu
    for img in content.find_all("img", src=True):
        absu = urljoin(page.url, img["src"])
        page.images.append(absu)
        img["src"] = absu
        if not img.get("alt"):
            img["alt"] = Path(urlparse(absu).path).stem

    page.markdown = to_markdown(str(content))
    return discovered


def sitemap_urls(s: requests.Session, delay: float) -> list[str]:
    r = get(s, BASE_URL + "sitemap.xml", delay)
    if not r:
        return []
    locs = re.findall(r"<loc>\s*([^<]+?)\s*</loc>", r.text)
    out = []
    for loc in locs:
        # le sitemap MkDocs pointe souvent vers http://0.0.0.0:8000/... -> on remappe
        path = urlparse(loc).path.lstrip("/")
        base_path = urlparse(BASE_URL).path.lstrip("/")
        if path.startswith(base_path):
            path = path[len(base_path):]
        out.append(normalize(urljoin(BASE_URL, path)))
    return out


# --------------------------------------------------------------------------- crawl

def crawl(delay: float) -> tuple[list[Page], list[str]]:
    s = session()
    queue: deque[str] = deque([BASE_URL])
    for u in sitemap_urls(s, delay):
        queue.append(u)
    seen: set[str] = set()
    order: list[str] = []  # ordre de découverte = ordre de la navigation MkDocs
    pages: dict[str, Page] = {}
    failed: list[str] = []

    while queue:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)
        r = get(s, url, delay)
        if r is None or "text/html" not in r.headers.get("content-type", ""):
            failed.append(url)
            continue
        page = Page(url=url, rel=url[len(BASE_URL):])
        found = extract(page, r.text)
        pages[url] = page
        order.append(url)
        print(f"[{len(pages):3}] {page.rel or '/':45} {page.title}")
        for u in found:
            if u not in seen:
                queue.append(u)

    # ordre final : celui de la nav de la home (liens dans l'ordre d'apparition)
    home = BeautifulSoup(get(s, BASE_URL, delay).text, "html.parser")
    nav_order = []
    for a in home.select("a[href]"):
        u = normalize(urljoin(BASE_URL, a["href"]))
        if u in pages and u not in nav_order:
            nav_order.append(u)
    nav_order = [BASE_URL] + [u for u in nav_order if u != BASE_URL]
    nav_order += [u for u in order if u not in nav_order]
    return [pages[u] for u in nav_order], failed


# ------------------------------------------------------------------------- outputs

def download_images(pages: list[Page], out: Path, delay: float) -> dict[str, str]:
    s = session()
    mapping: dict[str, str] = {}
    all_imgs = sorted({i for p in pages for i in p.images if i.startswith(BASE_URL)})
    print(f"\nTéléchargement de {len(all_imgs)} images…")
    for n, url in enumerate(all_imgs, 1):
        local = out / "images" / url[len(BASE_URL):]
        if not local.exists():
            r = get(s, url, delay)
            if r is None:
                continue
            local.parent.mkdir(parents=True, exist_ok=True)
            local.write_bytes(r.content)
        mapping[url] = str(local.relative_to(out))
        if n % 50 == 0:
            print(f"  {n}/{len(all_imgs)}")
    return mapping


def rel_to(target: str, from_file: Path) -> str:
    depth = len(from_file.parent.parts)
    return "../" * depth + target


def split_chunks(page: Page) -> list[dict]:
    """Découpe une page en chunks par titre de niveau 2 (pour RAG)."""
    chunks, current, heading = [], [], page.title
    for line in page.markdown.splitlines():
        m = re.match(r"^(#{1,2})\s+(.*)", line)
        if m and current and any(l.strip() for l in current):
            chunks.append((heading, "\n".join(current).strip()))
            current = []
        if m:
            heading = m.group(2).strip()
        current.append(line)
    if current:
        chunks.append((heading, "\n".join(current).strip()))
    return [{
        "id": f"{page.rel.strip('/') or 'index'}#{i}",
        "url": page.url,
        "section": page.section,
        "page_title": page.title,
        "heading": h,
        "text": t,
    } for i, (h, t) in enumerate(chunks) if t]


def write_outputs(pages: list[Page], out: Path, img_map: dict[str, str], failed: list[str]) -> None:
    (out / "pages").mkdir(parents=True, exist_ok=True)

    def localize(md: str, md_file: Path) -> str:
        for remote, local in img_map.items():
            md = md.replace(f"]({remote}", f"]({rel_to(local, md_file)}")
        return md

    all_md = [
        "# Cisco Catalyst Center Instant Demo 3.2 — Base de connaissances\n",
        f"Source : {BASE_URL}  \nPages : {len(pages)}\n",
    ]
    index = ["# Sommaire\n", f"Source : {BASE_URL}\n"]
    chunks = []
    current_section = None

    for p in pages:
        md_rel = Path("pages") / slug_path(p.rel)
        md_file = out / md_rel
        md_file.parent.mkdir(parents=True, exist_ok=True)
        front = (
            "---\n"
            f"title: {json.dumps(p.title, ensure_ascii=False)}\n"
            f"section: {p.section}\n"
            f"source: {p.url}\n"
            f"images: {len(p.images)}\n"
            f"links: {len(p.links)}\n"
            "---\n\n"
        )
        md_file.write_text(front + localize(p.markdown, md_rel), encoding="utf-8")

        if p.section != current_section:
            current_section = p.section
            index.append(f"\n## {p.section.capitalize()}\n")
        index.append(f"- [{p.title}]({md_rel.as_posix()}) — <{p.url}>")

        # dans le fichier unique, on descend les titres d'un niveau
        body = re.sub(r"^(#{1,5}) ", r"#\1 ", localize(p.markdown, Path("knowledge_base.md")), flags=re.M)
        all_md.append(f"\n---\n\n<!-- source: {p.url} -->\n{body}")
        chunks.extend(split_chunks(p))

    (out / "index.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    (out / "knowledge_base.md").write_text("\n".join(all_md), encoding="utf-8")
    with (out / "chunks.jsonl").open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    with (out / "links.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["page", "page_title", "type", "text", "url"])
        w.writeheader()
        for p in pages:
            for l in p.links:
                w.writerow({k: l[k] for k in w.fieldnames})
            for i in p.images:
                w.writerow({"page": p.url, "page_title": p.title, "type": "image", "text": "", "url": i})

    manifest = {
        "source": BASE_URL,
        "scraped_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "pages": [{"url": p.url, "title": p.title, "section": p.section,
                   "file": (Path("pages") / slug_path(p.rel)).as_posix(),
                   "headings": [h[1] for h in p.headings if h[0] <= 2]} for p in pages],
        "failed": failed,
    }
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="output", help="dossier de sortie (défaut: output)")
    ap.add_argument("--images", action="store_true", help="télécharger aussi les captures d'écran")
    ap.add_argument("--delay", type=float, default=0.1, help="pause entre requêtes (s)")
    args = ap.parse_args()

    out = Path(args.out)
    pages, failed = crawl(args.delay)
    img_map = download_images(pages, out, args.delay) if args.images else {}
    write_outputs(pages, out, img_map, failed)

    n_links = sum(len(p.links) for p in pages)
    n_imgs = sum(len(p.images) for p in pages)
    print(f"\n✓ {len(pages)} pages, {n_links} liens, {n_imgs} images -> {out.resolve()}")
    if failed:
        print(f"  {len(failed)} URL(s) en échec : voir manifest.json")


if __name__ == "__main__":
    main()
