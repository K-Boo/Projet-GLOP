# DIRECTIVE D'ALIGNEMENT DE L'ENVIRONNEMENT D'EQUIPE (.antigravity/setup_equipe.md)

Cette directive decrit l'infrastructure complete des agents du projet ShopLoc et fournit a tout agent Antigravity operant sur la machine d'un membre de l'equipe (Master 2 MIAGE - UE GLOP 2026-2027) la procedure d'auto-configuration autonome pour repliquer exactement l'environnement de reference.

---

## 1. Vue d'Ensemble de l'Infrastructure Agentique

Le projet repose sur une architecture multi-agents cloisonnee et deterministe :

```text
Projet-GLOP/
├── .antigravity/
│   ├── instructions.md            # Routeur d'orchestration global (chef d'orchestre)
│   ├── setup_equipe.md            # Cette directive d'alignement pour l'agent du collegue
│   ├── agent_projet.md            # Directives du pole Gestion de Projet & Livrables
│   ├── agent_code.md              # Directives du pole Ingenierie Logicielle & Code
│   ├── roles/                     # Prompts systemes et contrats des sous-agents
│   │   ├── po_role.md             # Sous-agent PO (modele flash, US INVEST, Linear MCP)
│   │   ├── architect_role.md      # Sous-agent Architecte (modele pro, OpenAPI, SQL 3NF)
│   │   ├── developer_role.md      # Sous-agent Dev TDD (modele pro/flash, Clean Code)
│   │   ├── qa_role.md             # Sous-agent QA (modele flash_lite, assertions, zero emoji)
│   │   └── finops_role.md         # Sous-agent FinOps (modele flash_lite, audit tokens)
│   └── workflows/
│       └── workflow_sprint.md     # Machine a etats deterministe (pipeline en 5 etapes)
│
├── .agents/
│   ├── mcp_config.json            # Configuration du serveur MCP Linear
│   └── skills/                    # 40 competences d'ingenierie logicielle
│
├── agent_projet/                  # [POLE GESTION DE PROJET & LIVRABLES]
│   ├── AGENTS.md                  # Regles locales pour les livrables
│   ├── docs/                      # Cadrage R1, glossaire, ADR, modeles
│   ├── images/                    # Logos officiels Universite de Lille et Faculte
│   └── scripts/
│       ├── generate_pdf.py        # Compilateur PDF vectoriel A4 (LaTeX/HTML)
│       ├── drive_sync.py          # Synchronisation automatique Google Drive
│       ├── token_tracker.py       # Moniteur FinOps & Green AI CLI (Quotas, LLM, Energie, Eau)
│       ├── watch_tokens.bat       # Lanceur Windows du moniteur
│       └── setup_env.py           # Script d'auto-alignement de l'environnement (5 etapes)
│
├── config.local.json              # Pointeur local vers Google Drive et le depot GitLab (ignore Git)
├── README.md                      # Guide d'onboarding collaboratif epure (zero emoji)
└── PROJECT_RULES.md               # Regles directrices d'ingenierie
```

---

## 2. Fonctionnement des Composants Cles

### A. Le Routage Multi-Modeles (Model Tiering)
Pour ne pas saturer les quotas de l'abonnement Gemini Pro :
* `flash_lite` : Reserve a la QA, aux verifications d'assertions et a l'audit FinOps (~90% d'economie).
* `flash` : Reserve au cadrage PO, a la generation de tickets Linear et aux syntheses documentaires (~70% d'economie).
* `pro` : Reserve strictement a la conception d'architecture complexe (PostgreSQL 3NF) et aux algorithmes financiers critiques.

### B. Les Workflows Deterministes par Contrats JSON
Les sous-agents ne dialoguent pas en texte libre. L'orchestrateur suit la machine a etats de `workflow_sprint.md` :
1. Etape 1 : Le sous-agent PO analyse le besoin et genere les US dans Linear ou `sprint_N.json`.
2. Etape 2 : Le Scrum Master etudiant valide le backlog.
3. Etape 3 : Le sous-agent Architecte produit le contrat OpenAPI et le schema SQL.
4. Etape 4 : Le sous-agent Dev developpe en cycle Red-Green-Refactor TDD.
5. Etape 5 : Le sous-agent QA valide la Definition of Done et l'absence totale de regression.

### C. Le Serveur MCP Linear
Declare dans `.agents/mcp_config.json`, il utilise le package `@modelcontextprotocol/server-linear`.
Chaque membre de l'equipe renseigne sa variable d'environnement `LINEAR_API_KEY` pour que son agent puisse creer des tickets et gerer les cycles de sprint automatiquement.

### D. Le Moniteur de Tokens, Routage & Green FinOps en Direct
Situe dans `agent_projet/scripts/token_tracker.py` et pilotable via `watch_tokens.bat`, il offre une interface terminal sobre et non-intrusive :
* **Suivi des Quotas Globaux** : Jauges d'utilisation du quota journalier (24h) et hebdomadaire (7 jours).
* **Routage LLM par Requete** : Affiche le modele exact sollicite a chaque etape (Gemini Flash, Sous-Agents Pro ou Flash Lite).
* **Mesure des Tokens** : Detail Entree (In), Sortie (Out) et Total.
* **Green AI / Impact Ecologique** : Estimation scientifique de l'empreinte electrique (Wh) et en eau (mL) par requete et en cumul.

### E. L'Etancheite Totale du Depot de Code Evalue (GitLab)
Le depot officiel evalue par les professeurs (`projet-glop-app` sur GitLab Univ-Lille) est rigoureusement etanche de l'outillage agentique. Aucun fichier d'instruction, role ou prompt n'y figure.

### F. La Politique Stricte Zero Emoji
Tout fichier cree ou modifie (README, documentation, code, commentaires, commits) doit imperativement respecter la regle d'interdiction totale des emojis.

---

## 3. Procedure d'Auto-Configuration par l'Agent

Des qu'un collegue ouvre le projet dans Antigravity et demande :
*« Aligne mon environnement sur la configuration d'equipe »* ou *« Configure ma machine »*,
l'agent execute automatiquement :

```bash
python agent_projet/scripts/setup_env.py
```

Ce script realise en totale autonomie :
1. **Verification et installation des packages Python** : installe `pymupdf`, `reportlab`, `pypdf`, `pillow` et `rich`.
2. **Verification du moteur PDF** : verifie la presence de Chromium / Edge headless pour la compilation A4.
3. **Detection de Google Drive pour ordinateur** : localise le dossier `Projet-GLOP`, cree les 5 sous-dossiers officiels (`01_Cadrage_Metier_R1` a `05_Demonstrations_Videos`), et genere un fichier `config.local.json` si le Drive n'est pas sur le lecteur `G:\`.
4. **Controle du depot Git principal (GitHub)** : verifie la connexion au remote `git@github.com:K-Boo/Projet-GLOP.git`.
5. **Detection et liaison du depot de code evalue (GitLab)** : localise ou clone `git@gitlab-ssh.univ-lille.fr:khalil.bouchama.etu/projet-glop-app.git` dans le dossier parent et l'enregistre dans `config.local.json`.

L'agent confirme ensuite au collegue que son poste est 100% conforme a l'environnement d'equipe.
