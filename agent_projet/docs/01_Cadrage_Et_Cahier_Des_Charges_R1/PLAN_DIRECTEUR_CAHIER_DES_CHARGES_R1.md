# PLAN DIRECTEUR & CADRE MÉTHODOLOGIQUE DU CAHIER DES CHARGES (R1)

## Université de Lille — Faculté des Sciences et Technologies — M2 MIAGE

### UE Génie Logiciel par la Pratique (GLOP) 2026-2027

---

## Informations Documentaires

| Métadonnée                       | Valeur                                                               |
| ---------------------------------- | -------------------------------------------------------------------- |
| **Intitulé du Projet**      | Plateforme ShopLoc — Marketplace & Fidélisation Territoriale       |
| **Identifiant Officiel**     | `MiageShopLoc`                                                     |
| **Référence Documentaire** | `GLOP-2026-R1-PLAN-DIRECTEUR-v1.0`                                 |
| **Type de Document**         | Feuille de Route Méthodologique & Structure Validée du Livrable R1 |
| **Statut du Document**       | Validé par l'équipe projet — Prêt pour exécution                |
| **Date d'Arrêté**          | 16 Septembre 2026                                                    |

---

## 1. Principes Directeurs & Règle d'Étanchéité Documentaire

Conformément à la Règle Permanente 7 de [`PROJECT_RULES.md`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/PROJECT_RULES.md) et la Règle Permanente 11 de [`.antigravity/instructions.md`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/.antigravity/instructions.md), la démarche de rédaction repose sur deux principes cardinaux :

### 1.1. Posture Professionnelle des Livrables Officiels

- **Niveau d'exigence éditeur / scale-up** : Le Cahier des Charges (Livrable R1), les diagrammes BPMN, le MCD, l'architecture logicielle et le code source doivent être rédigés du point de vue d'une société d'ingénierie logicielle répondant à un appel d'offres public.
- **Interdiction absolue du contexte étudiant** : Aucune mention relative au profil de l'équipe (élèves en apprentissage, manque d'expérience, contraintes académiques) ne doit figurer dans les livrables du projet. Tous les choix techniques (ex. Monolithe Modulaire Multi-Tenant) sont justifiés exclusivement par des critères d'ingénierie logicielle : frugalité des coûts d'exploitation (Run), robustesse transactionnelle, maintenabilité et absence de sur-ingénierie.

### 1.2. Dispositif Parallèle de Guides Pédagogiques Annexes

- Pour permettre aux membres de l'équipe de maîtriser en profondeur chaque concept et de défendre les choix lors des soutenances, un dossier d'accompagnement interne est réservé : `agent_projet/docs/guides_equipe/`.
- Ces guides annexes décortiquent les choix techniques et financiers de manière pédagogique et restent strictement étanches des livrables remis aux évaluateurs.

---

## 2. Démarche d'Ingénierie par Arborescence Inversée

## 2. Démarche d'Ingénierie par Arborescence Inversée & Rôle de l'Agent

### 2.1. Contrat de Rôle de l'Agent : Super-Conseiller & Mentor Méthodologique

- **Aucune génération à l'aveugle** : L'agent ne produit aucun livrable de manière anticipée ou autonome.
- **Principe Human-in-the-Loop strict** : Pour chaque livrable, une session dédiée est ouverte. L'agent applique le protocole `/grill-me` (questions ultra-spécifiques) pour challenger l'équipe, soumettre les options d'ingénierie et s'assurer que l'équipe étudiante maîtrise, comprend et valide 100% des choix avant toute écriture.
- **Traçabilité ascendante stricte** : Chaque livrable est alimenté exclusivement par les informations consolidées des livrables précédents afin de garantir une cohérence absolue des données.

### 2.2. Distinction Fondamentale : Ordre Éditorial vs Pipeline de Fabrication

Une erreur classique consiste à confondre l'ordre de lecture d'un document et l'ordre réel de sa conception :

- **L'Ordre Éditorial (Table des Matières finale)** : Scénarisé pour le lecteur / jury. Le Lean Canvas y figure en première section comme synthèse exécutive pour donner la vision d'ensemble en 2 minutes.
- **Le Pipeline Chronologique de Fabrication (Graphe de dépendances réelles)** : On ne peut pas concevoir un Lean Canvas ni calculer des coûts complets au début du projet. Le Lean Canvas est un **artefact de synthèse consolidée**, fabriqué à l'étape 10 une fois que les personas, les flux BPMN, le modèle de données et l'architecture technique sont stabilisés.

```text
PIPELINE CHRONOLOGIQUE DE FABRICATION (ORDRE RÉEL DE PRODUCTION) :

[Étape 01] Cadrage du Besoin Canonique (APTE : Bête à cornes & Pieuvre, Positionnement 2 axes)
     │   -> Fixe à qui l'on rend service, les fonctions principales (FP) et contraintes (FC).
     ▼
[Étape 02] Personas Approfondis & Parcours Utilisateurs (User Journeys)
     │   -> Incarnation vivante des acteurs identifiés en Étape 01 (Pierre, Suzanne, Marius, etc.).
     ▼
[Étape 03] Modélisation des Processus Métiers (BPMN)
     │   -> Met en mouvement les parcours des personas (commandes, passage caisse, statut VFP 15j).
     ▼
[Étape 04] Modèle Conceptuel de Données (MCD / ERD)
     │   -> Déduit directement des entités et données manipulées dans les flux BPMN (Étape 03).
     ▼
[Étape 05] Architecture de l'Information, Ergonomie & Accessibilité RGAA AA
     │   -> Traduit les étapes des flux BPMN et les contraintes seniors en écrans et zonings clairs.
     ▼
[Étape 06] User Story Mapping & Backlog MoSCoW (Critères Gherkin)
     │   -> Découpe les fonctions des BPMN et des zonings en briques de dev INVEST (V1 MVP vs V2/V3).
     ▼
[Étape 07] Cadrage Technique Préliminaire & Trajectoire d'Architecture (C4)
     │   -> Dimensionne le socle (Monolithe Modulaire, PostgreSQL) pour faire tourner le backlog.
     ▼
[Étape 08] Gouvernance Projet, WBS & Diagramme de Gantt
     │   -> Planifie dans le temps le développement du backlog (Étape 06) sur l'architecture (Étape 07).
     ▼
[Étape 09] Analyse Financière par Coûts Complets (Centres d'Analyse & UO)
     │   -> Évalue le coût réel de revient du Run (serveurs Étape 07) et du Build (temps Étape 08).
     ▼
[Étape 10] Synthèse Panoramique : LE LEAN CANVAS
     │   -> Rempli en toute fin : ses 9 cases sont alors 100% maîtrisées, chiffrées et cohérentes !
     ▼
[Étape 11] Consolidation du Cahier des Charges Maître & Compilation PDF A4
         -> Assemblage dans l'ordre éditorial officiel (le Lean Canvas est placé en Section 01).
```

---

## 3. Structure Complète Validée du Cahier des Charges (Livrable R1)

Le document maître regroupe 9 sections thématiques modulaires :

```text
CAHIER DES CHARGES SHOPLOC (LIVRABLE OFFICIEL R1)
│
├── 1. Cadrage Stratégique & Expression du Besoin
│    ├── Positionnement & Double finalité (Revitalisation commerciale & Cohésion urbaine)
│    ├── Matrice de Positionnement Concurrentiel (2 axes : Flux physique vs Délocalisation, Gratuité/Souveraineté vs Commissions privées)
│    ├── Synthèse Panoramique du Modèle : Le Lean Canvas (9 blocs synthétiques sur 1 page A4)
│    ├── Formalisation Canonique du Besoin (Méthode APTE) : Diagramme Bête à Cornes & Diagramme Pieuvre (FP / FC)
│    ├── Enonciations des Besoins (Stratégiques, Tactiques avec convention tripartite, Opérationnels)
│    ├── Périmètre strict (Click & Collect en boutique obligatoire, zéro livraison à domicile)
│    ├── Scalabilité territoriale & Modularité (Multi-tenancy par ville, étanchéité des données)
│    ├── Justification d'ingénierie : Monolithe Modulaire vs Microservices (Frugalité & Maintien)
│    ├── Matrice des KPIs à double échelle (Locale par ville & Macroscopique nationale)
│    └── Principe de gratuité citoyenne intégrale
│
├── 2. Personas & Parcours Utilisateurs Cibles
│    ├── 4 Personas officiels (Pierre senior, Suzanne commerçante, Marius collectivité, Julie & Arthur)
│    ├── Parcours utilisateurs nominaux de bout en bout (User Journey Maps sans carte d'empathie)
│    └── Dispositif d'inclusion : Tiers de confiance / Procuration de retrait (Planification V2/V3)
│
├── 3. Modélisation des Processus Métiers (BPMN)
│    ├── Processus 1 : Conventionnement municipal et adhésion commerçante
│    ├── Processus 2 : Commande Click & Collect, réservation stock et retrait boutique
│    ├── Processus 3 : Enregistrement de passage en caisse et calcul VFP (fenêtre glissante 15 jours)
│    ├── Processus 4 : Conversion de l'avantage fidélité en mobilité urbaine (Bus / Parking)
│  
│
├── 4. Modélisation Conceptuelle des Données (MCD)
│    ├── Schéma conceptuel entités-associations (Mermaid ERD)
│    ├── Dictionnaire formel des données (Entités, attributs, types logiques, contraintes)
│    └── Règles d'intégrité et de découplage (Points marchands vs Statut VFP territorial)
│
├── 5. Architecture de l'Information, Ergonomie & Accessibilité
│    ├── Arborescence des vues selon le profil connecté
│    ├── Spécifications de conformité RGAA niveau AA / WCAG 2.1
│    └── Zonings et principes d'écrans clés (Caisse commerçant, tableau de bord, vue client, carte papier)
│
├── 6. Spécifications Fonctionnelles Détaillées & Backlog
│    ├── User Story Mapping (Découpage en tranches de release : V1 MVP, V2, V3)
│    ├── Backlog priorisé selon la méthode MoSCoW
│    └── Spécification des User Stories majeures (Format INVEST & critères d'acceptation Gherkin)
│
├── 7. Cadrage Technique Préliminaire & Trajectoire d'Architecture
│    ├── Diagrammes d'architecture C4 (Contexte & Conteneurs)
│    ├── Orientations techniques (PostgreSQL relationnel, API REST documentées, conteneurisation Docker)
│    └── Exigences non-fonctionnelles (Sécurité RBAC/JWT, temps de réponse, pseudonymisation RGPD)
│
├── 8. Gouvernance Projet & Planification
│    ├── Cadre méthodologique Agile Scrum (Rôles, rituels, cadence des sprints)
│    ├── Organigramme des tâches (WBS) & Matrice des responsabilités (RACI)
│    ├── Définitions de maturité (Definition of Ready / Definition of Done)
│    ├── Diagramme de Gantt avec les jalons contractuels du projet (R1 à R5)
│    └── Registre des risques projet et plans de mitigation
│
└── 9. Cadrage Économique Préliminaire & Analyse par Coûts Complets
     ├── Modèle économique contractuel (Convention tripartite Mairie / Association / ShopLoc)
     ├── Démarche d'analyse a posteriori par la Méthode des Coûts Complets
     ├── Identification des centres d'analyse (Build, Run, Support, Administration) et Unités d'Œuvre
     └── Détermination du coût de revient et de la grille tarifaire justifiable
```

---

## 4. Matrice de Répartition par Section et Agents

| Section      | Titre de la Section                           | Agent Responsable                       | Fichier Source Modulaire                                                   |
| ------------ | --------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------- |
| **01** | Cadrage Stratégique & Pyramide des Besoins   | Product Owner (`flash`)               | `agent_projet/docs/cdc_sections/01_cadrage_strategique_besoins.md`       |
| **02** | Personas & Parcours Utilisateurs Cibles       | Business Analyst (`flash`)            | `agent_projet/docs/cdc_sections/02_personas_et_parcours_utilisateurs.md` |
| **03** | Modélisation des Processus Métiers (BPMN)   | Architecte Fonctionnel (`pro`)        | `agent_projet/docs/cdc_sections/03_processus_metier_bpmn.md`             |
| **04** | Modélisation Conceptuelle des Données (MCD) | Architecte Données (`pro`)           | `agent_projet/docs/cdc_sections/04_modele_conceptuel_donnees_mcd.md`     |
| **05** | Ergonomie & Accessibilité (RGAA AA)          | Expert UX & Qualité (`flash`)        | `agent_projet/docs/cdc_sections/05_ergonomie_accessibilite_rgaa.md`      |
| **06** | User Story Mapping & Backlog MoSCoW           | Product Owner (`flash`)               | `agent_projet/docs/cdc_sections/06_backlog_user_story_mapping.md`        |
| **07** | Cadrage Technique Préliminaire (C4)          | Architecte Logiciel (`pro`)           | `agent_projet/docs/cdc_sections/07_cadrage_technique_architecture.md`    |
| **08** | Gouvernance Agile & Gantt                     | Scrum Master (`flash`)                | `agent_projet/docs/cdc_sections/08_gouvernance_agile_gantt.md`           |
| **09** | Cadrage Financier par Coûts Complets         | CFO Stratégie Financière (`pro`)    | `agent_projet/docs/cdc_sections/09_analyse_financiere_couts_complets.md` |
| **10** | Document Maître Unifié & PDF A4             | QA & Security Sentinel (`flash_lite`) | `agent_projet/docs/CAHIER_DES_CHARGES_R1.md`                             |

---

## 4.1. Articulation des 3 Modèles Visuels Majeurs Intégrés

Pour respecter le principe directeur de réduction drastique du texte au profit de supports visuels denses et synthétiques, trois modèles majeurs sont intégrés dès la Section 01 :

1. **La Matrice de Positionnement Concurrentiel (2 axes)** :
   - *Niveau d'intervention* : Niveau stratégique macro (Section 01, positionnement marché).
   - *Combinaison* : Se combine directement avec la **Vision Stratégique** et la **Pyramide des Besoins**. Elle oppose le modèle ShopLoc (ancrage physique piétonnier en centre-ville, gratuité citoyenne et souveraineté communale) aux modèles prédateurs des géants du e-commerce (livraison motorisée délocalisée, prélèvement de commissions privées).
2. **Le Lean Canvas (9 blocs sur 1 page A4)** :
   - *Niveau d'intervention* : Synthèse panoramique de modèle économique et opérationnel (Section 01).
   - *Combinaison* : Il agit comme la colonne vertébrale visuelle du livrable en reliant :
     - Les *Segments Clients* aux **Personas** (Section 02).
     - La *Solution* et les *Canaux* aux **Processus Métiers BPMN** (Section 03) et à l'**Ergonomie** (Section 05).
     - La *Structure des Coûts* et les *Flux de Revenus* au **Cadrage Financier par Coûts Complets** (Section 09).
3. **Le Diagramme Bête à Cornes & Diagramme Pieuvre (Méthode APTE)** :
   - *Niveau d'intervention* : Ingénierie des exigences et frontière fonctionnelle du système (Section 01).
   - *Combinaison* :
     - *Bête à cornes* : Formalise en une bulle visuelle à qui le système rend service (Citoyens, Commerçants, Mairie), sur quoi il agit (le commerce de proximité et la mobilité) et dans quel but.
     - *Diagramme Pieuvre* : Les **Fonctions Principales (FP)** alimentent directement les grandes Épiques du **User Story Mapping** (Section 06), tandis que les **Fonctions Contraintes (FC)** dictent les exigences de sécurité RGPD, d'accessibilité RGAA AA et de frugalité technique (Sections 05 et 07).

---

## 5. Prochaine Étape (Session 17)

La prochaine session sera consacrée à l'**outillage graphique et au pilotage** :

1. Choix et configuration des serveurs MCP et outils de modélisation visuelle (Mermaid, BPMN, MCD).
2. Définition de la **charte graphique globale** du projet (palette de couleurs sobre, typographies, règles de mise en page).
3. Mise en place de l'outil de pilotage visuel pour le suivi de production des livrables.
