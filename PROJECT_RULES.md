# SHOPLOC — RÈGLES PROJET & DIRECTIVES D'INGÉNIERIE (PROJECT_RULES.md)
> **Cadre** : M2 MIAGE — UE Génie Logiciel par la Pratique (GLOP) 2026-2027, Université de Lille  
> **Client (MOA)** : Laurence Duchien, Anne Etien, François Secchi, Jérémy Woirhaye  
> **Format d'équipe** : Société d'ingénierie logicielle / Éditeur SaaS (5 étudiants-ingénieurs)  
> **Tag officiel communications** : `[GLOP]`  
> **Identifiant du projet** : `MiageShopLoc` (ou nom final de votre société)

---

## 1. Posture & Organisation d'Équipe

1. **Gouvernance Agile / Scrum** :
   - **Aucun chef de projet unique** : Rôle de **Scrum Master tournant** à chaque sprint/itération.
   - **6 Pôles de responsabilités** répartis sur les 5 membres de l'équipe :
     * *Responsable Qualité (QA)* : Validateur de la DoD (Definition of Done), couverture de tests, conformité des livrables.
     * *Responsable Communication* : Gestionnaire du site de suivi de projet, diffusion des comptes-rendus de réunions et documentation interne.
     * *Responsable Déploiement / DevOps* : Pipelines CI/CD, conteneurisation Docker, gestion des releases et notices d'installation.
     * *Spécialiste Outils & Ingénieur Logiciel* : Veille outillage, intégration IDE/linters/Sonar, support technique à l'équipe.
     * *Responsable Architecture Back-Office* : Modélisation SQL, sécurité API, logique métier, scalabilité multi-villes.
     * *Responsable Architecture Front-Office* : Ergonomie multi-personas, accessibilité inclusive (RGAA), interfaces web/mobiles.

2. **Standards Documentaires Obligatoires (Consignes Évaluées)** :
   - Tout document officiel doit comporter le **cartouche normalisé** :
     * Identifiant projet + Logos (Projet & Université de Lille).
     * Rédacteur, date de rédaction, nomenclature de version, nombre total de pages, titre.
     * Cartouche de validation formelle (*qui valide, à quel titre, date de validation*).
   - **Table des matières / Index obligatoire** pour tout document dépassant 10 pages.
   - **Interdiction stricte des emojis** : Aucun emoji dans les livrables, la documentation, le `README.md` ou les commentaires de code. Présentation épurée, sobre et digne d'un master d'ingénierie.
   - **Format de livraison** : Documents officiels systématiquement livrés en **PDF**.
   - **Glossaire du projet tenu à jour** : Tout terme métier (VFP, Click & Collect, Clearing, Multi-tenancy, etc.) consigné par ordre alphabétique avec son auteur et sa définition.

---

## 2. Principes d'Architecture & Exigences Techniques

1. **Stack Technique Cible** :
   - **Backend** : Java (Spring Boot) OU TypeScript (Node.js / NestJS). Architecture en couches (Controller / Service / Repository / DTO) avec validation stricte des entrées (Bean Validation / Zod).
   - **Persistance** : Base de données SQL relationnelle (PostgreSQL recommandé). Modèle normalisé 3NF, contraintes d'intégrité référentielle fortes, transactions ACID pour les opérations Click & Collect et fidélité.
   - **Frontend** : Application Web responsive moderne (React / Angular / Vue) pensée pour deux cibles opposées :
     * *Pierre (74 ans)* : Typographies lisibles, contrastes élevés, parcours dépouillé, respect des normes RGAA (niveau AA).
     * *Suzanne (22 ans - Commerçante)* : Tableau de bord ergonomique pour la gestion rapide des stocks et la validation des retraits.
   - **Services tiers & Interopérabilité** : Tous les systèmes externes (API stationnement mairie, logiciels de caisse commerçants POS) doivent être modélisés sous forme d'**APIs simulées (mocks REST / OpenAPI)**.

2. **Propriétés Système Non-Négociables (Slides du sujet)** :
   - **Passage à l'échelle (Scalabilité)** : Architecture multi-tenant capable de supporter une petite commune (<20k hab.), une ville moyenne (20k-100k hab.) ou une métropole (>100k hab.).
   - **Sécurité & Respect de la vie privée (RGPD)** : Cloisonnement strict des données inter-commerces (aucun commerçant ne voit les ventes de son voisin), pseudonymisation des paniers d'achats pour les administrateurs (Marius), recueil explicite du consentement usager.
   - **Éco-conception (Green IT)** : Requêtes SQL optimisées, limitation des charges réseau, images compressées, architecture frugale.

---

## 3. Normes de Développement & DevOps

1. **Gestion de Version & Workflow Git** :
   - Branches protégées : `main` (production), `develop` (intégration continue), `feature/<nom-tâche>` pour chaque user story.
   - Messages de commits normalisés (Conventional Commits) : `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`.
   - **Commits réguliers et équilibrés** : Le jury évalue la régularité des commits de chaque membre sur l'année.

2. **Qualité & Stratégie de Test (DoD)** :
   - Approche **TDD (Test-Driven Development)** pour les règles métiers critiques (calcul des points, attribution/perte du statut VFP, validation d'un panier).
   - Tests unitaires systématiques (JUnit / Jest), tests d'intégration API, et couverture minimale suivie via SonarQube.
   - Conteneurisation complète via `Dockerfile` multi-stage et `docker-compose.yml` reproductible en une seule commande.

---

## 4. Protocole d'Efficacité & Économie de Quota Agentique

1. **Règle d'or : 1 Session = 1 Tâche Atomique** :
   - Ne jamais conserver une session de chat pour l'intégralité du projet.
   - Clôturer le chat dès qu'une tâche est achevée et ouvrir une nouvelle session pour la suivante.
   - La mémoire du projet est persistée dans les fichiers Markdown de `agent_projet/docs/` (pas dans l'historique infini du chat).

2. **Méthode Avant Code (Planning Mode)** :
   - Toujours formaliser un plan d'action (architecture, signatures d'APIs, schéma BDD) avant d'écrire le code source.
   - Valider le plan permet de réussir l'implémentation en 1 passe, économisant ainsi 80% de tokens de correction.

3. **Exécution Ciblée & Propre** :
   - Limiter la verbosité des commandes terminal (utiliser des filtres et cibler précisément les fichiers de tests).
   - Garder le workspace ordonné avec deux pôles étanches : `agent_projet/` (docs, livrables, drive) et `agent_code/` (backend, frontend, docker, tests).

4. **Routage Multi-Modèles Économique (Model Tiering)** :
   - Déléguer au moins 70% des tâches à `flash` (PO, rédaction, analyse) et `flash_lite` (QA, assertions, conformité zéro emoji).
   - Réserver le modèle `pro` aux seules phases d'architecture (modélisation BDD 3NF) et aux calculs financiers critiques.

5. **Contrôle & Audit de Consommation de Jetons** :
   - Auditer régulièrement la consommation de jetons de la session via le script dédié :
     `python agent_projet/scripts/token_tracker.py`
