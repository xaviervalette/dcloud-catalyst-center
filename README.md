# « Le Wi-Fi rame » : et si on trouvait la cause sans taper une commande ?

*Script de démo Catalyst Center 3.2 Instant Demo (dCloud) · Troubleshooting wireless · 25 min (version 10 min en fin de document)*

Quand j'échange avec des équipes réseau, le ticket wireless le plus redouté n'est pas la panne franche. C'est le « ça rame », signalé le lendemain matin, sur un problème qui a disparu depuis.

> Comment trouver la cause d'un problème qui n'existe plus au moment où on le regarde ?

C'est le fil rouge de cette démo.

---

## Le besoin

Lundi, 8h45, chez PseudoCo. Le helpdesk transfère un ticket de Grace Smith, site de Londres, 1er étage :

> *« Mon iPad met des plombes à se connecter au Wi-Fi, et c'est pas la première fois. »*

Deux autres tickets arrivent dans la foulée. Même étage.

La méthode classique, tout le monde la connaît : demander l'adresse MAC, se connecter en SSH sur le WLC, lancer un `show wireless client mac-address … detail`, activer une radioactive trace… puis attendre que ça se reproduise. Sauf que le problème, c'était cette nuit. Ce matin, tout est vert.

L'ingénieur réseau a quatre questions à se poser :

1. Qui est impacté, et quand ?
2. Un seul client, ou tout l'étage ?
3. Quelle est la cause : la RF, le WLC, l'AAA, le DHCP ?
4. Y a-t-il un problème de fond à corriger pour que ça ne revienne pas ?

On les annonce en début de démo. Chaque acte répond à une question.

---

## La solution, en 5 actes

Convention : 🖱️ ce qu'on clique, 🎤 ce qu'on dit.

### Acte 1 · Qui et quand ? (6 min)

#### L'assistant IA… et le piège

🖱️ **AI Assistant** > *Troubleshooting* > « Troubleshoot a specific client » > taper `grace smith`.

L'assistant répond sur un seul équipement : **Grace.Smith-iPhone**. PseudoCo-Corp en 6 GHz, RSSI -50 dBm, SNR 39 dB, 674 Mbps, 0 % de retry, aucun échec sur 24 h. Verdict : *« No action is required at this time. »*

> 🎤 « Je n'ai qu'un nom dans le ticket. Pas de MAC, pas d'IP. Je demande à l'assistant… et il me dit que tout va bien. C'est exactement la réponse du helpdesk : "j'ai regardé, votre connexion est parfaite". Oui, l'iPhone de Grace va très bien. Mais le ticket parle de l'iPad. L'assistant a trouvé la personne, le site et le WLC en deux secondes. La bonne question reste : quel équipement, et à quel moment ? »

*Note : ne pas cacher ce moment. Devant une audience sceptique sur l'IA, c'est un point de crédibilité : l'outil aide, l'ingénieur garde la main.*

#### User 360 : une personne, cinq équipements

🖱️ Recherche globale `Grace Smith` > **Client 360 de Grace.Smith-iPad** > onglet **User Defined Network**.

> 🎤 « Catalyst Center raisonne par utilisateur, pas par adresse MAC. Grace Smith a 5 équipements connectés (iPad, MacBook Pro, Galaxy, iPhone, PC). L'iPhone va bien. L'iPad, lui, est en 2.4 GHz. »

#### La timeline : remonter dans le temps

🖱️ Graphe 24 h en haut de page, survoler la zone rouge.

> 🎤 « Entre 23h et 4h du matin, la santé de l'iPad s'effondre. Ce matin tout est vert : un `show` sur le WLC ne m'aurait rien appris. En dessous, sans une commande : score 7/10, Wi-Fi 6, SSID PseudoCo-Corp, VLAN 100, AP CW9178I-LDN1-01. »

#### L'incident rattaché au client

🖱️ Section **Issues (1)** > cliquer sur l'incident.

P1 : *Wireless client took a long time to connect (SSID: PseudoCo-Corp, AP: CW9178I-LDN1-01, Band: 2.4 GHz) · Excessive time due to Association failures*.

> 🎤 « 123,4 secondes pour se connecter, au lieu de moins de 10. Pourtant chaque étape est rapide : association 0 s, authentification 1,4 s, adressage IP 1,2 s. La clé est la dernière ligne : 2 tentatives, 120,8 secondes. Ce n'est pas une lenteur, c'est un échec suivi d'un retry. »

#### Éliminer le suspect n°1 : la couverture

🖱️ **Summary > RSSI > View Details**, puis onglet **RF > Per Band**.

> 🎤 « Premier réflexe terrain : "il manque une borne". Or le RSSI est bon 100 % du temps (entre -43 et -59 dBm), le SNR autour de 40 dB. Ce n'est pas la couverture. On vient d'économiser un site survey. »

#### Ce que voit l'iPad

🖱️ Onglet **iOS Analytics**.

> 🎤 « L'iPad remonte ce qu'il voit, lui : 5 APs voisines, dont CW9166I-LDN1-05 sur le canal 6 (on va la recroiser), et ses raisons de désassociation. C'est la vue côté client, qu'aucun WLC ne donne. »

### Acte 2 · Grace, ou tout l'étage ? (6 min)

#### Ce que la supervision classique ne voit pas

🖱️ **Assurance > Issues and Events > Issues**, plage 24 h, filtre **P1**.

4 incidents P1, tous filaires : *Interface Connecting Network Devices is Down*, *Layer 2 loop symptoms*, *Switch unreachable*, *Fabric Devices Connectivity · DHCP Underlay*.

> 🎤 « Dans mes P1, le Wi-Fi n'existe pas. Aucun lien down, aucun équipement injoignable. Et pourtant trois personnes n'arrivent pas à se connecter. Une dégradation d'expérience, ce n'est pas une panne. Il faut une autre façon de la détecter. »

🖱️ Onglet **All**, puis toggle **AI-Driven**.

5 incidents P2, marqués **AI** : *Excessive failures to connect*, *Excessive time to connect*, *Excessive time to get an IP Address*, *Drop in radio throughput for Cloud Applications*, *Drop in total radio throughput*.

> 🎤 « Ces incidents ne reposent pas sur un seuil fixe. Catalyst Center apprend ce qui est normal pour chaque SSID, chaque bâtiment, chaque heure. Il alerte quand on sort de cette normale. »

#### La baseline

🖱️ Ouvrir **Excessive failures to connect · High deviation from baseline** > instance *At least 11% increase in failures on SSID PseudoCo-Corp in London 1/1st Floor*.

> 🎤 « La bande verte, c'est le taux d'échec attendu : entre 10 et 25 % selon l'heure. La courbe bleue, c'est la réalité : elle monte à 40 % entre 22h et 6h. Retenez ce chiffre : 40 %, pas 100 %. Des clients échouent, d'autres passent. C'est une dégradation, pas une coupure. »

#### Impact : qui, et où ?

🖱️ **Impact > Impacted Clients**.

> 🎤 « Et voilà Grace.Smith-iPad dans la liste, avec la même MAC que tout à l'heure. Mais aussi son MacBook, son Galaxy S23, des PC Linux, des téléphones Android… Tous les OS, tous les types de terminaux. Ce n'est pas un problème de driver ou de terminal. »

🖱️ Onglet **Top 10 Impacted APs**.

> 🎤 « Côté bornes : CW9166I-LDN1-08 à 94 % d'échecs, -10 à 94 %, -06 à 81 %… Presque toutes les APs de l'étage. Et regardez la colonne Band : ces APs sont en 5 GHz, alors que l'iPad de Grace était en 2.4 GHz. »

> Plusieurs bornes, deux bandes, tous les terminaux : qu'est-ce qu'ils ont en commun ?

> 🎤 « Pas la RF, pas une borne. Ils partagent le même SSID, le même WLC… et les mêmes serveurs derrière. »

#### Root cause : où ça casse

🖱️ **Root Cause Analysis > Network Causes**.

> 🎤 « Les échecs d'onboarding sont corrélés dans le temps avec deux courbes : les échecs d'authentification AAA et les timeouts DHCP. Même fenêtre, même forme. »

🖱️ Onglet **Failed Distribution**.

> 🎤 « Chaque tentative ratée, décomposée par étape et par raison : AUTH avec *AAA AUTH FAIL*, ASSOC avec *MAC FILTER FAIL*, DHCP avec *DHCP TIMEOUT*. »

*Note : le MAC filtering se joue pendant l'association, et il interroge le serveur AAA. C'est pour ça que l'iPad de Grace remontait des « association failures » alors que la radio était bonne. La suggestion n°4 de son incident le disait déjà : vérifier le serveur AAA 192.168.139.168 pendant la MAC Authentication.*

🖱️ **Suggested Actions** : vérifier le DHCP, la charge du serveur AAA, le CPU du WLC, la RF.

### Acte 3 · Prouver que ce n'est pas le réseau (4 min)

🖱️ **Issues**, plage **7 days**, onglet **P3** > *Wireless clients failed to connect · AAA Server Rejected Clients* (AP CW9166I-LDN1-02).

> 🎤 « Le métier d'un ingé réseau, c'est souvent de prouver que ce n'est pas le réseau. Ici, un client du même étage (Sargio.Villa, un poste Linux) est rejeté par le RADIUS. »

🖱️ **Root Cause Analysis (MRE)** > **Run Machine Reasoning**.

> 🎤 « Le Machine Reasoning Engine, c'est l'expertise du TAC Cisco codée en workflows. Il teste chaque segment : Client ✅, Wireless Network ✅, Wired Network ✅, RADIUS Server ❌. Il analyse les syslogs ISE pour remonter les causes possibles. J'ai en main l'argument pour l'équipe sécurité, preuves à l'appui. »

> Alors, quelle est la root cause ?

> 🎤 « Soyons précis. Un rejet RADIUS, ça veut dire que le serveur répond : il dit non. Ce n'est pas un serveur mort. Ce qu'on a démontré : une dégradation intermittente des services partagés (AAA et DHCP) pendant la nuit, qui touche tout l'étage, toutes les bornes, tous les terminaux. Le Wi-Fi est la victime, pas le coupable. Pourquoi l'ISE et le DHCP ont décroché cette nuit, c'est la prochaine question. Mais je la pose à la bonne équipe, avec un dossier complet, en 15 minutes au lieu de deux jours. »

*Note pour les avancés : la liste des P1 sur 7 jours contient aussi « Fabric Devices Connectivity · ISE Server ». On peut la citer comme piste à creuser, pas comme une corrélation démontrée par l'outil.*

> Mais pourquoi ce 1er étage est-il aussi fragile ?

### Acte 4 · Le problème de fond : la RF en 2.4 GHz (6 min)

#### AP Performance Advisories : 4 semaines d'analyse

🖱️ **Assurance > AI Network Analytics > Trends and Insights**.

> 🎤 « Les incidents, c'est l'aigu. Ici, c'est le chronique. L'IA analyse 4 semaines de données et regroupe les radios qui dégradent l'expérience client, par cause : 4 insights, 23 radios. »

🖱️ Carte **High Co-Channel Interference · 2.4 GHz** (6 radios, 30 endpoints).

> 🎤 « Dans le top, on retrouve CW9166I-LDN1-05, celle que l'iPad de Grace voyait sur le canal 6. Ces radios subissent beaucoup plus d'interférence co-canal que les radios de référence de votre propre réseau. Remédiation proposée : baisser la puissance (TPC) et désactiver les bas débits. »

🖱️ Cliquer sur **CW9166I-LDN1-05** > **+** > ajouter le KPI **Speed**.

> 🎤 « La radio tourne plus souvent à bas débit. En 2.4 GHz, c'est du temps d'antenne gaspillé. Ce n'est pas la cause de l'incident de cette nuit, c'est un facteur aggravant : un onboarding qui échoue sur un canal saturé, c'est un retry plus long. »

#### L'AP devient analyseur de spectre

🖱️ **Assurance > Health > Network** > une AP > **Intelligent Capture > Spectrum Analysis > Start** > Next > Deploy > Submit.

> 🎤 « Pas besoin d'envoyer quelqu'un sur site avec un analyseur. En 2.4 GHz : interférence, duty cycle, FFT temps réel. »

🖱️ Basculer en 5 GHz pour comparer, puis **Stop Spectrum Analysis > Accept**.

#### (Option) Capture OTA

🖱️ Recherche `CW9166-LDN1-01` > Device 360 > **Run OTA Capture** > 2 APs > bande et canal > Run > Deploy > Submit > Stop > **Download**.

> 🎤 « Pour les amateurs de Wireshark : une capture over-the-air pilotée à distance, en PCAP. Pratique pour clore un débat avec un éditeur de terminal. »

### Acte 5 · Corriger et vérifier que ça tient (3 min)

🖱️ **AI Enhanced RRM** > *Launch AI-Enhanced RRM Deployment Workflow* > *Enable Without Device Provisioning* > site **London1** > un **AI RF Profile** > Deploy.

> 🎤 « Plutôt que retoucher les canaux AP par AP, je confie le plan RF de London 1 au RRM assisté par l'IA. Il optimise sur l'historique, en 2.4, 5 et 6 GHz. »

🖱️ **AI Network Analytics > Baselines**.

> 🎤 « Chaque cercle est un bâtiment. LONDON 1 est rouge : bonne moyenne, mais une anomalie, c'est notre nuit. Et regardez SAN FRANCISCO 1 : bleu, mais à droite, avec un temps d'onboarding élevé en permanence. L'IA le considère comme normal. C'est pour ça que ce tableau existe. Voilà votre prochain ticket, avant qu'il n'arrive. »

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

---

## Conclusion

> 🎤 « Le ticket disait "le Wi-Fi rame". La réponse, c'est : le Wi-Fi va bien, ce sont l'AAA et le DHCP qui ont décroché cette nuit, et on a un chantier RF en 2.4 GHz à mener en parallèle. Trouver ça en un quart d'heure, sans que le problème soit encore là, c'est ça le changement. »

> Et vous, quel est le ticket wireless qui vous a coûté le plus de temps ?

---

## Version courte (10 min)

1. Ticket de Grace Smith, et l'assistant qui répond « tout va bien » sur l'iPhone (1 min 30)
2. Client 360 de l'iPad : la nuit, l'incident P1, 2 tentatives en 120,8 s, RSSI bon (3 min)
3. Incident IA : 40 % d'échecs, Grace dans la liste, 5 GHz et 2.4 GHz, AAA et DHCP (3 min)
4. Machine Reasoning : réseau ✅, RADIUS ❌ (2 min)
5. Teaser AP Performance Advisories : CW9166I-LDN1-05 en co-canal 2.4 GHz (30 s)

---

## Ce que la démo prouve, et ce qu'elle ne prouve pas

La démo est simulée : chaque écran est un scénario indépendant. L'histoire les relie, mais il faut savoir où s'arrêtent les données.

**Démontré par les écrans :**
- L'iPad de Grace échoue à l'association puis réessaie (2 tentatives, 120,8 s), avec une bonne RF.
- Sur l'étage, le taux d'échec d'onboarding monte à 40 % la nuit, au-dessus de la baseline.
- Les échecs touchent de nombreuses APs, en 5 GHz et 2.4 GHz, et tous les types de terminaux.
- Ils sont corrélés avec des échecs AAA et des timeouts DHCP.
- Pour un client, le Machine Reasoning valide Client, Wireless et Wired, et désigne le RADIUS.

**Non démontré, à ne pas affirmer :**
- Pourquoi l'ISE et le DHCP ont décroché (charge, maintenance, lien…).
- Que le serveur AAA soit tombé : un rejet RADIUS prouve au contraire qu'il répond.
- Un lien de cause entre la P1 *Fabric Devices Connectivity · ISE Server* et nos échecs.
- Que l'interférence co-canal 2.4 GHz soit la cause de l'incident de la nuit : c'est un problème chronique, distinct.

---

## Préparation

| Point | Détail |
|---|---|
| Navigateur | Google Chrome obligatoire (moteur de simulation) |
| Login | Automatique, sinon `demo` / `demo1234!` |
| Reset | Se déconnecter remet la démo à zéro |
| Démo simulée | Ne cliquer que sur ce parcours. Tout n'est pas simulé : le répéter une fois avant. |
| Dates | Elles varient selon les écrans (2024, 2025, 2026). Dire « cette nuit », ne pas lire les dates. |
| AI Assistant | Utiliser exactement les prompts du script, seuls ceux-là sont simulés. |

Onglets à pré-ouvrir : Home, Assurance > Issues and Events, Assurance > AI Network Analytics > Trends and Insights.

## Pièges en live

- Sur `grace smith`, l'assistant analyse l'iPhone (sain), pas l'iPad. C'est voulu dans le script.
- Issues sur 24 h : les P1 sont 4 incidents filaires, les incidents wireless IA sont en P2. Sur 7 jours : 9 P1, dont celle de Grace, et l'incident *AAA Server Rejected* (P3) apparaît.
- La P1 de Grace n'affiche ni client impacté ni Client Count (Site = Global). Le lien avec Grace se fait par son Client 360, ou par l'onglet Impact de l'incident IA.
- Incident IA : le bandeau annonce 8 clients impactés, la table en liste 18. Ne pas citer le chiffre.
- Le dashlet Summary de User 360 est statique (identique pour tous les clients).
- Le Client Health dashboard ne filtre que sur Global.
- Seuls Grace.Smith-iPad et Grace Smith Galaxy-S23 ont des incidents dans Client 360.

## Questions probables

| Question | Réponse |
|---|---|
| Qu'est-ce qu'il faut pour les incidents IA, AP Performance, Baselines ? | Équipements gérés par Catalyst Center, télémétrie WLC, service cloud Cisco AI Analytics activé. Environ une semaine de données pour les baselines. |
| Quels WLC ? | La démo tourne sur Catalyst 9800 (`LDN1-C9800-01`). À valider selon la plateforme. |
| iOS Analytics, pour tous les terminaux ? | Non, Apple uniquement. D'autres constructeurs remontent des infos client (Samsung par exemple), à vérifier selon les versions. |
| L'IA corrige toute seule ? | Non. Elle détecte, explique, suggère. L'opérateur déclenche et valide. |
| Mes données partent dans le cloud ? | Seules les fonctions AI Analytics utilisent le cloud (télémétrie). À traiter en rendez-vous dédié. |
| Licence ? | Assurance avancée et IA relèvent du niveau Advantage. À confirmer avec le partenaire ou l'account manager. |

---

*Sources : guide public [Catalyst Center 3.2 Instant Demo](https://networkingtoolbox.cisco.com/guides/catalyst-center-instant-demo-3-2/), et vérifications sur l'instance dCloud (AI Assistant, Issues sur 24 h et 7 jours, P1 CW9178I-LDN1-01).*

## Contenu du repo

- `README.md` : ce script de démo
- [`catalyst-center-kb/`](catalyst-center-kb/) : scraper et base de connaissances Markdown du guide (captures non incluses, régénérables avec `scrape.py --images`)
