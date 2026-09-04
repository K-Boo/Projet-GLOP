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

# QUESTIONNAIRE D'INSTRUCTION MÉTIER APPROFONDIE (SHOPLOC)
## Cadrage Fonctionnel & Découverte du Besoin Réel (Version Consolidée)

---

## Informations Générales sur le Document

| Champ | Information |
|---|---|
| **Intitulé du Projet** | **Projet ShopLoc** — Marketplace & Fidélisation multi-commerces |
| **Identifiant Officiel du Projet** | `MiageShopLoc` |
| **Titre du Document** | *Questionnaire de cadrage fonctionnel approfondi (36 questions métiers — 9 volets)* |
| **Référence Documentaire** | `GLOP-2026-R1-QUESTIONNAIRE-DETAILLE-v1.0` |
| **Contexte Académique** | Master 2 MIAGE — UE Génie Logiciel par la Pratique (GLOP) 2026-2027, Université de Lille |
| **Destinataires (MOA)** | Laurence Duchien, Anne Etien, François Secchi, Jérémy Woirhaye |
| **Date de Soumission** | 07 Septembre 2026 |
| **Statut du Document** | Version 1.0 — *Pour instruction et arbitrage de la MOA* |
| **Tag obligatoire communications** | `[GLOP]` *(à inclure dans tout objet de courriel)* |

---

### Objectif du Document
Dans le cadre de l'UE GLOP et de la préparation de notre réponse technique et financière (Livrable R1), notre équipe d'étudiants a analysé l'ensemble des besoins présentés dans le sujet ShopLoc. Afin de concevoir une architecture logicielle adaptée et de lever toute ambiguïté sur les règles de gestion, nous avons réuni cette liste de questions ciblées. Pour chaque point, nous présentons notre interrogation ainsi que son intérêt concret pour le développement de l'application.

---

## 1. Rôles des Acteurs et Organisation Territoriale

### Q.A1 — Rôle et accès de l'Association des Commerçants
* **La question** : L'énoncé indique que des associations de commerçants ont sollicité ShopLoc. Quel est leur rôle prévu dans l'application :
  - Doivent-elles valider l'inscription des commerçants de leur ville pour s'assurer qu'il s'agit bien de commerces locaux indépendants ?
  - Ont-elles accès à un tableau de bord pour suivre les statistiques globales de vente de leur commune ?
  - Ou n'ont-elles aucun compte dans l'application et interviennent-elles uniquement lors de la signature du projet ?
* **L'intérêt** : Savoir si nous devons développer un espace dédié pour les associations avec des droits de modération et de suivi.

### Q.A2 — Répartition des rôles entre la Mairie et l'Association des Commerçants
* **La question** : Le sujet mentionne des services à destination de la mairie (notamment via le service Citoyen Numérique). Comment s'organise la collaboration entre la mairie et l'association :
  - La mairie dispose-t-elle de son propre compte d'accès ?
  - Qui décide de lancer les campagnes de promotion et les sondages d'opinion : la mairie ou l'association ?
  - En cas d'avis divergent sur une communication, qui a la priorité décisionnelle ?
* **L'intérêt** : Clarifier les droits de chacun pour l'envoi de messages aux usagers et définir les profils d'utilisateurs à créer.

### Q.A3 — Modèle économique et facturation de la solution
* **La question** : À qui ShopLoc vend-elle son service :
  - À la Mairie, qui finance la plateforme dans le cadre de sa politique d'attractivité du centre-ville ?
  - À l'Association des commerçants, via les cotisations de ses membres ?
  - Ou directement aux commerçants, qui paient chacun un abonnement à ShopLoc ?
* **L'intérêt** : C'est la base de notre étude financière (Livrable R3). Cela détermine comment ShopLoc génère ses revenus et auprès de qui émettre les factures.

### Q.A4 — Processus d'inscription d'un commerçant
* **La question** : Comment se déroule l'arrivée d'un nouveau commerçant sur la plateforme :
  - L'inscription est-elle libre et immédiate en ligne ?
  - Ou nécessite-t-elle une validation préalable (vérification du SIRET, conformité du commerce) par l'administrateur ShopLoc ou l'association locale avant l'ouverture de la boutique ?
* **L'intérêt** : Déterminer si nous devons gérer un statut d'attente de validation pour les nouveaux comptes commerçants.

---

## 2. Déploiement et Gestion Multi-Villes

### Q.B1 — Choix entre plateforme mutualisée (SaaS) ou déploiement séparé par ville
* **La question** : L'énoncé demande une architecture logicielle réutilisable dans différentes villes. Quel modèle devons-nous privilégier :
  - Une application unique et partagée (SaaS multi-tenant), où chaque ville possède son propre espace au sein d'une même base de données ?
  - Ou une application installée et hébergée séparément sur des serveurs distincts pour chaque ville cliente ?
* **L'intérêt** : C'est un choix d'architecture majeur. Une solution mutualisée réduit les coûts d'infrastructure et simplifie les mises à jour, tandis qu'un déploiement séparé isole complètement les données de chaque commune.

### Q.B2 — Ville de rattachement principale et avantages des résidents
* **La question** : Un compte usager (ex : Julie) fonctionne dans toutes les villes partenaires. L'usager peut-il déclarer une « ville de rattachement principale » (sa commune de résidence) :
  - Les avantages financés par une commune (ex : heures de stationnement gratuit, chèques d'achat locaux) sont-ils réservés aux seuls habitants de cette commune ?
  - Un usager extérieur gagne-t-il les mêmes points qu'un résident local ?
  - Les points de fidélité sont-ils utilisables uniquement dans la ville où ils ont été acquis, ou dans l'ensemble des villes du réseau ?
* **L'intérêt** : Permettre aux mairies de réserver leurs aides financières à leurs propres contribuables et cadrer la validité des points de fidélité.

### Q.B3 — Adaptation selon la taille de la commune (Petite, Moyenne, Grande Ville)
* **La question** : Le sujet distingue 3 tailles de villes (<20k, 20k-100k, >100k habitants). Qu'implique cette distinction dans l'application :
  - S'agit-il seulement de dimensionner les serveurs pour supporter un volume d'utilisateurs plus important ?
  - Ou certaines fonctionnalités doivent-elles pouvoir être activées ou désactivées selon la ville (ex : désactiver le module parking dans les petites communes sans horodateurs payants, découper en quartiers pour les grandes villes) ?
* **L'intérêt** : Savoir si nous devons concevoir des modules optionnels configurables par ville.

### Q.B4 — Objectifs attendus pour le cap des 18 mois
* **La question** : L'énoncé fixe comme objectif de devenir leader du marché à 18 mois. Sur quels indicateurs ce succès sera-t-il évalué :
  - Le nombre de villes partenaires signées ?
  - Le nombre de commerçants actifs et de produits proposés ?
  - Le volume des ventes réalisées et la rentabilité financière ?
* **L'intérêt** : Aligner nos choix techniques, notre calendrier de déploiement et notre offre financière sur les attentes concrètes du client.

---

## 3. Paiements, Commissions et Gestion des Litiges

### Q.C1 — Circuit d'encaissement des commandes en ligne
* **La question** : Lors d'un achat réglé en ligne sur l'application :
  - L'argent est-il encaissé sur un compte central ShopLoc avant d'être reversé régulièrement aux commerçants ?
  - Ou le paiement est-il automatiquement ventilé et transféré directement sur le compte bancaire de chaque commerçant au moment de l'achat (via une solution comme Stripe Connect) ?
* **L'intérêt** : Encaisser l'argent au nom de tiers impose des contraintes réglementaires fortes (statut d'intermédiaire financier). Savoir quel modèle retenir oriente le choix de notre passerelle de paiement.

### Q.C2 — Modèle de commissionnement sur les ventes
* **La question** : Comment ShopLoc se rémunère-t-elle sur les commandes Click & Collect :
  - Par un pourcentage sur chaque commande (ex : 3 % du montant) ?
  - Par des frais fixes par panier (ex : 0,50 € par commande) ?
  - Ou sans commission sur les ventes, si les commerçants paient déjà un abonnement mensuel ?
  - Qui prend en charge les frais bancaires de transaction par carte ?
* **L'intérêt** : Nécessaire pour coder le calcul automatique des montants reversés aux commerçants et construire notre plan financier prévisionnel (Livrable R3).

### Q.C3 — Facturation et TVA
* **La question** : Lors d'un achat sur l'application, quelle facture le client reçoit-il :
  - Une facture émise directement par le commerçant, avec les taux de TVA propres à ses produits (5,5 % pour l'alimentaire, 20 % pour les produits manufacturés) ?
  - Ou une facture globale émise par ShopLoc ?
* **L'intérêt** : Respecter les règles fiscales françaises en appliquant les bons taux de TVA et les bonnes mentions légales sur chaque justificatif d'achat.

### Q.C4 — Gestion des retours, produits manquants et litiges
* **La question** : Que se passe-t-il si un client constate un problème lors du retrait (produit abîmé, manquant ou non conforme) :
  - Le commerçant peut-il effectuer un remboursement partiel ou total directement depuis son application ?
  - Le commerçant peut-il proposer un produit de remplacement en accord avec le client ?
  - L'application doit-elle intégrer un module de réclamation pour contacter le support ShopLoc ?
* **L'intérêt** : Savoir si nous devons développer un système de suivi des litiges en ligne ou si ces situations se règlent directement en boutique.

---

## 4. Produits, Stocks, Vente au Poids et Horaires (Suzanne)

### Q.D1 — Gestion des articles vendus au poids réel (Boucherie, Fromagerie, Primeur)
* **La question** : Dans les commerces alimentaires de centre-ville, beaucoup d'articles sont vendus au poids (ex : un client commande 300g, mais la découpe finale fait 320g ou 290g). Comment gérer le paiement :
  - Peut-on utiliser une pré-autorisation bancaire ajustée au montant exact une fois la commande pesée par le commerçant ?
  - Ou impose-t-on des portions à prix fixe pour simplifier le système ?
* **L'intérêt** : Permettre aux commerces de bouche d'utiliser facilement la plateforme sans bloquer les commandes pour quelques grammes d'écart.

### Q.D2 — Délais de préparation et créneaux de retrait
* **La question** : Comment s'organise la préparation des commandes côté commerçant :
  - Le commerçant peut-il définir son délai de préparation par article (ex : 1 heure pour des fleurs, 24 heures pour un gâteau sur commande) ?
  - Le client choisit-il un créneau précis de passage (ex : entre 17h30 et 18h) ?
  - Le commerçant peut-il suspendre temporairement la prise de commandes en cas d'affluence en magasin ?
* **L'intérêt** : Éviter qu'un client arrive avant que sa commande ne soit prête et permettre au commerçant de gérer son rythme de travail.

### Q.D3 — Mise à jour des stocks et liaison avec les caisses existantes
* **La question** : Suzanne vend ses produits à la fois aux clients en boutique et aux usagers de l'application. Comment gère-t-elle ses stocks :
  - Doit-elle mettre à jour ses stocks manuellement dans l'application ShopLoc ?
  - Ou devons-nous prévoir un import de catalogue par fichier (Excel/CSV), voire une connexion possible avec des logiciels de caisse courants ?
* **L'intérêt** : Éviter aux commerçants une double saisie fastidieuse qui risquerait de provoquer des erreurs de stock et des abandons d'utilisation.

### Q.D4 — Gestion des horaires d'ouverture et des congés
* **La question** : Concernant les horaires des commerces :
  - L'application bloque-t-elle automatiquement les commandes si le magasin est fermé au moment demandé pour le retrait ?
  - Le commerçant dispose-t-il d'un mode « fermeture exceptionnelle / congés » qui masque temporairement ses produits sans les supprimer ?
* **L'intérêt** : Garantir que les clients ne commandent pas sur des plages de fermeture et afficher des horaires fiables.

---

## 5. Programme de Fidélité, Récompenses et Stationnement

### Q.E1 — Valeur financière d'un point de fidélité
* **La question** : Quelle équivalence financière souhaite-t-on donner aux points :
  - Existe-t-il un barème commun à toute la ville (ex : 100 points = 5 € de réduction ou 1 heure de parking) ?
  - Ou chaque commerçant fixe-t-il librement la valeur de ses points ?
* **L'intérêt** : Établir la grille de conversion nécessaire au catalogue de cadeaux et calibrer l'échange contre du temps de stationnement.

### Q.E2 — Financement des cadeaux échangés entre commerces différents
* **La question** : Si un client cumule des points chez un boucher et les utilise pour obtenir un cadeau chez Suzanne (boutique de vêtements) :
  - Suzanne offre-t-elle ce cadeau sans contrepartie ?
  - Ou existe-t-il une compensation financière (via une caisse commune gérée par l'association ou ShopLoc) pour rembourser Suzanne de la valeur de l'article offert ?
* **L'intérêt** : Si les commerçants ne sont pas dédommagés lorsqu'un client dépense des points acquis ailleurs, ils ne proposeront pas d'articles attractifs. Il est donc crucial de clarifier s'il y a un mécanisme de remboursement inter-commerces.

### Q.E3 — Responsabilité du catalogue de récompenses
* **La question** : Qui a le droit d'ajouter des cadeaux dans l'application :
  - Chaque commerçant propose-t-il ses propres récompenses depuis son espace ?
  - Ou l'association des commerçants gère-t-elle un catalogue commun pour tout le centre-ville (ex : bons d'achat valables partout, entrées de cinéma) ?
* **L'intérêt** : Définir qui a les droits de gestion sur les récompenses dans la base de données.

### Q.E4 — Durée de validité des points accumulés
* **La question** : Les points sont-ils valables indéfiniment ou expirent-ils après une période sans achat (ex : 12 mois sans commande) ?
* **L'intérêt** : Éviter l'accumulation de points dormants qui représenteraient un engagement financier difficile à gérer pour les commerçants sur le long terme.

### Q.E5 — Fonctionnement pratique du stationnement offert en ville
* **La question** : Quand un usager utilise ses points pour obtenir une heure de parking gratuit, comment cela se concrétise-t-il :
  - L'application génère-t-elle un code promotionnel à saisir sur l'horodateur ?
  - L'usager renseigne-t-il sa plaque d'immatriculation pour un enregistrement automatique auprès du service de voirie municipale ?
  - Ou l'application affiche-t-elle un ticket virtuel avec QR code ?
* **L'intérêt** : Définir l'interface exacte à proposer à l'usager et le mode d'interconnexion avec les systèmes de stationnement municipaux.

### Q.E6 — Prise en charge du coût du stationnement offert
* **La question** : Qui prend en charge le coût des heures de stationnement offertes :
  - La Mairie, qui accorde cette gratuité pour encourager les habitants à fréquenter les commerces de centre-ville ?
  - Ou l'association des commerçants, qui rembourse la mairie pour chaque heure de stationnement consommée ?
* **L'intérêt** : Prévoir le suivi financier et les bilans réguliers entre ShopLoc, la mairie et les commerçants.

---

## 6. Administration, Outils Marketing et Protection des Données (Marius)

### Q.F1 — Critères de calcul du statut VFP (Very Frequent Purchaser)
* **La question** : Quels critères précis déclenchent l'obtention du statut VFP :
  - Un montant minimum dépensé par mois (ex : plus de 150 €) ?
  - Un nombre minimum de commandes (ex : au moins 4 achats par mois) ?
  - Une condition de mixité (ex : avoir acheté dans au moins 2 ou 3 commerces différents pour favoriser la diversité des achats en centre-ville) ?
* **L'intérêt** : Coder l'algorithme qui calculera automatiquement ce statut de fidélité chaque nuit.

### Q.F2 — Perte du statut VFP et relances marketing
* **La question** : L'énoncé indique que Marius exploite les données pour relancer les clients, notamment lors de la perte du statut VFP :
  - Le statut est-il recalculé chaque mois ?
  - Une alerte préventive est-elle envoyée au client avant la perte de son statut (ex : un message l'informant qu'il lui reste 7 jours et 1 achat pour conserver ses avantages) ?
  - Marius déclenche-t-il ces relances manuellement, ou le système les envoie-t-il automatiquement ?
* **L'intérêt** : Déterminer le degré d'automatisation des relances marketing à programmer dans l'application.

### Q.F3 — Canaux de diffusion des offres promotionnelles
* **La question** : Quand Marius diffuse une offre commerciale ou une annonce municipale :
  - Par quel canal l'offre est-elle transmise : notifications sur smartphone, e-mails, SMS, ou bandeau dans l'application ?
  - Si des SMS sont utilisés, qui prend en charge leur coût d'envoi ?
* **L'intérêt** : Choisir les services d'envoi à intégrer et chiffrer leurs coûts dans notre proposition financière R1.

### Q.F4 — Filtres de ciblage disponibles pour Marius
* **La question** : Quels critères de recherche Marius peut-il combiner pour cibler ses campagnes :
  - Les clients inactifs depuis une certaine durée (ex : aucun achat depuis 30 jours) ?
  - Les clients fidèles détenant le statut VFP ?
  - Les usagers résidant dans un quartier ou code postal particulier ?
  - Les clients habitués à une catégorie de commerce (ex : boulangerie, prêt-à-porter) ?
* **L'intérêt** : Concevoir le formulaire de filtrage et optimiser les requêtes de recherche dans la base de données.

### Q.F5 — Gestion des sondages de satisfaction
* **La question** : Le sujet mentionne que Marius peut lancer des sondages auprès des usagers :
  - Marius peut-il créer lui-même de nouvelles questions depuis son interface (notes, choix multiples, texte libre) ?
  - L'attribution de points de fidélité bonus (ex : 10 points) est-elle prévue pour encourager les citoyens à y répondre ?
* **L'intérêt** : Développer un module d'enquête adapté et le relier au solde de points des participants.

### Q.F6 — Respect de la vie privée et conformité RGPD
* **La question** : Le sujet insiste sur le respect de la vie privée. Quelles règles de confidentialité devons-nous appliquer :
  - Marius a-t-il accès aux détails nominatifs des paniers d'achat des clients, ou seulement à des statistiques globales et anonymisées ?
  - Les commerçants ont-ils l'interdiction de voir les achats réalisés par leurs clients dans les autres boutiques ?
  - Comment le client choisit-il les communications qu'il accepte de recevoir (opt-in pour les offres de la mairie, des commerces, etc.) ?
* **L'intérêt** : Assurer la conformité légale avec le RGPD, protéger la vie privée des citoyens et préserver le secret commercial entre boutiques partenaires.

---

## 7. Connexion, Sécurité et Accessibilité

### Q.G1 — Connexion simplifiée pour les usagers seniors (Pierre, 74 ans)
* **La question** : Pour faciliter l'accès des usagers seniors qui retiennent difficilement les mots de passe complexes :
  - Peut-on proposer des modes de connexion simplifiés comme un code PIN à 4 chiffres, un lien de connexion envoyé par e-mail (Magic Link) ou un code par SMS ?
  - Une connexion via FranceConnect est-elle envisageable pour réutiliser le compte officiel déjà connu des citoyens ?
* **L'intérêt** : Rendre l'application accessible à tous les âges et éviter l'abandon d'utilisation à cause d'une étape de connexion trop contraignante.

### Q.G2 — Sécurité des comptes commerçants et administrateur (2FA)
* **La question** : Les comptes de Suzanne (qui gère des coordonnées bancaires) et de Marius (qui a accès à la base usagers) manipulent des données sensibles. Doit-on imposer une double sécurité (code de vérification envoyé sur téléphone / 2FA) lors de leur connexion ?
* **L'intérêt** : Protéger les fonds des commerçants et les données personnelles contre les risques d'usurpation de compte.

### Q.G3 — Gestion de plusieurs utilisateurs pour un même commerce
* **La question** : En boutique, les personnes au comptoir sont souvent des employés ou des apprentis qui préparent les commandes de Click & Collect :
  - Un compte commerçant peut-il comporter plusieurs profils d'accès ?
    - Un profil « Vendeur / Préparateur » qui voit uniquement les commandes à préparer et les stocks, sans accès à la comptabilité ni aux coordonnées bancaires.
    - Un profil « Gérant » avec tous les droits de configuration et d'accès financier.
* **L'intérêt** : Répondre à l'organisation réelle des commerces de centre-ville et sécuriser les informations financières.

### Q.G4 — Options d'accessibilité visuelle (Normes RGAA)
* **La question** : Pour les personnes âgées ou malvoyantes, quelles options d'affichage ergonomique devons-nous intégrer :
  - Un bouton pour agrandir directement la taille des textes ?
  - Un mode à fort contraste visuel ?
  - La compatibilité avec les lecteurs d'écran pour la synthèse vocale ?
* **L'intérêt** : Respecter les critères d'accessibilité numérique (RGAA) mis en avant dans l'évaluation du projet.

---

## 8. Priorités pour la V1 (Décembre) et la V2 (Mars)

### Q.H1 — Choix du composant prioritaire pour la V1 de décembre
* **La question** : La slide 26 indique que pour le premier semestre (fin décembre), l'équipe doit réaliser un composant logiciel complet de bout en bout. Quel volet la MOA souhaite-t-elle voir réalisé en priorité :
  - Option A : Le module commerçant (création de boutique, catalogue de produits et gestion des stocks) ?
  - Option B : Le module client (consultation des commerces, panier d'achat et commande Click & Collect) ?
  - Option C : Le module fidélité et stationnement (calcul des points, attribution du statut VFP et échange contre du parking) ?
* **L'intérêt** : Concentrer nos efforts de développement dès le mois d'octobre sur le composant le plus stratégique pour la première soutenance.

### Q.H2 — Systèmes externes à simuler (Mocks) pour la V1
* **La question** : La slide 15 indique que les services partenaires seront simulés. Pour la démonstration de décembre, quels systèmes externes devons-nous simuler en priorité :
  - Une simulation d'API de stationnement municipal ?
  - Une simulation de passerelle de paiement par carte bancaire ?
  - Une simulation de logiciel de caisse de magasin ?
* **L'intérêt** : Définir dès maintenant le périmètre des simulateurs à programmer pour les tests et la démonstration orale.

### Q.H3 — Données de démonstration pour les présentations
* **La question** : Pour les soutenances et les tests de validation, avec quel volume de fausses données souhaitez-vous que nous préparions nos démonstrations :
  - Une ville témoin avec 5 à 10 commerces représentatifs (boulangerie, boucherie, prêt-à-porter, librairie) et une cinquantaine d'articles ?
  - Des comptes pré-remplis pour les différents personas (Pierre, Julie, Arthur, Suzanne, Marius) avec des historiques d'achats réalistes ?
* **L'intérêt** : Disposer d'un jeu de données de test complet illustrant immédiatement tous les parcours lors des revues de projet.

---

## 9. Démarche d'Éco-Conception (Green IT)

### Q.I1 — Critères d'évaluation de l'éco-conception logicielle
* **La question** : Les slides 16 à 19 soulignent l'importance de réduire l'impact environnemental des serveurs et du numérique. Sur quels critères concrets notre projet sera-t-il évalué sur ce point :
  - La légèreté des pages et la rapidité de chargement (mesurées avec des outils comme EcoIndex ou GreenIT Analysis) ?
  - L'optimisation des requêtes en base de données pour limiter la charge processeur des serveurs ?
  - Un dossier explicatif démontrant les choix d'architecture sobre retenus par l'équipe ?
* **L'intérêt** : Savoir précisément quelles mesures et quels indicateurs présenter pour justifier notre démarche d'éco-conception.
