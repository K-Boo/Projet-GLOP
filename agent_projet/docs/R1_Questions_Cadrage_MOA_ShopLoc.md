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

# DOSSIER DE CADRAGE PRÉALABLE & QUESTIONNAIRE D'INSTRUCTION MÉTIER
## Projet ShopLoc — Réponse à Appel d'Offres (Livrable R1)

---

##  Informations Générales sur le Document

| Champ | Information |
|---|---|
| **Intitulé du Projet** | **Projet ShopLoc** — Marketplace & Fidélisation multi-commerces |
| **Identifiant Officiel du Projet** | `MiageShopLoc` |
| **Titre du Document** | *Questionnaire de cadrage fonctionnel & levée des zones d'ombre métier* |
| **Référence Documentaire** | `GLOP-2026-R1-QUESTIONS-v1.0` |
| **Contexte Académique** | Master 2 MIAGE — UE Génie Logiciel par la Pratique (GLOP) 2026-2027, Université de Lille |
| **Destinataires (MOA)** | Laurence Duchien, Anne Etien, François Secchi, Jérémy Woirhaye |
| **Date de Soumission** | 07 Septembre 2026 |
| **Statut du Document** | Version 1.0 — *Pour instruction et arbitrage de la MOA* |
| **Tag obligatoire communications** | `[GLOP]` *(à inclure dans tout objet de courriel)* |

---

## Préambule & Démarche d'Instruction

Dans l'optique de concevoir une architecture logicielle robuste, extensible et parfaitement adaptée aux réalités opérationnelles des commerces de centre-ville, notre équipe a mené une analyse approfondie du cahier des charges initial.

Afin de ne laisser **aucune zone d'ombre** et d'aligner notre proposition technique et financière (rendu du 18/09/2026) avec les besoins réels de ShopLoc, nous avons formalisé ce questionnaire d'instruction détaillé. Chaque question est motivée par un impact direct sur le modèle de données, les flux financiers ou l'architecture applicative, et nous y associons une **hypothèse de travail préconisée** par notre cabinet.

---

## 1. Gouvernance Territoriale, Multi-Villes & Modèle Économique

### Q1.1 — Découpage territorial et Multi-Tenancy (Évolutivité Villes)
* **Contexte** : L'application doit s'adapter à 3 typologies urbaines : petites (<20k hab.), moyennes (20k-100k hab.) et grandes (>100k hab.).
* **Questions** :
  1. La plateforme doit-elle fonctionner en **SaaS multi-tenant mutualisé** (une base centrale où chaque ville/association est un espace virtuel partitionné) ou en **déploiements dédiés** par commune/association ?
  2. Un utilisateur (ex: Julie travaillant dans une grande ville et résidant dans une commune moyenne voisine) dispose-t-il d'un **compte unique transversal** lui permettant de basculer d'une ville à l'autre, ou doit-il recréer un profil par territoire ?
  3. Dans une grande ville, comment s'organise le périmètre : par quartier / arrondissement, ou à l'échelle globale de la métropole ?
* **Hypothèse préconisée par la MOE** : Architecture SaaS multi-tenant avec partitionnement logique (`tenant_id = ville_id`), compte client unique transversal géolocalisé, et filtrage par quartier/code postal pour les grandes métropoles.

### Q1.2 — Modèle Financier, Commissionnement et Flux de Paiement
* **Contexte** : ShopLoc est une marketplace intermédiaire entre commerçants indépendants, usagers et collectivités.
* **Questions** :
  1. Quel est le modèle économique de ShopLoc ?
     * Prélèvement d'une **commission sur les transactions Click & Collect** (ex: 2 à 5 %) ?
     * **Abonnement mensuel** facturé aux commerçants (ex: 19€/mois) ?
     * **Licence logicielle / subvention forfaitaire** prise en charge annuellement par la Mairie ou l'association des commerçants ?
  2. **Encaissement des commandes Click & Collect** :
     * Le client paie-t-il obligatoirement en ligne via la plateforme (exigeant un compte séquestre de paiement agréé type Stripe Connect / Lemonway avec split-payment) ?
     * Ou le paiement s'effectue-t-il au comptoir lors du retrait (l'application n'étant qu'un outil de réservation sans flux monétaire direct) ?
     * Ou un mode hybride au choix du commerçant ?
  3. En cas de paiement en ligne, quelle est la politique de versement des fonds aux commerçants (J+1, hebdomadaire, mensuel) et qui supporte les frais bancaires de transaction ?
* **Hypothèse préconisée par la MOE** : Mode hybride priorisant le paiement en ligne sécurisé (Stripe Connect) avec option "Paiement en boutique" paramétrable par le commerçant ; modèle mixte (subvention d'amorçage mairie + commission minime 2% pour assurer la rentabilité pérenne à 18 mois).

---

## 2. Parcours Click & Collect & Gestion des Commandes

### Q2.1 — Granularité du Panier d'Achat (Multi-Commerces vs Mono-Commerce)
* **Contexte** : Dans un centre-ville, un citoyen (Arthur) achète souvent son pain chez le boulanger, sa viande chez le boucher et un livre chez le libraire.
* **Questions** :
  1. Le système permet-il un **panier unique multi-boutiques** (paiement unique puis tournée de retrait dans chaque commerce), ou le client doit-il valider et payer **un panier distinct par commerçant** ?
  2. Si panier multi-boutiques : comment sont gérés les créneaux de retrait si un commerçant ferme à 18h et l'autre à 19h30 ?
* **Hypothèse préconisée par la MOE** : Panier global unifié avec ventilation automatique en sous-commandes indépendantes par boutique, chaque boutique ayant son propre statut de préparation et son créneau de mise à disposition.

### Q2.2 — Cycle de Vie de la Commande, Annulation & Produits Périssables
* **Contexte** : Les commerces de centre-ville vendent des produits frais à forte périssabilité.
* **Questions** :
  1. Quel est le workflow exact de la commande :
     * *Commande passée -> Acceptation par le commerçant -> En préparation -> Prête au retrait -> Retirée / Clôturée* ?
  2. Le commerçant a-t-il le droit de refuser une commande (ex: rupture imprévue) ? Si oui, remboursement automatique ?
  3. Que se passe-t-il en cas de **« No-Show »** (client qui ne vient jamais chercher son panier) ?
     * Pour les produits secs : annulation et remise en stock ?
     * Pour les produits frais/périssables : la somme reste-t-elle acquise au commerçant ?
  4. Comment gérer les articles vendus **au poids réel** (ex: boucherie/fromagerie : 300g commandés mais 325g pesés) ? Autorise-t-on une pré-autorisation bancaire avec ajustement au retrait ?
* **Hypothèse préconisée par la MOE** : Pré-autorisation bancaire avec capture lors de la préparation ; rétention de 100% du montant sur denrées périssables en cas de no-show sous 24h ; possibilité de signaler un poids réel avec marge tolérée de ±15%.

---

## 3. Système de Fidélisation & Statut VFP (Very Frequent Purchaser)

### Q3.1 — Règles d'Acquisition et Périmètre des Points
* **Contexte** : L'objectif affiché est de fidéliser la clientèle locale face aux zones commerciales périphériques.
* **Questions** :
  1. **Règle de conversion euros -> points** : Quel est le barème standard (ex: 1 € dépensé = 1 point, ou barème libre par commerçant) ?
  2. **Canal d'acquisition** : Les points sont-ils gagnés :
     * Uniquement sur les commandes Click & Collect passées via l'application ?
     * Ou également lors des **achats physiques directs en boutique** ? Si oui, comment le commerçant enregistre-t-il la transaction (scan du QR code client sur le smartphone de Suzanne, saisie du numéro de carte, ou intégration caisse) ?
  3. **Fongibilité des points** : Les points sont-ils **communs à toute la ville** (dépensables chez n'importe quel partenaire) ou **cloisonnés par commerce** ?
* **Hypothèse préconisée par la MOE** : Système de points unifiés au niveau de la ville, cumulables aussi bien via le Click & Collect qu'en magasin physique via un QR Code usager flashé par l'application commerçant.

### Q3.2 — Utilisation des Points & Chambre de Compensation (Clearing)
* **Contexte** : Un client peut utiliser ses points pour obtenir des cadeaux chez les commerçants ou du temps de stationnement.
* **Questions** :
  1. Qui définit le catalogue des cadeaux ? Chaque commerçant choisit-il ses propres récompenses et le nombre de points associés, ou l'association des commerçants gère-t-elle un catalogue standard ?
  2. **Mécanisme financier de compensation** : Si un client gagne 100 points chez le boucher et les utilise pour obtenir un cadeau chez le fleuriste, **qui rembourse le fleuriste** ? Y a-t-il une caisse commune de l'association qui redistribue la contre-valeur monétaire des points ?
  3. Quelle est la durée de validité des points de fidélité (ex: expiration glissante à 12 mois sans achat) ?
* **Hypothèse préconisée par la MOE** : Caisse de compensation gérée par l'association des commerçants avec valorisation monétaire fixe du point (ex: 1 pt = 0,05 €) reversée mensuellement aux commerçants émetteurs de cadeaux.

### Q3.3 — Règles d'Éligibilité et Rétention du Statut VFP
* **Contexte** : Le statut VFP offre des privilèges et sert de levier de réactivation marketing pour Marius.
* **Questions** :
  1. Quels sont les **critères précis d'obtention du statut VFP** ?
     * Un montant cumulé de dépenses mensuel (ex: > 150 € / mois) ?
     * Une fréquence d'achat minimale (ex: au moins 4 commandes par mois) ?
     * Une exigence de **mixité commerciale** (ex: avoir acheté dans au moins 3 commerces différents du centre-ville, pour favoriser la redynamisation collective) ?
  2. Quels sont les **avantages concrets** accordés à un VFP (remise permanente, files prioritaires click & collect, gratuité étendue de stationnement, invitations ventes privées) ?
  3. **Cycle de vie & Rétrogradation** :
     * À quel moment le statut est-il recalculé (en temps réel, à chaque fin de mois) ?
     * Quelle est la durée du préavis avant perte du statut (ex: alerte à J-15 puis J-7) ?
* **Hypothèse préconisée par la MOE** : Statut accordé sur une double condition (fréquence de 3 visites/mois + au moins 2 commerces distincts) ; recalcul mensuel avec période de grâce de 30 jours et notifications de relance personnalisées opérées par Marius.

---

## 4. Partenariat Municipal : Stationnement & « Citoyen Numérique »

### Q4.1 — Interopérabilité et Conversion "Points -> Stationnement"
* **Contexte** : Les points peuvent être convertis en temps de stationnement urbain.
* **Questions** :
  1. Quel est le mode d'intégration avec les services de stationnement de la ville ?
     * Partenariat avec un opérateur tiers (ex: PayByPhone, Flowbird, EasyPark) via API ?
     * Interfaçage avec les horodateurs de la ville (génération d'un code coupon à 6 chiffres à taper sur l'horodateur) ?
     * Émission d'un titre dématérialisé (QR Code) vérifiable par les Agents de Surveillance de la Voie Publique (ASVP) ?
     * Ou simulation d'une API de voirie municipale pour le cadre du projet ?
  2. **Financement du stationnement** : Qui prend en charge le coût des heures de stationnement offertes (la Mairie à titre gracieux dans sa politique d'attractivité, ou refacturé à l'association des commerçants) ?
* **Hypothèse préconisée par la MOE** : Génération d'un e-ticket / code barre de stationnement avec API partenaire simulée (mock RESTful documenté en OpenAPI) ; prise en charge budgétaire par la régie municipale du stationnement.

### Q4.2 — Rôle du Service Municipal « Citoyen Numérique »
* **Contexte** : Marius peut envoyer des offres à la demande de ce service communal.
* **Questions** :
  1. Le service « Citoyen Numérique » dispose-t-il d'un **accès back-office dédié** dans l'application, ou leurs demandes passent-elles exclusivement par l'administrateur ShopLoc (Marius) ?
  2. La mairie a-t-elle la possibilité de co-financer des campagnes promotionnelles (ex: « Chèque rentrée centre-ville » de 10 € offert à tous les administrés) ?
  3. Quels sont les indicateurs de reporting que la ville exige (taux de fréquentation du centre, part des usagers locaux vs périurbains, baisse du taux de vacance commerciale) ?
* **Hypothèse préconisée par la MOE** : Accès "Collectivité / Observatoire Économique" dédié en lecture seule sur les statistiques macro, avec module de soumission de campagnes d'intérêt public soumises à validation par l'admin ShopLoc.

---

## 5. Ergonomie, Inclusion & Spécificités Personas

### Q5.1 — Accessibilité Senior (Pierre, 74 ans)
* **Contexte** : Pierre représente la population senior de centre-ville, potentiellement moins à l'aise avec les démarches numériques complexes.
* **Questions** :
  1. Pierre doit-il obligatoirement posséder un smartphone ou un ordinateur pour bénéficier de ShopLoc ?
  2. Envisagez-vous la mise à disposition d'un **support physique** (carte de fidélité plastique avec code-barres / QR Code imprimable au format papier) permettant à Pierre de cumuler et dépenser ses points directement en caisse sans manipuler d'application ?
  3. Quelles normes d'accessibilité UX/UI devons-nous respecter (RGAA niveau AA, contrastes renforcés, typographies agrandies, validation vocale) ?
* **Hypothèse préconisée par la MOE** : Double interface : web/mobile ultra-accessible conforme RGAA AA, complétée par une fonctionnalité "Carte physique imprimable" avec QR Code réutilisable chez les commerçants.

### Q5.2 — Espace Commerçant & Gestion des Stocks (Suzanne, 22 ans)
* **Contexte** : Suzanne gère sa boutique de prêt-à-porter ou de commerce de proximité et a des contraintes opérationnelles fortes.
* **Questions** :
  1. **Gestion de catalogue** : La saisie des articles et des stocks se fait-elle uniquement à la main dans le back-office commerçant, ou devons-nous prévoir des imports de masse (fichiers CSV/Excel) voire des connecteurs d'API avec des caisses informatisées existantes ?
  2. **Alertes de rupture** : Quel est le canal attendu pour les alertes de stock critique (email immédiat, push web/mobile, SMS) et le seuil d'alerte est-il configurable article par article ?
  3. Suzanne peut-elle définir des délais de préparation personnalisés (ex: 30 minutes pour une baguette, 24 heures pour un gâteau sur commande) ?
* **Hypothèse préconisée par la MOE** : Interface web intuitive de saisie + import CSV de catalogues ; alertes push et email paramétrables avec seuil d'alerte personnalisable ; gestion de créneaux de préparation spécifiques par article.

---

## 6. Administration, Big Data & Conformité Légale (Marius, 27 ans)

### Q6.1 — Profilage, Relances & Sondages
* **Contexte** : Marius analyse les habitudes de consommation pour cibler des offres et lancer des sondages.
* **Questions** :
  1. **Canaux de diffusion** : Par quels canaux Marius diffuse-t-il les offres et sondages (Push notifications, e-mails, SMS, bannières in-app) ?
  2. **Moteur de segmentation** : Quels sont les filtres de ciblage métier indispensables (par fréquence d'achat, commerces favoris, statut VFP, code postal, panier moyen) ?
  3. Les sondages de satisfaction permettent-ils d'attribuer des points bonus de fidélité pour encourager la participation citoyenne ?
* **Hypothèse préconisée par la MOE** : Ciblage multi-critères avec attribution optionnelle de points bonus (ex: +20 pts pour un sondage complété) ; diffusion multi-canale in-app et par email.

### Q6.2 — Conformité RGPD & Respect de la Vie Privée
* **Contexte** : Le sujet souligne explicitement le « respect de la vie privée » comme propriété critique d'évaluation.
* **Questions** :
  1. Quel est le degré de détail des historiques d'achat consultables par Marius et par les commerçants ?
     * Marius voit-il les paniers détaillés nominatifs, ou uniquement des métriques agrégées et pseudonymisées ?
     * Un commerçant peut-il voir les achats d'un client réalisés chez d'autres commerçants concurrents ? (Clôture stricte d'étanchéité des données)
  2. Quelle est la politique d'opt-in requise pour la géolocalisation et le profilage marketing ?
* **Hypothèse préconisée par la MOE** : Cloisonnement strict (un commerçant ne voit que ses propres ventes) ; pseudonymisation des paniers pour l'administrateur ShopLoc ; conformité RGPD stricte avec recueil de consentements granulaires et registre de traitement intégré.

---

## 7. Cadrage Technique, Volumétrie & Exigences Non-Fonctionnelles

### Q7.1 — Dimensionnement et Volumétrie Attendue
* **Contexte** : Nécessaire pour estimer les coûts d'infrastructure, le choix du moteur SQL et les serveurs d'hébergement pour le rendu R1.
* **Questions** :
  1. Pour la phase d'expérimentation (pilote printemps 2027), quelles sont les cibles dimensionnantes :
     * Nombre de commerces partenaires pilotes (ex: 30 à 100) ?
     * Nombre d'utilisateurs actifs mensuels (ex: 5 000 à 20 000) ?
     * Volume de requêtes / commandes en pic (ex: samedi après-midi ou fêtes de fin d'année) ?
* **Hypothèse préconisée par la MOE** : Dimensionnement initial calibré pour une ville moyenne : 10 000 utilisateurs actifs, 80 commerçants, pics à 50 commandes/heure, architecture conteneurisée auto-scalable.

### Q7.2 — Enveloppe Budgétaire Cible
* **Contexte** : Le livrable R1 exige une proposition tarifaire détaillée (conception, réalisation, hébergement et maintenance sur 18 mois).
* **Questions** :
  1. La MOA a-t-elle fixé une enveloppe indicative (budget plafond ou fourchette cible d'investissement) pour la réalisation de ce marché ?
* **Hypothèse préconisée par la MOE** : Grille tarifaire basée sur un forfait de développement agile (TJM junior consultant) complété par un abonnement d'exploitation/MCO (Maintien en Conditions Opérationnelles) mensuel forfaitaire.

---

## Synthèse du Plan de Remise du 07/09/2026

* **Modalité de transmission** : Email officiel adressé à `laurence.duchien@univ-lille.fr` et `anne.etien@univ-lille.fr` avec l'objet formaté :  
  `[GLOP] Questionnement préliminaire de cadrage - Équipe MiageShopLoc`
* **Pièce jointe** : Le présent document converti en PDF normalisé selon la charte du projet.
