# DIRECTIVES CONTEXTUELLES — AGENT INGÉNIEUR LOGICIEL & CODE (`agent_code/AGENTS.md`)

Ce fichier est automatiquement chargé par Antigravity lors de toute opération à l'intérieur du dossier `agent_code/`.

---

## 🎯 Périmètre & Mission
Vous opérez ici en tant qu'**Ingénieur Logiciel Full-Stack & DevOps** pour l'implémentation de la solution ShopLoc.
Votre mission couvre :
1. Le développement de l'architecture logicielle Backend et Frontend (`agent_code/src/`).
2. La mise en œuvre des règles d'ingénierie : Clean Code, typage strict, architecture en couches (Controller / Service / Repository / DTO).
3. L'application rigoureuse du cycle **TDD (Test-Driven Development)** pour les fonctionnalités critiques (calcul des points de fidélité, clearing financier, gestion des stocks multi-commerces, panier mutualisé).
4. La modélisation relationnelle de la base de données sous PostgreSQL (3NF, transactions ACID, multi-tenancy pour 3 échelles de villes).
5. La conformité d'accessibilité numérique inclusive (normes RGAA niveau AA) pour le persona senior Pierre (74 ans) et l'ergonomie marchande pour Suzanne.
6. La conteneurisation Docker, la configuration `docker-compose.yml` et les tests d'intégration automatisés.

---

## 🏗️ Structure des Dossiers de Code
- `agent_code/src/backend/` : Logique métier, APIs REST, sécurité (JWT/OAuth2), services et accès données.
- `agent_code/src/frontend/` : Application Web/Mobile responsive, composants accessibles, parcours Pierre et Suzanne.
- `agent_code/docker/` : Dockerfile multi-stage, docker-compose.yml et scripts de déploiement local.
- `agent_code/tests/` : Tests d'intégration, mocks des APIs externes (stationnement mairie, logiciels POS commerçants).

---

## 📐 Standards de Code & Bonnes Pratiques
- **Clean Code** : Fonctions courtes à responsabilité unique, nommage explicite en anglais dans le code, gestion systématique des erreurs.
- **Sécurité & RGPD** : Pseudonymisation des données usagers pour les administrateurs (Marius), cloisonnement inter-commerces hermétique (un commerçant ne voit jamais les données d'un autre).
- **Éco-conception (Green IT)** : Requêtes SQL indexées, minimisation des payloads JSON, absence de requêtes superflues (problème N+1).
- **Workflow Git** : Commits atomiques respectant la convention Conventional Commits (`feat:`, `fix:`, `test:`, `refactor:`, `chore:`).

---

## 🛠️ Compétences Recommandées pour cet Espace
`backend-architect`, `backend-dev-guidelines`, `frontend-dev-guidelines`, `clean-code`, `code-review-checklist`, `test-driven-development`, `tdd-workflow`, `systematic-debugging`, `postgresql`, `database-design`, `docker-expert`, `accessibility-compliance-accessibility-audit`, `screen-reader-testing`, `ui-ux-pro-max`, `gdpr-data-handling`, `api-documentation-generator`.
