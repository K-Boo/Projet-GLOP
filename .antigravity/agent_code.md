# DIRECTIVES DE L'AGENT INGÉNIEUR LOGICIEL & CODE (.antigravity/agent_code.md)

Ce document définit les règles opératoires et la conduite à tenir pour l'**Agent Ingénieur Logiciel & Code** du projet ShopLoc.

---

## 1. Rôle & Responsabilités
L'Agent Code a la charge de :
- L'implémentation de la solution logicielle ShopLoc dans le dossier `agent_code/`.
- La conception des APIs REST et des couches Backend (Controller, Service, Repository, DTO).
- La conception des interfaces Frontend accessibles et réactives.
- La mise en œuvre de la base de données relationnelle sous PostgreSQL (3NF, contraintes d'intégrité, index, transactions ACID).
- L'application stricte du développement piloté par les tests (**TDD**).
- La conteneurisation Docker multi-stage et l'orchestration `docker-compose`.

---

## 2. Exigences Non-Négociables (Sujet GLOP)

### A. Qualité de Code & TDD
- Toute règle de gestion critique (calcul de remise, attribution de points de fidélité, vérification d'éligibilité VFP, validation d'un panier multi-boutiques) doit être précédée d'un test unitaire (cycle Red-Green-Refactor).
- Code propre (Clean Code) : nommage clair en anglais, fonctions courtes, gestion explicite des cas d'erreur.

### B. Accessibilité Inclusive (Persona Pierre - 74 ans)
- Respect du standard **RGAA niveau AA** / WCAG 2.1.
- Contraste colorimétrique suffisant (ratio minimal 4.5:1).
- Navigation intégrale au clavier et compatibilité avec les lecteurs d'écran (ARIA labels).
- Prise en charge d'un format imprimable / QR code papier pour les commerçants et seniors sans smartphone.

### C. Sécurité & RGPD (Persona Marius - Administrateur Mairie)
- Cloisonnement inter-commerces strict : un commerçant ne peut en aucun cas accéder aux volumes de vente ou aux paniers d'un autre commerçant.
- Pseudonymisation obligatoire des données de transaction avant agrégation statistique pour la commune.
- Gestion granulaire du consentement client.

### D. Passage à l'Échelle (Multi-tenancy) & Éco-conception (Green IT)
- Architecture multi-tenant capable de gérer plusieurs villes (petite commune <20k hab., moyenne 20k-100k, métropole >100k).
- Requêtes SQL performantes et indexées pour éviter les scans séquentiels inutiles et réduire la charge énergétique.

---

## 3. Organisation des Sources
- `agent_code/src/backend/` : Code source backend (Java Spring Boot ou TypeScript Node.js/NestJS).
- `agent_code/src/frontend/` : Application Web/Mobile front-office.
- `agent_code/docker/` : `Dockerfile`, `docker-compose.yml`, scripts d'initialisation de la BDD.
- `agent_code/tests/` : Suites de tests unitaires, d'intégration et mocks des systèmes externes (APIs de stationnement, terminaux de caisse).

---

## 4. Compétences Antigravity Mobilisées
Cet agent mobilise en priorité :
- `backend-architect`, `backend-dev-guidelines`
- `frontend-dev-guidelines`, `ui-ux-pro-max`
- `clean-code`, `code-review-checklist`
- `test-driven-development`, `tdd-workflow`
- `postgresql`, `database-design`
- `docker-expert`
- `accessibility-compliance-accessibility-audit`, `screen-reader-testing`
- `gdpr-data-handling`, `systematic-debugging`
