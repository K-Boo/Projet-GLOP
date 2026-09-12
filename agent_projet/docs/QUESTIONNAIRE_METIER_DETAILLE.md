# Questionnaire de Cadrage Métier — Projet ShopLoc

Ce document recense les questions de cadrage fonctionnel pour l'application ShopLoc, en distinguant :
- Les réponses et arbitrages d'ores et déjà validés lors des échanges avec la MOE (identifiés en vert).
- Les questions restant en attente d'arbitrage lors de la seconde entrevue (identifiées en orange).

---

# Première Vague : Questions de Cadrage Initiales

---

## 1. Rôles des Acteurs et Organisation Territoriale

### Question 1.1 (Q.A1 — Rôle et accès de l'Association des Commerçants)
* **La question** : L'énoncé indique que des associations de commerçants ont sollicité ShopLoc. Quel est leur rôle prévu dans l'application :
  - Doivent-elles valider l'inscription des commerçants de leur ville pour s'assurer qu'il s'agit bien de commerces locaux indépendants ?
  - Ont-elles accès à un tableau de bord pour suivre les statistiques globales de vente de leur commune ?
  - Ou n'ont-elles aucun compte dans l'application et interviennent-elles uniquement lors de la signature du projet ?
* **Intérêt pour le projet** : Savoir si nous devons développer un espace dédié pour les associations avec des droits de modération et de suivi.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">La demande émane conjointement de l'association des commerçants (structure à but non lucratif loi 1901) et de la mairie, qui formalisent une convention pour attirer plus de clients dans le centre-ville. Le commerçant doit obligatoirement être adhérent de l'association locale pour intégrer ShopLoc. C'est l'association qui contrôle les adhésions et débloque les accès. Elle dispose d'un panel de gestion et de visualisation des indicateurs pour suivre l'activité et prévenir les fraudes.</span>

---

### Question 1.2 (Q.A2 — Répartition des rôles entre la Mairie et l'Association des Commerçants)
* **La question** : Le sujet mentionne des services à destination de la mairie (notamment via le service Citoyen Numérique). Comment s'organise la collaboration entre la mairie et l'association :
  - La mairie dispose-t-elle de son propre compte d'accès ?
  - Qui décide de lancer les campagnes de promotion et les sondages d'opinion : la mairie ou l'association ?
  - En cas d'avis divergent sur une communication, qui a la priorité décisionnelle ?
* **Intérêt pour le projet** : Clarifier les droits de chacun pour l'envoi de messages aux usagers et définir les profils d'utilisateurs à créer.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">L'association et la mairie sont liées par la convention. Les rôles et promesses sont répartis : les commerces promettent des points et des cadeaux sur leurs produits ; la mairie promet des tickets de bus et du stationnement gratuit. Chacune des deux entités dispose d'un panel de gestion ou de visualisation des données propre.</span>

---

### Question 1.3 (Q.A3 — Modèle économique et facturation de la solution)
* **La question** : À qui ShopLoc vend-elle son service :
  - À la Mairie, qui finance la plateforme dans le cadre de sa politique d'attractivité du centre-ville ?
  - À l'Association des commerçants, via les cotisations de ses membres ?
  - Ou directement aux commerçants, qui paient chacun un abonnement à ShopLoc ?
* **Intérêt pour le projet** : C'est la base de notre étude financière (Livrable R3). Cela détermine comment ShopLoc génère ses revenus et auprès de qui émettre les factures.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">ShopLoc facture directement l'association des commerçants. La mairie verse une subvention à l'association pour financer le dispositif. L'équipe est totalement libre de définir et calibrer le modèle économique qu'elle souhaite. Cette liberté devra être défendue et justifiée par la suite via un prévisionnel d'activité détaillé couplé à une définition claire du modèle d'affaires (Livrables R1 et R3).</span>

---

### Question 1.4 (Q.A4 — Processus d'inscription d'un commerçant)
* **La question** : Comment se déroule l'arrivée d'un nouveau commerçant sur la plateforme :
  - L'inscription est-elle libre et immédiate en ligne ?
  - Ou nécessite-t-elle une validation préalable (vérification du SIRET, conformité du commerce) par l'administrateur ShopLoc ou l'association locale avant l'ouverture de la boutique ?
* **Intérêt pour le projet** : Déterminer si nous devons gérer un statut d'attente de validation pour les nouveaux comptes commerçants.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">Le commerçant doit obligatoirement être adhérent de l'association locale. C'est l'association qui donne et valide l'accès au commerçant dans l'application.</span>

---

## 2. Déploiement et Gestion Multi-Villes

### Question 2.1 (Q.B1 — Choix entre plateforme mutualisée (SaaS) ou déploiement séparé par ville)
* **La question** : L'énoncé demande une architecture logicielle réutilisable dans différentes villes. Quel modèle devons-nous privilégier :
  - Une application unique et partagée (SaaS multi-tenant), où chaque ville possède son propre espace au sein d'une même base de données ?
  - Ou une application installée et hébergée séparément sur des serveurs distincts pour chaque ville cliente ?
* **Intérêt pour le projet** : C'est un choix d'architecture majeur. Une solution mutualisée réduit les coûts d'infrastructure et simplifie les mises à jour, tandis qu'un déploiement séparé isole complètement les données de chaque commune.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">Libre sur le choix d'architecture, à condition d'être capable de défendre nos choix. L'écosystème associe la mairie et l'association de chaque ville. L'équipe retient l'architecture SaaS multi-tenant avec partitionnement logique (`tenant_id = ville_id`) pour concilier frugalité des serveurs et capacité de déploiement rapide.</span>

---

### Question 2.2 (Q.B2 — Ville de rattachement principale et comptes usagers)
* **La question** : Un usager (ex : Julie travaillant dans une grande ville et résidant dans une commune voisine) dispose-t-il d'un compte unique transversal lui permettant de basculer d'une ville à l'autre, ou doit-il recréer un compte distinct par commune ?
* **Intérêt pour le projet** : Modélisation des tables d'authentification et gestion des droits selon la commune d'achat.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">Si une personne souhaite disposer de plusieurs comptes distincts ou d'un compte unique, le système doit offrir cette flexibilité. Les avantages mobilité restent rattachés à la ville où les passages et achats ont été effectués.</span>

---

### Question 2.3 (Q.B3 — Adaptation selon la taille de la commune (Petite, Moyenne, Grande Ville))
* **La question** : Le sujet distingue 3 tailles de villes (<20k, 20k-100k, >100k habitants). Qu'implique cette distinction dans l'application en termes de charge et de modularité ?
* **Intérêt pour le projet** : Savoir si nous devons concevoir des modules optionnels configurables par ville.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">L'architecture doit être hautement scalable en termes de volume de données et de nombre d'utilisateurs simultanés.</span>

---

### Question 2.4 (Q.B4 — Objectifs attendus pour le cap des 18 mois)
* **La question** : L'énoncé fixe comme objectif de devenir leader du marché à 18 mois. Sur quels indicateurs ce succès sera-t-il évalué ?
* **Intérêt pour le projet** : Aligner nos choix techniques et notre calendrier sur les critères d'évaluation.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">L'indicateur clé pour devenir leader à 18 mois est la part de marché. Il s'agit simplement de piloter et suivre le Chiffre d'Affaires (CA) et de générer un niveau de croissance suffisant pour conquérir et asseoir cette position de leader sur le marché des villes cibles.</span>

---

## 3. Paiements, Commissions et Gestion des Litiges

### Question 3.1 (Q.C1 — Circuit d'encaissement des commandes en ligne)
* **La question** : Lors d'un achat réglé en ligne sur l'application, comment s'effectue le paiement d'un panier multi-commerçants ?
* **Intérêt pour le projet** : Savoir si nous devons intégrer une passerelle de paiement réelle avec split-payment ou simuler le flux.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">Le client peut régler une commande multi-commerçants en un seul paiement en ligne. Le client doit ensuite passer chez tous les commerçants de son panier pour collecter ses achats. La partie bancaire et financière est entièrement simulée dans le cadre du projet académique.</span>

---

### Question 3.2 (Q.C2 — Modèle de commissionnement sur les ventes)
* **La question** : ShopLoc prélève-t-elle une commission sur les transactions Click & Collect ou se finance-t-elle exclusivement par forfait ?
* **Intérêt pour le projet** : Modélisation des flux financiers et plan prévisionnel du Livrable R3.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">La composante financière réelle étant simulée, le modèle de tarification est libre. L'équipe privilégie une redevance annuelle/mensuelle forfaitaire auprès de l'association sans commission sur les ventes, afin de maximiser l'adhésion des commerçants locaux.</span>

---

### Question 3.3 (Q.C3 — Règle de non-retrait d'une commande (No-Show))
* **La question** : Que se passe-t-il si un client ne vient jamais retirer sa commande Click & Collect en boutique ?
* **Intérêt pour le projet** : Définir la machine à états de la commande et la politique d'annulation pour les denrées périssables.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">Si un client ne passe pas retirer sa commande dans le délai imparti (no-show), il perd définitivement sa commande. Le montant payé reste intégralement acquis au commerçant.</span>

---

## 4. Produits, Stocks, Vente au Poids et Horaires (Suzanne)

### Question 4.1 (Q.D1 — Choix de l'unité des produits)
* **La question** : Dans les commerces alimentaires, comment modéliser les articles vendus à la pièce, au poids ou à la part ?
* **Intérêt pour le projet** : Modélisation de la table `Article` et flexibilité du catalogue pour les artisans de bouche.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">Le commerçant a le choix de l'unité du produit (à la pièce, au kg, aux 100g, à la part). Pour la V1, le prix unitaire est fixé à la commande pour simplifier la saisie et les transactions.</span>

---

### Question 4.2 (Q.D2 — Délais de disponibilité et cohérence des plannings)
* **La question** : Comment s'organise la préparation des commandes côté commerçant et la cohérence des tournées de collecte ?
* **Intérêt pour le projet** : Gestion des contraintes d'ordonnancement pour les retraits.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">Le commerçant peut définir un délai de disponibilité par produit. Le système doit obligatoirement intégrer et rendre cohérents les articles avec une gestion des emplois du temps et horaires de chaque commerçant.</span>

---

### Question 4.3 (Q.D3 — Gestion des stocks en Click & Collect)
* **La question** : Comment Suzanne gère-t-elle ses stocks : saisie manuelle ou synchronisation avec des caisses informatisées ?
* **Intérêt pour le projet** : Définir si un module d'import de caisse est nécessaire en V1.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">Le commerçant entre manuellement ses produits et gère son stock dans l'application Click & Collect. Fréquence journalière ou dépendante du commerce. Une cohérence de stock peut être mise en place, mais l'interconnexion automatique avec des caisses externes n'est pas requise pour la première version.</span>

---

### Question 4.4 (Q.D4 — Gestion des horaires d'ouverture et fermetures exceptionnelles)
* **La question** : Concernant les horaires :
  - L'application bloque-t-elle automatiquement les commandes si le magasin est fermé au moment demandé pour le retrait ?
  - Le commerçant dispose-t-il d'un mode « fermeture exceptionnelle / congés » qui masque temporairement ses produits sans les supprimer ?
* **Intérêt pour le projet** : Garantir des créneaux fiables et éviter les déconvenues pour l'usager.

**<span style="color: #166534;">Réponse validée MOE (Séance 1) :</span>**  
<span style="color: #166534;">Prise en compte obligatoire des horaires d'ouverture de chaque commerce pour le calcul de l'itinéraire optimal de collecte (plus court chemin ou plus court en temps).</span>

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE (Fermetures exceptionnelles / congés)</span>**

---

## 5. Programme de Fidélité, Récompenses et Stationnement

### Question 5.1 (Q.E1 — Valeur financière et barème des points)
* **La question** : Existe-t-il un barème commun à toute la ville pour les points de fidélité ou chaque commerçant fixe-t-il son barème ?
* **Intérêt pour le projet** : Modélisation des règles de conversion euros/points.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">Découplage strict en 2 systèmes totalement indépendants : d'un côté le système de points d'achat, de l'autre la régularité VFP. Pour les points, on gagne des points quand on achète : c'est chaque commerçant qui fixe le nombre de points par produit et par achat.</span>

---

### Question 5.2 (Q.E2 — Périmètre des points (Cantonnement vs Mutualisation))
* **La question** : Un client peut-il utiliser des points gagnés chez un boucher pour retirer un lot chez Suzanne (commerce différent) ?
* **Intérêt pour le projet** : Déterminer si une chambre de compensation financière inter-commerces est nécessaire.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">Les points sont strictement propres à chaque commerçant : on ne mélange pas les points entre boutiques. Les points gagnés chez un commerçant ne sont utilisables que chez ce même commerçant. Pour obtenir un cadeau, l'usager doit en outre avoir un historique d'achat et présenter sa carte lors du paiement d'un achat en cours.</span>

---

### Question 5.3 (Q.E3 — Responsabilité du catalogue de récompenses)
* **La question** : Qui a le droit d'ajouter des cadeaux dans l'application : les commerçants individuellement ou l'association ?
* **Intérêt pour le projet** : Définition des écrans de gestion et droits CRUD sur les lots.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">Chaque commerçant définit ses propres lots et cadeaux dans son propre catalogue (ex : Suzanne ajustant son lot de tarte au maroilles vers une mini-viennoiserie).</span>

---

### Question 5.4 (Q.E4 — Durée de validité des points accumulés)
* **La question** : Les points sont-ils valables indéfiniment ou expirent-ils après une période sans achat ?
* **Intérêt pour le projet** : Mise en place d'un batch d'expiration automatique des points en base de données.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">Les points expirent au bout d'un an (12 mois).</span>

---

### Question 5.5 (Q.E5 — Prise en charge du coût des avantages mobilité)
* **La question** : Qui prend en charge le coût des tickets de bus et des heures de stationnement offertes ?
* **Intérêt pour le projet** : Établir la convention financière de reversement entre la ville et les opérateurs.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">La mairie promet et finance directement les tickets de bus et les 20 minutes de parking dans le cadre de sa politique d'attractivité du centre-ville.</span>

---

## 6. Administration, Outils Marketing et Protection des Données (Marius)

### Question 6.1 (Q.F1 — Algorithme de calcul du statut VFP (Régularité glissante))
* **La question** : Quels critères précis déclenchent l'obtention du statut VFP et son maintien ?
* **Intérêt pour le projet** : Coder l'algorithme exact du service VFP exécuté chaque nuit.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">1. Le statut VFP repose exclusivement sur le nombre de passages dans les commerces selon une règle de fenêtre glissante : on n'est pas VFP au début, il faut au moins 10 passages dans les 15 derniers jours pour débloquer le statut.<br>
2. Un client peut passer autant de fois qu'il le souhaite dans une même boutique : il n'y a aucune limite de passage par jour ni obligation de mixité commerciale. L'usager peut effectuer l'ensemble de ses passages dans un seul commerce s'il le souhaite.<br>
3. Dès les 10 passages cumulés, l'usager déclenche 1 ticket de bus ou 20 minutes de parking.<br>
4. Il n'y a aucun plafond de cumul des avantages : chaque nouveau passage supplémentaire octroie à nouveau 1 ticket ou 20 minutes de parking tant que la régularité est maintenue.</span>

---

### Question 6.2 (Q.F2 — Perte du statut VFP et alertes marketing)
* **La question** : L'énoncé indique que Marius exploite les données pour relancer les clients lors de la perte du statut VFP. Le système doit-il envoyer des alertes préventives automatisées (ex: alerte à J-3) ?
* **Intérêt pour le projet** : Déterminer le degré d'automatisation des relances marketing à coder.

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

---

### Question 6.3 (Q.F3 — Canaux de diffusion des offres promotionnelles)
* **La question** : Par quel canal Marius diffuse-t-il les offres : notifications push web/mobile, courriels, bannières in-app, SMS ?
* **Intérêt pour le projet** : Choisir les connecteurs d'envoi et chiffrer les coûts d'infrastructure dans le livrable R1.

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

---

### Question 6.4 (Q.F4 — Filtres de segmentation disponibles pour Marius)
* **La question** : Quels critères de recherche Marius peut-il combiner pour cibler ses campagnes (inactivité, statut VFP, quartier) ?
* **Intérêt pour le projet** : Spécification de l'API de filtrage dynamique et optimisation des index PostgreSQL.

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

---

### Question 6.5 (Q.F5 — Portée des sondages de satisfaction usagers)
* **La question** : Le sujet mentionne (page 3, persona Marius) que l'administrateur peut *« lancer des sondages de satisfaction aux usagers »*. Quelle est la portée attendue pour cette fonctionnalité :
  - L'application doit-elle intégrer un moteur complet d'enquêtes (création de questions à choix multiples par Marius, recueil des réponses et statistiques) ?
  - Ou s'agit-il simplement d'un canal de diffusion permettant de pousser une notification avec un lien externe (type formulaire web) ?
* **Intérêt pour le projet** : Déterminer l'ampleur du module d'enquête à développer et modéliser dans la base relationnelle.

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

---

### Question 6.6 (Q.F6 — Respect de la vie privée et conformité RGPD)
* **La question** : Quel est le cadre de conformité et de remontée de données pour la mairie et l'association ?
* **Intérêt pour le projet** : Conception des vues SQL sécurisées et respect des exigences RGPD.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">L'association et la mairie doivent récupérer de la data pour évaluer le système et détecter les fraudes. Chaque partie prenante doit disposer d'un panel de gestion ou de visualisation des données. Les flux de données détaillés doivent respecter le secret commercial entre boutiques (aucun accès croisé aux paniers des concurrents).</span>

---

## 7. Connexion, Sécurité et Accessibilité

### Question 7.1 (Q.G1 — Connexion simplifiée pour les usagers seniors (Pierre, 74 ans))
* **La question** : Pour Pierre, peut-on proposer une connexion simplifiée par Magic Link ou code PIN à 4 chiffres sans mot de passe complexe ?
* **Intérêt pour le projet** : Ergonomie et accessibilité senior (RGAA).

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

---

### Question 7.2 (Q.G2 — Niveau de sécurité d'authentification par typologie d'utilisateur)
* **La question** : Quel niveau d'exigence de sécurité doit-on mettre en place pour l'authentification en fonction de chaque type d'utilisateur :
  - Pour les clients usagers (ex: Pierre, Julie, Arthur) : mot de passe standard ou authentification simplifiée sans friction ?
  - Pour les commerçants (ex: Suzanne) et administrateurs (ex: Marius) : niveau de sécurité renforcé en fonction de la criticité des données manipulées ?
* **Intérêt pour le projet** : Définir la politique d'authentification, les règles de complexité et la gestion des sessions dans l'architecture de sécurité backend J2E.

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

---

### Question 7.3 (Q.G3 — Matérialisation de l'activation des avantages mobilité)
* **La question** : Comment le client fait-il valoir son droit au ticket de bus et au stationnement gratuit ?
* **Intérêt pour le projet** : Définition des flux de déblocage des privilèges dans l'interface usager.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">Pour avoir le ticket de transport en commun, il faut passer sa carte de la ville (ex: carte Pass Pass / Ilévia). Pour le stationnement, l'usager entre son numéro de plaque d'immatriculation dans l'application et déclenche son compteur de 20 minutes offertes.</span>

---

## 8. Priorités pour la V1 (Décembre) et la V2 (Mars)

### Question 8.1 (Q.H1 — Choix du composant prioritaire pour la V1 de décembre)
* **La question** : Quel sous-système logiciel doit être prioritairement livré de bout en bout pour la soutenance de fin décembre ?
* **Intérêt pour le projet** : Focalisation des sprints de développement à partir d'octobre.

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

---

### Question 8.2 (Q.H2 — Systèmes externes à simuler (Mocks))
* **La question** : Quels systèmes externes doivent faire l'objet d'une simulation ?
* **Intérêt pour le projet** : Délimitation exacte des mocks RESTful à développer.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">Toutes les interactions avec des systèmes externes doivent être obligatoirement simulées (mocks logiciels d'API) : passerelle bancaire de paiement, réseau de transport urbain et système de stationnement. Aucune dépendance externe réelle non maîtrisée.</span>

---

### Question 8.3 (Q.H3 — Périmètre des données et scénarios de démonstration pour les revues clients)
* **La question** : Quel jeu de données représentatif et quels scénarios types la MOA souhaite-t-elle voir préparés afin de rendre les revues et démonstrations clients pleinement pertinentes ?
* **Intérêt pour le projet** : Calibrer les scripts de seed SQL et les comptes de test pour illustrer immédiatement tous les parcours lors des revues de projet.

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

---

## 9. Démarche d'Éco-Conception (Green IT)

### Question 9.1 (Q.I1 — Critères d'évaluation de l'éco-conception logicielle)
* **La question** : Quels indicateurs précis et outils concrets seront évalués pour la démarche d'éco-conception logicielle ?
* **Intérêt pour le projet** : Outillage dans la chaîne CI/CD et métriques à consigner dans les dossiers techniques.

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

---

# SECONDE VAGUE : QUESTIONS D'APPROFONDISSEMENT MÉTIER (POUR LA 2NDE ENTREVUE MOE)

---

## 10. Questions d'Instruction Approfondie pour le Développement

### Question 10.1 (Q.J1 — Seuil d'achat pour la validation d'un passage VFP)
* **Contexte** : Il est acté qu'un acte d'achat est obligatoire pour valider un passage en boutique (un simple scan de présence au comptoir sans achat n'est pas toléré). Un usager peut effectuer autant de passages qu'il le souhaite dans une même boutique sans limitation ni mixité imposée.
* **La question** : Existe-t-il un montant minimum d'achat exigé pour valider un passage (ex: seuil minimal de 1 € ou 2 €) ou n'importe quel achat, quel que soit son montant (ex: une baguette à 1,10 € ou un paquet de bonbons à 0,50 €), valide-t-il le passage ?
* **Intérêt pour le projet** : Paramétrage du filtre de validation dans le service de comptabilisation des passages VFP.

**<span style="color: #166534;">Réponse validée MOE (Principe de l'achat) :</span>**  
<span style="color: #166534;">Un acte d'achat est obligatoirement requis pour valider un passage en boutique (les scans de complaisance sans achat sont exclus).</span>

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE (Montant seuil éventuel)</span>**

---

### Question 10.2 (Q.J2 — Vérification applicative du retrait des cadeaux en caisse)
* **Contexte** : Le sujet indique (page 3, persona Julie) : *« Pour obtenir un cadeau, il faut avoir fait au moins un achat antérieur dans la boutique concernée, et présenter sa carte lors du paiement de l'achat en cours (on ne peut pas juste venir prendre un cadeau). »*
* **La question** : Comment l'application commerçant (vue Suzanne) valide-t-elle cette règle :
  - L'application vérifie-t-elle automatiquement dans l'historique l'antériorité d'un achat client dans cette boutique ?
  - L'application bloque-t-elle la délivrance du cadeau si aucun achat concomitant n'est enregistré lors de la session de caisse ?
* **Intérêt pour le projet** : Spécification des règles de gestion bloquantes dans le contrôleur de distribution des lots.

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

---

### Question 10.3 (Q.J3 — Ordonnancement du panier multi-commerçants et plages de retrait)
* **Contexte** : Un panier unique peut regrouper des produits provenant de commerces aux horaires et délais de préparation hétérogènes.
* **La question** : Comment le système synchronise-t-il les créneaux de retrait lors d'une commande multi-commerçants ?
* **Intérêt pour le projet** : Algorithme d'ordonnancement de tournée et gestion des états des sous-commandes marchandes.

**<span style="color: #166534;">Réponse validée MOE :</span>**  
<span style="color: #166534;">Le système gère les créneaux boutique par boutique, combinés avec un algorithme d'optimisation du plus court chemin qui minimise le temps d'attente entre chaque créneau afin de regrouper au mieux la tournée de retrait pour l'usager.</span>

---

### Question 10.4 (Q.J4 — Ruptures partielles sur commande multi-commerçants)
* **Contexte** : Dans un panier groupé réglé en un paiement unique en ligne, un artisan peut subir une rupture de stock imprévue sur l'un de ses articles.
* **La question** : Quelle est la politique d'annulation : l'annulation de la sous-commande concernée génère-t-elle un remboursement partiel automatique tout en maintenant fermes les commandes chez les autres artisans ?
* **Intérêt pour le projet** : Gestion des états transactionnels partiels dans la machine à états de la commande.

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

---

### Question 10.5 (Q.J5 — Rôles et profils multiples au sein d'une même boutique)
* **Contexte** : En boutique, les employés ou apprentis (comme Suzanne) préparent les commandes de Click & Collect et scannent les cartes en caisse, tandis que le propriétaire gère les finances et coordonnées bancaires.
* **La question** : Doit-on prévoir une segmentation des habilitations au sein d'un compte commerçant :
  - Profil « Préparateur / Vendeur » (accès restreint aux stocks et commandes) ?
  - Profil « Gérant / Propriétaire » (accès complet à la configuration financière et aux coordonnées bancaires) ?
* **Intérêt pour le projet** : Modélisation des rôles RBAC (Role-Based Access Control).

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

---

### Question 10.6 (Q.J6 — Alertes et détection de fraude sur les avantages municipaux)
* **Contexte** : Les notes précisent que la mairie et l'association doivent récupérer de la data pour évaluer le système et prévenir les fraudes.
* **La question** : Quels mécanismes d'alerte automatisée doivent être intégrés au panel de pilotage (détection de fréquences de passages anormales, possibilité de suspension temporaire de compte usager suspect) ?
* **Intérêt pour le projet** : Conception du module de détection d'anomalies de fréquentation.

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

---

## 11. Points complémentaires identifiés dans le sujet (Seconde Vague)

---

### Question 11.1 (Q.K1 — Contrôle du stationnement par un agent municipal)
* **Contexte** : Le sujet source mentionne explicitement qu'« un policier municipal voyant sa voiture pourra rentrer le numéro de plaque sur son téléphone et savoir si la voiture est en stationnement illégal ou non ».
* **La question** : Ce cas d'usage de contrôle du stationnement par un agent municipal fait-il partie du périmètre fonctionnel attendu de l'application ShopLoc (ex. profil ou interface dédiée), ou relève-t-il exclusivement du système externe de gestion de voirie interfacé via API simulée ?
* **Intérêt pour le projet** : Délimitation exacte du périmètre des acteurs, des rôles applicatifs et des cas d'utilisation du Livrable R4.

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

---

### Question 11.2 (Q.K2 — Tarification de la solution selon la taille de la commune)
* **Contexte** : Le sujet source exige expressément que « le prix de la solution doit tenir compte du segment de clients auquel elle s'adresse » (petite, moyenne ou grande ville).
* **La question** : La redevance facturée à l'Association des commerçants doit-elle être modulée selon la taille de la collectivité locale (ex. selon des paliers démographiques ou le nombre de commerces adhérents), et existe-t-il des barèmes indicatifs attendus ?
* **Intérêt pour le projet** : Élaboration de la grille tarifaire et de l'étude financière prévisionnelle du Livrable R3.

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

---

### Question 11.3 (Q.K3 — Gratuité de l'inscription et de la carte pour l'usager final)
* **Contexte** : Le persona Arthur indique qu'un client « doit pouvoir s'abonner au service et obtenir sa carte de fidélité », sans préciser les conditions tarifaires d'accès pour les administrés.
* **La question** : L'inscription au service ShopLoc, la création du compte client et la délivrance de la carte de fidélité sont-elles strictement gratuites pour l'usager final ?
* **Intérêt pour le projet** : Hypothèse structurante pour le modèle économique et les projections financières du Livrable R3.

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

---

### Question 11.4 (Q.K4 — Périmètre technologique : application Web responsive ou mobile native)
* **Contexte** : Les expressions de besoin font référence au « site » ou à « l'application web », sans mentionner de magasins d'applications mobiles (App Store, Google Play Store).
* **La question** : Le périmètre de développement pour les livrables applicatifs porte-t-il exclusivement sur une application Web responsive accessible sur navigateur (desktop et mobile), ou une application mobile native (iOS / Android) est-elle attendue ?
* **Intérêt pour le projet** : Choix de la pile technologique frontend, dimensionnement des charges de développement et architecture logicielle pour R4/R5.

**<span style="color: #c2410c;">Statut : En attente d'arbitrage MOE</span>**

