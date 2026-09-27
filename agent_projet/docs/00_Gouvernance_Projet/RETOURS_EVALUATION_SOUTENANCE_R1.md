# RAPPORT D'ÉVALUATION & CAPITALISATION DES RETOURS MOA (JALON R1)
## Projet ShopLoc — Master 2 MIAGE — UE Génie Logiciel par la Pratique (GLOP) 2026-2027
### Université de Lille — Faculté des Sciences et Technologies — Département Informatique

---

## 1. Informations Générales sur le Document

| Champ | Information |
|---|---|
| **Intitulé du Projet** | Plateforme ShopLoc — Marketplace & Fidélisation Territoriale |
| **Identifiant Officiel** | `MiageShopLoc` |
| **Titre du Document** | Registre d'Évaluation & Plan d'Action Post-Soutenance R1 |
| **Référence Documentaire** | `GLOP-2026-GOUV-RETOUR-R1-v1.0` |
| **Date d'Émission** | 27 Septembre 2026 |
| **Statut du Document** | Validé — Référentiel interne d'ingénierie et d'ajustement d'équipe |
| **Équipe Prestataire (Maître d'Œuvre)** | Entreprise Garik (5 élèves-ingénieurs M2 MIAGE) |
| **Maîtrise d'Ouvrage (Jury Évaluateur)** | Laurence Duchien, Anne Etien, François Secchi, Jérémy Woirhaye |
| **Document de Référence Évalué** | `GARIK_GLOP-2026-LIVRABLE-R1.pdf` (Version officielle soumise le 18/09/2026) |

---

## 2. Synthèse Exécutive des Retours de la MOA

À l'issue de la remise du livrable R1 le 18 septembre 2026 et de la soutenance orale du 21 septembre 2026 en amphithéâtre Turing, la maîtrise d'ouvrage (équipe pédagogique de l'UE GLOP) a transmis une synthèse critique de relecture sur le document soumis.

Les questions posées lors de la soutenance ont confirmé l'analyse du document écrit. Les retours se structurent autour de **cinq axes d'amélioration majeurs** :

1. **Étude fonctionnelle superficielle & Manque de Cas d'Utilisation formalisés** : Le sujet n'a pas été exploré avec une profondeur suffisante d'ingénierie logicielle. Le formalisme agile (User Story Mapping) a masqué l'absence d'une véritable analyse des cas d'utilisation UML (acteurs, préconditions, scénarios d'exception, gestion des pannes et règles de gestion détaillées).
2. **Absence d'une véritable analyse des risques** : La section 5.3 du livrable s'est limitée à 3 mesures d'organisation d'équipe génériques. Une véritable matrice de gestion des risques conforme aux standards (ISO 31000 : probabilité, gravité, criticité, plans de mitigation et plan de continuité d'activité) est formellement requise.
3. **Périmètre de la Release 1 (décembre) irréaliste & Découpage de planning à refondre** : L'équipe a promis pour décembre (Jalon R4) l'intégralité du produit (les 10 User Stories Must Have du MVP). Ce périmètre est irréaliste pour une première livraison de fin de semestre 3. Le découpage doit être resserré sur un périmètre restreint et atteignable (l'architecture complète + un seul composant vertical déployé et testé), et le diagramme de Gantt doit être réajusté en conséquence.
4. **Ambiguïté sur les rôles institutionnels & Rôles d'administration flous** :
   - Qui est ShopLoc ? Distinction nette exigée entre ShopLoc (l'entreprise donneuse d'ordre / marque de la plateforme) et Garik (l'équipe prestataire / société d'ingénierie).
   - Quels sont les rôles d'administrateurs ? Nécessité de séparer clairement l'administration technique, l'administration municipale, l'administration de l'association de commerçants et la gestion de boutique.
5. **Fragilité de la modélisation financière** : Incohérence constatée entre le volume horaire global annoncé pour l'équipe (900 à 1 000 heures) et les heures de Main d'Œuvre Directe valorisées au tableau des coûts (480 heures). Hypothèses de commercialisation SaaS à consolider avant le jalon financier dédié R3.

---

## 3. Analyse Détaillée des 5 Axes Critiques & Relevé du Document Annoté

### Axe 1 : Analyse Fonctionnelle Approfondie & Cas d'Utilisation UML

#### Constat & Diagnostic
* Dans le document soumis (pages 8 à 10), la démarche d'ingénierie a sauté directement des 5 personas narratifs vers une cartographie de *User Story Mapping* (modèle Jeff Patton), sans formaliser les cas d'utilisation selon les standards du génie logiciel.
* En page 6 du document remis, le paragraphe d'introduction de la méthode APTE (*« à travers l'outil de la Bête à cornes »*) est surligné par le jury : l'analyse du besoin fondamentale a été amorcée mais n'a pas été déclinée jusqu'au niveau d'exigence attendu pour la spécification des cas d'usage nominatifs et dégradés.
* Les comportements en cas d'anomalies opérationnelles (rupture de stock concurrente lors d'un panier multi-commerces, indisponibilité de l'API bancaire, non-retrait d'une commande par le client dit *no-show*, contestation de passage en caisse, contrôle en voirie sans réseau) n'étaient pas spécifiés formellement.

#### Décision d'Ingénierie & Action Corrective
* Élaborer un **Diagramme de Cas d'Utilisation UML global** modélisant l'ensemble des cas d'usage du système avec formalisation explicite des relations de dépendance (`<<include>>`, `<<extend>>`) et de généralisation d'acteurs.
* Rédiger **cinq Fiches de Cas d'Utilisation Approfondies** au standard international Cockburn / AFNOR :
  1. `UC-01` : Passer une commande Click & Collect multi-commerces sous protocole transactionnel en deux phases (2PC).
  2. `UC-02` : Enregistrer un passage en caisse commerçante, scanner le pass optique et créditer la double fidélité en moins de 3 secondes.
  3. `UC-03` : Activer une franchise de stationnement de 20 minutes (Citoyen VFP) et contrôler la validité de stationnement en voirie (Police municipale).
  4. `UC-04` : Évaluer la régularité d'achats sur fenêtre glissante de 15 jours et attribuer/suspendre le statut VFP (Batch nocturne).
  5. `UC-05` : Conventionner une boutique adhérente et provisionner un nouveau commerce (Association des commerçants & Mairie).
* Chaque fiche de cas d'utilisation doit spécifier : Acteur principal, Acteurs secondaires, Préconditions, Déclencheur, Scénario nominal pas-à-pas, Scénarios d'exception/alternatifs, Postconditions et Règles de gestion associées.

---

### Axe 2 : Registre Formel des Risques Projet (Norme ISO 31000)

#### Constat & Diagnostic
* En page 15 du document soumis, la sous-section *5.3 Dispositif de sécurisation des délais et gestion des risques* ne comportait qu'une description organisationnelle en trois points (temps de travail moyen, buffer de 72h avant jalon, réunion hebdomadaire).
* Pour un jury universitaire d'ingénierie logicielle, ce paragraphe constitue un dispositif de gouvernance d'équipe, mais nullement une **analyse de risques**.
* Aucun registre des aléas n'était présenté, aucune échelle de probabilité ni de gravité n'était définie, et aucune stratégie formelle de mitigation ou de contingence n'était associée aux aléas techniques, juridiques et métier du projet ShopLoc.

#### Décision d'Ingénierie & Action Corrective
* Intégrer la **Matrice d'Analyse des Risques ISO 31000** pré-calibrée dans nos travaux de gouvernance interne, structurée selon une échelle formelle :
  * Probabilité d'occurrence : de 1 (Très faible) à 5 (Quasi-certaine).
  * Gravité de l'impact : de 1 (Négligeable) à 5 (Critique / Bloquant).
  * Score de Criticité : $C = P \times G$ (Mineur : 1-4, Modéré : 5-9, Majeur : 10-15, Critique : 16-25).
* Renseigner le registre exhaustif couvrant les 6 risques majeurs :
  * `R-01` (Technique) : *Complexité de l'orchestration transactionnelle 2PC sur panier multi-boutiques* ($P=3, G=4 \Rightarrow C=12$). Mitigation : Transactions ACID locales PostgreSQL, mocks bancaires OpenAPI 3.1, couverture de tests TDD dès le Sprint 2.
  * `R-02` (Métier / Adoption) : *Résistance des commerçants à la saisie manuelle des stocks et temps de passage en caisse* ($P=3, G=3 \Rightarrow C=9$). Mitigation : Interface commerçante ultra-frugale, scan QR en moins de 2 secondes sans clic additionnel, pass papier universel bi-média (ADR-012).
  * `R-03` (Sécurité / RGPD) : *Fuite de données d'achats nominatives ou transgression du secret des affaires inter-commerces* ($P=2, G=5 \Rightarrow C=10$). Mitigation : Pseudonymisation salée SHA-256, cloisonnement strict par `tenant_id`, requêtes d'agrégation k-anonymisées pour les tableaux de bord municipaux.
  * `R-04` (Organisationnel / Humain) : *Déséquilibre d'investissement ou surcharge asymétrique au sein de l'équipe* ($P=3, G=4 \Rightarrow C=12$). Mitigation : Principe du Scrum Master tournant à chaque jalon, rotation des binômes, suivi transparent de la répartition des commits sur GitLab.
  * `R-05` (Calendrier / Dérive) : *Glissement des échéances de livraison lié aux examens ou contraintes d'alternance* ($P=3, G=4 \Rightarrow C=12$). Mitigation : Règle stricte du code freeze à J-3 avant chaque jalon, sanctuarisation du backlog MoSCoW.
  * `R-06` (Partenaires) : *Indisponibilité des serveurs réels de la collectivité et des opérateurs tiers* ($P=4, G=3 \Rightarrow C=12$). Mitigation : Découplage total via simulateurs (mocks REST) conteneurisés sous Docker Compose dès le jalon R2.
* Définir un **Plan de Continuité d'Activité (PCA)** incluant le protocole d'escalade sous 24h et les règles d'arbitrage en cas de blocage.

---

### Axe 3 : Réalisme de la Release 1 de Décembre & Découpage de Gantt

#### Constat & Diagnostic
* En page 8 du livrable (texte surligné dans le document) et sur le tableau de Story Mapping en page 9, l'équipe a défini la **Release 1 (MVP)** comme intégrant la totalité des 10 User Stories *Must Have* pour les jalons R4 et R5.
* En page 14, le texte d'introduction du diagramme de Gantt prévisionnel est surligné par le jury : le planning présenté ne démontrait pas la faisabilité concrète d'une telle masse de développements entre mi-octobre et mi-décembre 2026 (7 semaines effectives de développement).
* **Consigne contractuelle officielle de l'UE GLOP (Sujet, page 7)** :  
  Pour le jalon R4 du 18 décembre 2026, l'attendu est formellement :
  > *« Réaliser **un (au choix) des composants logiciels** avec les outils choisis jusqu'au déploiement et aux tests. »*
* Vouloir livrer l'intégralité du système (Panier multi-commerces + Algorithme d'optimisation piétonne TSP + Scan caisse + Moteur de fidélité VFP + Vouchers bus et parking + Dashboards DSI) pour la soutenance de janvier constituait un engagement irréaliste sanctionné par les évaluateurs.

#### Décision d'Ingénierie & Action Corrective
* **Restructuration du Découpage par Release (Périmètres R4 vs R5)** :
  * **Jalon R4 — 18 Décembre 2026 (Release V1 / Prototype Démontrable)** :
    * *Dossier d'Architecture Logicielle complet* : Vues 4+1 C4 (contexte, conteneurs, composants, code), diagrammes de classes du domaine métier, schéma relationnel PostgreSQL normalisé en 3NF et justifications des propriétés NFR (réutilisabilité, maintenabilité, performance, accessibilité).
    * *Réalisation d'UN composant logiciel vertical déployé de bout en bout* : **Le Composant de Commande & Panier Multi-Commerces Click & Collect sous protocole Two-Phase Commit (2PC)** (couvrant l'API REST Spring Boot, la persistance PostgreSQL transactionnelle, le mock bancaire conteneurisé, la couverture de tests unitaires/intégration TDD $\ge 80\,\%$ et l'interface web de commande React/TypeScript).
    * *Pitch de projet* : proposition de valeur, choix marketing et engagements RSE.
  * **Jalon R5 — 19 Mars 2027 (Release V2 / Solution Complète Industrielle)** :
    * Intégration des composants complémentaires : Caisse express marchande (< 3s), Moteur batch SQL de double fidélité (Points boutique + Statut VFP sur 15 jours glissants), Module d'émission des titres mobilité (Bus et Stationnement 20 min).
    * Portail de reporting et supervision municipale (Marius DSI).
    * Campagne de tests de charge, recette d'ensemble, bilan d'éco-conception et clôture du projet.
* **Mise à jour du Diagramme de Gantt** : Repositionnement des vagues de développement avec granularité fine par composant, identification des dépendances techniques et matérialisation claire du chemin critique.

---

### Axe 4 : Clarification Institutionnelle (ShopLoc) & Précision des Rôles d'Administration

#### Constat & Diagnostic
* Le livrable entretenait une confusion sémantique entre **ShopLoc**, **Garik**, la **Mairie** et l'**Association des commerçants**. Le jury a explicitement interrogé l'équipe : *« Qui est ShopLoc ? »*.
* Les rôles d'administration étaient regroupés sous des appellations vagues (ex. *« Admin mairie »*, *« Tous rôles »* sur l'US-02), sans modélisation formelle du modèle de sécurité et des habilitations d'accès (*Role-Based Access Control* - RBAC).

#### Décision d'Ingénierie & Action Corrective
* **Clarification Institutionnelle Intangible (ADR-020)** :
  * **ShopLoc** : Désigne la **société donneuse d'ordre et éditrice de la solution SaaS territoriale**, propriétaire de la marque et du concept de marketplace locale mutualisée. C'est l'entité qui lance l'appel d'offres initial pour équiper les collectivités locales françaises.
  * **Garik** : Désigne notre **société d'ingénierie logicielle prestataire (maître d'œuvre)**, constituée des 5 élèves-ingénieurs MIAGE, titulaire du marché pour la conception, le développement, l'intégration continue, le déploiement et la maintenance de la plateforme logicielle.
  * **La Mairie (Collectivité territoriale)** : Client institutionnel qui souscrit à la plateforme ShopLoc via une convention de revitalisation du cœur de ville, finance les avantages mobilité douce et mandate l'association de commerçants.
  * **L'Association des Commerçants de Centre-Ville** : Organisme pivot de terrain, tiers de confiance assurant l'animation du programme, l'enrôlement des artisans adhérents et la distribution des supports physiques.
* **Matrice Formelle des 4 Niveaux d'Administration RBAC** :
  1. `ROLE_SUPER_ADMIN` (**Super-Administrateur Plateforme ShopLoc - Exploitant SaaS**) : Habilité à provisionner une nouvelle ville (`tenant_id`), surveiller les métriques techniques globales d'infrastructure, configurer les passerelles partenaires et gérer les incidents système transverses.
  2. `ROLE_CITY_ADMIN` (**Administrateur Collectivité Territoriale - Marius / DSI Mairie**) : Habilité à valider la convention tripartite communale, paramétrer les plafonds budgétaires des subventions mobilité (enveloppes de tickets de bus Ilévia et quotas d'heures de stationnement voirie), consulter les tableaux de bord macroscopiques k-anonymisés. *Interdiction stricte d'accès aux flux marchands nominatifs et aux paniers d'achats individuels (secret des affaires et RGPD).*
  3. `ROLE_ASSOCIATION_ADMIN` (**Administrateur Association des Commerçants**) : Habilité à instruire les demandes d'adhésion des commerces locaux, vérifier les statuts Kbis et conventions, activer ou suspendre les boutiques sur la marketplace locale, et administrer le catalogue des lots et cadeaux communs de la ville.
  4. `ROLE_MERCHANT_ADMIN` (**Gestionnaire Boutique - Suzanne / Artisane**) : Responsable exclusif de l'administration de son commerce, de la saisie et mise à jour de ses stocks d'articles, de la validation des retraits Click & Collect et de la consultation de ses propres statistiques de ventes. *Étanchéité totale interdisant toute visibilité sur l'activité des confrères concurrents.*

---

### Axe 5 : Consolidation de la Modélisation Financière (Coûts Complets & Modèle SaaS)

#### Constat & Diagnostic
* En page 18 du livrable soumis, la ligne du tableau des charges indirectes *« Centre Production & Maintenance (480 heures de développement à 52,00 € / h = 24 960,00 €) »* est directement mise en exergue par les annotations de relecture.
* Le tableau de calcul financier impute un volume de **480 heures de développement**, alors que la page 15 du document annonçait explicitement : *« L'investissement de chaque membre est calibré à environ 6 à 8 heures de travail effectif par semaine sur les 25 semaines actives du projet, soit un volume global de 900 à 1 000 heures de travail sur l'ensemble de la réalisation »*.
* Cette incohérence arithmétique (480h retenues vs 1 000h déclarées) fragilise la crédibilité de l'évaluation des coûts de revient complets.
* De plus, la simulation de rentabilité SaaS en section 6.5 (page 19) proposant un abonnement annuel de 3 900 € HT par commune sur 3 communes partenaires génère un chiffre d'affaires cumulé sur 3 ans de $3 \times 3\,900 \times 3 = 35\,100\text{ \euro}$, ce qui demeure insuffisant pour amortir les $50\,400\text{ \euro}$ de coût de revient complet et dégager la marge bénéficiaire cible de 20 % ($60\,480\text{ \euro}$).

#### Décision d'Ingénierie & Action Corrective
* **Réconciliation Globale du Bilan Horaire** :
  * Décomposer formellement le volume d'effort global de 1 000 heures en séparant :
    * La Main d'Œuvre Directe de développement logiciel pur (Build & intégration).
    * Le temps dédié à la gouvernance, la gestion de projet, l'assurance qualité et les revues documentaires.
    * Le temps dédié à la relation commerciale, l'avant-vente et l'assistance au déploiement sur site.
* **Calibrage Rigoureux du Modèle Économique pour le Jalon R3 (30 Novembre 2026)** :
  * Le Jalon R3 étant spécifiquement dédié à l'évaluation de la rentabilité de l'investissement (calcul du ROI, de la Valeur Actuelle Nette - VAN et du Taux de Rentabilité Interne - TRI), consolider un compte de résultat prévisionnel sur 3 ans cohérent :
    * Hypothèse réaliste de déploiement progressif : 1 collectivité pilote en Année 1 (subvention d'amorçage + abonnement), 3 collectivités en Année 2, 8 collectivités en Année 3.
    * Grille tarifaire segmentée selon la taille de commune conformément au sujet (petite ville < 20k hab., ville moyenne 20k-100k hab., grande métropole > 100k hab.).
    * Calcul rigoureux du point mort (seuil de rentabilité en volume et en date).

---

## 4. Feuille de Route d'Ajustement par Jalon Contractuel

```text
Calendrier de Déploiement des Correctifs MOA (2026-2027)
├── JALON R1 (Addendum & Référentiel) : Formalisation UML Use Cases, Risques ISO 31000, Clarification ShopLoc / Rôles
├── JALON R2 (12 Octobre 2026)        : Socle DevOps, GitLab, Docker multi-stage & Simulateurs alignés sur les Use Cases
├── JALON R3 (30 Novembre 2026)       : Étude Financière approfondie (Coûts complets, P&L 3 ans, VAN, TRI, Seuil de rentabilité)
├── JALON R4 (18 Décembre 2026)       : Architecture V1 C4 + 1 Composant vertical déployé (Panier 2PC) sous TDD
└── JALON R5 (19 Mars 2027)           : Système V2 complet (Fidélité, Mobilité, Dashboards) & Soutenance finale de clôture
```

### 1. Actions Immédiates pour le Référentiel R1 (Addendum de Cadrage)
* [x] Enregistrement officiel de la décision d'arbitrage `ADR-020` dans `DECISIONS.md`.
* [x] Création du présent rapport de capitalisation des retours dans la gouvernance projet.
* [ ] Modélisation du diagramme de cas d'utilisation UML global du système ShopLoc.
* [ ] Rédaction des fiches de cas d'utilisation Cockburn pour les 5 processus clés.
* [ ] Mise à jour du registre des risques (tableau complet ISO 31000 avec criticité et parades).

### 2. Directives Opérationnelles pour le Jalon R2 (12 Octobre 2026)
* Responsable : **Rayane Alli** (*Scrum Master Sprint 1 / Spécialiste Outils*).
* Le choix et la configuration des outils doivent refléter directement la clarification des rôles :
  * Dépôt officiel GitLab configuré avec étanchéité absolue (aucune trace d'IA).
  * Pipeline `.gitlab-ci.yml` configuré pour valider automatiquement la compilation, les tests unitaires JUnit et le Quality Gate SonarQube ($\ge 80\,\%$ de couverture).
  * Fichier `docker-compose.yml` multi-services démarrant en une seule commande le backend Spring Boot, la base PostgreSQL 16, le frontend React et les simulateurs externes.
  * Les 3 simulateurs (mocks REST OpenAPI 3.1) doivent implémenter précisément les endpoints des cas d'utilisation révisés (débit/rollback 2PC, validation des titres Ilévia et lecture de plaque voirie).

### 3. Directives Opérationnelles pour le Jalon R3 (30 Novembre 2026)
* Responsable : **Gautam Demeulemeester** (*Scrum Master Sprint 2 / Gestion Financière*).
* Élaboration du dossier financier complet basé sur les coûts complets, éliminant l'incohérence horaire de R1, avec calculs actualisés de VAN, TRI et retour sur investissement sur 36 mois.

### 4. Directives Opérationnelles pour le Jalon R4 (18 Décembre 2026)
* Responsable : **Ilyas Ait Ali** (*Scrum Master Sprint 3 / Architecture & Prototypage*).
* Focalisation absolue sur la production des vues d'architecture 4+1 C4 et la réalisation du **Composant Panier & Réservation 2PC** déployé sous Docker, démontrable et testé sous TDD, conformément aux exigences de cadrage resserré de la MOA.
