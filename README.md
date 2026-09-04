# Projet ShopLoc — Marketplace & Fidelisation de Centre-Ville
> **Master 2 MIAGE — UE Genie Logiciel par la Pratique (GLOP) 2026-2027**  
> Universite de Lille — Faculte des Sciences et Technologies (FST)

---

## 1. Presentation du Projet

ShopLoc est une solution territoriale numerique visant a revitaliser les commerces de proximite face aux grandes surfaces de peripherie :
* **Marketplace Click & Collect multi-commerces** avec panier mutualise unique.
* **Programme de fidelite partage** entre commerces independants avec compensation financiere.
* **Interconnexion avec les services municipaux** (conversion des points en gratuite de stationnement).
* **Tableaux de bord d'analyse** pour l'association des commercants et la Mairie (respect strict du RGPD).
* **Accessibilite inclusive** (persona senior Pierre 74 ans, conformite RGAA niveau AA).

---

## 2. Architecture Bi-Depots : Cockpit & Code Evalue

Pour garantir une etancheite absolue entre les travaux de gouvernance / outillage agentique interne et le code source presente aux professeurs evaluateurs, le projet est scinde en **deux depots Git distincts** :

| Element | Depot 1 : Cockpit Projet (GitHub) | Depot 2 : Code Evalue (GitLab Univ-Lille) |
| :--- | :--- | :--- |
| **Depot distant** | `git@github.com:K-Boo/Projet-GLOP.git` | `git@gitlab-ssh.univ-lille.fr:khalil.bouchama.etu/projet-glop-app.git` |
| **Dossier local** | `.../Projet-GLOP` (ce depot) | `.../projet-glop-app` (dossier frere) |
| **Visibilite** | Prive (Equipe projet uniquement) | **Public / Partage aux professeurs evaluateurs** |
| **Contenu** | Gouvernance, cadrage R1, etude financiere R3, dossiers techniques, infra d'agents, FinOps | **Code source pur uniquement** (Backend, Frontend, Docker, Tests TDD, CI/CD) |
| **Traces d'IA** | Presentes (`.antigravity`, roles, prompts, FinOps) | **ZERO trace** : aucun fichier d'agent ni mention de LLM |

### Structure attendue sur la machine de chaque membre :
```text
Dossier_GLOP/
├── Projet-GLOP/                   [COCKPIT PROJET - CE DEPOT GITHUB]
│   ├── agent_projet/              # Livrables R1, R3, scripts PDF et Google Drive
│   ├── .antigravity/              # Directives d'orchestration, contrats et roles
│   ├── .agents/                   # MCP Linear et competences logicielles
│   ├── config.local.json          # Pointeur local vers Google Drive et GitLab (ignore par Git)
│   └── README.md                  # Ce guide d'installation
│
└── projet-glop-app/               [DEPOT DE CODE - GITLAB UNIV-LILLE]
    ├── .git/                      # Remote GitLab Univ-Lille
    ├── .gitignore                 # Standard de developpement etanche
    ├── README.md                  # Documentation technique pour les evaluateurs
    ├── backend/                   # Code backend (apres validation de la stack)
    ├── frontend/                  # Code frontend accessible RGAA
    ├── docker/                    # Dockerfile, docker-compose.yml
    └── tests/                     # Suites de tests TDD
```

---

## 3. Guide d'Installation Rapide pour l'Equipe

Chaque membre du groupe doit pouvoir reproduire exactement le meme environnement de travail. Deux methodes sont possibles : **automatique via Antigravity** (recommandee) ou **manuelle en ligne de commande**.

### Pre-requis Generaux pour Tous les Membres :
1. **Git** installe sur la machine.
2. **Cles SSH** configurees :
   * Une cle autorisee sur votre compte **GitHub** (pour cloner `Projet-GLOP`).
   * Une cle autorisee sur votre compte **GitLab Universite de Lille** (pour `projet-glop-app`).
   * Test de connexion :
     ```bash
     ssh -T git@github.com
     ssh -T git@gitlab-ssh.univ-lille.fr
     ```
3. **Python 3.10+** installe et accessible dans votre invite de commande (`python --version`).
4. **Google Drive pour ordinateur** installe et connecte a votre compte universitaire pour acceder au dossier partage `Projet-GLOP`.

---

### Methode A : Configuration Automatique via Antigravity (Recommandee)

Cette methode configure 100% de votre poste en une seule phrase grace a l'agent d'alignement.

#### Etape 1 : Cloner le depot principal
Placez-vous dans votre dossier de travail de Master 2 (par exemple `Documents/GLOP`) :
```bash
git clone git@github.com:K-Boo/Projet-GLOP.git
cd Projet-GLOP
```

#### Etape 2 : Ouvrir le projet dans l'IDE Antigravity
Lancez Antigravity et ouvrez le dossier `Projet-GLOP`.

#### Etape 3 : Demander l'alignement automatique a l'agent
Dans le chat avec votre agent Antigravity, saisissez simplement :
> *« Aligne mon environnement sur la configuration d'equipe »*

L'agent lit automatiquement `.antigravity/setup_equipe.md` et execute le script d'alignement `agent_projet/scripts/setup_env.py` qui realise en totale autonomie :
1. **Packages Python** : installe automatiquement `pymupdf`, `reportlab`, `pypdf`, `pillow` et `rich`.
2. **Moteur PDF** : detecte le moteur headless de votre machine (Microsoft Edge, Google Chrome ou Chromium).
3. **Google Drive** : detecte l'emplacement de votre dossier partage `Projet-GLOP`, initialise les 5 dossiers officiels de livrables (`01_Cadrage_Metier_R1` a `05_Demonstrations_Videos`).
4. **Depot Principal** : verifie la liaison Git GitHub `K-Boo/Projet-GLOP`.
5. **Depot GitLab** : clone automatiquement le depot de code `projet-glop-app` dans le dossier parent frere s'il n'est pas encore present, et cree votre fichier personnel `config.local.json`.

#### Etape 4 : Configurer votre identite etudiante sur le depot de code GitLab
Dans un terminal, placez-vous dans le dossier de code clone et renseignez votre identite officielle :
```bash
cd ../projet-glop-app
git config user.name "Votre Prenom Nom"
git config user.email "votre.nom.etu@univ-lille.fr"
```

Votre poste est desormais pret et conforme a 100%.

---

### Methode B : Configuration Manuelle Pas-a-Pas (Sans passer par l'agent)

Si vous preferez executer l'installation vous-meme en terminal :

#### Etape 1 : Cloner les deux depots cotes a cote
```bash
# Dans votre dossier de travail (ex: Documents/GLOP)
git clone git@github.com:K-Boo/Projet-GLOP.git
git clone git@gitlab-ssh.univ-lille.fr:khalil.bouchama.etu/projet-glop-app.git
```

#### Etape 2 : Configurer votre identite sur le depot GitLab
```bash
cd projet-glop-app
git config user.name "Votre Prenom Nom"
git config user.email "votre.nom.etu@univ-lille.fr"
cd ../Projet-GLOP
```

#### Etape 3 : Installer les dependances Python
```bash
python -m pip install pymupdf reportlab pypdf pillow rich
```

#### Etape 4 : Lancer le script d'auto-alignement
```bash
python agent_projet/scripts/setup_env.py
```
Le script configure votre fichier `config.local.json` et verifie tous les acces.

---

## 4. Outils Integrés : FinOps, Green AI & Synchronisation

### A. Moniteur de Jetons & Empreinte Ecologique (Green FinOps)
Un outil en ligne de commande 100% local (sans compte cloud ni configuration externe) permet de suivre en direct :
* Vos **quotas de tokens** journalier (24h) et hebdomadaire (7 jours).
* Le **modele LLM exact** sollicite par l'agent a chaque requete (Gemini Flash, Sous-Agent Architecte Pro, Sous-Agent QA Flash Lite).
* L'estimation de l'**empreinte energetique** (Wh avec equivalence ampoule LED 10W) et de l'**empreinte en eau** (mL avec equivalence en gorgees d'eau) basees sur la litterature scientifique (Luccioni et al. 2023, Shaolei Ren et al. 2023).

Pour le lancer :
* **Sous Windows** : Double-cliquez directement sur `agent_projet/scripts/watch_tokens.bat`.
* **En ligne de commande** :
  ```bash
  # Mode tableau de bord en direct (actualise a chaque fin de requete)
  python agent_projet/scripts/token_tracker.py --watch

  # Mode journal continu defilant
  python agent_projet/scripts/token_tracker.py --stream
  ```

### B. Synchronisation Automatique Google Drive
Lors de la generation d'un livrable officiel (cahier des charges R1 en PDF, etude financiere R3, etc.) :
```bash
python agent_projet/scripts/drive_sync.py agent_projet/docs/01_Cadrage_Metier_R1/cahier_des_charges_R1.pdf
```
Le script pousse automatiquement le fichier dans le dossier Google Drive partage de l'equipe.

### C. Gestion Agile des Sprints via Linear (MCP)
Le fichier `.agents/mcp_config.json` integre le serveur Model Context Protocol pour Linear :
* Chaque membre renseigne sa variable d'environnement `LINEAR_API_KEY` (cle personnelle creee sur Linear dans *Settings > Security & Access > Personal API Keys*).
* L'agent PO peut alors synchroniser le backlog, creer les User Stories et mettre a jour les statuts de sprint en direct.

---

## 5. Regles d'Or Obligatoires pour Toute l'Equipe

Pour preserver la qualite de la notation et l'homogeneite du projet, chaque membre doit respecter :

1. **Interdiction Totale des Emojis (Regle Absolue)** :
   * Aucun emoji dans les fichiers Markdown, le code, les commentaires et les messages de commit.
   * L'ensemble de nos livrables doit refleter la rigueur et le serieux d'eleves-ingenieurs en Master 2 MIAGE.
2. **Etancheite Totale de GitLab** :
   * Ne **JAMAIS** commiter de fichier `.antigravity`, `.agents`, `AGENTS.md` ou script Python dans le depot GitLab `projet-glop-app`.
   * Le depot GitLab ne doit contenir que du code source professionnel, des tests et des configurations Docker.
3. **Format des Messages de Commit (Conventional Commits)** :
   * Vos commits sur GitLab doivent respecter la norme : `feat(...)`, `fix(...)`, `test(...)`, `refactor(...)`, `chore(...)`.
4. **Pas de Code Premature** :
   * Le depot de code reste vierge tant que le cadrage fonctionnel (Livrable R1) et le choix formel de la stack technologique (ADR d'architecture) n'ont pas ete arretes par le groupe.
