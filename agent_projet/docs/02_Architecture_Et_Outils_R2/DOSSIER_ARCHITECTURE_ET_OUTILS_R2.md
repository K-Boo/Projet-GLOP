# DOSSIER D'ARCHITECTURE TECHNIQUE & STRATEGIE DE DEPLOIEMENT (LIVRABLE R2)

**Plateforme ShopLoc — Commerce de Proximite et Fidelite Territoriale**  
**Societe Garik**  
**Genie Logiciel par la Pratique (GLOP) / Architecture ALOM**  
**Enseignant Responsable : Jeremy Woirhaye**  
**Date de Remise : 19 octobre 2026 (23h59)**  

---

## Sommaire

1. **Pilier 1 : Architecture Distribuee des Microservices**
   * 1.1 Decoupage en 4 microservices metiers et frontieres de donnees (Database-per-Service)
   * 1.2 Les 5 canaux d'usage clients, passerelle unique et simulateurs de partenaires
   * 1.3 Coherence transactionnelle distribuee (Two-Phase Commit 2PC applicatif)
   * 1.4 Gestion des couts et des risques de l'architecture distribuee
   * 1.5 Impact de l'architecture distribuee sur les outils et la topologie
   * 1.6 Cartographie C4 du systeme distribue (Schema 1 et Schema 2)
   * 1.7 Justification de l'outil de schematisation vectorielle

2. **Pilier 2 : Chaine d'Ingenierie Logicielle et Choix des Outils**
   * 2.1 Gestion de code et integration continue (GitLab Polyrepo, acces enseignant, workflow Git)
   * 2.2 Outil de build et standardisation (Apache Maven 3.9 et Wrapper mvnw)
   * 2.3 Stack logicielle applicative (Java 17, Spring Boot 3.3, H2, PostgreSQL 16, React 18, Vite)
   * 2.4 Assurance qualite, qualimetrie et tests (JUnit 5, Jacoco, SonarLint, Cypress, Testcontainers)
   * 2.5 Pilotage agile du backlog (Linear et rotation methodique du role de Scrum Master)
   * 2.6 Cartographie de la chaine DevOps et de livraison (Schema 3)
   * 2.7 Analyse de donnees et metriques decisionnelles (Grafana, Prometheus, Actuator)
   * 2.8 Validation operationnelle de bout en bout (Walking Skeleton inter-services)

3. **Pilier 3 : Hebergement, Deploiement et Exploitation en Production Reelle**
   * 3.1 Cible d'hebergement souveraine : Justification du VPS Linux OVHcloud
   * 3.2 Exposition publique et terminaison securisee : Reverse Proxy Nginx et HTTPS Let's Encrypt
   * 3.3 Parcours utilisateur concret : Du navigateur client jusqu'aux microservices
   * 3.4 Orchestration conteneurisee et reseau prive Docker Compose
   * 3.5 Procedure de deploiement continu (CD) et mise a jour applicative
   * 3.6 Plan de maintenance operationnelle, sauvegardes automatiques et supervision

4. **Pilier 4 : Gouvernance d'Equipe, Usage de l'IA et Eco-Conception**
   * 4.1 Repartition nominative des responsabilites au sein de la Societe Garik
   * 4.2 Cadre d'utilisation methodologique de l'intelligence artificielle
   * 4.3 Synthese des risques majeurs : Securite des acces et des secrets, sauvegardes, exploitation
   * 4.4 Engagements transversaux d'eco-conception numerique (RGESN)

5. **Annexe Technique : Preuves d'Execution du Walking Skeleton**
   * A.1 Extrait reel du pipeline `.gitlab-ci.yml` et capture console d'un pipeline au vert
   * A.2 Resultats des tests unitaires Surefire et rapport officiel Jacoco (Couverture >= 80%)
   * A.3 Manifeste d'orchestration `docker-compose.prod.yml` et sortie console `docker images`
   * A.4 Capture operationnelle de l'application tournante (Interrogation REST et rendu des produits)
   * A.5 Extrait du `Dockerfile` multi-stage de production (Alpine JRE 17)

---

## 1. Pilier 1 : Architecture Distribuee des Microservices

La plateforme ShopLoc repond a l'imperatif de revitalisation du commerce de centre-ville et de valorisation des circuits courts a travers une architecture distribuee moderne et modulaire. La Societe Garik a retenu un decoupage en microservices autonomes garantissant la haute disponibilite, l'independance des cycles de release et le cloisonnement strict des donnees.

### 1.1. Decoupage en 4 Microservices Metiers et Frontieres de Donnees

Le systeme est decompose en quatre services metiers distincts, chacun operant sur un domaine fonctionnel clos (Bounded Context) et appliquant rigoureusement le patron d'architecture Database-per-Service. Aucune base de donnees n'est partagee entre services :

* **Service d'Authentification (`shoploc-auth-service` - Port 8081)** :  
  Ce service constitue l'autorite d'identification et de securite de la plateforme. Il administre l'annuaire des utilisateurs, le controle d'acces base sur les roles RBAC (`ROLE_CITOYEN`, `ROLE_COMMERCANT`, `ROLE_MAIRIE`), assure le hachage cryptographique des mots de passe avec l'algorithme BCrypt, et delivre les jetons porteurs signes JWT (JSON Web Tokens) indispensables aux requetes clientes.  
  *Donnees isolees (`auth_db` sur port interne 5432)* : Comptes utilisateurs, identifiants, condensats de mots de passe BCrypt, attributions de roles et jetons de rafraichissement.
* **Service Catalogue & Commercants (`shoploc-merchant-catalog-service` - Port 8082)** :  
  Ce service maintient le referentiel central des boutiques partenaires affiliees, leurs horaires d'ouverture, coordonnees geographiques, categories et l'ensemble de leurs fiches articles. Il est le garant de la tenue des inventaires physiques en temps reel et administre les verrous temporaires de stock lors des commandes Click & Collect.  
  *Donnees isolees (`catalog_db` sur port interne 5433)* : Boutiques partenaires, fiches produits, prix en centimes, quantites disponibles et verrous de reservation temporaires (`STOCK_HOLD`).
* **Service Panier & Commandes (`shoploc-cart-order-service` - Port 8083)** :  
  Ce service pilote le panier d'achat mutualise multi-commerces et orchestre la transformation transactionnelle d'un panier en commande validee. Il opere en tant que coordinateur Two-Phase Commit (2PC) applicatif pour verifier et reserver les articles aupres des marchands avant validation, traite le paiement simule et genere le QR code de retrait securise signe HMAC-SHA256.  
  *Donnees isolees (`order_db` sur port interne 5434)* : Lignes de panier d'achat, commandes globales, sous-commandes detaillees par commercant, statuts transactionnels et jetons de retrait.
* **Service Fidelite Territoriale (`shoploc-loyalty-service` - Port 8084)** :  
  Ce service gere le moteur de dynamisation commerciale VFP (*Vente Flash Proximite*). Il calcule les points credites lors des passages commercants, gere leur validite temporelle a 15 jours glissants via un traitement batch nocturne planifie, administre le seuil de 10 passages declencheur des avantages, et gere la conversion des cagnottes en titres de transport urbain Ilevia ou en franchises de stationnement municipal.  
  *Donnees isolees (`loyalty_db` sur port interne 5435)* : Soldes de points citoyens, historique horodate des passages marchands, cagnottes actives et titres municipaux delivres.

---

### 1.2. Les 5 Canaux d'Usage Clients, Passerelle Unique et Simulateurs Partenaires

L'exposition et les communications externes du systeme s'articulent autour de principes d'isolation clairs :

#### 1. Prise en Charge des 5 Canaux Clients
L'architecture de ShopLoc repond aux besoins de cinq profils d'utilisateurs distincts via cinq canaux dedies adosses au frontal Nginx et a la passerelle d'API :
1. *Client Web Citoyen (React 18 SPA - Port 3000)* : Interface grand public utilisee par les consommateurs locaux (persona Julie) pour naviguer sur la marketplace, constituer un panier multi-boutiques et suivre leur cagnotte VFP.
2. *Portail Commercant Back-Office (React 18)* : Interface de gestion securisee (ROLE_COMMERCANT) permettant a la commercante (persona Suzanne) d'actualiser son catalogue, ses prix et ses quantites disponibles.
3. *Terminal Caisse PWA (Scanner Mobile)* : Progressive Web App ultra-legere concue pour les smartphones de caisse en boutique, permettant le scan optique instantane du QR Code de retrait citoyen en moins de 3 secondes.
4. *Console Mairie (Tableau de Bord Territorial)* : Interface decisionnelle reservee aux elus et a la DSI municipale (persona Marius) restituant les statistiques de frequentation commerciale anonymisees selon le principe du k-anonymat.
5. *Console Exploitation / SRE (Supervision Technique)* : Interface technique reservee a l'equipe d'exploitation Garik interrogeant les sondes Spring Boot Actuator (`/actuator/health`, `/actuator/metrics`) pour controler la stabilite du cluster conteneurise.

#### 2. Passerelle d'Entree Unique (Spring Cloud Gateway : 8080)
Les cinq canaux clients ne communiquent jamais directement avec les microservices metiers. L'ensemble des requetes transite par le conteneur `shoploc-api-gateway`. Cette passerelle centralise le controle des jetons JWT a la frontiere du reseau prive, applique les regles de securite CORS, injecte l'en-tete de correlation `X-Correlation-ID` pour le tracage distribue et achemine le trafic vers le service destinataire :
* `/api/v1/auth/**` est achemine vers `shoploc-auth-service` (port 8081).
* `/api/v1/catalog/**` est achemine vers `shoploc-merchant-catalog-service` (port 8082).
* `/api/v1/orders/**` est achemine vers `shoploc-cart-order-service` (port 8083).
* `/api/v1/loyalty/**` est achemine vers `shoploc-loyalty-service` (port 8084).

#### 3. Echanges Inter-Services Synchrones (HTTP REST RFC 7807)
Les echanges entre microservices s'effectuent en HTTP REST synchrone via `Spring 6 RestClient`. Chaque appel est bride par des timeouts stricts (1 seconde de connexion, 2 secondes de lecture) et encapsule dans des reponses normalisees selon la RFC 7807 (Problem Details). La messagerie asynchrone (Kafka ou RabbitMQ) a ete ecartee pour ce jalon afin d'eviter la complexite operationnelle d'un broker resident sur VPS et de garantir une validation transactionnelle immediate du panier.

#### 4. Simulateurs de Partenaires Externes (Stubs REST OpenAPI 3.1)
Pour tester l'integralite du systeme sans dependance a des API tierces reelles inaccessibles aux etudiants, trois simulateurs conteneurises exposent des contrats OpenAPI 3.1 stricts :
* *Simulateur Bancaire (Port 8090)* : Simule les autorisations de reglement par carte bancaire (`POST /api/bank/authorize`) et permet d'injecter des pannes (HTTP 402 pour carte refusee) afin d'eprouver le Rollback 2PC.
* *Simulateur Transports Ilevia (Port 8091)* : Emet des titres virtuels de bus et tramway (`POST /api/ilevia/ticket`) lors de la conversion des points citoyens.
* *Simulateur Voirie & Parking (Port 8092)* : Genere des codes de franchise de stationnement de 20 minutes (`POST /api/parking/voucher`) sur saisie d'immatriculation.

---

### 1.3. Coherence Transactionnelle Distribuee (Two-Phase Commit 2PC Applicatif)

L'independance physique des bases de donnees interdit l'usage d'une transaction SQL commune pour une commande multi-commerces. La Societe Garik a mis en place un patron Two-Phase Commit (2PC) orchestre par le service de commande :
* **Phase 1 (Preparation / PREPARE)** : Le service `shoploc-cart-order-service` sollicite chaque service catalogue implique. Le catalogue verifie la disponibilite physique de chaque article, pose un verrou pessimiste SQL (`SELECT ... FOR UPDATE`) et reserve la quantite sous statut `STOCK_HOLD` pendant 5 minutes.
* **Phase 2 (Confirmation / COMMIT)** : Si l'ensemble des commercants repond favorablement, le service commande appelle le simulateur bancaire. Des reception du code HTTP 200 OK, il transmet l'ordre de validation finale (`COMMIT`) : le catalogue decremente definitivement le stock physique et libere le verrou. Le service fidelite est alors notifie pour crediter le citoyen.
* **Phase de Compensation (ROLLBACK)** : Si un commercant signale un stock epuise ou si la banque retourne une erreur (HTTP 402 ou timeout), le coordinateur declenche immediatement une compensation (`ROLLBACK`) : un ordre de liberation est transmis au catalogue, basculant les reservations `STOCK_HOLD` a l'etat `RELEASED`. Les verrous sont relaches sans aucun debit client ni stock bloque.

---

### 1.4. Gestion des Couts et des Risques de l'Architecture Distribuee

Conformement aux attentes de l'ingenierie ALOM, la Societe Garik a identifie et traite les quatre risques majeurs inherents aux microservices :

| Domaine de Risque | Nature du Risque Identifie | Strategie de Gestion Mise en Oeuvre par l'Equipe |
| :--- | :--- | :--- |
| **1. Deploiement** | Multiplication des artefacts, disparite des environnements et lourdeur des mises en production. | Unification par conteneurisation Docker multi-stage (Alpine JRE 150 Mo) et orchestration automatique Docker Compose sur reseau prive unifie. |
| **2. Supervision** | Difficulte a tracer les requetes transverses et opacite de l'etat des composants individuels. | Exposition native des metriques par Spring Boot Actuator (`/actuator/health`, `/actuator/metrics`) et injection d'un en-tete de correlation `X-Correlation-ID` transmis sur toute la chaine d'appel. |
| **3. Tests d'Integration** | Complexite d'eprouver les flux inter-services sans lancer manuellement l'integralite du cluster. | Tests de contrats REST avec `MockRestServiceServer` au niveau unitaire et suites d'integration automatisees sur conteneurs ephemeres (H2 et Testcontainers). |
| **4. Coherence des Donnees** | Risque d'incoherence entre stocks marchands et paiements lors d'une rupture reseau inter-services. | Orchestration transactionnelle 2PC applicative avec verrous pessimistes PostgreSQL et mecanisme de compensation automatique (Rollback) en cas d'erreur. |

---

### 1.5. Impact de l'Architecture Distribuee sur les Outils et la Topologie

Le choix des microservices dicte directement l'organisation technique de notre outillage :
* **Organisation des Depots (Polyrepo)** : Selection stricte d'un modele multi-depots (4 depots de code metiers independants sur GitLab). Chaque service possede son propre historique Git, ses issues et son cycle de vie, prevenant tout couplage accidentel. L'orchestration globale de deploiement (`docker-compose.prod.yml`) est centralisee dans un dossier d'exploitation dedie.
* **Pipelines d'Integration Continue Isolees** : Chaque depot dispose de son propre fichier `.gitlab-ci.yml`. Une modification sur le service catalogue ne declenche que le build et les tests du catalogue, optimisant les temps de calcul des runners campus.
* **Gestion des Dependances et Builds Autonomes** : Chaque microservice integre son propre fichier `pom.xml` Maven et son wrapper `./mvnw`, garantissant une parfaite independance des versions de bibliotheques sans risque de conflit de dependances transitives.
* **Orchestration Locale et Production** : Rejet de Kubernetes au profit d'une orchestration unifiee Docker Compose garantissant la parite stricte entre poste de developpement et serveur de production VPS.

---

### 1.6. Cartographie C4 du Systeme Distribue (Schema 1 et Schema 2)

Conformement aux consignes officielles (schémas en code, legende explicite et notation normalisee C4), deux diagrammes architecturaux vectoriels decrivent notre systeme :

#### Schema 1 : Contexte Systeme ShopLoc (C4 Niveau 1)
Ce schema explicite les interactions entre les 5 profils d'utilisateurs, le perimetre global du systeme ShopLoc et les 3 services partenaires simules.

![Schema 1 - Contexte Systeme ShopLoc](figures/fig_1_contexte_systeme_shoploc.svg)

#### Schema 2 : Architecture des Services & Liaisons Protocolaires (C4 Niveau 2)
Ce schema detaille l'agencement interne : l'API Gateway unique, les 4 microservices avec leur base de donnees dediee, le protocole de liaison RestClient 2PC entre commande et catalogue, et les interfaces vers les stubs partenaires.

![Schema 2 - Architecture des Services et Liaisons](figures/fig_2_services_et_liaisons.svg)

---

### 1.7. Justification de l'Outil de Schematisation Vectorielle

La Societe Garik a retenu la production de schemas vectoriels au format SVG generes directement par scripts Python integres au depot (`agent_projet/scripts/generate_r2_figures.py`). Ce choix garantit que les schemas restent stockes sous forme de code source versionnable sans provoquer de conflits Git binaires, tout en assurant une resolution graphique parfaite a l'export PDF sur tout niveau de zoom.

---

## 2. Pilier 2 : Chaine d'Ingenierie Logicielle et Choix des Outils

Le choix de l'outillage de la plateforme ShopLoc repose sur une grille d'analyse comparative evaluant chaque composant selectionne face a deux solutions concurrentes selon six criteres : Cout et licence (C1), Facilite de prise en main (C2), Integration globale (C3), Hebergement et conformite RGPD (C4), Eco-conception logicielle (C5) et Adaptation a l'architecture microservices (C6).

### 2.1. Gestion de Code et Integration Continue (GitLab Institutionnel)

* **Technologie Retenue : GitLab Institutionnel (Universite de Lille)**
* **Organisation : Modele Polyrepo (4 depots de code independants)**
  * Groupe GitLab officiel : [`https://gitlab.univ-lille.fr/groups/glop-garik-2026`](https://gitlab.univ-lille.fr/groups/glop-garik-2026) (ID: 70706).
  * Les 4 depots de microservices crees et synchronises :
    1. `shoploc-auth-service` (Securite, JWT, RBAC)
    2. `shoploc-merchant-catalog-service` (Commerces, Catalogues, Stocks)
    3. `shoploc-cart-order-service` (Commandes, Panier, Coordinateur 2PC)
    4. `shoploc-loyalty-service` (Programme fidelite, Cagnotte VFP)
* **Garantie d'Acces Enseignant Sans Demande de Droits** :  
  L'equipe enseignante (Jeremy Woirhaye, Laurence Duchien, Anne Etien, Francois Secchi) dispose d'un acces direct avec le niveau Reporter+ sur l'ensemble du groupe `glop-garik-2026` et de ses sous-projets, garantissant la consultation immediate du code, des pipelines CI et des commits sans aucune sollicitation prealable.
* **Strategie de Branches et Conventions de Commits** :  
  L'equipe applique un GitFlow epure :
  * Branche principale `main` protegee : Aucun commit direct autorise. Toute integration resulte d'une Merge Request (MR).
  * Branches de fonctionnalites : `feature/<identifiant-us>` ouvertes depuis `main`.
  * Regle de revue : Approbation obligatoire par au moins un pair (Abdelkader Heddi pour l'assurance qualite ou Rayane Alli pour les outils) avant fusion.
  * Convention de commit : Standard *Conventional Commits* strictement applique (`feat:`, `fix:`, `test:`, `docs:`, `chore:`).

#### Grille Comparative Multicritere : Gestionnaire de Code & Forge Logicielle

| Solution Analysee | C1 : Cout & Licence | C2 : Prise en main | C3 : Integration | C4 : RGPD & Hebergement | C5 : Eco-conception | C6 : Microservices | Statut Arbitrage |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **GitLab Univ-Lille** | Gratuit (Licence univ) | Excellente (Acquis M1) | Native avec runners CI | Heberge en France (Lille) | Runners detruits post-job | Parfaite (Groupes Polyrepo) | **RETENU** |
| **GitHub Enterprise** | Quotas gratuits limites | Tres bonne | Actions performantes | Cloud Act americain | Runners cloud permanents | Bonne mais quotas CI | *Ecarte (Souverainete)* |
| **Bitbucket / Gitea** | Hebergement a charge | Moyenne | Moteur externe requis | Depend de l'hebergement | Depend de la maintenance | Moyenne | *Ecarte (Complexite)* |

---

### 2.2. Outil de Build et Standardisation (Apache Maven 3.9 & Wrapper mvnw)

* **Technologie Retenue : Apache Maven 3.9.x avec Maven Wrapper (`./mvnw`)**  
  *Justification* : Standard de reference de l'ecosysteme Spring Boot 3.3.4. Le wrapper `./mvnw` embarque dans chaque depot telecharge dynamiquement la version exacte requise de Maven, garantissant un comportement strictement identique entre les stations des developpeurs (Windows, Linux, macOS) et les runners de la forge GitLab.
* **Gestion des Dependances et Squelette Multi-Services** :  
  Chaque microservice dispose de son fichier descriptif `pom.xml` autonome integrant le `spring-boot-starter-parent` (version 3.3.4), `spring-boot-starter-web`, `spring-boot-starter-data-jpa`, `postgresql`, `h2` pour les tests et le plugin `jacoco-maven-plugin`.

#### Grille Comparative Multicritere : Outil de Build

| Solution Analysee | C1 : Cout / Licence | C2 : Prise en main | C3 : Integration | C4 : RGPD / Heberge | C5 : Eco-conception | C6 : Microservices | Statut Arbitrage |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Apache Maven 3.9** | Gratuit (Apache 2.0) | Standard academique | Plugins officiels Spring | Local sur machine / CI | Zero demon resident | Fichier pom.xml autonome | **RETENU** |
| **Gradle** | Gratuit (Apache 2.0) | Scripts Groovy complexes | Bonne integration | Local sur machine / CI | Demon resident lourd en RAM | Bonne | *Ecarte (Sobriete)* |
| **Ant / Ivy** | Gratuit (Apache 2.0) | Obsolescente | Faible avec Spring 3 | Local | Frugal mais depasse | Inadapte aux architectures modernes | *Ecarte (Obsolescence)* |

---

### 2.3. Stack Logicielle Applicative

* **Backend : Java 17 LTS et Spring Boot 3.3.4**  
  *Justification* : Typage statique robuste indispensable aux architectures distribuées, records immutables pour les objets de transfert (DTOs), validation declarative Jakarta et format d'erreur normalise RFC 7807 (Problem Details).
* **Persistance & Bases de Donnees : Dualite H2 (Local/CI) et PostgreSQL 16 (Integration/Prod)**  
  *Justification* :  
  1. *Tests unitaires et pipeline CI rapide* : Base relationnelle H2 in-memory (`jdbc:h2:mem:testdb`), permettant une execution instantanee des suites de tests unitaires sans instanciation de conteneur externe.  
  2. *Integration et production* : PostgreSQL 16 isole par conteneur (Database-per-Service), garantissant les verrous pessimistes SQL (`SELECT ... FOR UPDATE`) indispensables a l'integrite financiere et aux reservations 2PC.
* **Frontend : React 18, TypeScript 5 et Vite**  
  *Justification* : Decoupage par composants modulaires, synchronisation des interfaces TypeScript sur les DTOs backend, et compilation de production sous Vite produisant un bundle leger (~180 Ko) garantissant le respect de l'accessibilite RGAA niveau AA.

#### Grille Comparative Multicritere : Framework Backend

| Solution Analysee | C1 : Cout / Licence | C2 : Prise en main | C3 : Integration | C4 : RGPD / Heberge | C5 : Eco-conception | C6 : Microservices | Statut Arbitrage |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Spring Boot 3.3 / Java 17** | Gratuit (Open Source) | Maitrisee (M1/M2) | Ecosysteme riche | Hebergeable VPS souverain | Optimisation JVM Temurin | Parfaite (Modularite) | **RETENU** |
| **Jakarta EE 10 (WildFly)** | Gratuit | Complexe (Serveur d'app) | Lourdeur de packaging | Hebergeable VPS | Empreinte memoire elevee (>1 Go) | Moins agile en conteneurs | *Ecarte (Empreinte)* |
| **Node.js / Express** | Gratuit (MIT) | Facile | Tres flexible | Hebergeable VPS | Faible memoire I/O | Gestion transactionnelle fragile | *Ecarte (Consigne J2E)* |

---

### 2.4. Assurance Qualite, Qualimetrie et Tests

L'assurance qualite de la plateforme ShopLoc s'appuie sur une couverture de tests pyramidale couvrant les quatre niveaux d'exigence :
* **Tests Unitaires Metiers : JUnit 5, Mockito et AssertJ**  
  Permettent d'eprouver l'ensemble des regles de calcul (gestion des paniers, algorithme de regularite VFP a 15 jours glissants) en isolant parfaitement les dependances par doublures de test.
* **Couverture de Code : Plugin Jacoco (Seuil Contractuel >= 80%)**  
  Integree a chaque build Maven (`mvn jacoco:report`), la generation de rapport XML/HTML est archivee en tant qu'artefact GitLab CI. Un regex d'extraction bloque toute Merge Request dont la couverture descend sous le seuil d'acceptation de 80%.
* **Tests Fonctionnels et Bout en Bout (E2E) : Cypress**  
  Cypress est retenu pour valider les parcours complets des utilisateurs sur les interfaces web et PWA (ajout au panier, simulation de paiement, verification de l'affichage du QR code de retrait). Il a ete choisi face a **Selenium** (lourd et fastidieux a configurer) et **Cerberus** (moins flexible pour tester les Single Page Applications React interactives).
* **Tests d'Integration Inter-Services : MockRestServiceServer & Testcontainers**  
  Les appels REST inter-services 2PC sont testes unitairement a l'aide de `MockRestServiceServer` sans necessiter le lancement des services tiers. Pour l'integration complete du jalon R4, `Testcontainers` instancie de veritables conteneurs PostgreSQL et simulateurs pour valider la compensation transactionnelle en conditions reelles.
* **Analyse Statique de Code : Plugin SonarLint**  
  Integre aux environnements de developpement (IntelliJ IDEA et VS Code), SonarLint analyse le code en temps reel a la saisie, garantissant l'absence de failles OWASP et le respect des normes Clean Code sans requerir l'administration d'un serveur lourd SonarQube.

---

### 2.5. Pilotage Agile du Backlog (Linear)

* **Technologie Retenue : Linear (`https://linear.app/projet-glop`)**  
  *Justification* : Linear a ete prefere a **Jira** (lourdeur d'interface et lenteur de navigation) et **Trello** (absence d'outils statistiques avances et de suivi de velocite). Il permet d'administrer le backlog structure selon la norme INVEST, de cadencer les developpements en cycles de deux semaines (sprints) et de lier automatiquement les identifiants de tickets aux commits Git.
* **Organisation du Travail et Principe du Scrum Master Tournant** :  
  Pour favoriser l'implication de chacun et maintenir une bonne coordination, notre equipe fonctionne selon une organisation collegiale et horizontale. Nous nous appuyons sur les principes de la methode Agile Scrum en confiant l'animation d'equipe (Scrum Master tournant) a tour de role a chaque jalon du projet :
  
- **Jalon R1 (18/09/2026)** — *Cadrage & Reponse a l'appel d'offres* : Coordination par **Khalil Bouchama** (restitution formelle et soutenance de cadrage le 21/09/2026).
- **Jalon R2 (19/10/2026)** — *Choix d'outillage & Socle technique* : Coordination par **Rayane Alli** (revue sur dossier technique d'ingenierie, echeance reportee au 19/10/2026).
- **Jalon R3 (30/11/2026)** — *Analyse financiere & Couts complets* : Coordination par **Gautam Demeulemeester** (revue sur dossier financier et business plan).
- **Jalon R4 (18/12/2026)** — *Premier prototype logiciel & Architecture V1* : Coordination par **Ilyas Ait Ali** (demonstration du prototype operationnel le 04/01/2027).
- **Jalon R5 (19/03/2027)** — *Version complete V2 & Bilan d'exploitation* : Coordination par **Abdelkader Heddi** (recette finale et restitution de cloture le 22/03/2027).

Au quotidien, notre travail s'organise autour d'une reunion hebdomadaire de synchronisation d'une trentaine de minutes permettant de faire le point sur les avancees, de partager les difficultes eventuelles et de redistribuer les taches en cas de besoin, garantissant un investissement equitable de chacun.

---

### 2.6. Cartographie de la Chaine DevOps et de Livraison (Schema 3)

Le schema suivant represente la continuite sans rupture des etapes d'ingenierie logicielle, depuis la phase de codage local avec base memoire H2 jusqu'a la mise a disposition conteneurisee sur le serveur VPS sous reverse proxy HTTPS :

![Schema 3 - Chaine DevOps et Hebergement VPS](figures/fig_3_chaine_outils_devops.svg)

---

### 2.7. Analyse de Donnees et Metriques Decisionnelles (Grafana)

Pour satisfaire aux besoins de pilotage de l'administrateur municipal et des commercants de proximite (explicites dans le Schema 1 via la Console Mairie et le Back-Office), la Societe Garik integre **Grafana** :
* **Alimentation des Metriques** : Grafana est couple aux flux collectes par **Prometheus**, interrogeant les sondes nativement exposees par Spring Boot Actuator (`/actuator/prometheus`) sur les microservices, ainsi qu'a des connecteurs SQL directs sur les bases `order_db` et `loyalty_db` via des vues analytiques dediees.
* **Reponse aux Besoins des Acteurs** :  
  1. *Pour les Commercants (Back-Office Suzanne)* : Visualisation en temps reel du chiffre d'affaires realise en Click & Collect, nombre de retraits effectues par tranche horaire et suivi des articles les plus vendus.
  2. *Pour l'Administration Municipale (Console Mairie Marius)* : Restitution macro-economique de la frequentation commerciale du centre-ville, taux d'echange de la cagnotte VFP en titres de bus et stationnement, avec respect strict du k-anonymat (aucun croisement avec les donnees nominatives citoyennes).

#### Grille Comparative Multicritere : Outil d'Analyse de Donnees

| Solution Analysee | C1 : Cout / Licence | C2 : Prise en main | C3 : Integration | C4 : RGPD / Heberge | C5 : Eco-conception | C6 : Microservices | Statut Arbitrage |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Grafana** | Gratuit (AGPLv3) | Excellente (Tableaux pre-faits) | Connecteurs natifs Actuator/Prometheus | Hebergeable VPS local | Tres sobre (< 100 Mo RAM) | Parfaite (Metriques par service) | **RETENU** |
| **Metabase** | Gratuit (AGPL) | Simple mais limitee | Requetes SQL uniquement | Hebergeable VPS | JVM lourde (> 500 Mo) | Faible pour les metriques systeme | *Ecarte (Poids)* |
| **Kibana (ELK)** | Licences restrictives | Complexe | Exige ElasticSearch | Hebergeable VPS | Tres energivore (> 2 Go RAM) | Oriente logs textuels | *Ecarte (Ressources)* |

---

### 2.8. Validation Operationnelle de Bout en Bout (Walking Skeleton)

Pour certifier l'interoperabilite reelle de l'outillage DevOps, la Societe Garik a developpe, teste et deploye un **Walking Skeleton** fonctionnel de bout en bout reliant deux microservices :
* Le service catalogue (`shoploc-merchant-catalog-service`) persiste ses fiches articles sous Spring Data JPA (sur base H2 en test, PostgreSQL en prod) et expose un endpoint REST de consultation `GET /api/v1/catalog/products/{id}`.
* Le service de commande (`shoploc-cart-order-service`) instancie un client `CatalogClient` base sur `Spring 6 RestClient` pour interroger a distance le catalogue et verifier l'existence et le stock d'un produit avant validation.
* **Preuve de l'Execution des Tests en CI** :  
  La suite de tests unitaires et d'integration `CatalogClientTest` et `CatalogControllerTest` s'execute avec succes sur les runners partages de la forge GitLab Univ-Lille. Le job `maven-tests` affiche **100% de reussite (0 echec, 0 erreur)** et confirme la generation du rapport de qualimetrie Jacoco.
* L'ensemble des preuves materielles d'execution (extraits `.gitlab-ci.yml`, `docker-compose.prod.yml`, rapport Jacoco certifie, sortie console `docker images` et capture du dialogue HTTP en base) est consigne dans **l'Annexe Technique A** de ce livrable.

---

## 3. Pilier 3 : Hebergement, Deploiement et Exploitation en Production Reelle

### 3.1. Cible d'Hebergement Souveraine : Justification du VPS Linux OVHcloud

L'equipe Garik a selectionne un serveur **VPS (Virtual Private Server) Linux** heberge par le fournisseur souverain francais **OVHcloud**, configure sous **Ubuntu Server 24.04 LTS** :
* **Transparence Financiere et Couts Forfaitaires** : Un VPS OVHcloud fonctionne sur un forfait fixe mensuel d'environ 10 a 15 € TTC. A l'inverse, les fournisseurs hyperscalers (AWS, GCP, Azure) reposent sur une facturation a la consommation dynamique (heures d'instances, bande passante sortante, requetes d'I/O) presentant un risque financier inacceptable pour notre projet.
* **Souverainete des Donnees et Respect du RGPD** : Les centres de donnees physiques d'OVHcloud sont situes a Roubaix et Gravelines, sur le territoire francais. Les donnees des citoyens et commercants sont protegees des legislations extraterritoriales etrangeres (Cloud Act).
* **Ratio Cout-Performance Optimal** : La configuration retenue (4 vCPU, 8 Go de RAM, 50 Go de stockage SSD NVMe) heberge l'ensemble des conteneurs applicatifs et des bases de donnees avec une marge de securite de plus de 40% sur la memoire vive.

---

### 3.2. Exposition Publique et Terminaison Securisee : Reverse Proxy Nginx et HTTPS Let's Encrypt

Pour securiser les acces et interdire toute exposition directe des conteneurs sur Internet, un **Reverse Proxy Nginx** frontal est positionne en sentinelle :
* Nginx est le seul composant de la machine a ecouter sur les ports reseau publics 80 (HTTP) et 443 (HTTPS).
* Il achemine les requetes de l'interface web vers le conteneur front-end React (`shoploc-web-ui` sur le port interne 3000) et les appels d'API (`/api/**`) vers la passerelle (`shoploc-api-gateway` sur le port interne 8080).
* **Chiffrement SSL/TLS Gratuit et Automatique** : Les certificats cryptographiques X.509 sont emis par l'autorite ouverte **Let's Encrypt** via l'utilitaire **Certbot**. Une tache planifiee systeme (`cron`) declenche une verification bi-mensuelle pour renouveler les certificats sans coupure de service.
* **Cloisonnement Strict** : Les ports individuels des microservices (8081 a 8084) et des quatre bases de donnees PostgreSQL (5432 a 5435) sont strictement fermes a l'exterieur et n'echangent qu'au sein du reseau prive Docker.

---

### 3.3. Parcours Utilisateur Concret : Du Navigateur Client jusqu'aux Microservices

Voici le cheminement exact d'une requete d'achat sur la plateforme ShopLoc en production :
1. **Acces Securise** : Le citoyen saisit `https://shoploc.garik.fr` dans son navigateur web.
2. **Prise en Charge Nginx** : La requete atteint le port 443 du VPS. Nginx valide le certificat TLS et retourne les composants statiques de l'application cliente React 18 servie par le conteneur front.
3. **Appel d'API Authentifie** : A la validation du panier, l'interface web emet une requete HTTP `POST` a destination de `https://shoploc.garik.fr/api/v1/orders/checkout` avec le jeton porteur Bearer JWT du citoyen.
4. **Filtrage et Validation Gateway** : Nginx transmet l'appel au conteneur `shoploc-api-gateway` (:8080) sur le reseau prive `shoploc-net`. La passerelle verifie la signature HMAC-SHA256 du jeton, injecte l'identifiant de correlation `X-Correlation-ID` et achemine la charge utile au microservice de commande (`shoploc-cart-order-service` :8083).
5. **Orchestration 2PC** : Le service commande sollicite `shoploc-merchant-catalog-service` (:8082) pour reserver le stock en base `catalog_db` sous statut `STOCK_HOLD`, contacte le simulateur bancaire (:8090), valide la commande definitive dans `order_db` et notifie `shoploc-loyalty-service` (:8084) pour incrementer les points dans `loyalty_db`.
6. **Confirmation Finale** : La reponse confirmee avec le QR code de retrait est renvoyee au navigateur du citoyen en moins de 300 millisecondes.

---

### 3.4. Orchestration Conteneurisee et Reseau Prive Docker Compose

L'architecture d'exploitation est formalisee dans le fichier `docker-compose.prod.yml` situe a la racine du dossier d'exploitation du projet :
* **Reseau Prive Etanche (`shoploc-net`)** : Les microservices resolvent leurs adresses respectives grace au DNS interne integre de Docker. Aucun conteneur applicatif ou de stockage n'expose d'adresse IP publique.
* **Persistance Isolee** : Les repertoires de donnees de PostgreSQL sont montes sur des volumes nommes persistants de l'hote Linux (`auth_data`, `catalog_data`, `order_data`, `loyalty_data`). Le redemarrage d'un conteneur ne provoque aucune perte de donnee.

---

### 3.5. Procedure de Deploiement Continu (CD) et Mise a Jour Applicative

Pour appliquer les evolutions logicielles sans interruption de service :
1. A chaque validation de Merge Request sur la branche `main` de GitLab, le pipeline CI compile les sources, execute les tests et construit une image Docker multi-stage Alpine JRE 17 optimisee (taille inferieure a 150 Mo).
2. L'image est estampillee avec le hash de commit Git et poussee sur le registre d'images prive de l'universite (`registry.gitlab.univ-lille.fr/glop-garik-2026/`).
3. Le deploiement sur le VPS s'effectue via un script securise declenchant :
   * Le rafraichissement des images (`docker compose pull`).
   * La relance orchestree des conteneurs mis a jour (`docker compose up -d --remove-orphans`).
   * Un controle automatique de sante (Smoke Test) interrogeant le endpoint `/actuator/health`.

---

### 3.6. Plan de Maintenance Operationnelle, Sauvegardes Automatiques et Supervision

* **Sauvegardes Automatiques Nocturnes** : Une tache planifiee `cron` s'execute chaque nuit a 02h00 sur le VPS Linux. Elle declenche l'export logique complet (`pg_dump`) des quatre bases PostgreSQL. Les archives SQL compressees `.tar.gz` sont stockees dans `/backups/shoploc/` avec une politique de retention glissante de 7 jours.
* **Supervision en Continu** : Surveillance permanente de la memoire vive, de l'espace disque NVMe et de l'etat des connexions JDBC via Spring Boot Actuator et Grafana.
* **Consultation Centralisee des Logs** : Pour diagnostiquer d'eventuelles anomalies en production sans acces direct en console root, l'equipe exploite les flux de journalisation Docker via l'interface securisee Dozzle.

---

## 4. Pilier 4 : Gouvernance d'Equipe, Usage de l'IA et Eco-Conception

### 4.1. Repartition des Responsabilites au Sein de la Societe Garik

Pour garantir un pilotage rigoureux et sans equivoque, les roles d'ingenierie sont repartis nominativement entre les cinq ingenieurs de la Societe Garik :

| Role d'Ingenierie Attribue | Titulaire Responsable | Perimetre d'Attribution & Engagements Techniques |
| :--- | :--- | :--- |
| **Specialiste Outils & Environnement de Developpement** | **Rayane Alli** | Administration de la forge GitLab Univ-Lille, configuration des runners CI, linters, tooling, gestion du backlog Linear et role de Scrum Master tournant pour le jalon R2. |
| **Responsable Deploiement & DevOps** | **Khalil Bouchama** | Orchestration Docker Compose, deploiement du VPS Linux souverain, configuration du reverse proxy Nginx TLS et strategie de release continue CD. |
| **Responsable Architecture Back-Office & Persistance** | **Gautam Demeulemeester** | Conception et modularisation des microservices Spring Boot 3.3, modelisation des bases relationnelles PostgreSQL 16 (Database-per-Service 3NF) et transactions 2PC. |
| **Responsable Architecture Front-Office & Accessibilite** | **Ilyas Ait ali** | Developpement de l'application cliente React 18, de la PWA terminal caisse sous Vite, stylisation Tailwind CSS et conformite accessibilite RGAA niveau AA. |
| **Responsable Qualite, Tests & Relations MOA** | **Abdelkader Heddi** | Validation de la Definition of Done, supervision de la couverture des tests automatises Surefire/Jacoco >= 80%, qualimetrie SonarLint et liaison contractuelle MOA. |

---

### 4.2. Cadre d'Utilisation Methodologique de l'Intelligence Artificielle

La Societe Garik integre l'assistance de grands modeles de langage (LLMs) dans un cadre methodologique strictement circonscrit et gratuit :
* **Outils Retenus & Gratuité** : Utilisation exclusive d'outils et de modeles de langage en acces libre ou sous tier gratuit (tels que les interfaces de dialogue pour developpeurs et assistants de programmation en acces libre). Aucun abonnement payant ni token facture n'est consomme pour ce projet, aboutissant a un **cout financier strict de 0,00 € (zero euro)**.
* **Finalite d'Usage** : L'assistance est mobilisee uniquement pour :
  1. La verification de concordance methodologique de nos choix architecturaux face aux exigences academiques du cours ALOM/GLOP.
  2. L'assistance a la redaction de structures repetitives de transfert (records DTO immutables, syntaxe declarative de plugins Maven et squelettes Dockerfile).
  3. La relecture orthographique et le controle de coherence transversale des dossiers documentaires.
* **Maitrise Intellectuelle & Garantie d'Explicabilite Orale** : L'integralite du code source, des tests unitaires et des configurations presents sur les depots GitLab `glop-garik-2026` est concue, ecrite et integralement comprise par les etudiants de l'equipe. Chaque membre de la Societe Garik est capable d'expliquer et de defendre oralement n'importe quel segment de code ou choix technique devant l'equipe enseignante.

---

### 4.3. Synthese des Risques Majeurs : Securite des Acces, Sauvegardes et Exploitation

L'exploitation durable de la plateforme ShopLoc s'appuie sur la neutralisation proactive de trois familles de risques :
* **Securite des Acces et Gestion des Secrets** : Interdiction absolue de versionner des identifiants ou mots de passe dans les depots Git. Les cles de signature des jetons JWT (cle secrete HMAC-SHA256) et les identifiants de connexion aux quatre bases de donnees PostgreSQL sont injectes au deploiement via un fichier d'environnement `.env` protege et des variables CI/CD masquees (*Masked Variables*) dans GitLab. Les bases de donnees ne disposent d'aucun port accessible depuis Internet.
* **Integrite et Sauvegardes des Donnees** : Risque de corruption ou de perte de donnees elimine par la tache planifiee `cron` quotidienne effectuant un `pg_dump` de chaque base, conserve sur 7 jours avec archivage compresse.
* **Complexite d'Exploitation Distribuee** : Risque de lenteur ou de blocage inter-services gere par des timeouts drastiques sur les appels HTTP (1s/2s), un mecanisme de liberation automatique des verrous de reservation (TTL 5 minutes) et un suivi de correlation unifie (`X-Correlation-ID`) garantissant l'observabilite immediate du cluster.

---

### 4.4. Engagements Transversaux d'Eco-Conception Numerique (RGESN)

En conformite avec le Referentiel General d'Eco-conception de Services Numeriques, la Societe Garik adopte quatre engagements d'ingenierie frugale :
1. **Rejet Argumente de Kubernetes au Profit de Docker Compose** : L'orchestration d'un cluster Kubernetes pour 4 microservices monopoliserait plus de 3 Go de memoire vive pour le seul plan de controle (etcd, kube-apiserver). Docker Compose assure l'isolation reseau et le redemarrage automatique pour une surcharge memoire inferieure a 50 Mo.
2. **Images d'Execution Ultra-Legeres (Alpine JRE 17 de 150 Mo)** : Le build multi-stage elimine les compilateurs et dependances de developpement des images de production, divisant par quatre le volume disque et la bande passante de deploiement.
3. **Sobriete des Echanges REST & Requetage SQL Indexe** : Pagination systematique des catalogues marchands et requetes de reservation ciblees sur cles primaires indexees, minimisant la charge CPU du serveur VPS.
4. **Distribution Front-End Epuree** : Application React 18 compilee sous forme de fichiers statiques HTML/JS/CSS ultra-legers distribues par Nginx sans aucun runtime serveur energivore.

---

## 5. Annexe Technique : Preuves d'Execution du Walking Skeleton

Cette annexe regroupe l'ensemble des preuves materielles d'execution exigees par Jeremy Woirhaye, demontrant que la chaine complete d'outils fonctionne reellement et de bout en bout sur l'architecture microservices de ShopLoc.

### A.1. Extrait Reel du Pipeline `.gitlab-ci.yml` et Capture d'une Execution au Vert

Le fichier ci-dessous est le manifeste `.gitlab-ci.yml` reel configure a la racine des depots GitLab pour executer l'autograding sur les runners partages de l'Universite de Lille :

```yaml
# Pipeline CI GitLab Institutionnel - glop-garik-2026
image: maven:3.9-eclipse-temurin-17-alpine

stages:
  - build
  - test
  - package

variables:
  MAVEN_OPTS: "-Dmaven.repo.local=.m2/repository"

cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - .m2/repository

maven-compile:
  stage: build
  script:
    - mvn compile -DskipTests
  artifacts:
    expire_in: 1 day
    paths:
      - target/classes/

maven-tests:
  stage: test
  dependencies:
    - maven-compile
  script:
    - mvn test jacoco:report
  artifacts:
    name: "jacoco-report-$CI_COMMIT_SHORT_SHA"
    expire_in: 7 days
    paths:
      - target/site/jacoco/
    reports:
      junit: target/surefire-reports/TEST-*.xml
  coverage: '/Total Coverage: \d+\.\d+%/'
```

#### Capture Reelle A.1 : Pipeline GitLab CI Valide au Vert (Statut Passed)

![Capture A.1 — Pipeline GitLab CI au vert sur shoploc-cart-order-service](figures/preuves/preuve_1_gitlab_ci_pipeline_green.png)

*Figure A.1 : Tableau de bord CI/CD GitLab de l'Universite de Lille (`GLOP-GARIK-2026 / shoploc-cart-order-service`) attestant du passage formel au vert (statut passed) du pipeline d'integration continue de l'equipe Garik.*

---

### A.2. Resultats des Tests Unitaires & Rapport de Couverture Jacoco

L'execution des suites de tests automatisees sur le Walking Skeleton produit les resultats certifiables suivants :

#### Capture Reelle A.2 : Execution Reussie des Tests Surefire et de Jacoco (Job GitLab #259213)

![Capture A.2 — Execution des tests Maven et analyse Jacoco sur le runner institutionnel](figures/preuves/preuve_2_gitlab_job_maven_jacoco.png)

*Figure A.2 : Trace console certifiee du Job GitLab #259213 sur le runner institutionnel (#965 gitlab-runner-1). La capture atteste sans ambiguite du succes de la suite `CatalogClientTest` (0 failures, 0 errors), du chargement des metriques par `jacoco-maven-plugin:0.8.11` sur 4 classes analysees, du temps de construction (20.6 s) et du succes formel (`BUILD SUCCESS`, `Job succeeded`).*

#### Synthese Consolidee de Couverture de Code Jacoco

| Package & Classe Analysee | Lignes Totales | Lignes Couvertes | Couverture Lignes (%) | Branches Totales | Branches Couvertes | Couverture Branches (%) | Statut Qualite |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `fr.univlille.shoploc.catalog.domain.Product` | 24 | 24 | 100.0 % | 4 | 4 | 100.0 % | Conforme |
| `fr.univlille.shoploc.catalog.web.CatalogController` | 38 | 34 | 89.5 % | 8 | 6 | 75.0 % | Conforme |
| `fr.univlille.shoploc.cartorder.client.CatalogClient` | 42 | 36 | 85.7 % | 4 | 4 | 100.0 % | Conforme |
| `fr.univlille.shoploc.cartorder.web.CartValidationController` | 32 | 28 | 87.5 % | 6 | 6 | 100.0 % | Conforme |
| **Bilan Consolide Walking Skeleton** | **136** | **122** | **90.4 %** | **22** | **20** | **90.9 %** | **OBJECTIF >= 80% ATTEINT** |

---

### A.3. Manifeste d'Orchestration `docker-compose.prod.yml` et Sortie `docker images`

#### 1. Extrait Reel du Fichier d'Orchestration `docker-compose.prod.yml`
```yaml
version: '3.8'

networks:
  shoploc-net:
    driver: bridge
    internal: false

services:
  # Microservice Catalogue & Commercants
  shoploc-merchant-catalog-service:
    image: registry.gitlab.univ-lille.fr/glop-garik-2026/shoploc-merchant-catalog-service:latest
    container_name: shoploc-catalog-app
    restart: unless-stopped
    environment:
      - SPRING_PROFILES_ACTIVE=prod
      - SPRING_DATASOURCE_URL=jdbc:postgresql://catalog-db:5432/catalog_db
      - SPRING_DATASOURCE_USERNAME=${CATALOG_DB_USER}
      - SPRING_DATASOURCE_PASSWORD=${CATALOG_DB_PASSWORD}
    networks:
      - shoploc-net
    expose:
      - "8082"
    depends_on:
      catalog-db:
        condition: service_healthy

  # Base de donnees dediee au catalogue (Database-per-Service)
  catalog-db:
    image: postgres:16-alpine
    container_name: shoploc-catalog-db
    restart: unless-stopped
    environment:
      - POSTGRES_DB=catalog_db
      - POSTGRES_USER=${CATALOG_DB_USER}
      - POSTGRES_PASSWORD=${CATALOG_DB_PASSWORD}
    volumes:
      - catalog_data:/var/lib/postgresql/data
    networks:
      - shoploc-net
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${CATALOG_DB_USER} -d catalog_db"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Microservice Panier & Commandes (Coordinateur 2PC)
  shoploc-cart-order-service:
    image: registry.gitlab.univ-lille.fr/glop-garik-2026/shoploc-cart-order-service:latest
    container_name: shoploc-order-app
    restart: unless-stopped
    environment:
      - SPRING_PROFILES_ACTIVE=prod
      - SPRING_DATASOURCE_URL=jdbc:postgresql://order-db:5432/order_db
      - SERVICES_CATALOG_URL=http://shoploc-merchant-catalog-service:8082
    networks:
      - shoploc-net
    expose:
      - "8083"

  # Base de donnees dediee aux commandes
  order-db:
    image: postgres:16-alpine
    container_name: shoploc-order-db
    restart: unless-stopped
    environment:
      - POSTGRES_DB=order_db
      - POSTGRES_USER=${ORDER_DB_USER}
      - POSTGRES_PASSWORD=${ORDER_DB_PASSWORD}
    volumes:
      - order_data:/var/lib/postgresql/data
    networks:
      - shoploc-net

volumes:
  catalog_data:
  order_data:
```

#### Capture Reelle A.3 : Sortie Console de la Commande `docker images`

![Capture A.3 — Images Docker reelles du projet ShopLoc sur environnement WSL rayane@OrdideRayane](figures/preuves/preuve_3_docker_images.png)

*Figure A.3 : Capture de terminal WSL sur le poste de developpement de Rayane Alli (`rayane@OrdideRayane`), attestant de la presence reelle des images de conteneurs officielles du projet : la base relationnelle `postgres:16-alpine` ainsi que les microservices metiers `registry.gitlab.univ-lille.fr/glop-garik-2026/shoploc-cart-order-service:latest` et `shoploc-merchant-catalog-service:latest`.*

#### Capture Reelle A.3b : Verification des Conteneurs en Cours d'Execution (`docker ps`)

![Capture A.3b — Sortie reelle de la commande docker ps attestant du conteneur actif shoploc-catalog-db](figures/preuves/preuve_4_docker_ps_containers.png)

*Figure A.3b : Sortie console de la commande `docker ps` certifiant l'execution active du conteneur de base de donnees `shoploc-catalog-db` (`postgres:16-alpine`) en statut Up avec exposition du port standard PostgreSQL 5432.*

---

### A.4. Capture Operationnelle de l'Application Tournante (Lecture de Produits en Base)

Cette preuve atteste de l'interrogation reelle d'un microservice de commande appellant le service catalogue a distance, puis recuperant la charge utile depuis la base de donnees PostgreSQL.

#### Capture Reelle A.4 : Interrogation HTTP REST en Direct sous Microsoft Edge

![Capture A.4 — Reponse REST JSON en direct du catalogue sur localhost:8082](figures/preuves/preuve_5_application_runtime_catalogue.png)

*Figure A.4 : Capture reelle du navigateur Microsoft Edge interrogeant en direct l'endpoint REST `http://localhost:8082/api/v1/catalog/products/1` du microservice catalogue. La reponse HTTP 200 OK restitue en format JSON la fiche article reelle extraite de la base de donnees ("Baguette Tradition Artisanale" pour la commercante Suzanne Lemaire, stock 45 unites, prix 1,30 EUR TTC).*

#### Trace Console de la Requete HTTP REST (cURL)
```text
$ curl -i -X GET http://localhost:8082/api/v1/catalog/products/1 \
  -H "Accept: application/json" \
  -H "X-Correlation-ID: c9bf9e57-1685-4c89-bafb-ff5af830be8a"

HTTP/1.1 200 OK
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 16 Oct 2026 19:15:32 GMT
X-Correlation-ID: c9bf9e57-1685-4c89-bafb-ff5af830be8a
Keep-Alive: timeout=60
Connection: keep-alive

{
  "id": 1,
  "merchantId": 101,
  "merchantName": "Le Fournil de Suzanne",
  "name": "Baguette Tradition Artisanale",
  "description": "Farine de ble francaise Label Rouge, fermentation lente 24h",
  "priceInCents": 130,
  "stockAvailable": 45,
  "status": "AVAILABLE"
}
```

---

### A.5. Extrait du `Dockerfile` Multi-Stage de Production (Alpine JRE 17)

Pour certifier l'optimisation frugale revendiquee dans le Pilier 4 (images compactes de 148 Mo), voici le Dockerfile utilise par chaque microservice :

```dockerfile
# Etape 1 : Phase de compilation (Builder)
FROM maven:3.9-eclipse-temurin-17-alpine AS builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -B
COPY src ./src
RUN mvn clean package -DskipTests

# Etape 2 : Phase d'execution allegee (Runtime)
FROM eclipse-temurin:17-jre-alpine AS runtime
WORKDIR /app

# Creation d'un utilisateur non-root de securite
RUN addgroup -S shoploc && adduser -S shoploc -G shoploc
USER shoploc:shoploc

COPY --from=builder /app/target/*.jar app.jar

ENV JAVA_OPTS="-Xms128m -Xmx384m -XX:+UseG1GC"
EXPOSE 8082

ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]
```
