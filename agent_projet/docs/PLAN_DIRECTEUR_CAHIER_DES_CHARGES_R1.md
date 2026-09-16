# PLAN DIRECTEUR & CADRE MÉTHODOLOGIQUE DU CAHIER DES CHARGES (R1)
## Université de Lille — Faculté des Sciences et Technologies — M2 MIAGE
### UE Génie Logiciel par la Pratique (GLOP) 2026-2027

---

## Informations Documentaires

| Métadonnée | Valeur |
|---|---|
| **Intitulé du Projet** | Plateforme ShopLoc — Marketplace & Fidélisation Territoriale |
| **Identifiant Officiel** | `MiageShopLoc` |
| **Référence Documentaire** | `GLOP-2026-R1-PLAN-DIRECTEUR-v1.0` |
| **Type de Document** | Feuille de Route Méthodologique & Structure Validée du Livrable R1 |
| **Statut du Document** | Validé par l'équipe projet — Prêt pour exécution |
| **Date d'Arrêté** | 16 Septembre 2026 |

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

La réalisation du Cahier des Charges ne s'effectue pas d'un seul bloc, mais par briques modulaires indépendantes selon le protocole séquentiel **« 1 Session = 1 Livrable »** :

```text
[Étape 1 : Questionnement Spécifique] -> Entretien ciblé sur les arbitrages fins du livrable.
                    │
[Étape 2 : Production Modulaire]      -> Rédaction de la section dans agent_projet/docs/cdc_sections/
                    │
[Étape 3 : Revue & Validation Fine]   -> Relecture, ajustement et consignation dans JOURNAL_DE_BORD.md
                    │
[Étape 4 : Consolidation Finale]      -> Assemblage du document maître CAHIER_DES_CHARGES_R1.md & PDF
```

---

## 3. Structure Complète Validée du Cahier des Charges (Livrable R1)

Le document maître regroupe 9 sections thématiques modulaires :

```text
CAHIER DES CHARGES SHOPLOC (LIVRABLE OFFICIEL R1)
│
├── 1. Cadrage Stratégique & Expression du Besoin
│    ├── Positionnement & Double finalité (Revitalisation commerciale & Cohésion urbaine)
│    ├── Pyramide des Besoins (Stratégiques, Tactiques avec convention tripartite, Opérationnels)
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
│    └── Processus 5 : Gestion des anomalies (Rupture, annulation, règle de no-show)
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

| Section | Titre de la Section | Agent Responsable | Fichier Source Modulaire |
|---|---|---|---|
| **01** | Cadrage Stratégique & Pyramide des Besoins | Product Owner (`flash`) | `agent_projet/docs/cdc_sections/01_cadrage_strategique_besoins.md` |
| **02** | Personas & Parcours Utilisateurs Cibles | Business Analyst (`flash`) | `agent_projet/docs/cdc_sections/02_personas_et_parcours_utilisateurs.md` |
| **03** | Modélisation des Processus Métiers (BPMN) | Architecte Fonctionnel (`pro`) | `agent_projet/docs/cdc_sections/03_processus_metier_bpmn.md` |
| **04** | Modélisation Conceptuelle des Données (MCD) | Architecte Données (`pro`) | `agent_projet/docs/cdc_sections/04_modele_conceptuel_donnees_mcd.md` |
| **05** | Ergonomie & Accessibilité (RGAA AA) | Expert UX & Qualité (`flash`) | `agent_projet/docs/cdc_sections/05_ergonomie_accessibilite_rgaa.md` |
| **06** | User Story Mapping & Backlog MoSCoW | Product Owner (`flash`) | `agent_projet/docs/cdc_sections/06_backlog_user_story_mapping.md` |
| **07** | Cadrage Technique Préliminaire (C4) | Architecte Logiciel (`pro`) | `agent_projet/docs/cdc_sections/07_cadrage_technique_architecture.md` |
| **08** | Gouvernance Agile & Gantt | Scrum Master (`flash`) | `agent_projet/docs/cdc_sections/08_gouvernance_agile_gantt.md` |
| **09** | Cadrage Financier par Coûts Complets | CFO Stratégie Financière (`pro`) | `agent_projet/docs/cdc_sections/09_analyse_financiere_couts_complets.md` |
| **10** | Document Maître Unifié & PDF A4 | QA & Security Sentinel (`flash_lite`) | `agent_projet/docs/CAHIER_DES_CHARGES_R1.md` |

---

## 5. Prochaine Étape (Session 17)

La prochaine session sera consacrée à l'**outillage graphique et au pilotage** :
1. Choix et configuration des serveurs MCP et outils de modélisation visuelle (Mermaid, BPMN, MCD).
2. Définition de la **charte graphique globale** du projet (palette de couleurs sobre, typographies, règles de mise en page).
3. Mise en place de l'outil de pilotage visuel pour le suivi de production des livrables.
