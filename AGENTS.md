# DIRECTIVES MAITRESSES DU COCKPIT SHOPLOC (AGENTS.md)

Ce fichier de regles permanentes s'applique de maniere automatique et inconditionnelle a l'ensemble du depot ShopLoc (Cockpit de Gouvernance Garik - Master 2 MIAGE GLOP).

---

## 1. Phase 0 : Interception & Optimisation Canonique Obligatoire

A chaque instruction ou requete utilisateur (qu'elle soit informelle, rapide ou telegraphique), l'agent applique systematiquement le protocole de normalisation issu du `GUIDE_PROMPTING_AGENTIQUE.md` avant toute action operationnelle :

1. **Resolution de Contexte** : Charger les contraintes depuis `.agents/skills.config.yaml` ou via le script `.venv/Scripts/python.exe agent_projet/scripts/optimize_prompt.py "<requete>"`.
2. **Formulation Canonique en 5 Blocs** :
   * **BLOC 1 - CONTEXTE** : Societe Garik, ShopLoc, Universite de Lille M2 MIAGE GLOP, cockpit ShopLoc vs depots de code GitLab.
   * **BLOC 2 - OBJECTIF ATOMIQUE (INVEST)** : Formule avec precision chirurgicale, sans ambiguite.
   * **BLOC 3 - CONTRAINTES & STANDARDS** : Zero emoji, etancheite IA, Spring Boot 3.3 / Java 17, 2PC, RGAA AA.
   * **BLOC 4 - SAFETY GATE** : Plan prealable obligatoire pour les actions modificatrices (code, livrables). Mentionner 'Non applicable (Consultation / Explication en lecture seule)' des lors qu'aucune modification de fichier n'est requise.
   * **BLOC 5 - PREUVE PAR L'EXECUTION** : Commande tangible console de certification (si action technique).
3. **Restitution Visuelle** : Afficher systematiquement le cartouche `[REQUETE OPTIMISEE - FORMULE CANONIQUE]` en tete de reponse pour garantir la parfaite synchronisation des attentes avec l'utilisateur.

---

## 2. Le Verrou Plan-First Safety Gate & Distinction des Requetes

Le Verrou Plan-First Safety Gate s'applique **exclusivement aux actions modificatrices**. L'agent a l'interdiction formelle de :
* Generer du code applicatif,
* Modifier des fichiers de code existants,
* Creer ou modifier des sections de livrables academiques officiels (R1, R3, R4/R5),
* Executer des commandes a impact fort,

**sans avoir prealablement soumis un Artifact de plan d'action detaille et obtenu l'accord humain explicite et textuel de l'utilisateur dans le chat**.

**DISPOSITION SPECIALE REQUETES EXPLICATIVES & ANALYSES (LECTURE SEULE)** :
Des lors que la requete utilisateur releve d'une question conceptuelle, d'une explication technique, d'un diagnostic ou d'une demande d'analyse sans ecriture (ex: "Pourquoi...", "Explique-moi...", "Analyse l'etat de..."), le Safety Gate est **inactif**. L'agent a l'interdiction formelle de generer un plan d'action ou de proposer des modifications : il repond **directement, integralement et exclusivement par du texte explicatif Markdown dans le fil de discussion**.

---

## 3. Preuve Tangible par l'Execution (Evidence-Based DoD)

Une fonctionnalite, un correctif ou un livrable ne peut JAMAIS etre declare termine sur une simple affirmation theorique.
La Definition of Done (DoD) exige imperativement :
1. Pour le code : L'execution reelle de `mvn test` affichant 0 echec et 0 erreur, avec une couverture de tests Jacoco >= 80%.
2. Pour les livrables documentaires : L'execution reelle de `.venv/Scripts/python.exe agent_projet/scripts/verify_deliverables.py` affichant 0 canari, 0 violation et 0 emoji.
3. Les traces d'execution de la console doivent figurer dans le compte-rendu.

---

## 4. Etancheite Absolue des Depots de Code Evalues (Zero Trace d'IA)

Le projet repose sur une isolation bi-depots stricte :
* `ShopLoc/` (GitHub) : Cockpit unique de gouvernance, memoire agentique, scripts FinOps, configuration Antigravity.
* `microservices/` (GitLab Univ-Lille, groupe `glop-garik`) : Depots de code de chaque microservice remis aux enseignants evaluateurs.
* **REGLE INVIOLABLE** : Aucun dossier `.antigravity`, `.agents`, script d'IA, trace de prompt ou mention d'assistant virtuel ne doit penetrer dans les depots de code evalues. Le code, les tests et les fichiers Docker/CI doivent etre d'un niveau d'artisanat logiciel pur (Software Craftsmanship).
* **ZERO BOT ET ZERO COMPTE SYNTHETIQUE DANS GITLAB** : Interdiction formelle d'utiliser des Group Access Tokens (GAT) qui generent des membres virtuels [Bot] visibles dans l'annuaire du groupe GitLab. Toute interaction API ou MCP avec la forge de l'Universite de Lille doit imperativement employer un Personal Access Token (PAT) nominatif etudiant, garantissant que seuls les membres humains reels de l'equipe figurent dans les membres du groupe.

---

## 5. Environnement Virtuel Python Dedie

Toute execution de script d'outillage, de verification, de compilation PDF ou de generation documentaire doit imperativement employer le binaire virtuel du projet :
`ShopLoc/.venv/Scripts/python.exe`

---

## 6. Politique Zero Emoji Absolue

Aucun caractere emoji n'est tolere dans :
* Le code source et les commentaires,
* Les fichiers Markdown, HTML, CSS,
* Les commits Git et les messages de journalisation,
* Les reponses textuelles de l'agent.
Le style redactionnel doit etre sobre, academique, rigoureux et digne d'un rapport professionnel de Master 2 MIAGE.

---

## 7. Configuration Technologique Centrale (Zero-Fork)

Toute competence ou developpement doit respecter la stack maitresse declaree dans `.agents/skills.config.yaml` :
* Backend : Java 17, Spring Boot 3.3.x, Maven, Jakarta Validation, Problem Details RFC 7807, Two-Phase Commit (2PC).
* Frontend : React 18, TypeScript, Tailwind CSS, RGAA / WCAG AA.
* BDD : PostgreSQL 16, normalisation 3NF, isolation stricte par microservice (Database-per-Service).
