# WORKFLOW DE SPRINT & MACHINE A ETATS (.antigravity/workflows/workflow_sprint.md)

Ce document decrit la machine a etats deterministe encadrant les passages de relais entre sous-agents du projet ShopLoc.

---

## 1. Vue d'Ensemble de la Machine a Etats

Pour eliminer le non-determinisme, le projet fonctionne selon une sequence lineaire stricte. Aucun agent ne peut demarrer sa phase tant que la condition de garde (Guard Condition) de l'etape precedente n'est pas remplie.

```text
[ETAPE 1 : CADRAGE & BACKLOG]
Sous-Agent PO (modele: flash)
    │
    ▼ Fichier genere : agent_projet/backlog/sprint_{N}.json + Tickets Linear
[ETAPE 2 : GATE DE VALIDATION HUMAINE]
Validation explicite du Scrum Master tournant (etudiant)
    │
    ▼ Feu vert donne
[ETAPE 3 : ARCHITECTURE & CONTRATS D'API]
Sous-Agent Architecte (modele: pro)
    │
    ▼ Fichiers generes : OpenAPI YAML + Schema SQL PostgreSQL 3NF
[ETAPE 4 : DEVELOPPEMENT TDD]
Sous-Agent Dev TDD (modele: pro ou flash selon complexite)
    │
    ▼ Fichiers generes : Tests unitaires Jest/JUnit + Code source green
[ETAPE 5 : ASSURANCE QUALITE & DOD]
Sous-Agent QA (modele: flash_lite)
    │
    ▼ Decision QA : PASSED (Zero regression, zero emoji, cartouche valide)
[CLOTURE DE TACHE & SYNCHRONISATION]
Orchestrateur met a jour Linear et invite a fermer la session (1 Session = 1 Tache)
```

---

## 2. Description des 5 Etapes & Conditions de Garde

### Etape 1 : Cadrage & Extraction des User Stories
* **Acteur** : `subagent_po` (Modele : `flash`)
* **Actions** :
  1. Lit les questions de cadrage dans `agent_projet/docs/`.
  2. Cree les tickets sur Linear via MCP ou ecrit `agent_projet/backlog/sprint_{N}.json`.
* **Condition de Garde (Pour passer a l'etape 2)** :
  - Chaque User Story possede au minimum 2 criteres d'acceptation Gherkin.
  - Chaque US est associee a un persona explicite (Pierre, Suzanne, Marius, ou Julie & Arthur).

### Etape 2 : Gate de Validation par le Scrum Master Humain
* **Acteur** : Etudiant occupant le role tournant de Scrum Master.
* **Actions** :
  - Valide la priorisation des US pour le sprint.
* **Condition de Garde (Pour passer a l'etape 3)** :
  - L'utilisateur envoie explicitement son approbation (*« Backlog Sprint N valide »*).

### Etape 3 : Conception Technique & Contrats d'Interface
* **Acteur** : `subagent_architecte` (Modele : `pro`)
* **Actions** :
  1. Formalise le contrat OpenAPI dans `agent_code/specs/api/`.
  2. Formalise les migrations SQL dans `agent_code/specs/database/`.
* **Condition de Garde (Pour passer a l'etape 4)** :
  - Schema PostgreSQL normalise en 3NF.
  - Multi-tenancy implemente par cloisonnement par ville.
  - Respect du RGPD pour Marius (pseudonymisation).

### Etape 4 : Developpement Pilote par les Tests (TDD)
* **Acteur** : `subagent_dev` (Modele : `pro` pour le calcul financier / `flash` pour les CRUD)
* **Actions** :
  1. Cycle Red : Redaction du test unitaire en echec.
  2. Cycle Green : Ecriture du code minimal faisant passer le test.
  3. Cycle Refactor : Nettoyage et respect du Clean Code.
* **Condition de Garde (Pour passer a l'etape 5)** :
  - Tous les tests du module sont au vert (100% passing).

### Etape 5 : Controle Qualite & Verification DoD
* **Acteur** : `subagent_qa` (Modele : `flash_lite`)
* **Actions** :
  1. Verification de la non-regression.
  2. Verification de l'absence totale d'emojis dans le code et les docs.
  3. Verification de la conformite aux standards académiques.
* **Resultat** :
  - Si `PASSED` : La tache est integree et le ticket Linear passe a `Done`.
  - Si `REJECTED` : Retour immediat a l'etape 4 avec le rapport des defauts a corriger.

---

## 3. Schema JSON Global de Suivi du Workflow
Ce schema pivot permet a l'orchestrateur de verifier l'etat du flux sans ambiguite :
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "sprintNumber": { "type": "integer" },
    "currentStage": { 
      "type": "string",
      "enum": ["PO_FRAMING", "SM_APPROVAL", "ARCHITECTURE", "TDD_DEVELOPMENT", "QA_AUDIT", "COMPLETED"]
    },
    "artifacts": {
      "type": "object",
      "properties": {
        "backlogFile": { "type": "string" },
        "apiContractFile": { "type": "string" },
        "dbSchemaFile": { "type": "string" },
        "testReportFile": { "type": "string" }
      }
    },
    "gateApprovedBy": { "type": "string" },
    "qaVerdict": { "type": "string", "enum": ["PENDING", "PASSED", "REJECTED"] }
  },
  "required": ["sprintNumber", "currentStage", "qaVerdict"]
}
```
