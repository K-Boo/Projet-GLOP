
Bonjour à toutes et à tous,

Attention, la date de rendu change : le rendu R2 est repoussé au 19/10. Il était prévu initialement le 12/10, vous avez donc une semaine de plus.

Voici ce que j'attends pour ce rendu : choisir, justifier et installer les outils de votre projet ShopLoc, et proposer une première version de votre architecture microservices. Le rendu est à me remettre au format PDF le 19/10.

1. Architecture microservices : première version

L'architecture de ShopLoc doit être une architecture microservices. Vos outils doivent donc être choisis pour la gérer. On vous demande ici une première version, volontairement légère. L'architecture détaillée, avec toutes ses vues et sa justification complète, sera demandée dans les rendus R4 et R5.

- Découpage en services : proposez au moins 3 services (par exemple clients et fidélité, catalogue et produits, commandes click & collect, notifications, administration et analyse). Expliquez vos choix : pourquoi ces services, ce que fait chacun, et quelles données lui appartiennent.
- Communication : comment les services échangent entre eux (API REST, messagerie asynchrone…), s'il y a un point d'entrée unique (API gateway), et comment vous gérez les services partenaires simulés.
- Données : une base par service ou une base partagée, et comment vous gardez des données cohérentes entre les services.
- Coûts et risques : les microservices ont un coût (déploiement, supervision, tests d'intégration, cohérence des données). Listez-les et dites comment votre équipe va les gérer.
- Impact sur les outils : expliquez clairement comment vos outils gèrent plusieurs services (un seul dépôt ou plusieurs, un pipeline par service, build et dépendances, Docker Compose ou Kubernetes, tests entre services).
- Schémas (3 maximum, lisibles et avec une légende) : un schéma de contexte (les 5 types d'utilisateurs, le système, les services partenaires simulés), un schéma des services et de leurs liens, et un schéma de la chaîne d'outils (du commit jusqu'au déploiement en conteneurs). Précisez la notation utilisée (UML…).
- Outil de schémas : choisissez-le comme les autres (draw.io, PlantUML, Mermaid, Structurizr…). Les schémas écrits en code et mis dans le dépôt sont fortement encouragés.

2. Choix et mise en place des outils

Pour chaque catégorie ci-dessous, présentez votre choix et justifiez-le en le comparant à 2 ou 3 autres solutions (coût et licence, facilité de prise en main pour l'équipe, lien avec les autres outils, hébergement et RGPD, éco-conception, adaptation aux microservices). Montrez aussi que l'outil est bien en place (capture d'écran, lien, extrait de configuration).

- Gestion de code (Git) : la plateforme, le ou les dépôts créés, l'accès donné à l'équipe enseignante, l'organisation pour plusieurs services (monorepo ou plusieurs dépôts), la stratégie de branches, les conventions de commit, les règles de revue (PR/MR).
- Build (Maven / Gradle) : un squelette de projet qui compile, la structure des modules et des services, la gestion des dépendances.
- Stack technique : Java (Spring Boot / J2E) et JavaScript/TypeScript, base de données SQL, framework front. Justifiez en fonction du sujet et d'une architecture distribuée.
- Intégration et déploiement continus : un pipeline qui fonctionne (GitHub Actions, GitLab CI, Jenkins…) avec au minimum le build, les tests et l'analyse de qualité, et capable de construire et déployer plusieurs services. Donnez la capture d'une exécution réussie.
- Conteneurisation et orchestration (Docker / Kubernetes) : un Dockerfile par service et un docker-compose (ou équivalent) qui démarre l'ensemble. Précisez où vous allez héberger l'application et dites si vous utilisez Kubernetes ou non, en justifiant.
- Tests et qualité : les outils pour les tests unitaires (JUnit…), de non-régression, fonctionnels/E2E (Cypress, Cerberus…), les tests d'intégration entre services et l'analyse statique (Sonar).
- Analyse de données : l'outil choisi (Grafana, …) et le lien avec les besoins de l'administrateur et des commerçants.
- Gestion agile : un outil pour le backlog et les sprints, un backlog déjà créé, et l'organisation du rôle tournant de Scrum Master.

3. Preuve que ça marche de bout en bout

Un "walking skeleton" : une toute petite version de l'application, mais qui marche vraiment et passe par toute votre chaîne d'outils. Ce n'est pas la qualité de l'application qui compte, c'est la preuve que vos outils fonctionnent ensemble.

- Contenu minimum : deux éléments qui communiquent (le front et un service, ou deux services), un accès à la base de données et un test automatique. Exemple : une page web qui appelle le service catalogue et affiche des produits lus en base.
- Il doit passer par : commit Git, pipeline CI, build, tests, analyse qualité, images Docker, déploiement.
- Dans le PDF par example : un petit schéma, la capture d'une pipeline au vert, les résultats des tests et de l'analyse, les images Docker et le docker-compose, la capture de l'application qui tourne, et le lien vers le dépôt.
- Pas besoin de fonctionnalités complètes, de tous les services ni d'un beau front.

4. Utilisation de l'IA

Indiquez les outils d'IA que vous utilisez ou prévoyez d'utiliser et pour quoi faire, comment vous gardez la trace de ce que l'IA génère, et une première estimation du coût de cet usage. Rappel : vous devrez être capables d'expliquer à l'oral n'importe quel morceau de code présent sur votre dépôt.

5. Responsabilités

Dites qui est responsable de quoi côté outils (spécialiste outils, responsable du déploiement, responsable qualité) et côté architecture (back office, front office). Ajoutez un court paragraphe sur les risques que vous avez identifiés : sécurité des accès et des secrets, sauvegardes, complexité d'exploitation d'une architecture distribuée.

Ce que nous allons vérifier

- que nous avons vraiment accès à votre dépôt Git, à votre site de suivi et à votre CI, sans avoir à demander de droits
- des commits réguliers, faits par plusieurs personnes
- un pipeline au vert avec au moins un test
- une vraie architecture microservices : plusieurs services construits et déployables séparément, dont deux au moins qui communiquent dans votre walking skeleton
- la cohérence entre votre découpage, vos schémas et vos outils
- la cohérence entre vos choix et leur justification : un choix sans comparaison ne rapportera pas tous les points

Pour résumer : rendu au format PDF le 19/10 (et non plus le 12/10).

N'hésitez pas à me poser vos questions d'ici le rendu.

Bon courage à tous,

Jérémy Woirhaye
M2 MIAGE - Génie Logiciel par la Pratique
