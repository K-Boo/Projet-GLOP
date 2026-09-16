# SYNTHÈSE INTÉGRALE DES QUESTIONS DE CADRAGE & ARBITRAGES MOE / MOA
## Projet ShopLoc — Marketplace & Programme de Fidélité Multi-Commerces
### Master 2 MIAGE — UE Génie Logiciel par la Pratique (GLOP) 2026-2027 — Université de Lille

---

<!-- EN-TÊTE GRAPHIQUE AVEC LES DEUX LOGOS OFFICIELS -->
<div align="center" style="margin-bottom: 25px;">
  <table style="width: 100%; border: none; background: transparent;">
    <tr style="border: none; background: transparent;">
      <td align="left" style="width: 50%; border: none; vertical-align: middle;">
        <img src="assets/logo_univ_lille.png" alt="Logo Université de Lille" style="height: 60px; max-width: 250px; object-fit: contain;">
      </td>
      <td align="right" style="width: 50%; border: none; vertical-align: middle;">
        <img src="assets/logo_fst_informatique.png" alt="Logo FST Département Informatique" style="height: 60px; max-width: 250px; object-fit: contain;">
      </td>
    </tr>
  </table>
</div>

---

## Informations Générales sur le Document

| Champ | Information |
|---|---|
| **Intitulé du Projet** | **Projet ShopLoc** — Marketplace & Fidélisation multi-commerces |
| **Identifiant Officiel du Projet** | `MiageShopLoc` |
| **Titre du Document** | **Recueil & Synthèse Intégrale des Questions de Cadrage Métier et Réponses de la MOE / MOA (Vagues 1 & 2)** |
| **Référence Documentaire** | `GLOP-2026-R1-SYNTHESE-CADRAGE-v2.0` |
| **Contexte Académique** | Master 2 MIAGE — UE Génie Logiciel par la Pratique (GLOP) 2026-2027 |
| **Maîtrise d'Ouvrage (Clients)** | Laurence Duchien, Anne Etien, François Secchi, Jérémy Woirhaye |
| **Date de Rédaction / Soumission** | 16 Septembre 2026 |
| **Statut du Document** | Version 2.0 — *Clôture définitive du Cadrage Métier (100% des arbitrages validés)* |
| **Tag obligatoire communications** | `[GLOP]` |

---

## Historique des Versions

| Version | Date | Auteur(s) | Nature des Modifications apportées |
|---|---|---|---|
| `v1.0` | 07/09/2026 | Équipe Projet | Consolidation de la première vague d'échanges MOE et identification des points en attente. |
| `v2.0` | 16/09/2026 | Équipe Projet | Intégration de la seconde vague de réponses MOE, clôture de 100% des points de cadrage, formalisation des impacts techniques et architecturaux. |

---

## Table des Matières

1. [Introduction et Périmètre du Document](#1-introduction-et-périmètre-du-document)
2. [Matrice Synthétique Globale des Questions / Réponses](#2-matrice-synthétique-globale-des-questions--réponses)
3. [Section 1 : Rôles des Acteurs et Organisation Territoriale (Q1.1 à Q1.4)](#3-section-1--rôles-des-acteurs-et-organisation-territoriale)
4. [Section 2 : Déploiement et Architecture Multi-Villes (Q2.1 à Q2.4)](#4-section-2--déploiement-et-architecture-multi-villes)
5. [Section 3 : Paiements, Commissions et Gestion des Litiges (Q3.1 à Q3.3)](#5-section-3--paiements-commissions-et-gestion-des-litiges)
6. [Section 4 : Produits, Stocks, Vente au Poids et Horaires (Q4.1 à Q4.4)](#6-section-4--produits-stocks-vente-au-poids-et-horaires)
7. [Section 5 : Programme de Fidélité, Récompenses et Stationnement (Q5.1 à Q5.5)](#7-section-5--programme-de-fidélité-récompenses-et-stationnement)
8. [Section 6 : Administration, Outils Marketing et Protection des Données (Q6.1 à Q6.7)](#8-section-6--administration-outils-marketing-et-protection-des-données)
9. [Section 7 : Connexion, Sécurité et Accessibilité (Q7.1 à Q7.3)](#9-section-7--connexion-sécurité-et-accessibilité)
10. [Section 8 : Priorités pour la V1 (Décembre) et la V2 (Mars) (Q8.1 à Q8.3)](#10-section-8--priorités-pour-la-v1-décembre-et-la-v2-mars)
11. [Section 9 : Démarche d'Éco-Conception et Green IT (Q9.1)](#11-section-9--démarche-déco-conception-et-green-it)
12. [Section 10 : Questions d'Instruction Approfondie pour le Développement (Q10.1 à Q10.6)](#12-section-10--questions-dinstruction-approfondie-pour-le-développement)
13. [Section 11 : Cadrage Complémentaire et Hypothèses Économiques (Q11.1 à Q11.4)](#13-section-11--cadrage-complémentaire-et-hypothèses-économiques)
14. [Section 12 : Modalités des Évaluations et Soutenances](#14-section-12--modalités-des-évaluations-et-soutenances)

---

## 1. Introduction et Périmètre du Document

Le présent document constitue le **référentiel unique et exhaustif** de l'ensemble des questions de cadrage fonctionnel, technique, économique et organisationnel soumises à la Maîtrise d'Ouvrage (MOA / MOE) au cours des deux vagues d'entretiens pour le projet ShopLoc.

Il intègre :
- Les réponses issues de la **première vague d'entretiens** (clarification des rôles, découplage fidélité/VFP, principes du Click & Collect, périmètre multi-villes).
- Les réponses issues de la **seconde et dernière vague d'entretiens** (clôture des alertes marketing, protocoles de transaction 2PC, segmentation, Green IT, sécurité par profil, gratuité usager, périmètre ASVP, et calibrage V1/V2).

Ce recueil sert de base contractuelle et immuable pour la finalisation du Cahier des Charges (Livrable R1), de l'Étude Financière Prévisionnelle (Livrable R3) et de l'Architecture Technique (Livrables R4/R5).

---

## 2. Matrice Synthétique Globale des Questions / Réponses

| ID | Thématique | Question Principale | Arbitrage & Décision MOE Validée | Statut |
|---|---|---|---|---|
| **Q1.1** | Organisation | Rôle de l'Association des Commerçants | Tiers de confiance : gère et valide les adhésions commerçants, dispose d'un panel de pilotage local. | **Validé** |
| **Q1.2** | Organisation | Répartition des rôles Mairie / Association | Convention conjointe : commerçants offrent points/cadeaux, mairie offre bus/parking. Panels distincts. | **Validé** |
| **Q1.3** | Modèle Économique | Facturation du service ShopLoc | Facturation directe à l'Association locale, subventionnée par la Mairie. Modèle libre à justifier (R1/R3). | **Validé** |
| **Q1.4** | Inscription | Processus d'onboarding commerçant | Adhésion préalable obligatoire auprès de l'association, qui débloque les accès dans l'application. | **Validé** |
| **Q2.1** | Architecture | SaaS Multi-tenant vs Instances isolées | Architecture libre. Choix retenu : SaaS Multi-tenant avec partitionnement logique (`tenant_id = ville_id`). | **Validé** |
| **Q2.2** | Multi-Villes | Compte unique usager ou par commune | Système flexible (compte unique ou multiple). Avantages mobilité rattachés à la ville d'achat. | **Validé** |
| **Q2.3** | Scalabilité | Tailles de communes (<20k, 20k-100k, >100k) | Architecture hautement scalable en volume de données et utilisateurs simultanés. | **Validé** |
| **Q2.4** | Objectifs | Leader de marché à 18 mois | Mesuré par la part de marché et la trajectoire de croissance du Chiffre d'Affaires (CA). | **Validé** |
| **Q3.1** | Paiements | Encaissement panier multi-commerçants | Paiement unique en ligne pour le panier groupé, puis collecte physique en boutique. Banque simulée. | **Validé** |
| **Q3.2** | Modèle Économique | Commissionnement sur les ventes | Libre. Retenu : redevance forfaitaire auprès de l'association (0% de commission pour maximiser l'adhésion). | **Validé** |
| **Q3.3** | Litiges | Règle de non-retrait (No-Show) | Si non-retrait dans le délai imparti : commande perdue pour le client, règlement acquis au commerçant. | **Validé** |
| **Q4.1** | Catalogue | Unité des articles alimentaires | Choix laissé au commerçant (pièce, kg, 100g, part). Prix unitaire ferme fixé à la commande en V1. | **Validé** |
| **Q4.2** | Ordonnancement | Délais de disponibilité et horaires | Délai configurable par article. Intégration stricte des emplois du temps et horaires commerçants. | **Validé** |
| **Q4.3** | Stocks | Gestion des stocks Click & Collect | Saisie manuelle par le commerçant. Pas d'interconnexion automatique avec caisses POS en V1. | **Validé** |
| **Q4.4** | Horaires | Fermetures exceptionnelles / congés | Mode configurable activé par le commerçant ; adaptation selon type de produit (délai de retrait mis à jour). | **Validé** |
| **Q5.1** | Fidélité | Barème des points marchands | Découplage strict : points fixés librement par chaque commerçant, indépendants du statut VFP. | **Validé** |
| **Q5.2** | Fidélité | Périmètre des points (Cantonnement) | Points strictement propres à chaque boutique (non échangeables). Achat antérieur requis pour un cadeau. | **Validé** |
| **Q5.3** | Récompenses | Gestion du catalogue de lots | Chaque commerçant crée et met à jour ses propres récompenses dans son catalogue. | **Validé** |
| **Q5.4** | Fidélité | Durée de validité des points | Expiration automatique des points au bout de 12 mois (1 an glissant). | **Validé** |
| **Q5.5** | Financement | Financement des avantages mobilité | La Mairie prend en charge et finance directement les tickets de bus et les 20 min de parking. | **Validé** |
| **Q6.1** | Fidélité | Algorithme du statut VFP | Glissant 15 jours, seuil de 10 passages dans les commerces. 10e passage = 1 ticket ou 20 min parking. Pas de plafond. | **Validé** |
| **Q6.2** | Marketing | Alertes de perte du statut VFP | L'équipe détermine les seuils d'alertes préventives, modulables selon l'adhésion du client. | **Validé** |
| **Q6.3** | Marketing | Canaux de diffusion des offres | L'équipe décide des canaux (ex: push/in-app en V1, courriel ou canal secondaire en V2). | **Validé** |
| **Q6.4** | Marketing | Filtres de segmentation (Marius) | Filtrage par quartier, par type / catégorie de commerçant, et par niveau d'activité usager. | **Validé** |
| **Q6.5** | Enquêtes | Sondages de satisfaction | L'application doit intégrer la possibilité de pousser directement un questionnaire QCM aux usagers. | **Validé** |
| **Q6.6** | RGPD | Confidentialité inter-commerces | Cloisonnement strict inter-commerces (secret d'affaires), agrégation et pseudonymisation pour Marius. | **Validé** |
| **Q6.7** | Ergonomie | Versions simplifiées des parcours | Possibilité et recommandation de proposer des versions épurées/simplifiées selon les cibles (Pierre). | **Validé** |
| **Q7.1** | Accessibilité | Ergonomie pour les usagers seniors | Parcours et connexion épurés pour les seniors (Pierre, 74 ans) sans barrière technique complexe. | **Validé** |
| **Q7.2** | Sécurité | Niveaux de sécurité par profil | Sécurité renforcée obligatoire pour commerçants et administrateurs (accès sensibles) vs client simplifié. | **Validé** |
| **Q7.3** | Mobilité | Déblocage pratique des avantages | Bus : passage/association carte de transport urbain. Parking : saisie plaque et décompte 20 min. | **Validé** |
| **Q8.1** | Planification | Choix du périmètre prioritaire V1 | L'équipe est totalement libre de choisir et justifier les fonctionnalités du MVP de décembre. | **Validé** |
| **Q8.2** | Architecture | Systèmes tiers à simuler (Mocks) | Simulation obligatoire par mocks OpenAPI : passerelle bancaire, transports urbains et stationnement. | **Validé** |
| **Q8.3** | Recette | Scénarios de démonstration | L'équipe définit et calibre ses jeux de données de test et ses scénarios de démonstration. | **Validé** |
| **Q9.1** | Green IT | Métriques d'éco-conception logicielle | Quantification et pilotage précis des ressources consommées (requêtes SQL, charge réseau, tokens). | **Validé** |
| **Q10.1** | Fidélité | Seuil minimal d'achat pour passage VFP | Aucun montant minimal imposé par la MOE. Les deux mécaniques (points vs VFP) sont complémentaires. | **Validé** |
| **Q10.2** | Récompenses | Contrôle applicatif de l'historique | Historique d'achat obligatoire mémorisé. Si aucun achat antérieur chez le marchand, cadeau bloqué. | **Validé** |
| **Q10.3** | Click & Collect | Ordonnancement du panier groupé | Créneaux par boutique avec calcul du plus court chemin pour minimiser l'attente lors de la collecte. | **Validé** |
| **Q10.4** | Transactions | Ruptures de stock et cohérence | Protocole transactionnel en 2 phases (2PC). Cohérence stricte du stock entre boutique et application. | **Validé** |
| **Q10.5** | Habilitations | Profils d'accès par boutique | 1 seul compte / profil administrateur par commerce (gestion unifiée pour l'artisan). | **Validé** |
| **Q10.6** | Sécurité | Détection et gestion des fraudes | Liberté complète pour l'équipe de caractériser les fraudes potentielles et d'intégrer des garde-fous. | **Validé** |
| **Q11.1** | Périmètre | Contrôle stationnement par agent municipal | Hors périmètre applicatif direct ShopLoc (géré par le système externe de voirie de la ville). | **Validé** |
| **Q11.2** | Modèle Économique | Dimensionnement selon taille de ville | L'infrastructure et les données s'adaptent à la taille de la commune (métrique de succès et de croissance). | **Validé** |
| **Q11.3** | Modèle Économique | Gratuité de la carte et du service usager | Strictement gratuit pour le client usager (levier d'incitation à la fréquentation des commerces). | **Validé** |
| **Q11.4** | Technologie | Nature de l'application cliente | Développement d'une application Web responsive (accessible desktop et mobile). | **Validé** |

---

## 3. Section 1 : Rôles des Acteurs et Organisation Territoriale

### Question 1.1 (Q.A1) — Rôle et accès de l'Association des Commerçants
* **Question formulée** : Quel est le rôle prévu pour l'Association des commerçants dans l'application : doit-elle valider l'inscription des commerçants de la commune, dispose-t-elle d'un tableau de bord statistique, ou n'intervient-elle qu'à la signature contractuelle ?
* **Intérêt pour le projet** : Définir si un espace dédié avec des droits de modération et de suivi doit être modélisé.
* **Réponse validée MOE / MOA** :  
  La demande émane conjointement de l'association des commerçants (association loi 1901) et de la mairie, liées par une convention pour revitaliser le centre-ville. Le commerçant doit **obligatoirement être adhérent de l'association locale** pour intégrer ShopLoc. C'est l'association qui contrôle les adhésions et débloque les accès dans l'application. Elle dispose d'un panel de gestion et de visualisation d'indicateurs pour suivre l'activité et prévenir les fraudes.
* **Impact d'ingénierie & Décision** :  
  Création de l'entité `MerchantAssociation` et d'un rôle `ROLE_ASSOCIATION_ADMIN` dans le système RBAC. Écran de validation des comptes commerçants pré-ouverture.

---

### Question 1.2 (Q.A2) — Répartition des rôles entre Mairie et Association
* **Question formulée** : Comment s'organise la collaboration entre la mairie et l'association : qui diffuse les communications, lance les campagnes et arbitre en cas de désaccord ?
* **Intérêt pour le projet** : Définir les habilitations respectives sur l'espace d'administration et de communication.
* **Réponse validée MOE / MOA** :  
  L'association et la mairie sont liées par convention. Les engagements et promesses sont clairement répartis :
  1. **Les commerces** promettent des points de fidélité et des cadeaux sur leurs articles.
  2. **La mairie** promet des tickets de bus et du stationnement gratuit (20 minutes).  
  Chacune des deux entités dispose d'un panel de gestion ou de visualisation propre.
* **Impact d'ingénierie & Décision** :  
  Cloisonnement des vues d'administration : Espace Ville (Marius / Mairie) centré sur la mobilité et les indicateurs territoriaux, Espace Association centré sur l'animation commerciale et la gestion des adhérents.

---

### Question 1.3 (Q.A3) — Modèle économique et facturation de la solution
* **Question formulée** : À qui ShopLoc vend-elle son service : à la Mairie, à l'Association des commerçants, ou directement aux commerçants par abonnement ?
* **Intérêt pour le projet** : Cadrage de l'étude financière (Livrable R3) et du circuit de facturation SaaS.
* **Réponse validée MOE / MOA** :  
  ShopLoc facture directement l'**Association des commerçants**. La mairie verse quant à elle une subvention à l'association pour financer le dispositif. L'équipe est totalement libre de calibrer son modèle économique (forfait, paliers), qui sera formellement défendu dans les livrables R1 et R3.
* **Impact d'ingénierie & Décision** :  
  Facturation SaaS B2B adressée à l'association locale. Pas de frais récurrents directs prélevés sur les artisans, favorisant une adoption massive.

---

### Question 1.4 (Q.A4) — Processus d'inscription d'un commerçant
* **Question formulée** : L'inscription d'un commerçant est-elle libre et immédiate en ligne ou nécessite-t-elle une validation préalable ?
* **Intérêt pour le projet** : Conception du workflow d'onboarding et des états du compte marchand (`PENDING_APPROVAL`, `ACTIVE`, `SUSPENDED`).
* **Réponse validée MOE / MOA** :  
  Le commerçant doit obligatoirement être adhérent de l'association locale. C'est l'association qui valide et débloque formellement l'accès du commerçant dans l'application.
* **Impact d'ingénierie & Décision** :  
  Machine à états stricte pour le commerçant. Enregistrement initial en statut `PENDING_ASSOCIATION_VALIDATION`, activation uniquement après validation manuelle par l'administrateur de l'association.

---

## 4. Section 2 : Déploiement et Architecture Multi-Villes

### Question 2.1 (Q.B1) — Plateforme mutualisée (SaaS) vs Déploiement isolé par ville
* **Question formulée** : Faut-il concevoir une application SaaS mutualisée (multi-tenant) ou une instance déployée séparément par collectivité ?
* **Intérêt pour le projet** : Choix fondamental d'architecture logicielle et de schéma de base de données relationnelle.
* **Réponse validée MOE / MOA** :  
  L'équipe est libre de son choix d'architecture à condition de savoir le justifier.  
  **Choix validé** : Architecture **SaaS multi-tenant avec base de données partagée et partitionnement logique strict** (`tenant_id = ville_id`).
* **Impact d'ingénierie & Décision** :  
  Enregistré dans l'ADR-004. Optimisation des coûts d'hébergement, simplicité des montées de version et isolation logique par filtres SQL / ORM automatiques.

---

### Question 2.2 (Q.B2) — Rattachement usager et gestion des comptes
* **Question formulée** : Un usager fréquentant plusieurs villes possède-t-il un compte unique transversal ou un compte par commune ?
* **Intérêt pour le projet** : Modélisation des tables d'utilisateurs et découplage des soldes de points par commune.
* **Réponse validée MOE / MOA** :  
  Le système doit offrir la flexibilité : possibilité pour l'usager d'utiliser un compte unique ou plusieurs comptes selon sa convenance. Les avantages mobilité (bus, parking) restent strictement rattachés à la ville où les passages et achats ont été réalisés.
* **Impact d'ingénierie & Décision** :  
  Gestion d'une identité utilisateur globale liée à des profils de fidélité et de mobilité cantonnés par ville (`UserCityProfile`).

---

### Question 2.3 (Q.B3) — Adaptation selon la taille de la commune
* **Question formulée** : Quelles sont les exigences liées aux trois tailles de communes (<20k, 20k-100k, >100k habitants) ?
* **Intérêt pour le projet** : Dimensionnement des capacités de montée en charge et modularité.
* **Réponse validée MOE / MOA** :  
  L'architecture logicielle et technique doit être hautement scalable pour absorber aussi bien une charge locale qu'une montée en charge d'envergure métropolitaine en termes de volume de données et de requêtes concurrentes.
* **Impact d'ingénierie & Décision** :  
  Conception de requêtes SQL indexées, pagination systématique des API et architecture prête pour le cache applicatif.

---

### Question 2.4 (Q.B4) — Objectifs d'évaluation pour le cap des 18 mois
* **Question formulée** : Sur quels indicateurs le succès et la position de leader à 18 mois seront-ils évalués ?
* **Intérêt pour le projet** : Aligner la stratégie produit et les tableaux de bord sur les attentes MOA.
* **Réponse validée MOE / MOA** :  
  L'indicateur clé est la **part de marché**, couplée au suivi rigoureux du Chiffre d'Affaires (CA) et à un niveau de croissance soutenu sur les villes cibles.
* **Impact d'ingénierie & Décision** :  
  Intégration d'indicateurs de performance (KPI) dans l'Espace d'administration pour suivre le taux de pénétration par commune et la dynamique d'adhésion marchande.

---

## 5. Section 3 : Paiements, Commissions et Gestion des Litiges

### Question 3.1 (Q.C1) — Encaissement du panier multi-commerçants
* **Question formulée** : Comment s'effectue le paiement d'une commande groupée comprenant des articles de plusieurs boutiques ?
* **Intérêt pour le projet** : Spécification du flux de paiement et modélisation des sous-commandes marchandes.
* **Réponse validée MOE / MOA** :  
  Le client effectue un **paiement unique en ligne** pour l'intégralité de son panier multi-commerçants. Il se rend ensuite physiquement chez chacun des artisans concernés pour retirer ses articles. La passerelle bancaire est entièrement simulée (mock REST OpenAPI).
* **Impact d'ingénierie & Décision** :  
  Modèle `Order` global regroupant plusieurs `MerchantSubOrder`. Service de simulation bancaire mocké sans dépendance monétique tierce.

---

### Question 3.2 (Q.C2) — Modèle de commissionnement sur les ventes
* **Question formulée** : ShopLoc prélève-t-elle une commission sur les transactions Click & Collect ?
* **Intérêt pour le projet** : Modélisation des flux financiers et étude prévisionnelle R3.
* **Réponse validée MOE / MOA** :  
  La partie financière réelle étant simulée, le modèle de tarification est laissé au choix de l'équipe. L'équipe retient une **redevance forfaitaire auprès de l'association sans prélèvement de commission sur les ventes** (0% de commission) afin de maximiser l'adhésion des commerçants de proximité.
* **Impact d'ingénierie & Décision** :  
  Aucune retenue financière sur le chiffre d'affaires des commerçants. Intégralité du montant de la commande reversée au commerçant lors de la collecte.

---

### Question 3.3 (Q.C3) — Règle de non-retrait d'une commande (No-Show)
* **Question formulée** : Que devient une commande payée en ligne si le client ne vient jamais la récupérer ?
* **Intérêt pour le projet** : Sécurisation de la machine à états et gestion des articles périssables.
* **Réponse validée MOE / MOA** :  
  Si le client ne se présente pas dans le créneau imparti (no-show), **la commande est définitivement perdue pour le client et le montant payé demeure intégralement acquis au commerçant**.
* **Impact d'ingénierie & Décision** :  
  État de commande `EXPIRED_NO_SHOW`. Protection économique des artisans face au gaspillage de denrées préparées.

---

## 6. Section 4 : Produits, Stocks, Vente au Poids et Horaires

### Question 4.1 (Q.D1) — Choix de l'unité des produits
* **Question formulée** : Comment modéliser les articles vendus à la pièce, au poids, aux 100g ou à la part ?
* **Intérêt pour le projet** : Conception de l'entité `Product` et flexibilité du catalogue alimentaire.
* **Réponse validée MOE / MOA** :  
  Le commerçant choisit librement l'unité du produit (à la pièce, au kg, aux 100g, à la part). Pour la V1, le prix unitaire est déterminé et fixé à la commande pour simplifier les calculs et éviter les régularisations a posteriori.
* **Impact d'ingénierie & Décision** :  
  Attribut énuméré `UnitType` (`PIECE`, `KG`, `HUNDRED_GRAMS`, `PORTION`) associé à un prix unitaire fixe.

---

### Question 4.2 (Q.D2) — Délais de disponibilité et cohérence des plannings
* **Question formulée** : Comment ordonnancer la préparation des commandes et garantir la cohérence des retraits ?
* **Intérêt pour le projet** : Algorithme de calcul des créneaux de disponibilité et optimisation de tournée.
* **Réponse validée MOE / MOA** :  
  Le commerçant peut définir un délai de préparation par article. Le système doit obligatoirement croiser ces délais avec les horaires d'ouverture de chaque boutique pour garantir la cohérence des créneaux de collecte.
* **Impact d'ingénierie & Décision** :  
  Moteur de vérification de créneau calculant l'heure minimale de disponibilité `max(delai_preparation) + heure_commande` et validant l'ouverture de l'établissement.

---

### Question 4.3 (Q.D3) — Gestion des stocks en Click & Collect
* **Question formulée** : La gestion des stocks est-elle manuelle ou connectée à des caisses enregistreuses externes (POS) ?
* **Intérêt pour le projet** : Délimitation du périmètre des connecteurs externes en V1.
* **Réponse validée MOE / MOA** :  
  Le commerçant saisit manuellement ses articles et ajuste ses stocks dans son interface dédiée (mise à jour journalière ou ponctuelle). L'interconnexion automatique avec des caisses externes n'est pas requise en V1.
* **Impact d'ingénierie & Décision** :  
  Tableau de bord commerçant avec actions rapides d'ajustement de stock et bascule de disponibilité en un clic.

---

### Question 4.4 (Q.D4) — Gestion des fermetures exceptionnelles et congés
* **Question formulée** : Comment gérer les congés ou fermetures inattendues sans supprimer les catalogues ?
* **Intérêt pour le projet** : Continuité de service et fiabilité des créneaux présentés aux usagers.
* **Réponse validée MOE / MOA (Vagues 1 & 2)** :  
  L'application doit proposer un **mode fermeture / congés** que le commerçant active à sa guise. Le système s'adapte selon la nature du produit : pour un article non périssable (ex: produit électrique ou manufacturé), le système ajuste automatiquement la date et le délai de retrait sans bloquer le catalogue.
* **Impact d'ingénierie & Décision** :  
  Flag `is_temporarily_closed` sur le profil marchand avec recalcul dynamique des dates de disponibilité proposées au panier.

---

## 7. Section 5 : Programme de Fidélité, Récompenses et Stationnement

### Question 5.1 (Q.E1) — Barème des points de fidélité marchands
* **Question formulée** : Le barème de points est-il unifié au niveau municipal ou propre à chaque artisan ?
* **Intérêt pour le projet** : Moteur de fidélité et découplage avec le statut citoyen VFP.
* **Réponse validée MOE / MOA** :  
  **Découplage strict en 2 mécaniques indépendantes** :
  1. Les points de fidélité marchands : chaque commerçant fixe librement son barème (points par produit ou par tranche d'achat).
  2. Le statut VFP : basé uniquement sur la régularité des passages.
* **Impact d'ingénierie & Décision** :  
  Enregistré dans l'ADR-005. Deux moteurs étanches : `MerchantPointsService` et `VFPStatusService`.

---

### Question 5.2 (Q.E2) — Périmètre des points (Cantonnement vs Mutualisation)
* **Question formulée** : Les points accumulés chez un marchand sont-ils utilisables chez un confrère ?
* **Intérêt pour le projet** : Éviter la complexité d'une chambre de compensation financière inter-commerces.
* **Réponse validée MOE / MOA** :  
  Les points sont **strictement cantonnés à chaque commerçant**. On ne mélange pas les points entre boutiques. Pour obtenir un cadeau, l'usager doit disposer d'un historique d'achat antérieur chez cet artisan et présenter sa carte lors d'un acte d'achat en cours.
* **Impact d'ingénierie & Décision** :  
  Table `MerchantCustomerBalance` avec clé composite `(customer_id, merchant_id)`. Pas de transfert de solde inter-boutiques.

---

### Question 5.3 (Q.E3) — Responsabilité du catalogue de récompenses
* **Question formulée** : Qui alimente et met à jour les lots et cadeaux disponibles ?
* **Intérêt pour le projet** : Droits d'administration CRUD sur les récompenses.
* **Réponse validée MOE / MOA** :  
  Chaque commerçant définit, calibre et met à jour ses propres récompenses dans son propre catalogue (ex: Suzanne adaptant ses viennoiseries ou douceurs).
* **Impact d'ingénierie & Décision** :  
  Entité `Reward` rattachée directement à `Merchant`. Interface commerçant dédiée à la création de lots avec coût en points associé.

---

### Question 5.4 (Q.E4) — Durée de validité des points accumulés
* **Question formulée** : Les points sont-ils valables indéfiniment ou soumis à une date d'expiration ?
* **Intérêt pour le projet** : Batch d'expiration automatique en base de données relationnelle.
* **Réponse validée MOE / MOA** :  
  Les points expirent automatiquement au bout de **12 mois (1 an glissant)** sans utilisation.
* **Impact d'ingénierie & Décision** :  
  Historisation des gains de points avec timestamp d'expiration et tâche planifiée nocturne d'invalidation des points échus.

---

### Question 5.5 (Q.E5) — Financement des avantages mobilité (Bus et Parking)
* **Question formulée** : Qui finance le coût des titres de transport et des 20 minutes de stationnement offerts ?
* **Intérêt pour le projet** : Modélisation des flux financiers municipaux et conventions de subventionnement.
* **Réponse validée MOE / MOA** :  
  **La Mairie finance et prend directement en charge** l'intégralité du coût des tickets de bus et des 20 minutes de parking dans le cadre de sa politique publique d'attractivité du centre-ville.
* **Impact d'ingénierie & Décision** :  
  Comptabilité analytique dédiée dans l'espace Mairie pour le décompte des avantages municipaux distribués et valorisation financière globale.

---

## 8. Section 6 : Administration, Outils Marketing et Protection des Données

### Question 6.1 (Q.F1) — Algorithme de calcul du statut VFP
* **Question formulée** : Quels critères régissent précisément l'obtention et le maintien du statut Very Faithful Person ?
* **Intérêt pour le projet** : Spécification formelle de l'algorithme nocturne VFP.
* **Réponse validée MOE / MOA** :  
  1. Calcul basé sur une **fenêtre glissante de 15 jours**.
  2. Seuil d'éligibilité : **au moins 10 passages avec achat** au cours des 15 derniers jours.
  3. Aucune limitation par jour ni obligation de mixité commerciale (les 10 passages peuvent être réalisés chez un artisan unique).
  4. À l'atteinte des 10 passages : déblocage immédiat d'un avantage au choix (1 ticket de bus ou 20 minutes de parking).
  5. **Aucun plafond de cumul** : chaque nouveau passage additionnel octroie un avantage supplémentaire tant que la condition de régularité (>= 10 passages sur 15 jours) demeure satisfaite.
* **Impact d'ingénierie & Décision** :  
  Service `VfpCalculationBatch` évaluant chaque nuit les événements d'achat des 15 derniers jours et incrémentant le crédit mobilité usager.

---

### Question 6.2 (Q.F2) — Perte du statut VFP et alertes marketing préventives
* **Question formulée** : Le système doit-il avertir automatiquement l'usager avant qu'il ne perde son statut VFP ?
* **Intérêt pour le projet** : Automatisation des notifications de rétention client.
* **Réponse validée MOE / MOA (Vague 2)** :  
  **Oui, l'équipe définit les seuils d'alerte**. Plusieurs seuils d'alerte préventive sont paramétrables en fonction du degré d'adhésion et d'engagement de l'usager (ex: alerte à J-3 ou J-2 avant la sortie de la fenêtre glissante).
* **Impact d'ingénierie & Décision** :  
  Déclencheur d'alerte automatique identifiant les usagers dont le nombre de passages valides risque de passer sous le seuil de 10 dans les 48h à 72h.

---

### Question 6.3 (Q.F3) — Canaux de diffusion des offres promotionnelles
* **Question formulée** : Par quels canaux l'administrateur (Marius) diffuse-t-il les offres et informations ?
* **Intérêt pour le projet** : Choix des connecteurs de notification (push web, e-mail, in-app).
* **Réponse validée MOE / MOA (Vague 2)** :  
  **Le choix est laissé à l'équipe**. Il est possible de déployer un canal principal en V1 (ex: notifications in-app et push web) et d'ajouter un second canal en V2 (ex: e-mailing ou notifications enrichies).
* **Impact d'ingénierie & Décision** :  
  Architecture modulaire avec interface `NotificationSender` implémentant le canal `InAppNotificationSender` en V1 et extensible pour d'autres canaux en V2.

---

### Question 6.4 (Q.F4) — Filtres de segmentation marketing disponibles
* **Question formulée** : Quels critères de filtrage Marius peut-il combiner pour cibler ses communications ?
* **Intérêt pour le projet** : Conception de l'API de filtrage dynamique et indexation de la base de données.
* **Réponse validée MOE / MOA (Vague 2)** :  
  Possibilité de filtrer et cibler par **quartier**, par **type / catégorie de commerçant** et par typologie d'activité client.
* **Impact d'ingénierie & Décision** :  
  Requête dynamique avec filtres multicritères sur les tables `Neighborhood`, `MerchantCategory` et `UserActivity`.

---

### Question 6.5 (Q.F5) — Portée des sondages de satisfaction usagers
* **Question formulée** : L'application doit-elle embarquer un moteur de sondage complet ou un lien externe ?
* **Intérêt pour le projet** : Modélisation des questionnaires de satisfaction dans le schéma relationnel.
* **Réponse validée MOE / MOA (Vague 2)** :  
  L'application doit **permettre de pousser directement un QCM (Questionnaire à Choix Multiples)** aux usagers ciblés.
* **Impact d'ingénierie & Décision** :  
  Modélisation des entités `Survey`, `SurveyQuestion` et `SurveyAnswer` pour diffuser des questionnaires courts sur les applications usagers.

---

### Question 6.6 (Q.F6) — Respect de la vie privée et conformité RGPD
* **Question formulée** : Quel est le cadre de conformité RGPD et de confidentialité commerciale ?
* **Intérêt pour le projet** : Vues de données sécurisées, pseudonymisation et consentement usager.
* **Réponse validée MOE / MOA** :  
  L'association et la mairie accèdent à des indicateurs consolidés pour piloter le dynamisme et prévenir les fraudes. **Cloisonnement strict et secret des affaires entre boutiques** : aucun commerçant ne peut accéder aux chiffres ou paniers d'un confrère. Les données administratives sont strictement agrégées et pseudonymisées.
* **Impact d'ingénierie & Décision** :  
  Enregistré dans l'ADR-008. Cloisonnement par rôles au niveau applicatif et politique stricte de confidentialité des données personnelles.

---

### Question 6.7 — Simplification des interfaces et personnalisation usager
* **Question formulée** : Est-il autorisé de proposer des interfaces simplifiées ou adaptées selon les profils ?
* **Intérêt pour le projet** : Conception UX/UI multi-personas (seniors, commerçants pressés).
* **Réponse validée MOE / MOA (Vague 2)** :  
  **Oui, simplification autorisée et encouragée**. L'équipe doit proposer des versions simplifiées selon ses choix de conception afin de maximiser l'accessibilité et l'adoption.
* **Impact d'ingénierie & Décision** :  
  Interface épurée et mode fort contraste pour le persona Pierre (74 ans), tableau de bord synthétique pour Suzanne.

---

## 9. Section 7 : Connexion, Sécurité et Accessibilité

### Question 7.1 (Q.G1) & Question 7.2 (Q.G2) — Niveaux de sécurité d'authentification par profil
* **Question formulée** : Quel niveau de sécurité et de complexité d'authentification appliquer pour chaque catégorie d'acteurs (clients vs commerçants et administrateurs) ?
* **Intérêt pour le projet** : Politique d'authentification backend, gestion des sessions et conformité RGAA.
* **Réponse validée MOE / MOA (Vague 2)** :  
  - Pour les **clients usagers** (ex: Pierre, Julie) : authentification simplifiée, ergonomique et accessible sans friction inutile.
  - Pour les **commerçants** et les **administrateurs** : **obligation de proposer un niveau de sécurité supérieur** (mots de passe renforcés, contrôle d'accès strict ou double facteur) compte tenu de la criticité des données gérées.
* **Impact d'ingénierie & Décision** :  
  Différenciation de la politique d'authentification : JWT standard avec interface adaptée pour les usagers, exigences de complexité et sessions sécurisées avec temporisation pour les espaces marchands et institutionnels.

---

### Question 7.3 (Q.G3) — Matérialisation de l'activation des avantages mobilité
* **Question formulée** : Comment l'usager fait-il valoir son droit au ticket de transport et au stationnement gratuit ?
* **Intérêt pour le projet** : Parcours usager de déblocage des privilèges dans l'interface web/mobile.
* **Réponse validée MOE / MOA** :  
  1. **Tickets de Bus** : L'usager associe ou présente sa carte de transport urbain de la collectivité (ex: carte Pass Pass / Ilévia).
  2. **Stationnement Gratuit** : L'usager saisit son numéro de plaque d'immatriculation dans l'application et déclenche son compteur de 20 minutes offertes.
* **Impact d'ingénierie & Décision** :  
  Écran « Mes Avantages Mobilité » avec compte à rebours visuel de 20 minutes pour le stationnement et liaison de carte de transport urbain.

---

## 10. Section 8 : Priorités pour la V1 (Décembre) et la V2 (Mars)

### Question 8.1 (Q.H1) — Choix du périmètre fonctionnel prioritaire pour la V1
* **Question formulée** : Quel sous-système logiciel doit obligatoirement être livré pour la soutenance de fin décembre ?
* **Intérêt pour le projet** : Trajectoire des sprints agiles et cadrage du MVP (Minimum Viable Product).
* **Réponse validée MOE / MOA (Vague 2)** :  
  **L'équipe est totalement libre de choisir les fonctionnalités de la V1**, à condition de formaliser, justifier et défendre ce périmètre dans ses livrables de cadrage.
* **Impact d'ingénierie & Décision** :  
  Périmètre V1 focalisé sur : Authentification multi-profils, Catalogue commerçant & Stock manuel, Panier Click & Collect multi-boutiques avec tournée optimale, Moteur de fidélité par points et calcul VFP, Mocks bancaires et mobilité.

---

### Question 8.2 (Q.H2) — Systèmes externes à simuler (Mocks)
* **Question formulée** : Quels systèmes tiers doivent faire l'objet d'une simulation logicielle ?
* **Intérêt pour le projet** : Définition des contrats d'interface OpenAPI.
* **Réponse validée MOE / MOA** :  
  Toutes les interactions avec des systèmes externes doivent être **obligatoirement simulées par des mocks logiciels d'API** :
  - Passerelle de paiement bancaire en ligne.
  - Système de billettique des transports urbains municipaux.
  - Système de gestion de stationnement en voirie.
* **Impact d'ingénierie & Décision** :  
  Développement de contrôleurs de mock dédiés avec contrats OpenAPI documentés, garantissant une autonomie totale en environnement de démonstration et de test.

---

### Question 8.3 (Q.H3) — Périmètre des données et scénarios de démonstration
* **Question formulée** : Quels scénarios types et jeux de données sont attendus lors des revues de projet ?
* **Intérêt pour le projet** : Calibrage des scripts de seed SQL pour les revues clients.
* **Réponse validée MOE / MOA (Vague 2)** :  
  **L'équipe décide de ses jeux de données et de ses scénarios de démonstration**.
* **Impact d'ingénierie & Décision** :  
  Mise à disposition d'un script de peuplement SQL complet instanciant la commune de référence avec commerçants types (Suzanne), clients types (Pierre, Julie, Arthur) et administrateur (Marius).

---

## 11. Section 9 : Démarche d'Éco-Conception et Green IT

### Question 9.1 (Q.I1) — Critères d'évaluation de l'éco-conception logicielle
* **Question formulée** : Quels indicateurs précis et démarches concrètes sont évalués pour le volet Green IT ?
* **Intérêt pour le projet** : Intégration de métriques d'éco-conception dans le cycle de développement.
* **Réponse validée MOE / MOA (Vague 2)** :  
  Il convient de **quantifier rigoureusement les ressources, mesurer la consommation de tokens / requêtes et piloter finement leur utilisation**.
* **Impact d'ingénierie & Décision** :  
  Mise en place de l'outil `token_tracker.py` et de la passerelle LiteLLM Proxy pour l'outillage de développement, requêtes SQL frugales et compression des flux d'images sur le produit applicatif.

---

## 12. Section 10 : Questions d'Instruction Approfondie pour le Développement

### Question 10.1 (Q.J1) — Seuil minimal d'achat pour validation d'un passage VFP
* **Question formulée** : Existe-t-il un montant d'achat minimum requis pour valider un passage éligible au statut VFP ?
* **Intérêt pour le projet** : Règle de validation dans le service de comptabilisation des passages.
* **Réponse validée MOE / MOA (Vague 2)** :  
  **Aucun montant minimum d'achat exigé**. Les deux systèmes sont complémentaires : le système de points par achat d'une part, et le système de régularité VFP d'autre part. Tout acte d'achat réel valide le passage.
* **Impact d'ingénierie & Décision** :  
  Enregistrement d'un passage VFP dès qu'une transaction marchande strictement supérieure à 0,00 € est validée en caisse ou en ligne.

---

### Question 10.2 (Q.J2) — Blocage applicatif lors de la délivrance des cadeaux
* **Question formulée** : Comment l'application commerçant valide-t-elle la condition d'achat antérieur lors du retrait d'une récompense ?
* **Intérêt pour le projet** : Règle bloquante dans le contrôleur de caisse.
* **Réponse validée MOE / MOA (Vague 2)** :  
  L'application **doit impérativement mémoriser l'historique des achats**. Il faut au moins un achat antérieur enregistré chez ce commerçant, **faute de quoi la délivrance du cadeau est automatiquement bloquée par l'application**.
* **Impact d'ingénierie & Décision** :  
  Vérification de l'existence d'au moins une transaction antérieure finalisée `Order.status = COMPLETED` pour le couple `(customer_id, merchant_id)` avant d'autoriser le débit des points et la délivrance du lot.

---

### Question 10.3 (Q.J3) — Ordonnancement de la collecte multi-commerçants
* **Question formulée** : Comment synchroniser les créneaux de retrait lors d'une commande multi-boutiques ?
* **Intérêt pour le projet** : Conception de l'algorithme d'itinéraire de retrait.
* **Réponse validée MOE / MOA** :  
  Gestion des créneaux boutique par boutique, combinée avec un **algorithme d'optimisation du plus court chemin** qui minimise les temps d'attente entre chaque étape de la tournée pour l'usager.
* **Impact d'ingénierie & Décision** :  
  Module de calcul d'itinéraire groupé proposant une séquence ordonnée de passage chez les commerçants partenaires.

---

### Question 10.4 (Q.J4) — Gestion transactionnelle des ruptures et cohérence des stocks
* **Question formulée** : Comment traiter les risques d'incohérence ou de rupture lors d'un paiement multi-boutiques ?
* **Intérêt pour le projet** : Conception de la couche transactionnelle backend (ACID / 2PC).
* **Réponse validée MOE / MOA (Vague 2)** :  
  Mise en place d'un **système transactionnel avec protocole en deux phases (Two-Phase Commit - 2PC)**. Le système part du principe que le stock affiché est disponible au moment de l'acte d'achat. Le commerçant doit maintenir une stricte cohérence entre son stock physique et l'application.
* **Impact d'ingénierie & Décision** :  
  Transaction distribuée ou orchestrée en 2 phases : Phase 1 (Réservation préalable des stocks chez chaque commerçant du panier), Phase 2 (Validation définitive du paiement et confirmation des commandes, ou rollback complet en cas d'indisponibilité).

---

### Question 10.5 (Q.J5) — Profils d'habilitation au sein d'une boutique
* **Question formulée** : Faut-il distinguer plusieurs rôles d'employés (vendeur vs propriétaire) au sein d'un compte commerçant ?
* **Intérêt pour le projet** : Complexité du modèle RBAC commerçant.
* **Réponse validée MOE / MOA (Vague 2)** :  
  **Un seul profil administrateur par commerçant**.
* **Impact d'ingénierie & Décision** :  
  Modélisation simplifiée et robuste : 1 compte marchand unique par boutique physique, évitant une hiérarchie complexe d'utilisateurs internes en V1.

---

### Question 10.6 (Q.J6) — Détection des fraudes et mécanismes de sécurité
* **Question formulée** : Quels garde-fous anti-fraude intégrer face aux abus potentiels sur les avantages municipaux ?
* **Intérêt pour le projet** : Conception du module de détection d'anomalies de fréquentation.
* **Réponse validée MOE / MOA (Vague 2)** :  
  **L'équipe est totalement libre de définir les typologies de fraudes potentielles et de sécuriser le système en conséquence**.
* **Impact d'ingénierie & Décision** :  
  Mise en place d'indicateurs d'alertes sur les fréquences de passages suspectes (ex: scans multiples en un intervalle de quelques secondes) et possibilité de suspension temporaire pour l'administrateur associatif / municipal.

---

## 13. Section 11 : Cadrage Complémentaire et Hypothèses Économiques

### Question 11.1 (Q.K1) — Contrôle du stationnement par un agent municipal (ASVP)
* **Question formulée** : Le cas d'usage de contrôle du stationnement en voirie par la police municipale fait-il partie de l'application ShopLoc ?
* **Intérêt pour le projet** : Périmètre des acteurs et des écrans applicatifs.
* **Réponse validée MOE / MOA (Vague 2)** :  
  **Hors périmètre direct de l'application ShopLoc**. Cette fonction relève du système externe de gestion de voirie de la ville (qui consomme l'API de stationnement simulée).
* **Impact d'ingénierie & Décision** :  
  Pas d'écran applicatif dédié à la police municipale à développer dans ShopLoc. Fourniture d'un endpoint API REST mocké `GET /api/v1/parking/check/{plateNumber}` pour simuler la vérification en voirie.

---

### Question 11.2 (Q.K2) — Dimensionnement de l'infrastructure selon la commune
* **Question formulée** : Comment calibrer la tarification et l'infrastructure selon la taille de la ville ?
* **Intérêt pour le projet** : Dimensionnement de l'hébergement serveur et grille tarifaire du Livrable R3.
* **Réponse validée MOE / MOA (Vague 2)** :  
  La taille des données et l'infrastructure serveur s'adaptent proportionnellement à la commune cible. Cela constituera un indicateur direct pour évaluer le succès et la croissance de la plateforme.
* **Impact d'ingénierie & Décision** :  
  Grille tarifaire à trois paliers (Petite ville <20k hab, Ville moyenne 20k-100k hab, Grande ville >100k hab) avec dimensionnement serveur adapté dans l'étude financière R3.

---

### Question 11.3 (Q.K3) — Gratuité de la solution pour l'usager final
* **Question formulée** : L'inscription et l'obtention de la carte de fidélité sont-elles gratuites pour l'administré ?
* **Intérêt pour le projet** : Hypothèse fondamentale pour l'étude de marché et le plan de financement.
* **Réponse validée MOE / MOA (Vague 2)** :  
  **Strictement gratuit pour le client usager**. La gratuité totale est le levier central pour inciter les citoyens à fréquenter les commerces physiques locaux.
* **Impact d'ingénierie & Décision** :  
  Aucun frais ni abonnement usager. Inscription libre et immédiate avec carte dématérialisée et support papier imprimable.

---

### Question 11.4 (Q.K4) — Périmètre technologique de développement
* **Question formulée** : Le développement porte-t-il sur une application Web responsive ou une application mobile native ?
* **Intérêt pour le projet** : Choix de la stack frontend et charge de développement.
* **Réponse validée MOE / MOA (Vague 2)** :  
  **Réaliser un développement applicatif Web responsive**.
* **Impact d'ingénierie & Décision** :  
  Développement d'une application Web responsive moderne (Desktop, Tablette, Mobile) accessible via navigateur universel.

---

## 14. Section 12 : Modalités des Évaluations et Soutenances

* **Format de soutenance validé** :
  - **15 minutes d'exposé / présentation** par l'équipe d'ingénierie.
  - **5 minutes d'échanges et questions / réponses** avec le jury MOA.
* **Implications méthodologiques** :
  - Synthèse percutante obligatoire lors des démonstrations.
  - Préparation d'un support visuel sobre, sans artifice, respectant la charte académique et valorisant les démonstrations logicielles en direct.

---

*Fin du document de synthèse de cadrage — 100% des questions arbitrées et validées par la MOE.*
