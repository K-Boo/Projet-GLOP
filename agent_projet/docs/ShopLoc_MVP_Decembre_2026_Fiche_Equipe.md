# FICHE D'ALIGNEMENT INTERNE — MVP DÉCEMBRE 2026 (JALON R4)
## Projet ShopLoc — Équipe Garik — Master 2 MIAGE GLOP (2026-2027)
### Université de Lille — Faculté des Sciences et Technologies — Département Informatique

---

## 1. Périmètre & Objectif Stratégique du MVP (Jalon R4 — 18 Décembre 2026)

Le présent document est une **fiche opérationnelle interne** destinée aux cinq membres de l'équipe Garik (Gautam, Rayane, Ilyas, Abdelkader, Khalil). Elle synthétise le périmètre contractuel à réaliser d'ici le **18 décembre 2026**.

### 1.1. La Règle d'Or du Jalon R4 (Consigne Officielle GLOP)
Le sujet de l'UE GLOP stipule expressément :
> *« Réaliser un au choix des composants logiciels jusqu'au déploiement et aux tests. »*

Tenter de développer les 15 User Stories du backlog initial en 7 semaines conduirait inévitablement à un prototype bâclé, truffé de mocks fragiles et sans tests. Conformément à l'arbitrage architectural ADR-020, **notre objectif est de livrer UN composant vertical d'excellence technique** :
* **Composant Cible :** Commande & Panier Multi-Commerces Click & Collect sous protocole Two-Phase Commit (2PC).
* **Critère de Succès Majeur (DoD) :** Couverture de tests unitaires et d'intégration TDD supérieure ou égale à 80 % (Jacoco) avec vérification réelle des cas nominaux et des annulations de commande (*Rollback*).
* **Déploiement :** Conteneurisation intégrale clé en main via `docker compose up --build`.

---

## 2. Matrice Synoptique des 4 Features & 5 User Stories du MVP

Le MVP de Décembre se concentre sur **4 Features interdépendantes** et **5 User Stories (US)** formant une chaîne de valeur complète :

| Réf. Feature | Titre de la Feature | User Stories Associées | Personas Impliqués | Objectif Technique Majeur |
|---|---|---|---|---|
| **F1** | Gestion des Identités &amp; RBAC | **US-01** (Inscription Citoyen)<br>**US-02** (Connexion RBAC) | Julie (Citoyenne)<br>Suzanne (Boulangère) | Sécurisation JWT HMAC-SHA256, isolation stricte ROLE_CITOYEN vs ROLE_MERCHANT_ADMIN. |
| **F2** | Gestion Magasin &amp; Stocks Temps Réel | **US-06** (Fiche Boutique)<br>**US-07** (Articles &amp; Stocks C&amp;C) | Suzanne (Boulangère) | Mise à jour des articles et gestion des quantités réservables en Click &amp; Collect. |
| **F3** | Panier Multi-Commerces &amp; Commande 2PC | **US-09** (Panier Mutualisé &amp; 2PC) | Julie (Citadine) | **Cœur de la démo** : orchestration 2PC, verrous pessimistes PostgreSQL (`SELECT FOR UPDATE`), mock bancaire OpenAPI 3.1. |
| **F4** | Retrait Click &amp; Collect &amp; Clôture | **US-09** (Cycle Retrait) | Julie &amp; Suzanne | Génération du QR Code de retrait signé HMAC-SHA256, validation par le commerçant, clôture transactionnelle. |

*(Note d'équipe : Les 16 autres User Stories du projet — scan caisse en boutique, algorithme VFP nocturne, tickets de bus Ilévia, franchise parking et tableaux de bord DSI — sont formellement planifiées pour le Jalon R5 de Mars 2027).*

---

## 3. Spécifications Détaillées des 4 Features (Règles de Gestion &amp; Gherkin)

### 3.1. Feature F1 : Gestion des Identités &amp; Accès Multi-Rôles (US-01 &amp; US-02)
* **US-01 (Inscription Citoyen) :** En tant que citoyenne (Julie), je crée mon compte en ligne pour obtenir un identifiant unique et ma carte numérique ShopLoc.
* **US-02 (Connexion Sécurisée RBAC) :** En tant qu'utilisateur (Julie ou Suzanne), je me connecte pour accéder à mon espace selon mes habilitations.
* **Règles de Gestion Clés :**
  * `RG-AUTH-01` : Mot de passe fort d'au moins 12 caractères (1 majuscule, 1 minuscule, 1 chiffre, 1 symbole spécial).
  * `RG-AUTH-02` : Attribution automatique d'un UUID v4 unique et d'un rôle strict (ROLE_CITOYEN ou ROLE_MERCHANT_ADMIN).
  * `RG-AUTH-03` : Jeton JWT signé HMAC-SHA256 valide 60 minutes avec rotation sécurisée par Refresh Token.
* **Critères d'Acceptation Gherkin :**
```gherkin
Scénario: Connexion réussie de la commerçante Suzanne
  Étant donné une commerçante enregistrée "suzanne@fournil.fr" avec le rôle "ROLE_MERCHANT_ADMIN"
  Quand elle saisit son adresse email et son mot de passe valide
  Alors le système génère un jeton JWT contenant le claim "role: ROLE_MERCHANT_ADMIN"
  Et elle est redirigée vers son espace de gestion des stocks

Scénario: Échec de connexion avec mot de passe incorrect
  Étant donné une citoyenne enregistrée "julie@citoyenne.fr"
  Quand elle saisit un mot de passe erroné
  Alors le système renvoie une erreur HTTP 401 Unauthorized
  Et aucun jeton de session n'est délivré
```

### 3.2. Feature F2 : Administration Magasin &amp; Stocks Click &amp; Collect (US-06 &amp; US-07)
* **US-06 (Fiche Magasin) :** En tant que commerçante (Suzanne), je configure les coordonnées et horaires d'ouverture de mon fournil.
* **US-07 (Catalogue &amp; Stocks) :** En tant que commerçante (Suzanne), je renseigne mes articles Click &amp; Collect et ajuste les stocks disponibles.
* **Règles de Gestion Clés :**
  * `RG-STK-01` : Chaque article possède un identifiant, une désignation, un prix unitaire TTC en centimes et une quantité entière positive ou nulle.
  * `RG-STK-02` : Si le stock passe à zéro, l'article bascule automatiquement en état RUPTURE et devient indisponible à l'ajout au panier.
  * `RG-STK-03` : La mise à jour d'un stock par le commerçant est immédiatement visible sur le catalogue public (latence inférieure à 500 ms).
* **Critères d'Acceptation Gherkin :**
```gherkin
Scénario: Mise à jour du stock de baguettes par Suzanne
  Étant donné Suzanne connectée sur sa boutique "Le Fournil de Suzanne"
  Quand elle saisit 10 unités pour l'article "Baguette Tradition"
  Alors le stock en base de données passe immédiatement à 10
  Et l'article apparaît comme "Disponible" sur la marketplace citoyenne
```

### 3.3. Feature F3 : Panier Multi-Commerces &amp; Commande Transactionnelle 2PC (US-09)
* **US-09 (Panier &amp; Commande 2PC) :** En tant que cliente (Julie), je sélectionne des produits de plusieurs commerces (Suzanne + Épicerie voisine) et je valide ma commande en une transaction atomique.
* **Règles de Gestion Transactionnelles :**
  * `RG-2PC-01 (Prepare - Réservation)` : À la confirmation de commande, le backend pose un verrou pessimiste PostgreSQL (`SELECT ... FOR UPDATE`) sur les articles et réserve les quantités demandées en statut `STOCK_HOLD` pendant 15 minutes.
  * `RG-2PC-02 (Prepare - Appel Bancaire)` : Le backend appelle le mock bancaire OpenAPI 3.1 conteneurisé.
  * `RG-2PC-03 (Commit)` : Si la banque répond HTTP 200 OK, le coordinateur 2PC valide le COMMIT : les stocks sont décrémentés en base, la commande passe à CONFIRMED et les commerçants reçoivent une notification.
  * `RG-2PC-04 (Rollback / Compensation)` : Si la banque répond HTTP 402 (refus de débit) ou en cas de timeout, le coordinateur déclenche immédiatement un ROLLBACK : les verrous sont relâchés, le statut `STOCK_HOLD` est annulé (`RELEASED`), les stocks reviennent à leur état initial et aucun débit n'est validé.
* **Critères d'Acceptation Gherkin :**
```gherkin
Scénario: Validation nominale d'une commande multi-commerces (Commit 2PC)
  Étant donné Julie avec un panier de 2 Baguettes (Fournil) et 1 Confiture (Épicerie)
  Quand Julie déclenche le paiement avec une carte valide
  Alors le coordinateur 2PC pose un verrou temporaire "STOCK_HOLD" sur les 2 commerces
  Et le mock bancaire retourne le code HTTP 200 OK
  Alors la commande passe au statut "CONFIRMED"
  Et les stocks respectifs des deux commerces sont décrémentés de façon atomique
  Et Julie reçoit son QR code de retrait sécurisé

Scénario: Défaillance bancaire et compensation automatique (Rollback 2PC)
  Étant donné Julie avec un panier de 3 Baguettes (Fournil)
  Quand Julie valide sa commande avec une carte rejetée par le simulateur (HTTP 402)
  Alors le coordinateur 2PC intercepte le refus bancaire
  Et déclenche le rollback immédiat de la réservation de stock
  Alors le statut "STOCK_HOLD" est immédiatement libéré (RELEASED)
  Et le stock du Fournil revient exactement à son niveau initial
  Et aucun montant n'est débité
```

### 3.4. Feature F4 : Retrait Click &amp; Collect &amp; Clôture (US-09 Cycle Retrait)
* **Règles de Gestion Clés :**
  * `RG-RET-01` : La commande confirmée génère un jeton de retrait chiffré sous forme de QR Code (signature HMAC-SHA256).
  * `RG-RET-02` : Le commerçant scanne le QR code lors du passage en boutique pour valider la remise des articles.
  * `RG-RET-03` : La commande bascule au statut COMPLETED et la transaction est archivée avec horodatage certifié.

---

## 4. Conducteur de la Démonstration Live du 18 Décembre (10-12 min)

Voici le scénario exact que nous jouerons en binôme devant le jury :

```
[00:00 - 02:30] ACTE 1 : Préparation & Inventaire Commerçant (Suzanne)
 └─ Connexion ROLE_MERCHANT_ADMIN → Consultation stock boutique → Mise à jour stock Click & Collect

[02:30 - 05:00] ACTE 2 : Expérience Citoyenne Multi-Commerces (Julie)
 └─ Connexion ROLE_CITOYEN → Navigation marketplace → Ajout d'articles de deux boutiques dans le panier

[05:00 - 08:30] ACTE 3 : Climax Transactionnel — Validation 2PC Nominale
 └─ Validation panier → Logs Spring Boot visibles en direct : SELECT FOR UPDATE (Phase 1 Prepare / STOCK_HOLD)
 └─ Appel Mock OpenAPI 3.1 → Réponse HTTP 200 OK → Exécution COMMIT 2PC (Phase 2)
 └─ Écran Julie : Émission du QR Code de retrait HMAC-SHA256
 └─ Écran Suzanne : Alerte commande entrante en temps réel avec décrémentation instantanée du stock

[08:30 - 11:30] ACTE 4 : La Preuve d'Excellence MIAGE — Panne Simulée & Rollback Automatique
 └─ Nouvelle commande avec simulation de carte refusée (HTTP 402 configuré sur le Mock Docker)
 └─ Logs Spring Boot : Détection HTTP 402 → Déclenchement automatique de la COMPENSATION (Rollback 2PC)
 └─ Libération immédiate des verrous PostgreSQL : STOCK_HOLD bascule en RELEASED
 └─ Écran Suzanne : Le stock est restitué à la seconde près, zéro blocage orphelin
 └─ Conclusion Qualité : Présentation de la couverture de tests automated (Jacoco >= 80 %, Testcontainers)
```

---

## 5. Répartition Opérationnelle des Tâches au Sein de l'Équipe Garik

Pour tenir le calendrier de 7 semaines sans dérive, les responsabilités sont réparties comme suit :

| Membre de l'Équipe | Rôle Principal | Responsabilités Techniques sur le MVP | Livrables Attendus |
|---|---|---|---|
| **Gautam** | Lead Backend &amp; Architecture | Coordinateur 2PC Spring Boot 3.3, verrous pessimistes PostgreSQL 16 (`SELECT FOR UPDATE`), persistance JPA/Hibernate, gestion des statuts de commande. | Code backend transactionnel, tests unitaires et intégration Testcontainers. |
| **Rayane** | Lead DevOps &amp; Systèmes | Déploiement docker compose, conteneurisation multi-stage, simulateur Mock OpenAPI 3.1 pour l'API bancaire, pipeline CI GitLab. | Environnement Docker clé en main, simulateurs REST configurables. |
| **Ilyas** | Lead Frontend &amp; Scrum Master | Interface React 18 / TypeScript, portail de gestion de stocks Suzanne, marketplace citoyenne, consultation du panier multi-boutiques. | Interface web responsive, composants d'administration marchande. |
| **Abdelkader** | Frontend &amp; Sécurité | Sécurité d'accès RBAC, gestion des jetons JWT, affichage réactif des QR codes de retrait, respect de l'accessibilité RGAA AA. | Module d'authentification frontend, modal de validation Click &amp; Collect. |
| **Khalil** | Lead QA &amp; Méthodes | Stratégie TDD, couverture de tests Jacoco (seuil strict >= 80 %), tests des scénarios de compensation (*Rollback*), audit qualité. | Rapports de couverture Jacoco, suites de tests Cucumber / Gherkin automatisées. |

---

## 6. Synthèse d'Alignement pour l'Équipe

* **Ce que nous livrons le 18 décembre :** Une application stable, conteneurisée, testée à plus de 80 %, avec une vraie gestion de concurrence et de résilience aux pannes réseau.
* **Ce que nous ne développons PAS pour décembre :** Les règles VFP sur 15 jours, les tickets de bus, le stationnement, les bornes physiques de caisse et les dashboards DSI (reportés au Jalon R5 de Mars 2027).
* **Date limite du Code Freeze :** 15 décembre 2026 (J-3 avant la soutenance, aucun ajout de code, répétition générale de la démo live).
