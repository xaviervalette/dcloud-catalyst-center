# Script de démo — Troubleshooting Wireless avec Catalyst Center
### « Le Wi-Fi du 1er étage de Londres » — Catalyst Center 3.2 Instant Demo (dCloud)

**Public :** ingénieurs réseau / wireless (N2-N3), responsables d'exploitation
**Durée :** ~25 min (version courte 10 min en fin de document)
**Message clé :** *Passer de « le Wi-Fi rame » à la cause racine prouvée, sans SSH, sans debug, sans attendre que le problème se reproduise.*

---

## 0. Préparation (avant la séance)

| Point | Détail |
|---|---|
| Navigateur | **Google Chrome** obligatoire (moteur de simulation) |
| Login | Automatique — sinon `demo` / `demo1234!` |
| Reset | Se déconnecter remet la démo à zéro |
| ⚠️ Démo simulée | Ne cliquer **que** sur le parcours ci-dessous. Tout n'est pas simulé : répétez-le une fois avant. |
| ⚠️ Dates | Les horodatages varient selon les écrans (2024 / 2025). Racontez « cette nuit » / « ce matin », ne lisez pas les dates à voix haute. |
| ⚠️ AI Assistant | Utiliser **exactement** les prompts du script (seuls ceux-là sont simulés). |

Onglets à pré-ouvrir (gain de temps) : Home · Assurance > Issues and Events · Assurance > AI Network Analytics > Trends and Insights.

---

## Le contexte à poser (1 min)

> 🎤 « Je vous propose de vous mettre dans la peau d'un ingénieur réseau chez **PseudoCo**. Lundi, 8h45. Le helpdesk vous transfère un ticket de **Grace Smith**, site de **Londres, 1er étage** : *"Mon iPad met des plombes à se connecter au Wi-Fi, et c'est pas la première fois."* Deux autres tickets similaires arrivent dans la foulée, même étage.
>
> Vous connaissez la suite habituelle : on demande l'adresse MAC, on se connecte en SSH sur le WLC, `show wireless client mac-address … detail`, on lance une radioactive trace… et on attend que ça se reproduise. Sauf que le problème, c'était **cette nuit**, et ce matin tout a l'air normal.
>
> Voyons comment on traite ce même ticket avec Catalyst Center. »

**Les 4 questions de l'ingénieur** — c'est le fil rouge, annoncez-les :
1. **Qui** est impacté et **quand** ? → Client 360
2. Est-ce **un** client ou **tout un étage** ? → AI-Driven Issues
3. **Quelle est la cause** ? RF, WLC, AAA, DHCP ? → Root Cause Analysis + Machine Reasoning
4. Y a-t-il un problème **de fond** à corriger pour que ça ne revienne pas ? → AP Performance Advisories, Spectrum, AI RRM

---

## Acte 1 — « Qui et quand ? » : partir du ticket (6 min)

### 1.1 Demander à l'assistant IA… et se faire piéger (1 min 30)

🖱️ Ouvrir **AI Assistant** → catégorie *Troubleshooting* → **« Troubleshoot a specific client »** → à la question de suivi, taper **`grace smith`**.

L'assistant répond sur **un seul équipement : `Grace.Smith-iPhone`** (« Showing 1 of 1 device(s) found ») :
connecté sur **PseudoCo-Corp en 6 GHz**, AP CW9178I, WLC `LDN1-C9800-01`, score **8**, RSSI -50 dBm, SNR 39 dB, 674 Mbps, 0 % de retry, aucune déconnexion ni échec d'auth/DHCP sur 24 h → *« No action is required at this time. »*

> 🎤 « Premier réflexe, je n'ai qu'un nom dans le ticket. Pas d'adresse MAC, pas d'IP. Je demande à l'assistant… et il me répond que **tout va bien** : RSSI -50, 674 Mbps, aucune erreur, rien à faire.
> Vous voyez le piège ? C'est exactement ce qui se passe au helpdesk : *"j'ai regardé, votre connexion est parfaite"*. Oui — **l'iPhone** de Grace, en 6 GHz, va très bien. Mais le ticket parle de **l'iPad**.
> L'assistant est un excellent point d'entrée, il a trouvé la personne, le site, le WLC en deux secondes. Mais la bonne question, c'est **quel équipement** et **à quel moment**. Et pour ça, on descend dans les données. »

> 💡 **Ne pas cacher ce moment, l'exploiter** : c'est la transition naturelle vers User 360. Si l'audience est sceptique sur l'IA, c'est même un point de crédibilité : on montre l'outil tel qu'il est et comment l'ingé garde la main.

### 1.2 User 360 : une personne, plusieurs équipements

🖱️ **Recherche globale** (loupe) → `Grace Smith` → ouvrir le résultat → **Client 360 de `Grace.Smith-iPad`**.
🖱️ Onglet **User Defined Network** (bas de page).

> 🎤 « Catalyst Center raisonne en **utilisateur**, pas en adresse MAC : Grace Smith a **5 équipements** connectés — iPad, MacBook Pro, Galaxy, iPhone, PC. L'iPhone qu'on vient de voir va bien. Celui qui pose problème, c'est l'iPad — et lui est en **2.4 GHz**. »

### 1.3 La timeline : remonter dans le temps

🖱️ Revenir en haut sur le **graphe global 24 h**. Survoler la zone rouge.

> 🎤 « Voilà l'intérêt n°1 : **la machine à remonter le temps**. Entre ~23h et ~4h du matin, la santé de l'iPad s'effondre (ligne rouge). Ce matin tout est vert — c'est pour ça qu'un `show` sur le WLC ne vous aurait rien montré.
> En dessous, les infos essentielles sans taper une commande : score **7/10**, **Wi-Fi 6**, SSID **PseudoCo-Corp**, VLAN 100, AP **CW9178I-LDN1-01**, London 1 / 1st Floor. »

### 1.4 L'issue remontée pour ce client

🖱️ Section **Issues (1)**.

> 🎤 « Une issue **P1 – Onboarding** : *Wireless client took a long time to connect (SSID PseudoCo-Corp, AP CW9178I-LDN1-01, 2.4 GHz) – Excessive time due to Association failures*. **3 occurrences.** Le ticket de Grace est confirmé et qualifié : c'est de l'onboarding, en 2.4 GHz. »

### 1.5 Éliminer le suspect n°1 : la couverture

🖱️ **Summary > Connectivity > RSSI → View Details** (RSSI 100 % Good), puis onglet **RF → Per Band**.

> 🎤 « Le premier réflexe terrain, c'est "il manque une borne". Or le RSSI est **bon 100 % du temps** (entre -43 et -59 dBm), le SNR autour de 40 dB. **Ce n'est pas un problème de couverture.** On vient d'économiser un site survey et une borne. »

### 1.6 Le point de vue de l'iPad lui-même (iOS Analytics)

🖱️ Onglet **iOS Analytics**.

> 🎤 « Grâce au partenariat Cisco–Apple, l'iPad nous remonte **ce qu'il voit, lui** : 5 APs voisins, dont **CW9166I-LDN1-05 sur le canal 6** (retenez ce nom, on va le recroiser), et ses 30 raisons de désassociation. C'est la vue *client-side* qu'aucun WLC ne vous donne. »

---

## Acte 2 — « Grace, ou tout l'étage ? » (5 min)

🖱️ **Assurance > Issues and Events > Issues**. Activer le filtre **AI Driven**.

> 🎤 « Trois tickets du même étage, ça sent le problème collectif. Les issues marquées **AI** ne reposent pas sur des seuils fixes : Catalyst Center apprend ce qui est *normal* pour **chaque** SSID, **chaque** bâtiment, **chaque** heure — et alerte quand on sort de cette normale. Fini les seuils statiques qui sonnent tout le temps ou jamais. »

🖱️ Ouvrir **Excessive failures to connect – High deviation from baseline** → l'instance **« At least 11% increase in failures on SSID PseudoCo-Corp in London 1/1st Floor »**.

### 2.1 Problème : la baseline

> 🎤 « **Cette nuit, de 22h à 6h**, au 1er étage de Londres, **8 clients impactés**. La bande verte, c'est ce que l'IA attendait ; la courbe bleue, la réalité ; en rouge, l'anomalie. Le cas de Grace n'est pas isolé. »

### 2.2 Impact : quelles APs ?

🖱️ **Impact > Top 10 Impacted APs**.

> 🎤 « Tout de suite les APs concernées : **CW9166I-LDN1-08 à 94 % d'échecs d'onboarding**, -10 à 94 %, -06 à 81 %… Toutes au 1er étage. On a le périmètre exact. »

### 2.3 Root Cause : où ça casse dans l'onboarding

🖱️ **Root Cause Analysis > Network Causes**, puis **Failed Distribution**.

> 🎤 « C'est **la** vue que j'aurais voulu avoir toute ma carrière. Onglet *Network Causes* : les échecs sont corrélés dans le temps avec **deux courbes — les AAA Auth Fail et les DHCP Timeout**.
> Onglet *Failed Distribution* : chaque tentative, par AP, décomposée par **étape** (ASSOC → AUTH → DHCP) et par **raison** : *AAA AUTH FAIL*, *MAC FILTER FAIL*, *DHCP TIMEOUT*. En un écran, on sait que l'association radio n'est pas le vrai sujet : ça casse **derrière**, côté services réseau. »

🖱️ **Suggested Actions**.

> 🎤 « Et des actions concrètes : vérifier la charge du serveur AAA, la réponse DHCP, le CPU du WLC. Ce n'est pas l'IA qui décide — c'est l'IA qui vous fait gagner les 2 premières heures d'enquête. »

### 2.4 (Option) Le détail chiffré d'une connexion

🖱️ Retour **Issues** → **Wireless client took a long time to connect (… CW9166I-LDN1-01, 2.4 GHz) – Excessive time due to Association failures** → ouvrir l'instance.

> 🎤 « Le détail d'une seule connexion : **123 secondes** pour se connecter, au lieu de moins de 10. Auth : 1,4 s, IP : 1,2 s — ce n'est donc pas une lenteur, ce sont des **échecs puis des retries**. Et la suggestion n°4 pointe déjà le serveur AAA **192.168.139.168** pendant la MAC Authentication. »

---

## Acte 3 — « Prouve-le » : Machine Reasoning (4 min)

🖱️ **Issues** → **(P3) Wireless clients failed to connect – AAA Server Rejected Clients** (SSID PseudoCo-Corp, AP CW9166I-LDN1-02, 2.4 GHz).

> 🎤 « Le problème d'un ingé réseau, c'est souvent de **prouver que ce n'est pas le réseau**. Ici, un client rejeté — *Sargio.Villa*, un poste Linux, même étage. »

🖱️ **Problem Details** (RADIUS Server 192.168.139.168) → **Root Cause Analysis (MRE)** → **Run Machine Reasoning**.

> 🎤 « Le **Machine Reasoning Engine**, c'est l'expertise du TAC Cisco codée en workflows. Il teste chaque segment, un par un :
> ✅ Client — ✅ Wireless Network — ✅ Wired Network — ❌ **RADIUS Server**.
> Il va jusqu'à analyser les **syslogs ISE**. En quelques secondes, vous avez l'argument à envoyer à l'équipe sécurité : *le réseau est sain, c'est le RADIUS 192.168.139.168 qui rejette*. Fini le ping-pong entre équipes. »

> 💡 **Point d'étape (à dire)** : « On a la cause immédiate du ticket de cette nuit : un problème AAA/DHCP. Mais un bon ingé ne s'arrête pas là : pourquoi cet étage est-il **aussi fragile en 2.4 GHz** ? »

---

## Acte 4 — Le problème de fond : la RF en 2.4 GHz (6 min)

### 4.1 AP Performance Advisories : l'analyse sur 4 semaines

🖱️ **Assurance > AI Network Analytics > Trends and Insights > AP Performance Advisories**.

> 🎤 « Les issues, c'est l'incident. Ici, c'est le **chronique** : l'IA analyse **4 semaines** de données et regroupe les radios qui dégradent l'expérience client, par cause. 4 insights, 23 radios. »

🖱️ Carte **High Co-Channel Interference – 2.4 GHz** (6 radios, 30 endpoints).

> 🎤 « Et qui retrouve-t-on dans le top ? **CW9166I-LDN1-05** — l'AP que l'iPad de Grace voyait sur le canal 6. Les radios de ce groupe montrent **beaucoup plus d'interférence co-canal et d'utilisation canal** que les radios de référence de votre propre réseau. Remédiation proposée : baisser la puissance (**TPC**) et **désactiver les bas débits**. »

🖱️ Cliquer sur une radio (ex. **CW9166I-LDN1-05**) → page **Details**, puis **+** pour ajouter le KPI **Speed**.

> 🎤 « KPI par KPI : RSSI, SNR, retries, packet failures… On ajoute le débit : la radio problématique tourne beaucoup plus souvent à **bas débit**. Des bas débits en 2.4 GHz, c'est de l'airtime gaspillé, donc des associations plus lentes et plus fragiles — exactement notre symptôme. »

### 4.2 Voir l'interférence : Spectrum Analysis (Intelligent Capture)

🖱️ **Assurance > Health > Network** → filtrer sur les APs → ouvrir un AP → **Intelligent Capture > Spectrum Analysis > Start Spectrum Analysis** → Next → Deploy → Submit.

> 🎤 « Sans sortir de spectrum analyzer ni envoyer quelqu'un sur site : l'AP devient **l'analyseur de spectre**. 2.4 GHz : *Interference & Duty Cycle*, FFT en temps réel. »
🖱️ Basculer en **5 GHz** pour comparer, puis **Stop Spectrum Analysis > Accept**.

### 4.3 (Option experts) Capture OTA → PCAP

🖱️ Recherche globale **CW9166-LDN1-01** → Device 360 → **Run OTA Capture** → choisir 2 APs sur le plan → bande/canal → Run → Deploy → Submit → Stop → **Download**.

> 🎤 « Pour les puristes Wireshark : capture **over-the-air** depuis les APs, pilotée à distance, PCAP téléchargeable. Idéal pour clore un débat avec un éditeur de terminal. »

---

## Acte 5 — Corriger et s'assurer que ça tient (3 min)

### 5.1 AI-Enhanced RRM

🖱️ **Assurance > AI Enhanced RRM** → **Launch AI-Enhanced RRM Deployment Workflow** → Next → **Enable Without Device Provisioning** → site **London1** → sélectionner un **AI RF Profile** → Next → Deploy.

> 🎤 « Plutôt que retoucher les canaux et puissances AP par AP, on confie le plan RF de London 1 à **l'RRM assisté par l'IA cloud**, qui optimise sur l'historique et pas seulement sur l'instant. Il couvre 2.4, 5 et 6 GHz. »

### 5.2 Baselines : garder un œil sur London 1

🖱️ **Assurance > AI Network Analytics > Baselines**.

> 🎤 « Chaque cercle est un bâtiment. **LONDON 1 est rouge** : bonnes performances en moyenne, mais une anomalie détectée — c'est notre nuit. On ajoute le SSID **PseudoCo-Corp** pour comparer.
> Et regardez **SAN FRANCISCO 1** : bleu, mais à droite, temps d'onboarding élevé **en permanence**. L'IA considère ça comme "normal" — c'est pour ça que ce tableau existe : un mauvais comportement chronique ne doit pas devenir invisible. Voilà votre prochain ticket, avant qu'il n'arrive. »

---

## Conclusion (1 min)

> 🎤 « Récapitulons le ticket de Grace :

| Question | Sans Catalyst Center | Avec Catalyst Center |
|---|---|---|
| Qui / quand ? | MAC à demander, `show` sur le WLC… problème déjà passé | **Client 360** : timeline de la nuit, 1 recherche |
| Un client ou l'étage ? | Corréler les tickets à la main | **AI-Driven Issue** : 8 clients, 1 étage, vs baseline |
| Quelle cause ? | Debugs, radioactive trace, attendre la récidive | **RCA + Machine Reasoning** : RADIUS en cause, preuve à l'appui |
| Pourquoi c'est fragile ? | Site survey, analyseur de spectre sur place | **AP Perf Advisories + Spectrum** à distance |
| Ça ne reviendra pas ? | Tuning RF manuel | **AI-Enhanced RRM + Baselines** |

> On n'a pas tapé une seule commande CLI, et on a traité **la cause immédiate et la cause de fond**. Le vrai gain, ce n'est pas l'IA pour l'IA : c'est que votre expertise wireless s'exerce sur la **décision**, plus sur la collecte. »

---

## Version courte (10 min)

1. Contexte ticket Grace Smith + AI Assistant qui répond « tout va bien » sur l'iPhone (1 min 30)
2. Client 360 `Grace.Smith-iPad` : timeline de la nuit + Issue P1 + RSSI OK (3 min)
3. AI Issue *Excessive failures to connect* : 8 clients, Top APs, Network Causes AAA/DHCP (3 min)
4. Machine Reasoning sur *AAA Server Rejected Clients* : ❌ RADIUS (2 min)
5. Teaser AP Performance Advisories : CW9166I-LDN1-05 en co-channel 2.4 GHz (1 min)

---

## Questions probables de l'audience

| Question | Éléments de réponse |
|---|---|
| « Il faut quoi pour avoir les issues IA / AP Perf / Baselines ? » | Équipements gérés par Catalyst Center, télémétrie WLC activée, service cloud **Cisco AI Analytics** activé. Les baselines ont besoin d'environ **une semaine** de données. |
| « Ça marche avec quels WLC ? » | Démo sur **Catalyst 9800** (`LDN1-C9800-01`). À valider selon la version/plateforme du client. |
| « iOS Analytics, c'est pour tous les terminaux ? » | Non, Apple (iPhone/iPad/Mac). D'autres constructeurs remontent aussi des infos client (ex. Samsung) — à vérifier selon les versions. |
| « L'IA corrige toute seule ? » | Non : elle détecte, explique, suggère. Les actions (RRM, reset radio…) restent déclenchées et validées par l'opérateur. |
| « Mes données partent dans le cloud ? » | Seules les fonctions *AI Analytics* utilisent le cloud (télémétrie). À traiter avec la fiche de confidentialité Cisco en rendez-vous dédié. |
| « Licence ? » | Les fonctions d'Assurance avancées / IA relèvent du niveau **Advantage** — à confirmer avec le partenaire / l'account manager. |

---

## Pièges à éviter en live

- Le Client Health dashboard ne filtre que sur **Global** (pas par site) dans la démo.
- Le dashlet **Summary** de User 360 est **statique** (identique pour tous les clients) : ne pas s'y attarder.
- Seuls `Grace.Smith-iPad` et `Grace Smith Galaxy-S23` ont des **issues** dans Client 360 ; les autres affichent « no data ».
- L'AI Assistant ne répond qu'aux prompts listés dans le guide (dont « Troubleshoot a specific client » → `grace smith` et « Troubleshoot a specific access point » → `CW9178I-LDN1-01`).
- Sur `grace smith`, l'assistant analyse **l'iPhone** (sain, 6 GHz), pas l'iPad : c'est voulu dans le script (acte 1.1), ne pas chercher à obtenir l'iPad via l'assistant.
- Les noms d'AP diffèrent légèrement selon les écrans (CW9178I-LDN1-01, CW9166I-LDN1-01…) : l'histoire tient car **tout est London 1 / 1st Floor / PseudoCo-Corp / 2.4 GHz**.

*Sources : guide public Catalyst Center 3.2 Instant Demo (networkingtoolbox.cisco.com) — pages Client 360, User 360, Issues, AI-Driven Issues, AP Performance Advisories, Intelligent Capture, OTA Sniffing, AI Enhanced RRM, Baselines, AI Assistant.*
