# 1. Cadrage Stratégique, Expression du Besoin & Méthode APTE

---

## Informations de Cadrage de la Section

| Métadonnée | Valeur |
|---|---|
| **Livrable Cible** | Cahier des Charges ShopLoc (Livrable R1) |
| **Identifiant Section** | `SEC-01` (Étape 01 du Pipeline de Fabrication) |
| **Référence Documentaire** | `GLOP-2026-R1-SEC-01-v1.0` |
| **Statut de Validation** | Version 1.0 — Conforme aux arbitrages MOA (ADR-004 à ADR-013) |
| **Norme d'Ingénierie** | Analyse Fonctionnelle du Besoin — Norme AFNOR NF X 50-151 |
| **Postulat Architectural** | Monolithe Modulaire Multi-Tenant à souveraineté territoriale |

---

## 1.1. Positionnement Stratégique & Double Finalité du Système

La plateforme ShopLoc est un dispositif numérique d'intérêt territorial conçu pour revitaliser le commerce physique de proximité tout en renforçant l'attractivité et la cohésion urbaine des collectivités partenaires. 

Le système répond à une **double finalité indissociable**, garantissant l'équilibre des intérêts entre les acteurs économiques de proximité et les décideurs institutionnels :

1. **Une finalité économique et commerciale** : Réamorcer le flux de chalands dans les boutiques physiques de centre-ville, sécuriser les commandes locales via un service de Click & Collect mutualisé, et fidéliser la clientèle de proximité à l'aide d'un double moteur de récompenses non prédateur.
2. **Une finalité politique et citoyenne** : Doter les municipalités d'un levier d'action publique souverain pour inciter aux comportements d'achat éco-responsables et de mobilité durable (transports en commun, stationnement réglementé), tout en restaurant le lien social au sein des quartiers.

Contrairement aux solutions de commerce en ligne délocalisées qui extraient la valeur des territoires par des commissions disproportionnées et accentuent la désertification urbaine, ShopLoc sanctuarise le tissu commercial local en subordonnant chaque acte numérique à un passage physique dans le commerce.

---

## 1.2. Matrice de Positionnement Concurrentiel (2 Axes Stratégiques)

Pour situer formellement la rupture apportée par ShopLoc au sein de l'écosystème du commerce et des plateformes urbaines, le modèle est positionné sur deux axes structurants :
* **Axe horizontal (Ancrage spatial et logistique)** : Mesure le caractère physique et pédestre du flux généré en centre-ville, en opposition aux livraisons motorisées délocalisées génératrices d'externalités négatives (congestion, émissions de gaz à effet de serre).
* **Axe vertical (Modèle économique et souveraineté)** : Mesure l'accessibilité citoyenne et la préservation de la valeur locale (service public et gratuité usager), en opposition aux prélèvements de commissions financières sur le chiffre d'affaires des commerçants.

<div class="diagram-container" style="margin: 16pt 0; text-align: center;">
  <h3 style="font-size: 10pt; color: #0F2A4A; margin-bottom: 8pt; text-transform: uppercase;">
    Figure 1.1 — Matrice de Positionnement Stratégique (2 Axes)
  </h3>

  <svg viewBox="0 0 650 380" width="100%" height="380" style="font-family: 'Inter', sans-serif;">
    <!-- Arriere-plan 4 quadrants -->
    <rect x="50" y="30" width="270" height="150" fill="#F8FAFC" />
    <rect x="330" y="30" width="270" height="150" fill="#F0FDF4" /> <!-- Quadrant cible ShopLoc -->
    <rect x="50" y="190" width="270" height="150" fill="#FEF2F2" />
    <rect x="330" y="190" width="270" height="150" fill="#FFFBEB" />

    <!-- Axe Horizontal (X) : Ancrage territorial -->
    <line x1="40" y1="185" x2="610" y2="185" stroke="#0F2A4A" stroke-width="2" />
    <polygon points="615,185 605,180 605,190" fill="#0F2A4A" />
    <text x="50" y="175" font-size="9" fill="#64748B">Délocalisé / Livraison motorisée</text>
    <text x="600" y="175" text-anchor="end" font-size="9" font-weight="bold" fill="#0F2A4A">Ancrage physique / Flux piétonnier en centre-ville (+)</text>

    <!-- Axe Vertical (Y) : Modèle économique -->
    <line x1="325" y1="360" x2="325" y2="20" stroke="#0F2A4A" stroke-width="2" />
    <polygon points="325,15 320,25 330,25" fill="#0F2A4A" />
    <text x="335" y="25" font-size="9" font-weight="bold" fill="#0F2A4A">Gratuité citoyenne & Souveraineté publique (+)</text>
    <text x="335" y="355" font-size="9" fill="#64748B">Commissions prédatrices sur CA marchand (-)</text>

    <!-- POSITIONNEMENT DES ACTEURS -->

    <!-- Acteur 1 : ShopLoc (Cible idéale : Haut Droite) -->
    <rect x="420" y="65" width="160" height="60" rx="6" fill="#0F2A4A" stroke="#166534" stroke-width="2" />
    <text x="500" y="90" text-anchor="middle" font-size="12" font-weight="bold" fill="#FFFFFF">Plateforme ShopLoc</text>
    <text x="500" y="108" text-anchor="middle" font-size="8" fill="#86EFAC">Flux physique & Souveraineté</text>

    <!-- Acteur 2 : Géants du E-Commerce (Bas Gauche : Amazon, etc.) -->
    <rect x="70" y="240" width="150" height="50" rx="4" fill="#FFFFFF" stroke="#991B1B" stroke-width="1.5" />
    <text x="145" y="262" text-anchor="middle" font-size="10" font-weight="bold" fill="#991B1B">Marketplaces Globales</text>
    <text x="145" y="278" text-anchor="middle" font-size="7.5" fill="#64748B">Livraison domicile & Commissions</text>

    <!-- Acteur 3 : Plateformes de livraison express (Bas Droite) -->
    <rect x="360" y="250" width="150" height="50" rx="4" fill="#FFFFFF" stroke="#B45309" stroke-width="1.2" />
    <text x="435" y="272" text-anchor="middle" font-size="10" font-weight="bold" fill="#B45309">Plateformes de Livraison</text>
    <text x="435" y="288" text-anchor="middle" font-size="7.5" fill="#64748B">Commerces locaux mais forte commission</text>

    <!-- Acteur 4 : Solutions de cartes de fidélité privées isolées (Haut Gauche) -->
    <rect x="90" y="75" width="150" height="50" rx="4" fill="#FFFFFF" stroke="#64748B" stroke-width="1.2" />
    <text x="165" y="97" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#334155">Programmes Privés Isolés</text>
    <text x="165" y="112" text-anchor="middle" font-size="7.5" fill="#64748B">Sans mutualisation territoriale</text>
  </svg>
</div>

L'analyse des quadrants met en exergue quatre dynamiques distinctes :
1. **Marketplaces Globales (Amazon, Temu)** : Modèle prédateur combinant une délocalisation totale des flux et une captation marchande aggressive (15% à 30% de commission sur les ventes). Ce quadrant accélère le déclin des commerces de centre-ville.
2. **Plateformes de Livraison Rapide (Deliveroo, UberEats)** : Bien qu'adossées à des commerces de proximité, ces solutions appliquent des frais de commission écrasants (jusqu'à 30%) et externalisent les livraisons par des flottes motorisées ou précaires, sans générer de fréquentation en boutique.
3. **Programmes Privés Isolés (Cartes de fidélité propriétaires)** : Solutions fragmentées, sans synergie inter-commerces ni interconnexion avec les politiques publiques de mobilité urbaine.
4. **Plateforme ShopLoc (Quadrant d'Excellence Territoriale)** : Positionnement unique alliant un ancrage physique exclusif en boutique (Click & Collect pédestre obligatoire) et un modèle vertueux fondé sur la gratuité citoyenne et la souveraineté territoriale (financement associatif et municipal sans ponction sur les transactions).

---

## 1.3. Formalisation Canonique du Besoin (Méthode APTE — AFNOR NF X 50-151)

Conformément à la norme française d'analyse fonctionnelle de la valeur (AFNOR NF X 50-151), l'expression du besoin de ShopLoc est décomposée en deux représentations canoniques : la **Bête à Cornes** (saisie de la finalité première) et le **Diagramme Pieuvre** (graphe des interactions avec l'environnement extérieur).

### 1.3.1. Énonciation du Besoin Fondamental (La Bête à Cornes)

La finalité d'existence du système ShopLoc est formalisée par la réponse aux trois questions canoniques :
* **À qui le produit rend-il service ?** Aux citoyens acheteurs, aux commerçants indépendants de centre-ville et aux collectivités territoriales partenaires.
* **Sur quoi agit-il ?** Sur les flux d'achats physiques en boutique et sur les comportements de mobilité urbaine éco-responsable.
* **Dans quel but ?** Revitaliser l'économie marchande de centre-ville, consolider le lien social de proximité et valoriser la fidélité citoyenne sans prédation financière.

<div class="diagram-container" style="margin: 16pt 0; text-align: center;">
  <h3 style="font-size: 10pt; color: #0F2A4A; margin-bottom: 8pt; text-transform: uppercase;">
    Figure 1.2 — Énonciation du Besoin Canonique (Bête à Cornes APTE)
  </h3>
  
  <svg viewBox="0 0 700 220" width="100%" height="220" style="font-family: 'Inter', sans-serif;">
    <!-- Bulle 1 : À qui rend-il service ? -->
    <rect x="30" y="20" width="200" height="60" rx="6" fill="#EFF6FF" stroke="#0F2A4A" stroke-width="1.5" />
    <text x="130" y="42" text-anchor="middle" font-size="11" font-weight="bold" fill="#0F2A4A">À qui rend-il service ?</text>
    <text x="130" y="60" text-anchor="middle" font-size="9.5" fill="#334155">Citoyens, Commerçants & Collectivité</text>

    <!-- Bulle 2 : Sur quoi agit-il ? -->
    <rect x="470" y="20" width="200" height="60" rx="6" fill="#EFF6FF" stroke="#0F2A4A" stroke-width="1.5" />
    <text x="570" y="42" text-anchor="middle" font-size="11" font-weight="bold" fill="#0F2A4A">Sur quoi agit-il ?</text>
    <text x="570" y="60" text-anchor="middle" font-size="9.5" fill="#334155">Flux d achats physiques & Mobilité</text>

    <!-- Centre : Système ShopLoc -->
    <rect x="250" y="80" width="200" height="50" rx="8" fill="#0F2A4A" stroke="#0F2A4A" stroke-width="2" />
    <text x="350" y="105" text-anchor="middle" font-size="12" font-weight="bold" fill="#FFFFFF">Plateforme ShopLoc</text>
    <text x="350" y="120" text-anchor="middle" font-size="8.5" fill="#CBD5E1">Système Multi-Tenant Territorial</text>

    <!-- Bulle 3 : Dans quel but ? -->
    <rect x="160" y="160" width="380" height="50" rx="6" fill="#F0FDF4" stroke="#166534" stroke-width="1.5" />
    <text x="350" y="180" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">Dans quel but ?</text>
    <text x="350" y="198" text-anchor="middle" font-size="9" fill="#334155">Revitaliser l économie de centre-ville et valoriser la fidélité citoyenne</text>

    <!-- Lignes de liaison -->
    <line x1="130" y1="80" x2="250" y2="105" stroke="#0F2A4A" stroke-width="1.5" stroke-dasharray="3,3" />
    <line x1="570" y1="80" x2="450" y2="105" stroke="#0F2A4A" stroke-width="1.5" stroke-dasharray="3,3" />
    <line x1="350" y1="130" x2="350" y2="160" stroke="#166534" stroke-width="1.5" />
  </svg>
</div>

### 1.3.2. Graphe des Interactions & Contraintes (Le Diagramme Pieuvre)

Le système ShopLoc est en interaction constante avec cinq entités majeures de son milieu extérieur. Ces relations se traduisent par deux Fonctions Principales (`FP`) et quatre Fonctions Contraintes (`FC`).

<div class="diagram-container" style="margin: 16pt 0; text-align: center;">
  <h3 style="font-size: 10pt; color: #0F2A4A; margin-bottom: 8pt; text-transform: uppercase;">
    Figure 1.3 — Graphe des Fonctions & Contraintes (Diagramme Pieuvre APTE)
  </h3>

  <svg viewBox="0 0 700 320" width="100%" height="320" style="font-family: 'Inter', sans-serif;">
    <!-- Acteur 1 : Citoyen Acheteur (Haut Gauche) -->
    <circle cx="120" cy="60" r="45" fill="#F8FAFC" stroke="#0F2A4A" stroke-width="1.5" />
    <text x="120" y="58" text-anchor="middle" font-size="10" font-weight="bold" fill="#0F2A4A">Citoyen</text>
    <text x="120" y="72" text-anchor="middle" font-size="8.5" fill="#64748B">Acheteur</text>

    <!-- Acteur 2 : Commerçant Partenaire (Haut Droite) -->
    <circle cx="580" cy="60" r="45" fill="#F8FAFC" stroke="#0F2A4A" stroke-width="1.5" />
    <text x="580" y="58" text-anchor="middle" font-size="10" font-weight="bold" fill="#0F2A4A">Commerçant</text>
    <text x="580" y="72" text-anchor="middle" font-size="8.5" fill="#64748B">Boutique</text>

    <!-- Acteur 3 : Réglementation RGPD & Éthique (Gauche) -->
    <circle cx="80" cy="180" r="40" fill="#FEF2F2" stroke="#991B1B" stroke-width="1.5" />
    <text x="80" y="178" text-anchor="middle" font-size="9" font-weight="bold" fill="#991B1B">RGPD</text>
    <text x="80" y="192" text-anchor="middle" font-size="8" fill="#64748B">Vie Privée</text>

    <!-- Acteur 4 : Collectivité & Mairie (Bas Centre) -->
    <circle cx="350" cy="275" r="40" fill="#F0FDF4" stroke="#166534" stroke-width="1.5" />
    <text x="350" y="272" text-anchor="middle" font-size="9" font-weight="bold" fill="#166534">Mairie</text>
    <text x="350" y="286" text-anchor="middle" font-size="8" fill="#64748B">Subvention</text>

    <!-- Acteur 5 : Systèmes Partenaires Mobilités (Droite) -->
    <circle cx="620" cy="180" r="40" fill="#EFF6FF" stroke="#1E40AF" stroke-width="1.5" />
    <text x="620" y="178" text-anchor="middle" font-size="9" font-weight="bold" fill="#1E40AF">Mobilité</text>
    <text x="620" y="192" text-anchor="middle" font-size="8" fill="#64748B">Bus / Parking</text>

    <!-- Centre : ShopLoc -->
    <rect x="270" y="110" width="160" height="65" rx="8" fill="#0F2A4A" stroke="#0F2A4A" stroke-width="2" />
    <text x="350" y="140" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">ShopLoc</text>
    <text x="350" y="156" text-anchor="middle" font-size="8.5" fill="#CBD5E1">Cœur Applicatif</text>

    <!-- Ligne FP1 : Traverse Citoyen -> ShopLoc -> Commerçant -->
    <path d="M 165 60 Q 350 20 535 60" fill="none" stroke="#166534" stroke-width="2.5" />
    <rect x="300" y="18" width="100" height="20" rx="3" fill="#DCFCE7" stroke="#166534" stroke-width="1" />
    <text x="350" y="32" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#166534">FP1 : Click & Collect + VFP</text>

    <!-- Lignes FC (Contraintes) -->
    <line x1="120" y1="180" x2="270" y2="150" stroke="#991B1B" stroke-width="1.5" />
    <text x="180" y="160" font-size="8" font-weight="bold" fill="#991B1B">FC1 (RGPD)</text>

    <line x1="350" y1="235" x2="350" y2="175" stroke="#166534" stroke-width="1.5" />
    <text x="360" y="210" font-size="8" font-weight="bold" fill="#166534">FC2 (Finances/Convention)</text>

    <line x1="580" y1="180" x2="430" y2="150" stroke="#1E40AF" stroke-width="1.5" />
    <text x="470" y="160" font-size="8" font-weight="bold" fill="#1E40AF">FC3 (Mocks API)</text>

    <!-- FC4 : Accessibilité Senior Pierre -->
    <line x1="150" y1="95" x2="280" y2="120" stroke="#B45309" stroke-width="1.5" stroke-dasharray="4,2" />
    <text x="175" y="112" font-size="8" font-weight="bold" fill="#B45309">FC4 (RGAA Senior)</text>
  </svg>
</div>

### 1.3.3. Caractérisation Formelle des Fonctions du Système

Chaque fonction identifiée est documentée selon les critères de qualification de la norme AFNOR NF X 50-151, précisant ses grandeurs d'appréciation, son niveau d'exigence et son degré de flexibilité :
* **F0 (Nulle)** : Exigence absolue, impérative et non négociable.
* **F1 (Faible)** : Tolérance quantitative strictement encadrée.
* **F2 (Moyenne)** : Ajustement négociable selon les retours d'usage.

| Code | Type | Désignation de la Fonction | Critère d'Appréciation | Niveau d'Exigence | Flexibilité |
|---|---|---|---|---|---|
| **FP1** | Principale | Permettre la commande en Click & Collect multi-commerces et la valorisation de la fidélité marchande | Délai de confirmation commande / Validité des points | Confirmation en moins de 1 minute / Validité 12 mois glissants | `F0` |
| **FP2** | Principale | Rémunérer la régularité de fréquentation physique par des avantages de mobilité institutionnelle (VFP) | Seuil d'éligibilité et vitesse de déblocage | 10 passages sur 15 jours glissants / Ticket bus ou 20 min parking | `F0` |
| **FC1** | Contrainte | Respecter la confidentialité de la vie privée et les directives souveraines du RGPD | Degré d'anonymisation des flux d'achat | Zéro transmission de données nominatives aux mairies et commerçants tiers | `F0` |
| **FC2** | Contrainte | Assurer une inclusion numérique universelle et l'accessibilité aux usagers seniors | Conformité RGAA niveau AA / Support physique | Ratios de contraste >= 4.5:1, carte papier QR sans smartphone requis | `F0` |
| **FC3** | Contrainte | Garantir la frugalité économique du coût d'exploitation (Run) pour les collectivités | Coût d'hébergement serveur mensuel par commune | TCO d'infrastructure < 120 euros par mois en configuration socle | `F1` |
| **FC4** | Contrainte | Assurer l'étanchéité technique et l'interopérabilité sans dépendance externe bloquante | Taux de disponibilité et temps de réponse des mocks | 99.9% de disponibilité simulée / Latence d'API simulée < 100 ms | `F0` |

---

## 1.4. Pyramide des Besoins Territoriaux

L'ingénierie des besoins de ShopLoc se structure selon une hiérarchie à trois étages interdépendants :

```text
               /\
              /  \
             /    \
            /      \
           / Strat. \      -> Niveau 1 : Vitalité économique & Attractivité de la cité
          /----------\
         /  Tactique  \    -> Niveau 2 : Convention Tripartite (Mairie / Assoc / ShopLoc)
        /--------------\
       / Opérationnel   \  -> Niveau 3 : Click & Collect boutique, Caisse express & VFP
      /------------------\
```

### Niveau 1 : Besoins Stratégiques (Politique Publique & Souveraineté)
* **Sauvegarde du tissu de centre-ville** : Lutter activement contre la vacance commerciale et le mitage urbain par la captation des flux d'achats alimentaires et d'équipement au cœur des quartiers.
* **Transition vers les mobilités douces** : Réduire l'impact carbone des déplacements en couplant la récompense d'achat local à l'utilisation des transports collectifs urbains (réseau de bus municipal) et à la rotation des véhicules sur le stationnement de courte durée (dépose-minute et 20 minutes gratuites).
* **Souveraineté des données communales** : Offrir aux élus et directeurs généraux des services (DGS) un observatoire économique territorial anonymisé sans dépendre d'acteurs privés monopolistiques.

### Niveau 2 : Besoins Tactiques (Gouvernance & Convention Tripartite)
* **Conventionnement Tripartite Solide** : La relation contractuelle lie la Municipalité, l'Association des Commerçants et l'éditeur ShopLoc. La Mairie alloue une subvention de modernisation commerciale à l'Association, laquelle souscrit l'abonnement SaaS à la plateforme et fédère ses adhérents (ADR-004).
* **Péréquation financière et confiance** : L'Association valide l'intégration des nouveaux commerces adhérents et veille à la déontologie locale, déchargeant ainsi la collectivité de la gestion directe des commerçants individuels.
* **Pérennité du modèle économique** : Financement mutualisé garantissant l'absence de commission sur les ventes des commerçants, préservant intégralement leurs marges déjà réduites.

### Niveau 3 : Besoins Opérationnels (Parcours Utilisateurs & Quotidien en Boutique)
* **Expérience Click & Collect sans friction** : Regroupement d'achats multi-boutiques en une commande unique, assorti d'un itinéraire de retrait piétonnier optimisé selon les horaires d'ouverture réels des commerçants.
* **Enregistrement caisse express** : Scan rapide d'un QR code client lors du passage physique (sur smartphone ou carte physique papier) permettant l'attribution simultanée des points fidélité de la boutique et l'incrémentation du compteur de passage VFP territorial.
* **Gestion des aléas de stock et no-show** : Mise à jour manuelle agile du catalogue par le commerçant et protection financière de ce dernier en cas de non-retrait d'une commande préparée (la marchandise périssable reste acquise au commerçant).

---

## 1.5. Périmètre Strict & Frontières du Système

Afin de prévenir tout phénomène de dérive de périmètre (*feature creep*) et de préserver l'impact écologique du projet, les frontières opérationnelles de ShopLoc sont strictement délimitées :

### 1.5.1. Ce qui est Strictement Inclus (In-Scope)
* **Retrait physique obligatoire en boutique (Click & Collect pédestre)** : L'usager se rend personnellement (ou via un tiers mandaté en V2/V3) au comptoir du commerçant.
* **Double mécanique de fidélité découplée** :
  * Volet Marchand : Points convertibles en réductions ou cadeaux au sein de la boutique émettrice uniquement (validité 12 mois).
  * Volet Territorial : Statut Very Faithful Person (VFP) basé sur la régularité physique (seuil de 10 passages sur 15 jours glissants) ouvrant droit à des avantages de mobilité (bus ou stationnement).
* **Panier multi-commerces** : Validation et paiement groupé avec ordonnancement du circuit piétonnier de retrait.
* **Accessibilité physique papier** : Génération et prise en charge intégrale de cartes de fidélité cartonnées avec QR code unique pour les populations non équipées d'écrans tactiles.
* **Multi-tenancy étanche par commune** : Cloisonnement strict des bases et des budgets.
* **Mocks de services tiers** : Simulation documentée des passerelles bancaires et des systèmes de voirie/mobilité.

### 1.5.2. Ce qui est Strictement Exclu (Out-of-Scope)
* **Interdiction formelle de la livraison à domicile** : Aucune logistique de livraison motorisée ni recours à des flottes de coursiers n'est admis dans le périmètre du système. Tout flux doit converger physiquement vers la boutique.
* **Absence de pont de fidélité inter-boutiques marchand** : Les points acquis chez un boucher ne sont en aucun cas transférables ni utilisables chez un fleuriste, protégeant ainsi l'équité comptable entre commerçants indépendants.
* **Interdiction de l'inter-opérabilité inter-villes non cloisonnée** : Les points et statuts VFP acquis dans la ville A ne peuvent être dépensés dans la ville B. Les budgets publics communaux demeurent strictement étanches.
* **Absence d'écrans ou de terminaux dédiés pour les agents de voirie municipale** : Les agents ASVP de terrain utilisent leur équipement professionnel préexistant pour vérifier la validité des plaques d'immatriculation bénéficiant des 20 minutes offertes, via un point d'API mocké léger, sans création d'une application dédiée lourde.

---

## 1.6. Scalabilité Territoriale & Modularité Multi-Tenant

Le socle technique de ShopLoc est nativement multi-tenant et conçu pour s'adapter à une diversité d'échelles démographiques : du bourg rural regroupant 15 commerces à la métropole régionale fédérant des centaines d'enseignes.

### Principes d'Isolation & Cloisonnement Territorial
1. **Cloisonnement Logique Strict des Données** : Chaque entité manipulée en base de données (commerces, transactions, soldes VFP, catalogues) est rattachée à un identifiant unique de collectivité territoriale (`tenant_id`). Aucune requête ne peut opérer sans filtrage automatique sur cet identifiant.
2. **Étanchéité des Budgets Publics** : Le financement alloué par la commune A pour ses avantages de mobilité douce (tickets de transport, places de stationnement) est sanctuarisé. Un usager effectuant des achats dans la ville A ne peut solliciter un avantage pris en charge par la ville B.
3. **Modularité par Briques Activables (*Feature Flags*)** : Chaque collectivité dispose de la faculté d'activer ou de masquer les modules de services selon son infrastructure locale :
   * *Module Mobilité / Bus* : Activé uniquement si la commune dispose d'un réseau de transport conventionné.
   * *Module Stationnement Voirie* : Activé uniquement si la commune dispose de zones payantes régulées.
   * *Module Carte Physique Papier* : Activé obligatoirement pour garantir l'inclusion républicaine.

---

## 1.7. Justification d'Ingénierie : Monolithe Modulaire Multi-Tenant vs Microservices

Le dimensionnement architectural d'un projet de cette envergure constitue un arbitrage structurant consigné dans l'**ADR-012**. Le choix s'est porté sur un **Monolithe Modulaire Multi-Tenant** plutôt que sur une constellation de microservices distribués.

| Critère d'Ingénierie | Monolithe Modulaire Multi-Tenant (Choix Retenu) | Architecture Microservices Distribués (Rejetée) |
|---|---|---|
| **Coût d'Exploitation Mensuel (Run)** | Extrêmement faible (< 100 à 150 euros/mois pour 10 villes). Socle mutualisé sur un conteneur unique et base PostgreSQL optimisée. | Élevé (> 600 à 1 200 euros/mois). Nécessite orchestrateur Kubernetes, registres d'images et instances multiples. |
| **Consistance Transactionnelle** | Intégrité ACID native. Atomicité parfaite sur le panier multi-commerces et le débit de points sans risque d'incohérence. | Éventuelle / Sagas complexes. Risque de transactions partielles en cas de coupure réseau entre services (Panier / Paiement / Stock). |
| **Complexité Déploiement & Exploitation** | Pipeline CI/CD direct, conteneurisation Docker standard, surveillance et logs unifiés. | Surveillance distribuée complexe (OpenTelemetry, tracing, maillage de services, latence réseau inter-pods). |
| **Maintenabilité Équipe** | Codebase claire, couplage faible entre modules métiers grâce à des interfaces TypeScript strictes. | Explosion du nombre de dépôts, duplication de code transverse, complexité de gestion des versions d'APIs. |
| **Adéquation au Besoin Métier** | Idéale pour une marketplace territoriale souveraine, frugale et résiliente. | Sur-ingénierie manifeste (*over-engineering*) disproportionnée par rapport aux volumes réels de requêtes. |

Le choix du Monolithe Modulaire garantit une gouvernance technique saine, élimine les latences réseau inutiles et offre un coût total de possession (TCO) parfaitement justifiable auprès des commissions d'appel d'offres des collectivités publiques.

---

## 1.8. Matrice des Indicateurs Clés de Performance (KPIs) à Double Échelle

Afin de mesurer l'efficacité concrète du dispositif et d'alimenter les tableaux de bord décisionnels, le pilotage de la performance s'articule à deux niveaux géographiques étanches :

### 1.8.1. Indicateurs Locaux (Échelle de la Collectivité / Tableau de Bord Marius)
* **Taux d'Usagers Réguliers VFP (`KPI-LOC-01`)** : Pourcentage d'acheteurs actifs atteignant le seuil de 10 passages sur 15 jours glissants (objectif cible : > 18% des inscrits).
* **Fréquence Moyenne de Visite (`KPI-LOC-02`)** : Nombre moyen de passages physiques par citoyen actif par semaine (objectif cible : >= 2.5 passages/semaine).
* **Taux d'Adhésion Commerciale (`KPI-LOC-03`)** : Ratio de commerçants indépendants conventionnés par rapport au tissu marchand total de la commune (objectif cible : > 40% à 12 mois).
* **Taux d'Usage des Avantages Mobilité (`KPI-LOC-04`)** : Répartition de conversion entre tickets de transport et stationnement court, mesurant l'incitation effective aux mobilités douces.

### 1.8.2. Indicateurs Globaux (Échelle Macro / Plateforme Nationale ShopLoc)
* **Parc de Collectivités Déployées (`KPI-MAC-01`)** : Nombre total de communes clientes sous convention active.
* **Volume Global d'Achats Locaux Sécurisés (`KPI-MAC-02`)** : Montant total cumulé des commandes Click & Collect injecté dans l'économie de proximité.
* **Indice de Frugalité Énergétique & Coût Serveur par Usager (`KPI-MAC-03`)** : Coût d'infrastructure rapporté au nombre de citoyens actifs mensuels (objectif : < 0.02 euro/usager/an).
* **Taux d'Émissions Carbone Évitées (`KPI-MAC-04`)** : Estimation de l'économie de CO2 issue de la substitution des livraisons motorisées délocalisées par le Click & Collect piétonnier et le recours aux transports urbains.

---

## 1.9. Principe de Gratuité Citoyenne & Dispositif d'Inclusion Universelle

### Gratuité Intégrale pour le Citoyen Final
L'adhésion au programme, le téléchargement de l'application mobile, la consultation des catalogues et la délivrance de la carte physique de fidélité sont **100% gratuites** pour l'ensemble des administrés. Aucun frais d'abonnement, droit d'entrée ou commission de paiement n'est exigé du client final. Cette gratuité absolue constitue le premier facteur d'adhésion de masse indispensable au succès du dispositif.

### Accessibilité Numérique et Inclusion des Publics Non-Connectés
Pour garantir l'accès au service à l'ensemble des citoyens, notamment aux seniors (incarnés par le persona Pierre, 74 ans) ou aux foyers non équipés de smartphones :
* **Carte Physique Papier / PVC avec QR Code Sécurisé** : Délivrée gratuitement par l'association des commerçants ou à l'accueil de la mairie. Ce support matériel permet d'accumuler les points marchands et d'incrémenter le statut VFP en caisse avec la même rapidité qu'une application mobile.
* **Conformité RGAA Niveau AA** : L'interface web et mobile respecte scrupuleusement les critères d'accessibilité (taille des cibles tactiles >= 44x44px, contrastes chromatiques >= 4.5:1, compatibilité avec les technologies d'assistance vocale).
* **Dispositif de Tiers de Confiance & Procuration (Planifié pour V2/V3)** : Pour les personnes à mobilité réduite ou empêchées, le système prévoit la désignation sécurisée d'un proche ou d'un aidant familial habilité à retirer les commandes Click & Collect en boutique au nom du titulaire.

---

## 1.10. Synthèse Exécutive et Articulation avec le Lean Canvas

Conformément à la démarche d'ingénierie par arborescence inversée formalisée dans le Plan Directeur (`PLAN_DIRECTEUR_CAHIER_DES_CHARGES_R1.md`), cette première section établit l'ensemble des fondations stratégiques et fonctionnelles. 

L'artefact de synthèse panoramique — **Le Lean Canvas ShopLoc** — rassemblera en une vue dense sur une page A4 l'intégralité de ces paramètres une fois consolidés par l'étude des personas (Section 02), les flux de processus BPMN (Section 03), le modèle conceptuel de données (Section 04) et l'analyse des coûts complets (Section 09). Ce Lean Canvas sera positionné en première page du document finalisé pour offrir aux évaluateurs une vision synthétique immédiate du modèle.
