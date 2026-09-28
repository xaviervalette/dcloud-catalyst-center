# Catalyst Center Instant Demo 3.2 — base de connaissances

Scrape du guide public https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/ en Markdown.

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python scrape.py            # texte + inventaire des liens
.venv/bin/python scrape.py --images   # + captures d'écran (~170 Mo)
```

Sorties dans `output/` :

| Fichier | Contenu |
|---|---|
| `index.md` | Sommaire par section (Home, Scenarios, Design, Provision, Assurance, Policy) |
| `pages/<section>/<page>.md` | Une page = un fichier, avec front-matter (titre, section, URL source) |
| `knowledge_base.md` | Tout le guide dans un seul fichier, dans l'ordre de la navigation |
| `chunks.jsonl` | Découpage par section `##` pour RAG / embeddings |
| `links.csv` | Tous les liens (internes, externes, UI dCloud, images) avec la page d'origine |
| `manifest.json` | Liste des pages, titres H1/H2, URL en échec |
| `images/` | Captures d'écran, référencées en relatif depuis les `.md` |

Le crawl suit tous les liens internes (pas seulement le menu), donc il récupère aussi
les pages absentes de la navigation (ex. `provision/fabric`, `provision/fiab`).
