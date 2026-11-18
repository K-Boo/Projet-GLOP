# DIRECTIVES GLOBALES DE L'ESPACE DE TRAVAIL GLOP (AGENTS.md)

Ce fichier de regles permanentes s'applique de maniere automatique et inconditionnelle a l'ensemble des repertoires et des sous-agents de l'espace de travail GLOP (Master 2 MIAGE - UE GLOP 2026-2027, Universite de Lille).

---

## 1. Phase 0 : Interception & Optimisation Canonique Obligatoire

A chaque instruction ou requete utilisateur (qu'elle soit informelle, rapide ou telegraphique), l'agent applique systematiquement le protocole de normalisation issu du `GUIDE_PROMPTING_AGENTIQUE.md` avant toute action operationnelle :

1. **Resolution de Contexte** : Charger les contraintes depuis `ShopLoc/.agents/skills.config.yaml` ou via le script `ShopLoc/.venv/Scripts/python.exe ShopLoc/agent_projet/scripts/optimize_prompt.py "<requete>"`.
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
2. Pour les livrables documentaires : L'execution reelle de `ShopLoc/.venv/Scripts/python.exe ShopLoc/agent_projet/scripts/verify_deliverables.py` affichant 0 canari, 0 violation et 0 emoji.
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
(Interdiction d'utiliser le python global Windows Store ou d'anciens environnements tiers).

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

Toute competence ou developpement doit respecter la stack maitresse declaree dans `ShopLoc/.agents/skills.config.yaml` :
* Backend : Java 17, Spring Boot 3.3.x, Maven, Jakarta Validation, Problem Details RFC 7807, Two-Phase Commit (2PC).
* Frontend : React 18, TypeScript, Tailwind CSS, RGAA / WCAG AA.
* BDD : PostgreSQL 16, normalisation 3NF, isolation stricte par microservice (Database-per-Service).

---

## 8. Protocole de Test Agentique Rigoureux (Principes Dan Luu)

Conformement aux decouvertes empiriques sur la verification agentique (Dan Luu, 2026), la couverture de code (Jacoco >= 80%) est une condition necessaire mais strictement insuffisante. L'agent applique les gardes-fous suivants :

1. **Interdiction Formelle du "Vanity Testing" & Sur-Mocking** :
   * Interdiction d'ecrire des tests unitaires tautologiques (tester qu'un getter renvoie sa propriete, ou tester un mock qui ne fait que retourner la valeur pre-programmee sans exercice logique).
   * Pour la persistance relationnelle, interdiction de mocker les repositories JPA : employer imperativement `@DataJpaTest` avec verifications des contraintes d'unicite, de cle et de rollback reel.

2. **Priorite aux Chemins de Defaillance (Adversarial & Fault Paths First)** :
   * Avant de rediger le test du cas nominal (Happy Path), l'agent concoit obligatoirement les tests d'echec : carte refusee (HTTP 402), indisponibilite de stock (stock epuise / concurrence), timeout reseau, payload invalide (Problem Details RFC 7807).
   * Pour le coordinateur 2PC : certification obligatoire que la compensation (*Rollback*) retablit l'etat initial des stocks et n'engendre aucun etat orphelin.

3. **Preuve de Sensibilite du Test (Mutation / Fault Injection)** :
   * Un test n'est declare valide que s'il est capable d'echouer lorsqu'un bug est reellement present. Si un composant passe ses tests meme lorsqu'on commente sa ligne critique de Rollback, la suite de tests est consideree comme nulle et non avenue.

---

## 9. Verrou Commit & Push Synchrone (Plan de Commits Modulaires)

L'agent a l'interdiction formelle d'executer `git commit` ou `git push` de maniere autonome sur les depots distants (GitHub ou GitLab).
* **Planification modulaire prealable** : Pour toute tache de code, l'agent decoupe le travail en un maximum de commits atomiques (1 couche logique ou 1 suite de tests par commit) et soumet ce plan avant generation.
* **Double aval prealable obligatoire** : Pour chaque commit du plan, l'agent presente le message en francais simple, la liste des fichiers et le contenu prevu, puis attend l'accord explicite de l'utilisateur dans le chat avant de generer et committer.
* **Execution atomique et horodatage coherent** : Des validation humaine d'un commit, l'agent execute dans le meme enchainement : validation des tests (`mvn test`), synchronisation (`git pull --rebase` si travail sur branche partagee), `git commit` et `git push` immediat pour garantir un arbre Git propre sans decalage d'horodatage.

---

## 10. Convention des Messages de Commit Git : Conventional Commits en Francais (Style Etudiant)

Les messages de commit doivent imperativement concilier le formalisme du standard **Conventional Commits** et l'usage exclusif de la **langue francaise** (tonalite etudiante simple, claire et directe).

1. **Format Canonique Obligatoire** :
   `<type>(<perimetre>): <description en francais>`
   *(Le perimetre entre parentheses precise le module ou la feature, ex: `commande`, `auth`, `panier`, `doc`, `ci`).*

2. **Types Normalises Autorisés** :
   * `feat` : Ajout d'une entite, d'un endpoint ou d'une fonctionnalite metier.
   * `fix` : Correction d'une anomalie, d'un bug ou d'un calcul.
   * `test` : Creation ou mise a jour de tests unitaires, d'integration ou qualimetrie JaCoCo.
   * `docs` : Actualisation de la documentation technique, du journal de bord ou des livrables.
   * `refactor` : Reorganisation du code sans impact fonctionnel.
   * `ci` : Modification des pipelines GitLab CI ou des Dockerfiles.
   * `build` : Modification des dependances Maven (`pom.xml`).
   * `chore` : Taches d'outillage interne ou de maintenance de l'espace de travail.

3. **Description Exclusivement en Francais (Style Etudiant)** :
   * La description apres les deux points doit etre redigee en francais simple, lisible et naturel.
   * Interdiction formelle de rediger la description en anglais (ex: "add feature", "implement service").

4. **Exemples Conformes** :
   * `feat(commande): ajout des entites jpa et de la machine a etats`
   * `test(authentification): ajout des tests d'integration pour le controleur qr code`
   * `docs(gouvernance): mise a jour du journal de bord session 54`
   * `fix(panier): correction du calcul des quantites et du montant total`
   * `ci(mock): conteneurisation alpine et suite de tests de validation`

5. **Exemples Proscrits** :
   * `feat(order): implement order jpa entities state machine and repository` (description en anglais : strictement interdit)
   * `ajout des entites commande` (absence du formalisme Conventional Commits : strictement interdit)
   * `fix: bug` (trop laconique et imprécis)

---

## 11. Gouvernance Linear : Etancheite MOA, Style Fonctionnel et Labels Stricts

L'espace Linear etant accessible aux enseignants evaluateurs, il est soumis aux memes regles d'etancheite absolue que les depots de code GitLab :
1. **Zero Trace Agentique ou Organisationnelle Interne** : Interdiction absolue de mentionner des ressources internes d'IA, methodes de test nommees ("Dan Luu"), prompts, cockpit de gouvernance ou la separation entre deux depots Git dans les titres, descriptions ou commentaires Linear.
2. **Contenu 100 % Fonctionnel (Zero Reference de Code)** : Les fiches de tickets Linear doivent decrire exclusivement le besoin metier, les regles de gestion, le comportement attendu ("Ce qui a ete realise" / "Ce qu'il y a a faire") dans un style direct et sobre d'etudiant M2 MIAGE. Interdiction de citer des noms de classes Java, packages, annotations techniques (`@DataJpaTest`, etc.) ou signatures de methodes.
3. **Triptyque Strict des Etiquettes Colorees** : Chaque ticket actif porte exclusivement trois labels maximum :
   * L'User Story parente (`US-01` a `US-18` ou `DevOps`),
   * Le microservice concerne (`service:auth`, `service:catalog`, `service:cart-order`, `service:loyalty`, `service:gateway-frontend`, `service:platform`),
   * L'iteration cible (`Sprint 1` a `Sprint 4`).
   Tout label technique (`tech:*`), de jalon (`milestone:*`) ou generique (`Bug`, `Feature`, `Improvement`) est proscrit.

---

## 12. Strategie Git Multi-Depots (Feature -> Merge Request -> Dev -> Main)

Une fois l'infrastructure GitLab configuree (branches protegees et `dev` creee sur les 5 depots du groupe `glop-garik-2026`) :
1. **Zero Push Direct sur `main`** : La branche `main` represente l'etat stable de demonstration / production et n'est alimentee que par Merge Request validee depuis `dev`.
2. **Branches Isolees par Ticket** : Tout developpement s'effectue sur une branche dediee (`feat/<id-ticket>-<resume>`) puis fait l'objet d'une Merge Request vers `dev` avec pipeline CI/CD au vert et relecture croisee par un pair.



