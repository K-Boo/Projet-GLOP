# DIRECTIVES GÉNÉRALES & ORCHESTRATION DU WORKSPACE (.antigravity/instructions.md)

Ce fichier est le point d'entrée principal pour tout agent Antigravity opérant sur ce workspace.
Il définit l'orchestration entre les deux domaines spécialisés du projet : **Gestion de Projet & Livrables** et **Ingénierie Logicielle & Code**.

---

## 1. Organisation Bimodale du Workspace

Le projet repose sur une architecture bi-depots strictement cloisonnee :
* **Depot 1 (Cockpit Projet - GitHub `Projet-GLOP`)** : Gouvernance, cadrage fonctionnel R1, etude financiere R3, dossiers techniques R4/R5, outillage agentique, suivi FinOps et synchronisation Google Drive.
* **Depot 2 (Code Pur Evalue - GitLab `projet-glop-app`)** : Depot officiel etudiant remis aux professeurs evaluateurs, reserve au code applicatif pur, aux tests TDD et au deploiement Docker/CI. Zéro trace d'IA ni de configuration agentique.

```text
GLOP/
├── ShopLoc/                       [COCKPIT PROJET & GOUVERNANCE - GITHUB]
│   ├── agent_projet/              # Cadrage R1, etude financiere R3, registres agiles, Drive sync
│   ├── .antigravity/              # Directives d'orchestration, contrats et roles agentiques
│   ├── .agents/                   # Configuration MCP Linear et competences logicielles
│   └── config.local.json          # Pointeur vers le depot GitLab local (ignore par Git)
│
└── projet-glop-app/               [DEPOT DE CODE EVALUE - GITLAB UNIV-LILLE]
    ├── .git/                      # Remote : git@gitlab-ssh.univ-lille.fr:khalil.bouchama.etu/projet-glop-app.git
    ├── .gitignore                 # Standard de developpement (exclut tout artefact local/IA)
    ├── README.md                  # Documentation technique pour les professeurs evaluateurs
    ├── backend/                   # Code source backend pur (apres validation de la stack)
    ├── frontend/                  # Code source frontend accessible RGAA
    ├── docker/                    # Dockerfile, docker-compose.yml
    └── tests/                     # Suites de tests unitaires et d'integration TDD
```

---

## 2. Aiguillage des Requetes Utilisateur

Des reception d'une instruction utilisateur, l'agent identifie le domaine concerne et applique la directive appropriee :

### Cas A : Demande liee au Projet, aux Livrables ou a la Gouvernance
- **Exemples** : Redaction ou modification de livrables (R1, R3, R4/R5), cadrage metier, questionnaires MOA, etude financiere, mise a jour du glossaire, diaporamas PPTX, synchronisation Google Drive.
- **Regle a appliquer** : Se conformer imperativement a [`.antigravity/agent_projet.md`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/.antigravity/agent_projet.md) et aux regles locales [`agent_projet/AGENTS.md`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/agent_projet/AGENTS.md).
- **Emplacement des fichiers** : Operer exclusivement dans `agent_projet/`.

### Cas B : Demande liee au Code, a l'Architecture ou aux Tests
- **Exemples** : Choix de la stack, ecriture de code applicatif, creation d'APIs REST, modelisation SQL, cycle TDD, composants React RGAA, conteneurs Docker, tests de charge, pipeline CI/CD.
- **Regle a appliquer** : Se conformer imperativement a [`.antigravity/agent_code.md`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/.antigravity/agent_code.md).
- **Emplacement des fichiers** : Operer exclusivement dans le depot de code GitLab `projet-glop-app/` (chemin local indique dans `config.local.json`).
- **Condition prealable** : Aucune generation de code prematuree tant que le cadrage (R1) et le choix de la stack technologique ne sont pas formellement valides.

---

## 3. Autonomie Opérationnelle & Gestion des Permissions

1. **Haute Autonomie sur l'Exploration, la Lecture et les Tests** :
   - L'agent exécute **en totale autonomie et sans solliciter de permission** toutes les opérations de diagnostic, lecture de fichiers, recherches grep, compilation de tests ou vérifications d'état.
2. **Arrêt et Demande de Validation (Stop & Wait) STRICTEMENT Réservés aux Actes Majeurs** :
   - L'agent **ne doit solliciter la validation explicite de l'utilisateur QUE dans les 3 cas suivants** :
     1. **Modification ou suppression** de code source ou de données existantes du projet.
     2. **Génération ou modification d'un livrable officiel** (cahier des charges R1, étude financière R3, dossiers techniques R4/R5, diaporama de soutenance).
     3. **Arbitrage structurant** (choix technologique majeur, validation d'hypothèse métier auprès de la MOA, arbitrage d'architecture).

---

## 4. Économie de Quota & Hygiène de Conversation

1. **Principe 1 Session = 1 Tâche Atomique** :
   - Clôturer le chat dès qu'une tâche est achevée et ouvrir une nouvelle session pour la suivante.
   - La mémoire pérenne du projet réside dans les fichiers Markdown de `agent_projet/docs/` et `agent_code/`.
2. **Méthode Avant Code (Planning Mode)** :
   - Toujours formaliser le plan (schémas, signatures d'API, entités) avant d'écrire du code de grande envergure.

---

## 5. Synchronisation Google Drive Automatique

- Tout livrable officiel produit dans `agent_projet/` doit être synchronisé dans le dossier Google Drive partagé de l'équipe (`G:\Mon Drive\Projet-GLOP` ou chemin configuré) en appelant :
  ```bash
  python agent_projet/scripts/drive_sync.py <fichier>
  ```
- Les sous-dossiers cibles sont :
  - `01_Cadrage_Metier_R1/`
  - `02_Etude_Financiere_R3/`
  - `03_Architecture_Technique_R4_R5/`
  - `04_Presentations_Diaporamas/`
  - `05_Demonstrations_Videos/`

---

## 6. Alignement Automatique de l'Environnement Équipe

Tout agent Antigravity opérant sur ce projet doit appliquer le protocole d'alignement défini dans [`.antigravity/setup_equipe.md`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/.antigravity/setup_equipe.md). Dès qu'un membre de l'équipe demande de vérifier, aligner ou synchroniser sa configuration, l'agent exécute automatiquement :
```bash
python agent_projet/scripts/setup_env.py
```

---

## 7. Charte Rédactionnelle & Interdiction Absolue des Emojis (Règle Permanente)

1. **Interdiction stricte des emojis** : Aucun emoji ne doit être utilisé dans la rédaction des fichiers du projet : `README.md`, documentation dans `agent_projet/docs/`, spécifications d'architecture dans `agent_code/`, livrables PDF/PPTX/HTML, commentaires de code et messages de commit.
2. **Exigence de sobriété et de propreté** : Le rendu visuel doit être épuré, structuré, rigoureux et digne d'un rapport professionnel d'élèves-ingénieurs en Master 2 MIAGE.
3. **Contrôle à chaque modification** : À chaque modification d'un document ou du `README.md`, l'agent doit impérativement s'assurer de l'absence totale d'emojis avant de valider ses changements.

---

## 8. Coordination Multi-Agents & Optimisation des Jetons (Model Tiering)

1. **Architecture par Contrats & Fichiers Partagés** :
   - Pour éliminer le non-déterminisme, les sous-agents ne dialoguent pas en texte libre mais s'échangent des contrats JSON typés et des fichiers de spécification versionnés selon la machine à états décrite dans [`.antigravity/workflows/workflow_sprint.md`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/.antigravity/workflows/workflow_sprint.md).
2. **Rôles de Sous-Agents Spécialisés** :
   - Sous-Agent PO (`.antigravity/roles/po_role.md`) : Découpage INVEST, critères Gherkin, synchronisation Linear via MCP (`.agents/mcp_config.json`). Modèle obligatoire : `flash`.
   - Sous-Agent Architecte (`.antigravity/roles/architect_role.md`) : Contrats OpenAPI, schémas PostgreSQL 3NF, multi-tenancy. Modèle obligatoire : `pro`.
   - Sous-Agent Développeur TDD (`.antigravity/roles/developer_role.md`) : Cycle Red-Green-Refactor, Clean Code. Modèle : `pro` (calculs financiers) ou `flash` (standard).
   - Sous-Agent QA & Conformité (`.antigravity/roles/qa_role.md`) : Validation DoD, non-régression, vérification cartouche et zéro emoji. Modèle obligatoire : `flash_lite`.
   - Sous-Agent FinOps (`.antigravity/roles/finops_role.md`) : Contrôle a priori du dimensionnement et respect de la frugalité. Modèle obligatoire : `flash_lite`.
3. **Optimisation des Quotas Gemini Pro** :
   - Plus de 70% des opérations doivent être déléguées à `flash` ou `flash_lite` pour réserver le quota `pro` aux seuls arbitrages complexes d'architecture et de logique financière.
   - Suivi régulier de la consommation via le script dédié :
     ```bash
     python agent_projet/scripts/token_tracker.py
     ```
