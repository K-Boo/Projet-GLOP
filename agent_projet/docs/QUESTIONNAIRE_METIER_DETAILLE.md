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
| **Titre du Document** | *Questionnaire de cadrage fonctionnel approfondi (34 questions métiers (dont Protection Juridique) — 9 volets)* |
| **Référence Documentaire** | `GLOP-2026-R1-QUESTIONNAIRE-DETAILLE-v1.0` |
| **Contexte Académique** | Master 2 MIAGE — UE Génie Logiciel par la Pratique (GLOP) 2026-2027, Université de Lille |
| **Destinataires (MOA)** | Laurence Duchien, Anne Etien, François Secchi, Jérémy Woirhaye |
| **Date de Soumission** | 07 Septembre 2026 |
| **Statut du Document** | Version 1.1 — *Consolidée suite aux arbitrages MOA (Séance du 07/09/2026)* |
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
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : L'association des commerçants (structure à but non lucratif loi 1901) est co-initiatrice du projet avec la mairie via une convention tripartite. Le commerçant doit être obligatoirement adhérent de l'association locale pour intégrer ShopLoc. C'est l'association qui contrôle les adhésions et débloque les accès. Elle dispose d'un panel de gestion et de visualisation des indicateurs pour suivre l'activité et prévenir les fraudes.

### Q.A2 — Répartition des rôles entre la Mairie et l'Association des Commerçants
* **La question** : Le sujet mentionne des services à destination de la mairie (notamment via le service Citoyen Numérique). Comment s'organise la collaboration entre la mairie et l'association :
  - La mairie dispose-t-elle de son propre compte d'accès ?
  - Qui décide de lancer les campagnes de promotion et les sondages d'opinion : la mairie ou l'association ?
  - En cas d'avis divergent sur une communication, qui a la priorité décisionnelle ?
* **L'intérêt** : Clarifier les droits de chacun pour l'envoi de messages aux usagers et définir les profils d'utilisateurs à créer.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : La mairie et l'association signent une convention définissant les objectifs d'attractivité du centre-ville. Les commerçants offrent des points de fidélité et des cadeaux sur leurs produits ; la mairie offre des avantages institutionnels de mobilité (tickets de transport en commun et 20 minutes de stationnement). Chacune des deux entités dispose d'un espace de gestion propre avec des droits séparés.

### Q.A3 — Modèle économique et facturation de la solution
* **La question** : À qui ShopLoc vend-elle son service :
  - À la Mairie, qui finance la plateforme dans le cadre de sa politique d'attractivité du centre-ville ?
  - À l'Association des commerçants, via les cotisations de ses membres ?
  - Ou directement aux commerçants, qui paient chacun un abonnement à ShopLoc ?
* **L'intérêt** : C'est la base de notre étude financière (Livrable R3). Cela détermine comment ShopLoc génère ses revenus et auprès de qui émettre les factures.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : ShopLoc contractualise et facture directement l'association des commerçants. La mairie verse une subvention d'amorçage et de fonctionnement à l'association pour financer le dispositif. L'équipe est libre de calibrer le modèle tarifaire exact (redevance logicielle récurrente selon la taille de la ville) en devant être capable de défendre ses choix lors du rendu R1/R3.

### Q.A4 — Processus d'inscription d'un commerçant
* **La question** : Comment se déroule l'arrivée d'un nouveau commerçant sur la plateforme :
  - L'inscription est-elle libre et immédiate en ligne ?
  - Ou nécessite-t-elle une validation préalable (vérification du SIRET, conformité du commerce) par l'administrateur ShopLoc ou l'association locale avant l'ouverture de la boutique ?
* **L'intérêt** : Déterminer si nous devons gérer un statut d'attente de validation pour les nouveaux comptes commerçants.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : L'inscription n'est pas ouverte sans contrôle : le commerçant doit être adhérent à l'association des commerçants. C'est l'association qui valide la conformité de l'établissement et lui attribue son compte commerçant actif.

---

## 2. Déploiement et Gestion Multi-Villes

### Q.B1 — Choix entre plateforme mutualisée (SaaS) ou déploiement séparé par ville
* **La question** : L'énoncé demande une architecture logicielle réutilisable dans différentes villes. Quel modèle devons-nous privilégier :
  - Une application unique et partagée (SaaS multi-tenant), où chaque ville possède son propre espace au sein d'une même base de données ?
  - Ou une application installée et hébergée séparément sur des serveurs distincts pour chaque ville cliente ?
* **L'intérêt** : C'est un choix d'architecture majeur. Une solution mutualisée réduit les coûts d'infrastructure et simplifie les mises à jour, tandis qu'un déploiement séparé isole complètement les données de chaque commune.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Liberté totale accordée à l'équipe, sous condition de justifier et défendre rigoureusement le choix architectural. La MOE valide l'orientation SaaS multi-tenant avec partitionnement logique (tenant_id = ville_id) pour permettre un déploiement rapide dans de nouvelles communes en 18 mois avec une équipe d'ingénieurs réduite, tout en minimisant l'empreinte serveur (éco-conception).

### Q.B2 — Ville de rattachement principale et avantages des résidents
* **La question** : Un compte usager (ex : Julie) fonctionne dans toutes les villes partenaires. L'usager peut-il déclarer une « ville de rattachement principale » (sa commune de résidence) :
  - Les avantages financés par une commune (ex : heures de stationnement gratuit, chèques d'achat locaux) sont-ils réservés aux seuls habitants de cette commune ?
  - Un usager extérieur gagne-t-il les mêmes points qu'un résident local ?
  - Les points de fidélité sont-ils utilisables uniquement dans la ville où ils ont été acquis, ou dans l'ensemble des villes du réseau ?
* **L'intérêt** : Permettre aux mairies de réserver leurs aides financières à leurs propres contribuables et cadrer la validité des points de fidélité.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Le système gère les usagers avec flexibilité : compte unique transversal ou comptes distincts selon le choix de l'utilisateur. Les avantages financés par une collectivité (tickets bus, stationnement) restent rattachés à la ville où les passages et achats ont été effectués.

### Q.B3 — Adaptation selon la taille de la commune (Petite, Moyenne, Grande Ville)
* **La question** : Le sujet distingue 3 tailles de villes (<20k, 20k-100k, >100k habitants). Qu'implique cette distinction dans l'application :
  - S'agit-il seulement de dimensionner les serveurs pour supporter un volume d'utilisateurs plus important ?
  - Ou certaines fonctionnalités doivent-elles pouvoir être activées ou désactivées selon la ville (ex : désactiver le module parking dans les petites communes sans horodateurs payants, découper en quartiers pour les grandes villes) ?
* **L'intérêt** : Savoir si nous devons concevoir des modules optionnels configurables par ville.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : L'architecture doit être hautement scalable en volume de données et nombre d'usagers. Elle doit supporter une configuration modulaire selon les paramètres locaux : présence ou non de transports en commun, présence ou non d'horodateurs payants, et découpage par quartier pour les métropoles.

### Q.B4 — Objectifs attendus pour le cap des 18 mois
* **La question** : L'énoncé fixe comme objectif de devenir leader du marché à 18 mois. Sur quels indicateurs ce succès sera-t-il évalué :
  - Le nombre de villes partenaires signées ?
  - Le nombre de commerçants actifs et de produits proposés ?
  - Le volume des ventes réalisées et la rentabilité financière ?
* **L'intérêt** : Aligner nos choix techniques, notre calendrier de déploiement et notre offre financière sur les attentes concrètes du client.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Atteindre le leadership sur le marché en 18 mois en prouvant la capacité à industrialiser et déployer rapidement la solution dans de nouvelles agglomérations avec une équipe réduite, tout en démontrant la rentabilité de l'investissement (calculs de ROI et de VAN requis pour le livrable R3).

---

## 3. Paiements, Commissions et Gestion des Litiges

### Q.C1 — Circuit d'encaissement des commandes en ligne
* **La question** : Lors d'un achat réglé en ligne sur l'application :
  - L'argent est-il encaissé sur un compte central ShopLoc avant d'être reversé régulièrement aux commerçants ?
  - Ou le paiement est-il automatiquement ventilé et transféré directement sur le compte bancaire de chaque commerçant au moment de l'achat (via une solution comme Stripe Connect) ?
* **L'intérêt** : Encaisser l'argent au nom de tiers impose des contraintes réglementaires fortes (statut d'intermédiaire financier). Savoir quel modèle retenir oriente le choix de notre passerelle de paiement.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Le client peut régler une commande groupée multi-commerçants en un seul paiement en ligne. La composante transactionnelle bancaire réelle est simulée dans le cadre du projet via des interfaces de mock conformes aux standards bancaires.

### Q.C2 — Modèle de commissionnement sur les ventes
* **La question** : Comment ShopLoc se rémunère-t-elle sur les commandes Click & Collect :
  - Par un pourcentage sur chaque commande (ex : 3 % du montant) ?
  - Par des frais fixes par panier (ex : 0,50 € par commande) ?
  - Ou sans commission sur les ventes, si les commerçants paient déjà un abonnement mensuel ?
  - Qui prend en charge les frais bancaires de transaction par carte ?
* **L'intérêt** : Nécessaire pour coder le calcul automatique des montants reversés aux commerçants et construire notre plan financier prévisionnel (Livrable R3).
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : La partie financière étant simulée, le modèle économique privilégie un forfait annuel/mensuel facturé à l'association des commerçants (subventionnée par la ville), sans ponctionner excessivement les marges des artisans locaux.

### Q.C3 — Gestion des retours, produits manquants et litiges
* **La question** : Que se passe-t-il si un client constate un problème lors du retrait (produit abîmé, manquant ou non conforme) :
  - Le commerçant peut-il effectuer un remboursement partiel ou total directement depuis son application ?
  - Le commerçant peut-il proposer un produit de remplacement en accord avec le client ?
  - L'application doit-elle intégrer un module de réclamation pour contacter le support ShopLoc ?
* **L'intérêt** : Savoir si nous devons développer un système de suivi des litiges en ligne ou si ces situations se règlent directement en boutique.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Gestion directe et concertée au comptoir entre le commerçant et le client. Règle stricte en cas de no-show : si le client ne vient pas retirer sa commande dans le créneau imparti, il perd sa commande et le montant reste acquis au commerçant.

---

## 4. Produits, Stocks, Vente au Poids et Horaires (Suzanne)

### Q.D1 — Gestion des articles vendus au poids réel (Boucherie, Fromagerie, Primeur)
* **La question** : Dans les commerces alimentaires de centre-ville, beaucoup d'articles sont vendus au poids (ex : un client commande 300g, mais la découpe finale fait 320g ou 290g). Comment gérer le paiement :
  - Peut-on utiliser une pré-autorisation bancaire ajustée au montant exact une fois la commande pesée par le commerçant ?
  - Ou impose-t-on des portions à prix fixe pour simplifier le système ?
* **L'intérêt** : Permettre aux commerces de bouche d'utiliser facilement la plateforme sans bloquer les commandes pour quelques grammes d'écart.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : L'application supporte le paramétrage de l'unité de vente par le commerçant (à la pièce, au kg, aux 100g, à la part). Pour la V1, modélisation avec prix unitaire fixé à la commande pour simplifier la saisie et les transactions.

### Q.D2 — Délais de préparation et créneaux de retrait
* **La question** : Comment s'organise la préparation des commandes côté commerçant :
  - Le commerçant peut-il définir son délai de préparation par article (ex : 1 heure pour des fleurs, 24 heures pour un gâteau sur commande) ?
  - Le client choisit-il un créneau précis de passage (ex : entre 17h30 et 18h) ?
  - Le commerçant peut-il suspendre temporairement la prise de commandes en cas d'affluence en magasin ?
* **L'intérêt** : Éviter qu'un client arrive avant que sa commande ne soit prête et permettre au commerçant de gérer son rythme de travail.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Le commerçant peut définir un délai de disponibilité et de préparation par produit ou catégorie. Le système intègre obligatoirement la gestion des emplois du temps et horaires de chaque boutique pour proposer des créneaux de retrait cohérents lors d'une tournée multi-commerçants.

### Q.D3 — Mise à jour des stocks et liaison avec les caisses existantes
* **La question** : Suzanne vend ses produits à la fois aux clients en boutique et aux usagers de l'application. Comment gère-t-elle ses stocks :
  - Doit-elle mettre à jour ses stocks manuellement dans l'application ShopLoc ?
  - Ou devons-nous prévoir un import de catalogue par fichier (Excel/CSV), voire une connexion possible avec des logiciels de caisse courants ?
* **L'intérêt** : Éviter aux commerçants une double saisie fastidieuse qui risquerait de provoquer des erreurs de stock et des abandons d'utilisation.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Le commerçant pilote son stock dans l'application via une saisie manuelle de ses produits et quantités Click & Collect. Fréquence journalière ou adaptée au commerce. Une interconnexion avec les caisses physiques pourra être envisagée en phase ultérieure mais n'est pas requise pour la première version (V1).

### Q.D4 — Gestion des horaires d'ouverture et des congés
* **La question** : Concernant les horaires des commerces :
  - L'application bloque-t-elle automatiquement les commandes si le magasin est fermé au moment demandé pour le retrait ?
  - Le commerçant dispose-t-il d'un mode « fermeture exceptionnelle / congés » qui masque temporairement ses produits sans les supprimer ?
* **L'intérêt** : Garantir que les clients ne commandent pas sur des plages de fermeture et afficher des horaires fiables.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Prise en compte obligatoire des horaires de chaque commerce pour le calcul de l'itinéraire optimal de collecte (plus court chemin ou plus court en temps). En cas de non-retrait d'une commande passée (no-show), celle-ci est définitivement perdue pour le client afin de protéger les stocks périssables.

---

## 5. Programme de Fidélité, Récompenses et Stationnement

### Q.E1 — Valeur financière d'un point de fidélité
* **La question** : Quelle équivalence financière souhaite-t-on donner aux points :
  - Existe-t-il un barème commun à toute la ville (ex : 100 points = 5 € de réduction ou 1 heure de parking) ?
  - Ou chaque commerçant fixe-t-il librement la valeur de ses points ?
* **L'intérêt** : Établir la grille de conversion nécessaire au catalogue de cadeaux et calibrer l'échange contre du temps de stationnement.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Découplage strict entre points d'achat et statut VFP. Pour le système de points, c'est chaque commerçant qui fixe librement le nombre de points attribués par produit ou par commande. Les deux systèmes (points vs régularité) sont totalement indépendants.

### Q.E2 — Financement des cadeaux échangés entre commerces différents
* **La question** : Si un client cumule des points chez un boucher et les utilise pour obtenir un cadeau chez Suzanne (boutique de vêtements) :
  - Suzanne offre-t-elle ce cadeau sans contrepartie ?
  - Ou existe-t-il une compensation financière (via une caisse commune gérée par l'association ou ShopLoc) pour rembourser Suzanne de la valeur de l'article offert ?
* **L'intérêt** : Si les commerçants ne sont pas dédommagés lorsqu'un client dépense des points acquis ailleurs, ils ne proposeront pas d'articles attractifs. Il est donc crucial de clarifier s'il y a un mécanisme de remboursement inter-commerces.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Les commerçants alimentent eux-mêmes leur catalogue de lots et avantages. Pour débloquer et retirer un cadeau chez un commerçant, le client doit obligatoirement avoir effectué au moins un achat antérieur dans cette boutique et présenter sa carte lors d'un achat en cours (interdiction de venir retirer un cadeau sans consommation).

### Q.E3 — Responsabilité du catalogue de récompenses
* **La question** : Qui a le droit d'ajouter des cadeaux dans l'application :
  - Chaque commerçant propose-t-il ses propres récompenses depuis son espace ?
  - Ou l'association des commerçants gère-t-elle un catalogue commun pour tout le centre-ville (ex : bons d'achat valables partout, entrées de cinéma) ?
* **L'intérêt** : Définir qui a les droits de gestion sur les récompenses dans la base de données.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Chaque commerçant reste maître de son offre de récompenses dans son propre catalogue (ex : Suzanne au Fournil ajustant son lot d'une part de tarte au maroilles vers une mini-viennoiserie).

### Q.E4 — Durée de validité des points accumulés
* **La question** : Les points sont-ils valables indéfiniment ou expirent-ils après une période sans achat (ex : 12 mois sans commande) ?
* **L'intérêt** : Éviter l'accumulation de points dormants qui représenteraient un engagement financier difficile à gérer pour les commerçants sur le long terme.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Les points de fidélité ont une durée de validité ferme de 1 an (12 mois). Passé ce délai sans utilisation, les points expirent automatiquement.

### Q.E5 — Prise en charge du coût du stationnement offert
* **La question** : Qui prend en charge le coût des heures de stationnement offertes :
  - La Mairie, qui accorde cette gratuité pour encourager les habitants à fréquenter les commerces de centre-ville ?
  - Ou l'association des commerçants, qui rembourse la mairie pour chaque heure de stationnement consommée ?
* **L'intérêt** : Prévoir le suivi financier et les bilans réguliers entre ShopLoc, la mairie et les commerçants.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : La Mairie prend directement en charge le coût des avantages de voirie et de mobilité (20 minutes de parking et tickets de bus journaliers) dans le cadre de sa politique d'attractivité et de soutien au commerce local.

---

## 6. Administration, Outils Marketing et Protection des Données (Marius)

### Q.F1 — Critères de calcul du statut VFP (Very Frequent Purchaser)
* **La question** : Quels critères précis déclenchent l'obtention du statut VFP :
  - Un montant minimum dépensé par mois (ex : plus de 150 €) ?
  - Un nombre minimum de commandes (ex : au moins 4 achats par mois) ?
  - Une condition de mixité (ex : avoir acheté dans au moins 2 ou 3 commerces différents pour favoriser la diversité des achats en centre-ville) ?
* **L'intérêt** : Coder l'algorithme qui calculera automatiquement ce statut de fidélité chaque nuit.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Le statut VFP (Very Faithful Person) repose exclusivement sur la régularité des visites (fréquence de passage dans les commerces partenaires). Règle de la fenêtre glissante : un client n'est pas VFP au départ ; il doit cumuler au moins 10 passages dans les commerces partenaires au cours des 15 derniers jours pour obtenir le statut.

### Q.F2 — Perte du statut VFP et relances marketing
* **La question** : L'énoncé indique que Marius exploite les données pour relancer les clients, notamment lors de la perte du statut VFP :
  - Le statut est-il recalculé chaque mois ?
  - Une alerte préventive est-elle envoyée au client avant la perte de son statut (ex : un message l'informant qu'il lui reste 7 jours et 1 achat pour conserver ses avantages) ?
  - Marius déclenche-t-il ces relances manuellement, ou le système les envoie-t-il automatiquement ?
* **L'intérêt** : Déterminer le degré d'automatisation des relances marketing à programmer dans l'application.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Dès les 10 passages cumulés sur 15 jours, l'usager déclenche 1 ticket de bus ou 20 minutes de parking gratuit. Ensuite, tant qu'il maintient sa régularité (au moins 10 passages sur les 15 derniers jours glissants), chaque nouveau passage lui octroie 1 ticket de bus ou 20 minutes de parking supplémentaires. Dès que la fréquence passe sous le seuil des 10 passages sur 15 jours (ex : Arthur pendant les vacances scolaires), le statut VFP est suspendu. Marius peut relancer les usagers perdant leur statut.

### Q.F3 — Canaux de diffusion des offres promotionnelles
* **La question** : Quand Marius diffuse une offre commerciale ou une annonce municipale :
  - Par quel canal l'offre est-elle transmise : notifications sur smartphone, e-mails, SMS, ou bandeau dans l'application ?
  - Si des SMS sont utilisés, qui prend en charge leur coût d'envoi ?
* **L'intérêt** : Choisir les services d'envoi à intégrer et chiffrer leurs coûts dans notre proposition financière R1.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Diffusion par notifications web/mobile et emails à la demande du service Citoyen Numérique de la ville ou de l'association des commerçants.

### Q.F4 — Filtres de ciblage disponibles pour Marius
* **La question** : Quels critères de recherche Marius peut-il combiner pour cibler ses campagnes :
  - Les clients inactifs depuis une certaine durée (ex : aucun achat depuis 30 jours) ?
  - Les clients fidèles détenant le statut VFP ?
  - Les usagers résidant dans un quartier ou code postal particulier ?
  - Les clients habitués à une catégorie de commerce (ex : boulangerie, prêt-à-porter) ?
* **L'intérêt** : Concevoir le formulaire de filtrage et optimiser les requêtes de recherche dans la base de données.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Marius dispose de filtres basés sur les habitudes de consommation, l'activité Click & Collect, les cadeaux retirés, la régularité et la perte du statut VFP, afin de cibler les campagnes de réactivation.

### Q.F5 — Gestion des sondages de satisfaction
* **La question** : Le sujet mentionne que Marius peut lancer des sondages auprès des usagers :
  - Marius peut-il créer lui-même de nouvelles questions depuis son interface (notes, choix multiples, texte libre) ?
  - L'attribution de points de fidélité bonus (ex : 10 points) est-elle prévue pour encourager les citoyens à y répondre ?
* **L'intérêt** : Développer un module d'enquête adapté et le relier au solde de points des participants.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Marius dispose depuis son panel d'administration de la capacité d'élaborer et de diffuser des sondages de satisfaction auprès des citoyens usagers pour évaluer la perception des actions municipales et du commerce de proximité.

### Q.F6 — Respect de la vie privée et conformité RGPD
* **La question** : Le sujet insiste sur le respect de la vie privée. Quelles règles de confidentialité devons-nous appliquer :
  - Marius a-t-il accès aux détails nominatifs des paniers d'achat des clients, ou seulement à des statistiques globales et anonymisées ?
  - Les commerçants ont-ils l'interdiction de voir les achats réalisés par leurs clients dans les autres boutiques ?
  - Comment le client choisit-il les communications qu'il accepte de recevoir (opt-in pour les offres de la mairie, des commerces, etc.) ?
* **L'intérêt** : Assurer la conformité légale avec le RGPD, protéger la vie privée des citoyens et préserver le secret commercial entre boutiques partenaires.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Cloisonnement strict des données : aucun commerçant n'a accès aux achats effectués chez ses confrères. Les données exploitées par la mairie et l'association sont agrégées et pseudonymisées pour piloter la politique locale et détecter les comportements frauduleux sans porter atteinte à la vie privée des administrés.

---

## 7. Connexion, Sécurité et Accessibilité

### Q.G1 — Connexion simplifiée pour les usagers seniors (Pierre, 74 ans)
* **La question** : Pour faciliter l'accès des usagers seniors qui retiennent difficilement les mots de passe complexes :
  - Peut-on proposer des modes de connexion simplifiés comme un code PIN à 4 chiffres, un lien de connexion envoyé par e-mail (Magic Link) ou un code par SMS ?
  - Une connexion via FranceConnect est-elle envisageable pour réutiliser le compte officiel déjà connu des citoyens ?
* **L'intérêt** : Rendre l'application accessible à tous les âges et éviter l'abandon d'utilisation à cause d'une étape de connexion trop contraignante.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Double modalité d'utilisation : mise à disposition d'une carte physique plastifiée avec QR code unique par abonné (scannable par les commerçants) pour les seniors, et accès direct à la carte dématérialisée via l'application web. Possibilité de charger en ligne une petite somme d'argent par carte bancaire sur la carte (type Izli) pour les menues dépenses du quotidien chez les partenaires.

### Q.G2 — Sécurité des comptes commerçants et administrateur (2FA)
* **La question** : Les comptes de Suzanne (qui gère des coordonnées bancaires) et de Marius (qui a accès à la base usagers) manipulent des données sensibles. Doit-on imposer une double sécurité (code de vérification envoyé sur téléphone / 2FA) lors de leur connexion ?
* **L'intérêt** : Protéger les fonds des commerçants et les données personnelles contre les risques d'usurpation de compte.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Authentification robuste et segmentation des habilitations. Chaque typologie d'acteur (client, commerçant, association, collectivité) dispose d'un panel d'administration et de visualisation dédié et étanche.

### Q.G3 — Gestion de plusieurs utilisateurs pour un même commerce
* **La question** : En boutique, les personnes au comptoir sont souvent des employés ou des apprentis qui préparent les commandes de Click & Collect :
  - Un compte commerçant peut-il comporter plusieurs profils d'accès ?
    - Un profil « Vendeur / Préparateur » qui voit uniquement les commandes à préparer et les stocks, sans accès à la comptabilité ni aux coordonnées bancaires.
    - Un profil « Gérant » avec tous les droits de configuration et d'accès financier.
* **L'intérêt** : Répondre à l'organisation réelle des commerces de centre-ville et sécuriser les informations financières.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Pour le ticket de bus : association et passage de la carte de transport de la ville (ex : Ilévia). Pour le stationnement : saisie de la plaque d'immatriculation sur le smartphone et déclenchement du compteur des 20 minutes gratuites ; contrôle en voirie par la police municipale via la saisie du numéro de plaque sur smartphone.

---

## 8. Priorités pour la V1 (Décembre) et la V2 (Mars)

### Q.H1 — Choix du composant prioritaire pour la V1 de décembre
* **La question** : La slide 26 indique que pour le premier semestre (fin décembre), l'équipe doit réaliser un composant logiciel complet de bout en bout. Quel volet la MOA souhaite-t-elle voir réalisé en priorité :
  - Option A : Le module commerçant (création de boutique, catalogue de produits et gestion des stocks) ?
  - Option B : Le module client (consultation des commerces, panier d'achat et commande Click & Collect) ?
  - Option C : Le module fidélité et stationnement (calcul des points, attribution du statut VFP et échange contre du parking) ?
* **L'intérêt** : Concentrer nos efforts de développement dès le mois d'octobre sur le composant le plus stratégique pour la première soutenance.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Réalisation d'un composant logiciel complet de bout en bout (backend J2E, persistance relationnelle SQL, frontend accessible) déployé sous Docker avec tests automatisés. Le cœur de métier à privilégier couvre le catalogue Click & Collect avec gestion de stock simplifiée et le moteur d'attribution VFP / stationnement.

### Q.H2 — Systèmes externes à simuler (Mocks) pour la V1
* **La question** : La slide 15 indique que les services partenaires seront simulés. Pour la démonstration de décembre, quels systèmes externes devons-nous simuler en priorité :
  - Une simulation d'API de stationnement municipal ?
  - Une simulation de passerelle de paiement par carte bancaire ?
  - Une simulation de logiciel de caisse de magasin ?
* **L'intérêt** : Définir dès maintenant le périmètre des simulateurs à programmer pour les tests et la démonstration orale.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Simulation complète (mocks d'APIs RESTful documentées) des services partenaires : passerelle de paiement bancaire en ligne, API de voirie municipale (contrôle stationnement par plaque) et interfaçage avec le réseau de transport public.

### Q.H3 — Données de démonstration pour les présentations
* **La question** : Pour les soutenances et les tests de validation, avec quel volume de fausses données souhaitez-vous que nous préparions nos démonstrations :
  - Une ville témoin avec 5 à 10 commerces représentatifs (boulangerie, boucherie, prêt-à-porter, librairie) et une cinquantaine d'articles ?
  - Des comptes pré-remplis pour les différents personas (Pierre, Julie, Arthur, Suzanne, Marius) avec des historiques d'achats réalistes ?
* **L'intérêt** : Disposer d'un jeu de données de test complet illustrant immédiatement tous les parcours lors des revues de projet.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Constitution d'un jeu de données représentatif intégrant une sélection de commerces de centre-ville et des comptes préconfigurés incarnant les 5 personas du projet (Pierre, Julie, Arthur, Marius, Suzanne).

---

## 9. Démarche d'Éco-Conception (Green IT)

### Q.I1 — Critères d'évaluation de l'éco-conception logicielle
* **La question** : Les slides 16 à 19 soulignent l'importance de réduire l'impact environnemental des serveurs et du numérique. Sur quels critères concrets notre projet sera-t-il évalué sur ce point :
  - La légèreté des pages et la rapidité de chargement (mesurées avec des outils comme EcoIndex ou GreenIT Analysis) ?
  - L'optimisation des requêtes en base de données pour limiter la charge processeur des serveurs ?
  - Un dossier explicatif démontrant les choix d'architecture sobre retenus par l'équipe ?
* **L'intérêt** : Savoir précisément quelles mesures et quels indicateurs présenter pour justifier notre démarche d'éco-conception.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Démarche d'éco-conception logicielle rigoureuse : sobriété du code, frugalité des ressources, optimisation des requêtes SQL, déploiement conteneurisé économe et transparence totale sur l'utilisation raisonnée et tracée des outils d'intelligence artificielle (conformément au règlement des études et aux exigences Green IT).


### Q.I2 — Protection juridique du logiciel (Axe 9 du sujet)
* **La question** : Quelles modalités de protection juridique devons-nous prévoir pour le projet ShopLoc :
  - Quel type de licence logicielle retenir pour le code source et la documentation ?
  - Comment protéger la propriété intellectuelle de la plateforme vis-à-vis des collectivités territoriales et des tiers ?
  - Quelles conditions générales d'utilisation (CGU) et mentions de protection des bases de données prévoir ?
* **L'intérêt** : Répondre explicitement à l'axe 9 du sujet ("Protection juridique du logiciel : faire un développement sur le sujet") exigé par les enseignants.
* **Arbitrage MOA & Décision Validée (Séance du 07/09/2026)** : Un développement juridique dédié sera formalisé dans les dossiers de cadrage R1 et d'architecture, articulé autour d'une licence SaaS propriétaire protégeant le patrimoine logiciel de ShopLoc, combinée aux licences open source des frameworks utilisés (Spring Boot / J2E), avec clauses contractuelles encadrant la convention Mairie-Association.
