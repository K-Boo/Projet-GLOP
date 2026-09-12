# WORKFLOW DE PRODUCTION FINANCIÈRE & STRATÉGIQUE (.antigravity/workflows/workflow_finance_strategique.md)

Ce document définit la machine à états déterministe pour la production, la vérification et la publication des livrables de gestion financière et stratégique (Chiffrage R1, Dossier financier R3, Diaporama de soutenance) pour le projet ShopLoc.

---

## 1. Vue d'Ensemble de la Machine à États Financière (Human-in-the-Loop)

Pour éliminer les hallucinations arithmétiques des modèles de langage, former les étudiants et garantir la maîtrise humaine des arbitrages, le workflow suit une chaîne outillée séquentielle :

```text
[PHASE PRÉALABLE : ATELIER HUMAN-IN-THE-LOOP & MONTÉE EN COMPÉTENCES]
Étudiants-Ingénieurs en dialogue avec l'Agent (Mode Tuteur / Copilote)
    │
    ▼ Objectif : Comprendre les méthodes (coûts complets, direct costing, VAN)
    ▼ L'équipe arrête elle-même ses hypothèses réelles sans aucune invention de l'IA
[PHASE 0 : VALIDATION FORMELLE DU FICHIER D'HYPOTHÈSES]
Sous-Agent CFO / Stratège (Modèle: pro / flash)
    │
    ▼ Fichier validé : agent_projet/financials/hypotheses_reelles.json
[PHASE 1 : EXÉCUTION DU MOTEUR DÉTERMINISTE PYTHON (MODE EXÉCUTANT)]
Moteur Python (financial_engine.py) (Modèle: flash_lite)
    │
    ▼ Fichiers générés : donnees_certifiees.json + classeur Excel auditable
[PHASE 2 : CONTRÔLE DE RÉCONCILIATION COMPTABLE & BALANCE]
Garde-Fou Arithmétique (Assertions automatiques Actif == Passif)
    │
    ▼ Condition de Garde : Équilibre bilanciel strict et balance analytique validés
[PHASE 3 : RÉDACTION DU LIVRABLE & REVUE CRITIQUE (MODE AUDITEUR)]
Sous-Agent CFO / Stratège & Simulation de questions de jury
    │
    ▼ Fichier généré : Livrable Markdown académique (Cartouche FST/Lille, zéro emoji)
[PHASE 4 : VERROU DE SORTIE & SÉCURITÉ DOCUMENTAIRE]
Garde-Fou de Sortie (verify_deliverables.py) (Modèle: flash_lite)
    │
    ▼ Condition de Garde : 0 canari, 0 violation stylométrique, 0 emoji
[PHASE 5 : COMPILATION PDF VECTORIEL & SYNCHRONISATION DRIVE]
Script de Compilation (generate_pdf.py & drive_sync.py)
    │
    ▼ Livrable officiel déposé dans 02_Etude_Financiere_R3/
[PHASE 6 : HISTORISATION & CLÔTURE DE SESSION]
Consignation dans JOURNAL_DE_BORD.md et DECISIONS.md (1 Session = 1 Tâche Atomique)
```

---

## 2. Description Détaillée des Phases & Conditions de Garde

### Phase Préalable : Atelier d'Apprentissage & Co-conception (Human-in-the-Loop)
* **Acteurs** : L'équipe étudiante et le sous-agent en **Mode Tuteur** (`[MODE: TUTEUR]`) ou **Mode Copilote** (`[MODE: COPILOTE]`).
* **Objectif** :
  1. L'équipe étudie les concepts du cours de Gestion stratégique des coûts à l'aide du guide [`agent_projet/docs/GUIDE_ASSISTANCE_FINANCIERE.md`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/agent_projet/docs/GUIDE_ASSISTANCE_FINANCIERE.md).
  2. L'équipe interroge l'agent pour tester des ordres de grandeur et comprendre les impacts sans rien acter prématurément.
  3. L'équipe formule et valide ses propres hypothèses de prix et de coûts en toute connaissance de cause.
* **Condition de Garde (Pour passer à la Phase 0)** :
  - L'équipe maîtrise la justification de chaque chiffre et a validé collectivement ses choix économiques.

### Phase 0 : Ingestion & Paramétrage des Hypothèses Financières
* **Acteur** : `subagent_cfo_strategist` (Modèle : `pro` pour l'arbitrage stratégique, `flash` pour l'extraction).
* **Condition Préalable Impérative** :
  - Cette phase ne peut être déclenchée QUE lorsque le projet atteint formellement le jalon de l'étude financière (R3 ou chiffrage officiel R1).
  - Tant que le projet est en phase d'analyse du besoin et de cadrage, le sous-agent reste en veille méthodologique et s'abstient de tout calcul financier prématuré.
  - **Interdiction formelle d'inventer des hypothèses** : chaque paramètre doit provenir de décisions réelles actées (`agent_projet/docs/DECISIONS.md`) ou d'arbitrages formels de la MOA.
* **Actions** :
  1. Vérifier que les documents sources sont assainis via `document_guardian.py` (ex. `detail_sujet_sanitized.md`, support de cours `La gestion stratégique des coûts 2026.pdf`).
  2. Recueillir auprès de l'équipe et de la MOA les hypothèses réelles validées :
     - Équipe de développement Build : 5 étudiants-ingénieurs, grille de valorisation RH réelle actée.
     - Coûts Run : Devis réels d'infrastructure cloud et outillage.
     - Grille tarifaire modulaire pour les 3 segments communaux (<20k, 20-100k, >100k hab.) issue des retours MOA.
     - Hypothèses de pénétration commerciale réelles.
     - Paramètres d'actualisation validés par l'équipe.
  3. Enregistrer les paramètres réels dans `agent_projet/financials/hypotheses_r3.json`.
* **Condition de Garde (Pour passer à la Phase 1)** :
  - Le fichier de configuration JSON est validé formellement par l'équipe sans aucune valeur fictive ou extrapolée par l'IA.

### Phase 1 : Exécution du Moteur Déterministe Python & Modélisation XLSX
* **Acteur** : Exécution automatisée de `financial_engine.py` orchestrée par le sous-agent (Modèle : `flash_lite`).
* **Actions** :
  1. Exécution de la commande :
     ```bash
     python agent_projet/scripts/financial_engine.py --config agent_projet/financials/hypotheses_r3.json --output-json agent_projet/financials/resultats_certifies_r3.json --output-xlsx agent_projet/docs/ShopLoc_Etude_Financiere_Modele.xlsx
     ```
  2. Calcul des coûts complets selon la méthode MIAGE :
     - Découpage de la chaîne de valeur (Vente, Réalisation, Maintenance + Fonctions support).
     - Répartition primaire et secondaire matricielle.
     - Calcul des coûts d'unités d'œuvre (UO).
  3. Calcul des coûts partiels (Direct Costing & Direct Costing Évolué) :
     - Marges sur coûts variables (MCV), TMCV, Seuil de rentabilité (SR), Marge de sécurité (MS), Indice de sécurité (IS).
     - Coûts spécifiques et marges de contribution par taille de commune.
  4. Modélisation P&L, Bilan prévisionnel sur 3 ans, Cash flows, VAN, TRI, Payback et ROI.
  5. Génération du classeur Excel natif avec vraies formules mathématiques via `xlsx-official`.
* **Condition de Garde (Pour passer à la Phase 2)** :
  - Le script se termine avec le code retour 0 et génère le fichier JSON de résultats scellés.

### Phase 2 : Contrôle de Réconciliation Comptable & Balance Bilancielle
* **Acteur** : Module d'audit intégré de `financial_engine.py` (Modèle : `flash_lite`).
* **Assertions Obligatoires** :
  - `Ecart_Bilan = abs(Total_Actif - Total_Passif) < 0.01` pour chaque année projetée.
  - `Balance_Analytique = abs(Total_Charges_Indirectes_Primaires - Total_Charges_Secondaires_Ventilees) < 0.01`.
  - `Coherence_Tresorerie = Tresorerie_N == Tresorerie_N_Moins_1 + Variation_Tresorerie_N`.
* **Condition de Garde (Pour passer à la Phase 3)** :
  - Toutes les assertions sont strictement vraies (`true`). En cas d'échec, le script s'interrompt avec une erreur explicite interdisant la rédaction du rapport.

### Phase 3 : Rédaction du Livrable Markdown Académique
* **Acteur** : `subagent_cfo_strategist` (Modèle : `flash`).
* **Actions** :
  1. Initialiser le fichier `agent_projet/docs/ETUDE_FINANCIERE_R3.md` à partir du modèle officiel `MODELE_ETUDE_FINANCIERE_R3.md`.
  2. Renseigner le cartouche complet (Université de Lille, Faculté des Sciences et Technologies, nomenclature `GLOP-2026-R3-FIN-v1.0`).
  3. Insérer les tableaux certifiés issus de `resultats_certifies_r3.json` :
     - Chaîne de valeur et tableau de répartition des charges indirectes (primaire/secondaire/UO).
     - Tableau de Direct Costing et Seuil de Rentabilité par palier.
     - Compte de résultat prévisionnel (3 ans).
     - Bilan prévisionnel équilibré (3 ans).
     - Tableau des flux de trésorerie et actualisation (VAN, TRI, Payback, ROI).
     - Argumentaire stratégique du pricing et de la convention tripartite (ADR-004).
     - Analyse de sensibilité et engagement Green IT / Frugalité numérique.
  4. Respecter rigoureusement la charte stylistique : style soutenu, précis, académique, **aucun emoji**.
* **Condition de Garde (Pour passer à la Phase 4)** :
  - Le livrable Markdown est complet, structuré et sans sections vides.

### Phase 4 : Verrou de Sortie Egress Guard & Conformité Anti-Canaris
* **Acteur** : `verify_deliverables.py` (Modèle : `flash_lite`).
* **Actions** :
  1. Lancer la vérification de conformité :
     ```bash
     python agent_projet/scripts/verify_deliverables.py
     ```
  2. Contrôler :
     - Absence absolue de termes canaris (ex. "Madagascar", "vélo violet", "protection juridique du logiciel").
     - Absence totale d'emojis Unicode dans le fichier `.md`.
     - Absence de marqueurs d'IA naïve.
* **Condition de Garde (Pour passer à la Phase 5)** :
  - Le script affiche `0 violations detectees`.

### Phase 5 : Compilation PDF Vectoriel & Synchronisation Google Drive
* **Acteur** : `generate_pdf.py` et `drive_sync.py` (Modèle : `flash_lite`).
* **Actions** :
  1. Compiler le livrable officiel en PDF vectoriel A4 haute définition avec styles LaTeX épurés :
     ```bash
     python agent_projet/scripts/generate_pdf.py
     ```
  2. Synchroniser le livrable officiel PDF et le classeur Excel vers le Google Drive partagé de l'équipe :
     ```bash
     python agent_projet/scripts/drive_sync.py agent_projet/docs/ShopLoc_Etude_Financiere_R3.pdf
     python agent_projet/scripts/drive_sync.py agent_projet/docs/ShopLoc_Etude_Financiere_Modele.xlsx
     ```
* **Condition de Garde (Pour passer à la Phase 6)** :
  - Le PDF vectoriel A4 est généré dans `agent_projet/docs/` et synchronisé avec succès dans `02_Etude_Financiere_R3/`.

### Phase 6 : Historisation & Clôture de Session
* **Acteur** : Orchestrateur / Agent Projet.
* **Actions** :
  1. Consigner l'entrée de synthèse dans `agent_projet/docs/JOURNAL_DE_BORD.md` (date, objectifs, livrables produits, métriques clés, reste à faire).
  2. Si un arbitrage financier structurant a été acté (ex. choix du taux d'actualisation ou fixation définitive des forfaits communaux), enregistrer l'ADR correspondant dans `agent_projet/docs/DECISIONS.md`.
  3. Inviter l'utilisateur à clôturer la session de chat afin d'appliquer la règle cardinale **1 Session = 1 Tâche Atomique**.
