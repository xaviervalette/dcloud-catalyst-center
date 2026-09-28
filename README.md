# « Le Wi-Fi rame » : et si on trouvait la cause sans taper une commande ?

Script de démo **Catalyst Center 3.2 Instant Demo (dCloud)** · Troubleshooting wireless · 25 min (version 10 min en fin de document)

Quand j'échange avec des équipes réseau, le ticket wireless le plus redouté n'est pas la panne franche. C'est le « ça rame », signalé le lendemain matin, sur un problème qui a disparu depuis.

**Comment trouver la cause d'un problème qui n'existe plus au moment où on le regarde ?** C'est le fil rouge de cette démo.

> [!NOTE]
> **Comment lire ce script**
> - **Faire** : les actions dans l'interface, numérotées. Les éléments d'interface sont en **gras**, le texte à taper en `code`.
> - **Dire** : le discours, en citation.
> - Les encadrés signalent une astuce, un piège de la démo simulée ou une limite à ne pas dépasser.

## Sommaire

| Acte | Question | Écrans | Durée |
|---|---|---|---|
| [Le besoin](#le-besoin) | Le ticket | | 1 min |
| [Acte 1](#acte-1--qui-et-quand-) | Qui et quand ? | AI Assistant, Client 360 | 6 min |
| [Acte 2](#acte-2--grace-ou-tout-létage-) | Grace, ou tout l'étage ? | Issues, AI-Driven Issues | 6 min |
| [Acte 3](#acte-3--prouver-que-ce-nest-pas-le-réseau) | Quelle est la cause ? | Machine Reasoning | 4 min |
| [Acte 4](#acte-4--le-problème-de-fond--la-rf-en-24-ghz) | Pourquoi c'est fragile ? | AP Performance Advisories, Spectrum | 6 min |
| [Acte 5](#acte-5--corriger-et-vérifier-que-ça-tient) | Ça ne reviendra pas ? | AI-Enhanced RRM, Baselines | 3 min |

Annexes : [résultats](#les-résultats) · [version courte](#version-courte-10-min) · [ce que la démo prouve](#ce-que-la-démo-prouve-et-ce-quelle-ne-prouve-pas) · [préparation](#préparation) · [pièges](#pièges-en-live) · [questions](#questions-probables)

---

## Le besoin

**Dire**

> « Lundi, 8h45, chez PseudoCo. Le helpdesk vous transfère un ticket de Grace Smith, site de Londres, 1er étage : *"Mon iPad met des plombes à se connecter au Wi-Fi, et c'est pas la première fois."* Deux autres tickets arrivent dans la foulée. Même étage.
>
> La méthode classique, vous la connaissez : demander l'adresse MAC, SSH sur le WLC, `show wireless client mac-address … detail`, une radioactive trace… puis attendre que ça se reproduise. Sauf que le problème, c'était cette nuit. Ce matin, tout est vert. »

Annoncer les quatre questions de l'ingénieur. Chaque acte répond à l'une d'elles.

1. Qui est impacté, et quand ?
2. Un seul client, ou tout l'étage ?
3. Quelle est la cause : la RF, le WLC, l'AAA, le DHCP ?
4. Y a-t-il un problème de fond à corriger pour que ça ne revienne pas ?

---

## Acte 1 · Qui et quand ?

### 1.1 L'assistant IA… et le piège

**Faire**

1. Ouvrir **AI Assistant**.
2. Catégorie **Troubleshooting** > **Troubleshoot a specific client**.
3. À la question de suivi, taper `grace smith`.

L'assistant répond sur un seul équipement, **Grace.Smith-iPhone** : PseudoCo-Corp en 6 GHz, RSSI -50 dBm, SNR 39 dB, 674 Mbps, 0 % de retry, aucun échec sur 24 h. Verdict : *« No action is required at this time. »*

**Dire**

> « Je n'ai qu'un nom dans le ticket. Pas de MAC, pas d'IP. Je demande à l'assistant… et il me dit que tout va bien. C'est exactement la réponse du helpdesk : "j'ai regardé, votre connexion est parfaite". Oui, l'iPhone de Grace va très bien. Mais le ticket parle de l'iPad.
>
> L'assistant a trouvé la personne, le site et le WLC en deux secondes. La bonne question reste : quel équipement, et à quel moment ? »

> [!TIP]
> Ne pas cacher ce moment. Devant une audience sceptique sur l'IA, c'est un point de crédibilité : l'outil aide, l'ingénieur garde la main.

### 1.2 User 360 : une personne, cinq équipements

**Faire**

1. Recherche globale (loupe) : taper `Grace Smith`.
2. Ouvrir le **Client 360** de **Grace.Smith-iPad**.
3. Descendre sur l'onglet **User Defined Network**.

**Dire**

> « Catalyst Center raisonne par utilisateur, pas par adresse MAC. Grace Smith a 5 équipements connectés (iPad, MacBook Pro, Galaxy, iPhone, PC). L'iPhone va bien. L'iPad, lui, est en 2.4 GHz. »

### 1.3 La timeline : remonter dans le temps

**Faire**

1. Remonter sur le graphe 24 h en haut de page.
2. Survoler la zone rouge.

**Dire**

> « Entre 23h et 4h du matin, la santé de l'iPad s'effondre. Ce matin tout est vert : un `show` sur le WLC ne m'aurait rien appris. En dessous, sans une commande : score 7/10, Wi-Fi 6, SSID PseudoCo-Corp, VLAN 100, AP CW9178I-LDN1-01. »

### 1.4 L'incident rattaché au client

**Faire**

1. Section **Issues (1)**.
2. Cliquer sur l'incident P1 : *Wireless client took a long time to connect (SSID: PseudoCo-Corp, AP: CW9178I-LDN1-01, Band: 2.4 GHz) · Excessive time due to Association failures*.
3. Lire la **Description**.

**Dire**

> « 123,4 secondes pour se connecter, au lieu de moins de 10. Pourtant chaque étape est rapide : association 0 s, authentification 1,4 s, adressage IP 1,2 s. La clé est la dernière ligne : 2 tentatives, 120,8 secondes. Ce n'est pas une lenteur, c'est un échec suivi d'un retry. »

### 1.5 Éliminer le suspect n°1 : la couverture

**Faire**

1. **Summary** > **RSSI** > **View Details**.
2. Puis onglet **RF** > **Per Band**.

**Dire**

> « Premier réflexe terrain : "il manque une borne". Or le RSSI est bon 100 % du temps (entre -43 et -59 dBm), le SNR autour de 40 dB. Ce n'est pas la couverture. On vient d'économiser un site survey. »

### 1.6 Ce que voit l'iPad

**Faire**

1. Onglet **iOS Analytics**.

**Dire**

> « L'iPad remonte ce qu'il voit, lui : 5 APs voisines, dont CW9166I-LDN1-05 sur le canal 6 (on va la recroiser), et ses raisons de désassociation. C'est la vue côté client, qu'aucun WLC ne donne. »

---

## Acte 2 · Grace, ou tout l'étage ?

### 2.1 Ce que la supervision classique ne voit pas

**Faire**

1. **Assurance** > **Issues and Events** > **Issues**, plage **24 hours**.
2. Cliquer sur le filtre **P1**.

Résultat : 4 incidents P1, tous filaires.

| Priorité | Incident | Rôle |
|---|---|---|
| P1 | Interface Connecting Network Devices is Down | DISTRIBUTION |
| P1 | Layer 2 loop symptoms | DISTRIBUTION |
| P1 | Switch unreachable | BORDER ROUTER |
| P1 | Fabric Devices Connectivity · DHCP Underlay | BORDER ROUTER |

**Dire**

> « Dans mes P1, le Wi-Fi n'existe pas. Aucun lien down, aucun équipement injoignable. Et pourtant trois personnes n'arrivent pas à se connecter. Une dégradation d'expérience, ce n'est pas une panne. Il faut une autre façon de la détecter. »

**Faire**

3. Revenir sur **All**.
4. Activer le toggle **AI-Driven**.

Résultat : 5 incidents P2 marqués **AI** : *Excessive failures to connect*, *Excessive time to connect*, *Excessive time to get an IP Address*, *Drop in radio throughput for Cloud Applications*, *Drop in total radio throughput*.

**Dire**

> « Ces incidents ne reposent pas sur un seuil fixe. Catalyst Center apprend ce qui est normal pour chaque SSID, chaque bâtiment, chaque heure. Il alerte quand on sort de cette normale. »

### 2.2 La baseline

**Faire**

1. Ouvrir **Excessive failures to connect · High deviation from baseline**.
2. Ouvrir l'instance *At least 11% increase in failures on SSID PseudoCo-Corp in London 1/1st Floor*.

**Dire**

> « La bande verte, c'est le taux d'échec attendu : entre 10 et 25 % selon l'heure. La courbe bleue, c'est la réalité : elle monte à 40 % entre 22h et 6h. Retenez ce chiffre : 40 %, pas 100 %. Des clients échouent, d'autres passent. C'est une dégradation, pas une coupure. »

### 2.3 Impact : qui, et où ?

**Faire**

1. **Impact** > onglet **Impacted Clients**.

**Dire**

> « Et voilà Grace.Smith-iPad dans la liste, avec la même MAC que tout à l'heure. Mais aussi son MacBook, son Galaxy S23, des PC Linux, des téléphones Android… Tous les OS, tous les types de terminaux. Ce n'est pas un problème de driver ou de terminal. »

**Faire**

2. Onglet **Top 10 Impacted APs**.

**Dire**

> « Côté bornes : CW9166I-LDN1-08 à 94 % d'échecs, -10 à 94 %, -06 à 81 %… Presque toutes les APs de l'étage. Et regardez la colonne Band : ces APs sont en 5 GHz, alors que l'iPad de Grace était en 2.4 GHz.
>
> Plusieurs bornes, deux bandes, tous les terminaux : qu'est-ce qu'ils ont en commun ? Pas la RF, pas une borne. Le même SSID, le même WLC… et les mêmes serveurs derrière. »

### 2.4 Root cause : où ça casse

**Faire**

1. **Root Cause Analysis** > onglet **Network Causes**.

**Dire**

> « Les échecs d'onboarding sont corrélés dans le temps avec deux courbes : les échecs d'authentification AAA et les timeouts DHCP. Même fenêtre, même forme. »

**Faire**

2. Onglet **Failed Distribution**.

**Dire**

> « Chaque tentative ratée, décomposée par étape et par raison : AUTH avec *AAA AUTH FAIL*, ASSOC avec *MAC FILTER FAIL*, DHCP avec *DHCP TIMEOUT*. »

> [!NOTE]
> Le MAC filtering se joue pendant l'association, et il interroge le serveur AAA. C'est pour ça que l'iPad de Grace remontait des « association failures » alors que la radio était bonne. La suggestion n°4 de son incident le disait déjà : vérifier le serveur AAA 192.168.139.168 pendant la MAC Authentication.

**Faire**

3. **Suggested Actions** : vérifier le DHCP, la charge du serveur AAA, le CPU du WLC, la RF.

---

## Acte 3 · Prouver que ce n'est pas le réseau

**Faire**

1. **Issues**, plage **7 days**, filtre **P3**.
2. Ouvrir *Wireless clients failed to connect · AAA Server Rejected Clients* (AP CW9166I-LDN1-02).

**Dire**

> « Le métier d'un ingé réseau, c'est souvent de prouver que ce n'est pas le réseau. Ici, un client du même étage (Sargio.Villa, un poste Linux) est rejeté par le RADIUS. »

**Faire**

3. **Root Cause Analysis (MRE)** > **Run Machine Reasoning**.

Résultat attendu :

| Segment | Résultat |
|---|---|
| Client | OK |
| Wireless Network | OK |
| Wired Network | OK |
| RADIUS Server | **En échec** |

**Dire**

> « Le Machine Reasoning Engine, c'est l'expertise du TAC Cisco codée en workflows. Il teste chaque segment, un par un, et analyse les syslogs ISE. Client, sans fil, filaire : sains. Le RADIUS : en cause. J'ai l'argument pour l'équipe sécurité, preuves à l'appui.
>
> Alors, quelle est la root cause ? Soyons précis. Un rejet RADIUS, ça veut dire que le serveur répond : il dit non. Ce n'est pas un serveur mort. Ce qu'on a démontré : une dégradation intermittente des services partagés (AAA et DHCP) pendant la nuit, qui touche tout l'étage, toutes les bornes, tous les terminaux. Le Wi-Fi est la victime, pas le coupable.
>
> Pourquoi l'ISE et le DHCP ont décroché cette nuit, c'est la prochaine question. Mais je la pose à la bonne équipe, avec un dossier complet, en 15 minutes au lieu de deux jours. »

> [!TIP]
> Pour une audience avancée : la liste des P1 sur 7 jours contient aussi *Fabric Devices Connectivity · ISE Server*. On peut la citer comme piste à creuser, pas comme une corrélation démontrée par l'outil.

**Transition**

> « Mais pourquoi ce 1er étage est-il aussi fragile ? »

---

## Acte 4 · Le problème de fond : la RF en 2.4 GHz

### 4.1 AP Performance Advisories : 4 semaines d'analyse

**Faire**

1. **Assurance** > **AI Network Analytics** > **Trends and Insights**.

**Dire**

> « Les incidents, c'est l'aigu. Ici, c'est le chronique. L'IA analyse 4 semaines de données et regroupe les radios qui dégradent l'expérience client, par cause : 4 insights, 23 radios. »

**Faire**

2. Cliquer sur la carte **High Co-Channel Interference · 2.4 GHz** (6 radios, 30 endpoints).

**Dire**

> « Dans le top, on retrouve CW9166I-LDN1-05, celle que l'iPad de Grace voyait sur le canal 6. Ces radios subissent beaucoup plus d'interférence co-canal que les radios de référence de votre propre réseau. Remédiation proposée : baisser la puissance (TPC) et désactiver les bas débits. »

**Faire**

3. Cliquer sur la radio **CW9166I-LDN1-05**.
4. Bouton **+** > ajouter le KPI **Speed**.

**Dire**

> « La radio tourne plus souvent à bas débit. En 2.4 GHz, c'est du temps d'antenne gaspillé. Ce n'est pas la cause de l'incident de cette nuit, c'est un facteur aggravant : un onboarding qui échoue sur un canal saturé, c'est un retry plus long. »

### 4.2 L'AP devient analyseur de spectre

**Faire**

1. **Assurance** > **Health** > onglet **Network**, filtrer sur les APs, ouvrir une AP.
2. **Intelligent Capture** > **Spectrum Analysis** > **Start Spectrum Analysis**.
3. **Next** > **Deploy** > **Submit**.
4. Observer la bande 2.4 GHz, puis basculer en 5 GHz.
5. **Stop Spectrum Analysis** > **Accept**.

**Dire**

> « Pas besoin d'envoyer quelqu'un sur site avec un analyseur. En 2.4 GHz : interférence, duty cycle, FFT temps réel. »

### 4.3 Capture OTA (optionnel)

**Faire**

1. Recherche globale : `CW9166-LDN1-01` > **Device 360**.
2. **Run OTA Capture** > sélectionner 2 APs sur le plan > **Next**.
3. Choisir bande, radio, largeur et canal > **Run** > **Apply**.
4. **Next** > **Deploy** > **Submit**.
5. **Stop** > **Download**.

**Dire**

> « Pour les amateurs de Wireshark : une capture over-the-air pilotée à distance, en PCAP. Pratique pour clore un débat avec un éditeur de terminal. »

---

## Acte 5 · Corriger et vérifier que ça tient

### 5.1 AI-Enhanced RRM

**Faire**

1. **Assurance** > **AI Enhanced RRM** > **Launch AI-Enhanced RRM Deployment Workflow**.
2. **Next** > **Enable Without Device Provisioning** > **Next**.
3. Site : `London1` > **Next**.
4. Sélectionner un **AI RF Profile** > **Next** > **Deploy**.

**Dire**

> « Plutôt que retoucher les canaux AP par AP, je confie le plan RF de London 1 au RRM assisté par l'IA. Il optimise sur l'historique, en 2.4, 5 et 6 GHz. »

### 5.2 Baselines

**Faire**

1. **Assurance** > **AI Network Analytics** > **Baselines**.
2. Cliquer sur le cercle rouge **LONDON 1**, ajouter le SSID **PseudoCo-Corp**.
3. Revenir sur **Network Overview**, pointer **SAN FRANCISCO 1**.

**Dire**

> « Chaque cercle est un bâtiment. LONDON 1 est rouge : bonne moyenne, mais une anomalie, c'est notre nuit. Et regardez SAN FRANCISCO 1 : bleu, mais à droite, avec un temps d'onboarding élevé en permanence. L'IA le considère comme normal. C'est pour ça que ce tableau existe. Voilà votre prochain ticket, avant qu'il n'arrive. »

---

## Les résultats

| Question | Sans Catalyst Center | Avec Catalyst Center |
|---|---|---|
| Qui, quand ? | MAC à demander, `show` sur le WLC, problème déjà passé | Client 360 : la nuit de l'iPad en une recherche |
| Un client ou l'étage ? | Corréler les tickets à la main | Incident IA : tout l'étage, tous les terminaux, comparé à la normale |
| Quelle cause ? | Debugs, radioactive trace, attendre la récidive | Root Cause Analysis et Machine Reasoning : services AAA et DHCP, réseau sain |
| Pourquoi c'est fragile ? | Site survey, analyseur sur place | AP Performance Advisories et spectre, à distance |
| Ça ne reviendra pas ? | Tuning RF manuel | AI-Enhanced RRM et Baselines |

Aucune commande CLI. La cause immédiate et la cause de fond traitées. L'expertise wireless de l'ingénieur sert à décider, plus à collecter.

## Conclusion

**Dire**

> « Le ticket disait "le Wi-Fi rame". La réponse, c'est : le Wi-Fi va bien, ce sont l'AAA et le DHCP qui ont décroché cette nuit, et on a un chantier RF en 2.4 GHz à mener en parallèle. Trouver ça en un quart d'heure, sans que le problème soit encore là, c'est ça le changement.
>
> Et vous, quel est le ticket wireless qui vous a coûté le plus de temps ? »

---

## Version courte (10 min)

1. Ticket de Grace Smith, et l'assistant qui répond « tout va bien » sur l'iPhone (1 min 30)
2. Client 360 de l'iPad : la nuit, l'incident P1, 2 tentatives en 120,8 s, RSSI bon (3 min)
3. Incident IA : 40 % d'échecs, Grace dans la liste, 5 GHz et 2.4 GHz, AAA et DHCP (3 min)
4. Machine Reasoning : réseau OK, RADIUS en échec (2 min)
5. Teaser AP Performance Advisories : CW9166I-LDN1-05 en co-canal 2.4 GHz (30 s)

## Ce que la démo prouve, et ce qu'elle ne prouve pas

La démo est simulée : chaque écran est un scénario indépendant. L'histoire les relie, mais il faut savoir où s'arrêtent les données.

> [!IMPORTANT]
> **Démontré par les écrans**
> - L'iPad de Grace échoue à l'association puis réessaie (2 tentatives, 120,8 s), avec une bonne RF.
> - Sur l'étage, le taux d'échec d'onboarding monte à 40 % la nuit, au-dessus de la baseline.
> - Les échecs touchent de nombreuses APs, en 5 GHz et 2.4 GHz, et tous les types de terminaux.
> - Ils sont corrélés avec des échecs AAA et des timeouts DHCP.
> - Pour un client, le Machine Reasoning valide Client, Wireless et Wired, et désigne le RADIUS.

> [!CAUTION]
> **Non démontré, à ne pas affirmer**
> - Pourquoi l'ISE et le DHCP ont décroché (charge, maintenance, lien…).
> - Que le serveur AAA soit tombé : un rejet RADIUS prouve au contraire qu'il répond.
> - Un lien de cause entre la P1 *Fabric Devices Connectivity · ISE Server* et nos échecs.
> - Que l'interférence co-canal 2.4 GHz soit la cause de l'incident de la nuit : c'est un problème chronique, distinct.

## Préparation

| Point | Détail |
|---|---|
| Navigateur | Google Chrome obligatoire (moteur de simulation) |
| Login | Automatique, sinon `demo` / `demo1234!` |
| Reset | Se déconnecter remet la démo à zéro |
| Onglets à pré-ouvrir | Home, Assurance > Issues and Events, Assurance > AI Network Analytics > Trends and Insights |

> [!WARNING]
> La démo est simulée. Ne cliquer que sur ce parcours, et le répéter une fois avant la séance. L'AI Assistant ne répond qu'aux prompts du script. Les dates varient selon les écrans (2024, 2025, 2026) : dire « cette nuit », ne pas lire les dates.

## Pièges en live

> [!WARNING]
> - Sur `grace smith`, l'assistant analyse l'iPhone (sain), pas l'iPad. C'est voulu dans le script.
> - Issues sur 24 h : les P1 sont 4 incidents filaires, les incidents wireless IA sont en P2. Sur 7 jours : 9 P1, dont celle de Grace, et l'incident *AAA Server Rejected* (P3) apparaît.
> - La P1 de Grace n'affiche ni client impacté ni Client Count (Site = Global). Le lien avec Grace se fait par son Client 360, ou par l'onglet Impact de l'incident IA.
> - Incident IA : le bandeau annonce 8 clients impactés, la table en liste 18. Ne pas citer le chiffre.
> - Le dashlet Summary de User 360 est statique (identique pour tous les clients).
> - Le Client Health dashboard ne filtre que sur Global.
> - Seuls Grace.Smith-iPad et Grace Smith Galaxy-S23 ont des incidents dans Client 360.

## Questions probables

<details>
<summary><b>Qu'est-ce qu'il faut pour les incidents IA, AP Performance, Baselines ?</b></summary>

Équipements gérés par Catalyst Center, télémétrie WLC, service cloud Cisco AI Analytics activé. Environ une semaine de données pour les baselines.
</details>

<details>
<summary><b>Quels WLC ?</b></summary>

La démo tourne sur Catalyst 9800 (`LDN1-C9800-01`). À valider selon la plateforme.
</details>

<details>
<summary><b>iOS Analytics, pour tous les terminaux ?</b></summary>

Non, Apple uniquement. D'autres constructeurs remontent des infos client (Samsung par exemple), à vérifier selon les versions.
</details>

<details>
<summary><b>L'IA corrige toute seule ?</b></summary>

Non. Elle détecte, explique, suggère. L'opérateur déclenche et valide.
</details>

<details>
<summary><b>Mes données partent dans le cloud ?</b></summary>

Seules les fonctions AI Analytics utilisent le cloud (télémétrie). À traiter en rendez-vous dédié.
</details>

<details>
<summary><b>Licence ?</b></summary>

Assurance avancée et IA relèvent du niveau Advantage. À confirmer avec le partenaire ou l'account manager.
</details>

---

Sources : guide public [Catalyst Center 3.2 Instant Demo](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/), et vérifications sur l'instance dCloud (AI Assistant, Issues sur 24 h et 7 jours, P1 CW9178I-LDN1-01).

**Contenu du repo**

- `README.md` : ce script de démo
- [`catalyst-center-kb/`](catalyst-center-kb/) : scraper et base de connaissances Markdown du guide (captures non incluses, régénérables avec `scrape.py --images`)
