# CONDUCTEUR ORAL DE SOUTENANCE — LIVRABLE R1
## Appel d'Offres ShopLoc — Master 2 MIAGE (UE GLOP 2026-2027)
### Entreprise Soumissionnaire : Garik
**Date de l'épreuve :** Lundi 21 septembre 2026 — Amphi Turing  
**Durée contractuelle :** 15 minutes d'exposé (chrono strict) + 5 minutes d'échanges / Q&A avec le jury  
**Support de projection :** `GARIK_GLOP-2026-SOUTENANCE-R1.html` (interactif) ou `GARIK_GLOP-2026-SOUTENANCE-R1.pdf` (16:9)

---

## 1. Répartition Temporelle Globale (15 minutes chrono)

| Créneau | Durée | Orateur | Rôle Opérationnel | Diapositives | Critères Évalués |
| :---: | :---: | :--- | :--- | :---: | :---: |
| **00:00 - 03:00** | 3 min | **Khalil Bouchama** | Scrum Master R1 · Pilotage | **Slide 01 & 02** | Critères 6 & 8 |
| **03:00 - 06:00** | 3 min | **Abdelkader Heddi** | Qualité, Exigences & Risques | **Slide 03 & 04** | Critères 3, 4 & 5 |
| **06:00 - 09:00** | 3 min | **Ilyas Ait Ali** | Architecture Front-end & UX | **Slide 05 & 06** | Critères 2, 3, 4 & 5 |
| **09:00 - 12:00** | 3 min | **Rayane Alli** | Architecture Back-end & DevOps | **Slide 07 & 08** | Critères 5 & 7 |
| **12:00 - 15:00** | 3 min | **Gautam Demeulemeester** | Gestion Financière & Stratégie | **Slide 09, 10 & 11** | Critères 1 & 2 |
| **15:00** | 30 s | **Khalil Bouchama** | Clôture & Lancement Q&A | **Slide 12** | Synthèse des 8 critères |

---

## 2. Script Détaillé Diapositive par Diapositive

---

### [00:00 – 01:30] Slide 01 : Titre & Cartouche GLOP
**Orateur : Khalil Bouchama**
* **Ce qu'on projette :** Page de garde officielle, logos Université de Lille, FST Informatique et Garik, cartouche des 5 ingénieurs.
* **Discours oral suggéré :**
  > *« Madame, Messieurs les membres du jury, bonjour.  
  > Nous représentons aujourd'hui l'entreprise étudiante Garik pour vous présenter notre réponse formelle à l'appel d'offres territorial ShopLoc.  
  > Face aux bouleversements qui frappent le commerce de centre-ville et aux risques d'exclusion numérique, notre ambition est claire : mettre les technologies numériques au service de l'ancrage physique, de la souveraineté municipale et de la solidarité locale.  
  > Notre collectif réunit cinq ingénieurs aux compétences complémentaires, pleinement engagés pour mener à bien ce projet sur l'ensemble de l'année universitaire. »*

---

### [01:30 – 03:00] Slide 02 : L'Entreprise Garik & Organisation Agile
**Orateur : Khalil Bouchama**
* **Ce qu'on projette :** Carte d'identité de Garik, matrice des 6 rôles GLOP, organisation Scrum Master tournant et rituels agiles.
* **Critères ciblés :** **Critère 6** *(Pilotage)* & **Critère 8** *(Références et expérience)*.
* **Discours oral suggéré :**
  > *« Garik est une société étudiante d'ingénierie logicielle positionnée sur la transformation frugale des systèmes d'information publics.  
  > Pour répondre aux exigences de l'appel d'offres sans dérive managériale, nous appliquons rigoureusement la matrice des 6 rôles recommandés par l'UE GLOP :  
  > - Abdelkader est le garant de la qualité et des critères d'acceptation ;  
  > - Rayane et Ilyas se partagent l'architecture logicielle, respectivement sur le back-end/DevOps et le front-end/UX ;  
  > - Gautam pilote la modélisation des coûts et la viabilité financière ;  
  > - Et j'assure, pour ce premier jalon R1, le rôle de Scrum Master tournant.  
  > Notre fonctionnement repose sur des sprints de 2 semaines, une intégration continue stricte sous GitLab et la tenue d'un registre de décisions d'architecture (ADR).  
  > Je passe la parole à Abdelkader pour le diagnostic territorial et l'analyse de nos utilisateurs. »*

---

### [03:00 – 04:30] Slide 03 : Contexte Territorial & Problématique Métier
**Orateur : Abdelkader Heddi**
* **Ce qu'on projette :** Les 3 fractures identifiées (évasion, prédation privée, fracture numérique) face à la proposition de valeur ShopLoc.
* **Critère ciblé :** **Critère 3** *(Réponse aux problématiques MOA)*.
* **Discours oral suggéré :**
  > *« Merci Khalil. Pour concevoir ShopLoc, nous sommes partis du terrain. Nos centres-villes subissent aujourd'hui une triple fracture :  
  > 1. Une évasion commerciale continue vers les zones périphériques et le e-commerce mondialisé ;  
  > 2. Une prédation financière insoutenable : les plateformes de livraison privées prélèvent entre 20 et 30 % de commission sur chaque transaction, asphyxiant les artisans de proximité ;  
  > 3. Et une fracture numérique sévère : plus d'un tiers de nos aînés ne disposent pas d'un smartphone récent ou refusent les paiements dématérialisés sur Internet.  
  > La réponse de ShopLoc est sans compromis : une plateforme publique territoriale, 100 % gratuite pour les usagers, sans commission sur les ventes pour les commerçants, dont l'unique but est d'amener physiquement le citoyen dans les boutiques de son quartier. »*

---

### [04:30 – 06:00] Slide 04 : Personas Clés & Réponses Inclusives
**Orateur : Abdelkader Heddi**
* **Ce qu'on projette :** Les 4 profils personas (Pierre 74 ans, Suzanne 22 ans, Julie & Arthur 32 ans, Marius 27 ans).
* **Critères ciblés :** **Critère 4** *(Totalité du périmètre)* & **Critère 5** *(Solutions innovantes et adaptées)*.
* **Discours oral suggéré :**
  > *« Pour valider l'universalité de notre solution, nous avons modélisé 4 personas représentatifs de l'écosystème :  
  > - Pierre, 74 ans, retraité habitué de son centre-ville : pour lui, aucune barrière technologique. Grâce à notre **Carte citoyenne physique dotée d'un QR code imprimé**, Pierre cumule ses avantages sans posséder de smartphone. L'interface respecte le niveau de contraste AAA des normes RGAA ;  
  > - Suzanne, jeune artisane boulangère : son impératif est la rapidité. Le scan client en caisse prend moins de 3 secondes, et elle conserve l'autonomie totale de son stock ;  
  > - Julie et Arthur, couple d'actifs éco-responsables : ils commandent en Click & Collect multi-commerces sur un panier unifié et retirent leurs achats à pied sous 2 heures ;  
  > - Enfin Marius, administrateur à la mairie : il dispose d'un tableau de bord macroscopique des flux économiques locaux, dans le respect absolu du RGPD et du secret des affaires.  
  > Je cède la parole à Ilyas pour vous détailler les règles métier et notre feuille de route. »*

---

### [06:00 – 07:30] Slide 05 : Périmètre Métier & Double Moteur de Fidélité
**Orateur : Ilyas Ait Ali**
* **Ce qu'on projette :** Architecture conceptuelle découplée : Moteur Marchand privé vs Moteur Territorial VFP public.
* **Critères ciblés :** **Critère 3** *(Fonctionnalités des services)* & **Critère 5** *(Solutions innovantes)*.
* **Discours oral suggéré :**
  > *« Merci Abdelkader. L'innovation majeure de ShopLoc réside dans le découplage strict entre deux moteurs de fidélisation indépendants :  
  > D'une part, le **Moteur Marchand décentralisé** : chaque commerçant reste le maître absolu de sa relation client. 1 euro dépensé rapporte des points propres à la boutique, et le commerçant choisit librement ses cadeaux. Pour sécuriser le commerçant contre la fraude, l'obtention d'un lot exige au moins un historique d'achat antérieur.  
  > D'autre part, le **Moteur Territorial VFP** : ici, la Mairie ne récompense pas le montant dépensé, mais la **régularité de la fréquentation piétonne**. Le statut VFP se déclenche dès lors qu'un citoyen enregistre **au moins 10 passages physiques dans des commerces sur une fenêtre glissante de 15 jours consécutifs**.  
  > L'usager débloque alors un avantage civique éco-responsable : 1 ticket de transport en commun ou 20 minutes de stationnement municipal offert. Le financement de cet avantage est intégralement pris en charge par le budget mobilités de la collectivité. »*

---

### [07:30 – 09:00] Slide 06 : User Story Mapping & Trajectoire en 3 Releases
**Orateur : Ilyas Ait Ali**
* **Ce qu'on projette :** Diagramme haute définition User Story Mapping (Figure 3.3) et tableau des 3 releases contractuelles.
* **Critères ciblés :** **Critère 2** *(Respect des délais)* & **Critère 4** *(Périmètre couvert)*.
* **Discours oral suggéré :**
  > *« Pour ordonnancer notre développement, nous avons formalisé la cartographie User Story Mapping projetée à l'écran, selon la méthode MoSCoW. Nous déclinons la trajectoire produit en trois releases nettes :  
  > - La **Release 1 (MVP — Jalon R4 au 18 décembre 2026)** : elle fournit le socle essentiel, à savoir l'annuaire des commerces, le catalogue en ligne, le panier Click & Collect multi-boutiques et la gestion des réservations ;  
  > - La **Release 2 (V1.5 — Février 2027)** : elle apporte la gestion des stocks simplifiée pour le commerçant, les alertes de retrait et le moteur de fidélité marchande ;  
  > - La **Release 3 (V2 Complète — Jalon R5 au 19 mars 2027)** : elle parachève la solution avec le moteur VFP territorial complet, la simulation des mobilités urbaines, le portail d'administration communal et les bilans d'éco-conception.  
  > Rayane va maintenant vous présenter l'architecture technique qui soutient cette vision. »*

---

### [09:00 – 10:30] Slide 07 : Architecture 3-Tiers Modulaire & Choix Outils
**Orateur : Rayane Alli**
* **Ce qu'on projette :** Diagramme d'architecture 3-tiers modulaire épuré (Figure 4.1) avec logos devicon officiels.
* **Critère ciblé :** **Critère 7** *(Maîtrise des technologies proposées)*.
* **Discours oral suggéré :**
  > *« Merci Ilyas. Sur le plan technique, nous avons fait le choix de la rigueur industrielle et de la sobriété.  
  > Nous rejetons explicitement l'usage prématuré de microservices. Pour une échelle territoriale de 100 à 200 commerces, les microservices multiplient les coûts d'infrastructure par cinq et introduisent une complexité réseau injustifiée.  
  > Nous avons donc retenu une **architecture 3-Tiers sous forme de monolithe modulaire** :  
  > - En présentation : React 18 avec TypeScript et Vite, offrant un temps de chargement minimal et une compatibilité PWA pour une utilisation fluide sur mobile comme sur desktop ;  
  > - En logique métier : Java 21 et Spring Boot 3, garantissant un typage strict, une modularité par packages étanches et des contrats d'API documentés sous OpenAPI 3.1 ;  
  > - En persistance : PostgreSQL 16, avec partitionnement logique multi-tenant pour isoler strictement les données par commune.  
  > Ce choix nous assure une frugalité exemplaire en phase d'exploitation. »*

---

### [10:30 – 12:00] Slide 08 : Fiabilité Transactionnelle & Démonstrateur Portable
**Orateur : Rayane Alli**
* **Ce qu'on projette :** Mécanisme du Two-Phase Commit (2PC) Click & Collect et architecture des Mocks partenaires.
* **Critères ciblés :** **Critère 5** *(Solutions adaptées)* & **Critère 7** *(Rigueur d'ingénierie)*.
* **Discours oral suggéré :**
  > *« Deux points d'ingénierie renforcent la fiabilité opérationnelle de notre solution :  
  > Premièrement, la gestion des commandes Click & Collect via un **protocole inspiré du Two-Phase Commit (2PC)** :  
  > Lorsqu'un client réserve un article en ligne, une notification parvient à Suzanne sur son terminal de caisse, posant un verrou temporaire sur le stock. Elle dispose de 2 heures pour confirmer la disponibilité physique en rayon. Dès validation, la commande est confirmée et le stock décrémenté. Si le commerçant ne répond pas dans le délai, le système effectue un rollback automatique, libérant l'article et informant le client. Cela élimine tout risque de faux espoir ou de conflit de stock.  
  > Deuxièmement, la simulation des services partenaires : conformément aux consignes du sujet, les interfaces avec la banque et le système d'information de la ville sont émulées par des **Mocks RESTful étanches**.  
  > Enfin, l'ensemble de la pile applicative est conteneurisé sous Docker. Lors des soutenances R4 et R5, le démonstrateur pourra être instancié en une seule commande `docker compose up -d`.  
  > Je laisse Gautam vous exposer la planification annuelle et l'étude financière. »*

---

### [12:00 – 13:15] Slide 09 : Diagramme de Gantt & Chemin Critique
**Orateur : Gautam Demeulemeester**
* **Ce qu'on projette :** Diagramme de Gantt Annuel Officiel HD (Figure 5.1) et tableau des 5 jalons contractuels.
* **Critère ciblé :** **Critère 2** *(Capacité à respecter les délais)*.
* **Discours oral suggéré :**
  > *« Merci Rayane. Notre calendrier de production s'aligne scrupuleusement sur les 5 jalons contractuels de l'appel d'offres :  
  > - R1 aujourd'hui avec le cadrage et l'offre économique ;  
  > - R2 le 12 octobre pour l'outillage et l'environnement DevOps ;  
  > - R3 le 30 novembre pour l'évaluation approfondie de la rentabilité (VAN, TRI, ROI) ;  
  > - R4 le 18 décembre pour l'architecture V1 et le premier démonstrateur Click & Collect ;  
  > - Et R5 le 19 mars pour le système complet intégrant la fidélité VFP.  
  > Le chemin critique traverse sans ambiguïté les briques fonctionnelles d'authentification, de réservation 2PC et de calcul VFP.  
  > Pour neutraliser tout aléa, notre planification intègre des **buffers de sécurité de 72 heures** avant chaque livraison, et nous avons neutralisé les semaines d'interruption pédagogique et la semaine IA. »*

---

### [13:15 – 14:15] Slide 10 : Analyse des Coûts Complets (Build & Run)
**Orateur : Gautam Demeulemeester**
* **Ce qu'on projette :** Charges directes (15,9 k€), charges indirectes (36 k€), répartition secondaire et coût d'unité d'œuvre (87,80 €/h).
* **Critère ciblé :** **Critère 1** *(Coût détaillé du projet : Build, Exploitation, Maintenance)*.
* **Discours oral suggéré :**
  > *« Venons-en au chiffrage de notre proposition, établi selon la méthode académique des coûts complets par centres d'analyse :  
  > En **charges directes de fabrication (Build)**, nous comptabilisons 480 heures de main-d'œuvre directe d'ingénierie au taux chargé de 25 €/h, soit 12 000 €, complétées par 2 400 € d'achats directs d'infrastructures (serveurs VPS, noms de domaine, certificats) et 1 500 € de démarches commerciales.  
  > En **charges indirectes**, les 36 000 € de charges de structure de l'entreprise (locaux, assurances, direction, serveurs de test) font l'objet d'une répartition secondaire intégrale : 24 960 € sont déversés sur le centre principal Production, et 11 040 € sur le centre Commercial.  
  > En retenant l'heure de développement comme unité d'œuvre, nous obtenons un **coût complet unitaire de 87,80 € / h d'UO**. Cela garantit à la collectivité une transparence arithmétique totale, sans coût caché. »*

---

### [14:15 – 15:00] Slide 11 : Modèle Économique SaaS & Rentabilité
**Orateur : Gautam Demeulemeester**
* **Ce qu'on projette :** Convention tripartite, compte de résultat An 1 (88 k€ de CA, 70,8 k€ de coûts complets, marge nette 17,2 k€ / 19,5 %).
* **Critère ciblé :** **Critère 1** *(Modèle économique et rentabilité à long terme)*.
* **Discours oral suggéré :**
  > *« Pour pérenniser le dispositif, notre modèle repose sur une **convention tripartite équilibrée** :  
  > - La Mairie subventionne l'ingénierie et finance les tickets de transport et stationnement ;  
  > - L'Association des Commerçants fédère les boutiques locales ;  
  > - Chaque commerçant adhérent s'acquitte d'un abonnement forfaitaire modique de **40 € HT par mois**, sans aucun prélèvement sur ses ventes.  
  > Sur la base d'une commune moyenne pilote comptant 120 commerces partenaires, le chiffre d'affaires annuel atteint **88 000 €**.  
  > Face à un coût de revient complet d'exploitation et de maintenance de 70 800 €, notre entreprise étudiante dégage un résultat net positif de **17 200 €**, soit un **taux de marge nette de 19,5 %**.  
  > Notre seuil de rentabilité est franchi dès 38 commerces adhérents. Le modèle est donc robuste et assure la viabilité pérenne de ShopLoc. »*

---

### [15:00] Slide 12 : Synthèse de l'Offre & Clôture
**Orateur : Khalil Bouchama**
* **Ce qu'on projette :** Les 4 piliers d'engagement de Garik (Souveraineté, Zéro exclusion, Rigueur de livraison, Transparence éthique) et message de clôture.
* **Critères ciblés :** Synthèse générale des 8 critères.
* **Discours oral suggéré :**
  > *« En synthèse, l'offre de l'entreprise Garik répond point par point aux 8 critères de la consultation : une gouvernance agile maîtrisée, une architecture éco-conçue, un coût complet rigoureusement justifié et une véritable réponse humaine à l'attractivité de notre territoire.  
  > Nous certifions l'appropriation intégrale de l'ensemble des concepts présentés par notre équipe d'étudiants-ingénieurs.  
  > Nous vous remercions pour votre écoute et nous sommes désormais à votre entière disposition pour répondre à vos questions. »*

---

## 3. Matrice de Préparation aux Questions / Réponses du Jury (5 minutes Q&A)

### Q1 : « Pourquoi avoir choisi une architecture modulaire plutôt que des microservices ? »
* **Répondant principal :** **Rayane Alli**
* **Argument clé :** Frugalité et éco-conception (Run). À l'échelle d'une commune de 100 à 200 commerçants, un cluster Kubernetes consomme inutilement 4 à 8 Go de RAM rien que pour le plan de contrôle, et multiplie la latence réseau. Le monolithe modulaire Spring Boot offre le même niveau d'isolation logique par packages sans surcoût d'hébergement.

### Q2 : « Comment évitez-vous qu'un usager valide 10 passages frauduleux en une journée pour obtenir son ticket de bus ? »
* **Répondant principal :** **Ilyas Ait Ali** ou **Abdelkader Heddi**
* **Argument clé :** La règle VFP impose une fenêtre glissante de 15 jours consécutifs avec un intervalle temporel minimum entre deux scans dans un même commerce. De plus, pour débloquer les récompenses chez les commerçants, le système vérifie qu'il y a eu au moins un achat antérieur authentifié en caisse.

### Q3 : « Pourquoi facturer 40 € par mois aux commerçants plutôt qu'une commission au pourcentage ? »
* **Répondant principal :** **Gautam Demeulemeester**
* **Argument clé :** La commission au pourcentage décourage les commerçants à forte valeur unitaire (boucheries, bijouteries) et pousse à la fraude hors-application. Le forfait fixe de 40 € HT/mois est indolore (environ 1,30 € par jour), préserve l'intégralité de la marge marchande et garantit à l'entreprise un revenu récurrent prévisible (ARR).

### Q4 : « Quelle a été la part exacte de l'Intelligence Artificielle dans vos productions ? »
* **Répondant principal :** **Khalil Bouchama**
* **Argument clé (Conformité stricte à la page 6 du sujet) :** Transparence totale. L'IA a été mobilisée comme un assistant outillé pour accélérer la mise en forme Markdown, la syntaxe des scripts et la génération vectorielle des diagrammes. En revanche, 100 % de l'analyse fonctionnelle, des règles de gestion VFP, du découpage WBS et des calculs de coûts complets ont été conçus, vérifiés et maîtrisés par les 5 membres de l'équipe Garik.
