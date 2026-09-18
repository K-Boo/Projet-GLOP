# 1. Présentation de l'entreprise Garik

## 1.1. Identité, vision et positionnement partenarial

L'entreprise **Garik** est une jeune société d'ingénierie logicielle créée par une équipe de cinq profils issus de la filière MIAGE de l'Université de Lille. Notre cursus nous apporte une double compétence, technique et méthodologique, adaptée aux besoins concrets du commerce local : d'un côté le développement web, l'architecture logicielle et l'intégration continue, et de l'autre l'analyse des besoins, la modélisation des processus et le suivi des coûts.

Nous répondons aujourd'hui à l'appel d'offres émis pour la conception de la plateforme **ShopLoc**. Ce projet répond à une préoccupation majeure partagée par de nombreuses communes : la perte de vitalité des centres-villes face à l'attractivité des grandes zones commerciales de périphérie et des grandes plateformes internationales de commerce en ligne. Notre vision repose sur la mise à disposition d'un outil numérique souverain, accessible et éthique, conçu pour fédérer les commerçants de proximité et redonner envie aux habitants de consommer au cœur de leur quartier.

Pour garantir l'adhésion immédiate des artisans et commerçants indépendants, nous défendons un positionnement clair et vertueux :
- **Gratuité intégrale pour les usagers citoyens :** Aucun frais d'accès ni surcoût sur les produits n'est appliqué aux habitants, ce qui encourage une adoption rapide et régulière de la plateforme.
- **Zéro commission sur les ventes des commerçants :** Contrairement aux plateformes privées qui ponctionnent une part importante du chiffre d'affaires des commerces de proximité, ShopLoc n'applique aucun prélèvement sur les commandes, préservant ainsi intégralement leurs marges.
- **Financement communal mutualisé :** Le fonctionnement technique du service et la maintenance sont pris en charge par la collectivité locale sous la forme d'un abonnement forfaitaire annuel, au titre de sa politique de soutien au commerce local et d'incitation aux mobilités douces.

Notre équipe met à disposition de la maîtrise d'ouvrage une réelle complémentarité de compétences, présentée dans la section suivante, permettant de couvrir l'ensemble du cycle de vie du projet, du dialogue fonctionnel jusqu'au déploiement opérationnel.

<div style="page-break-after: always;"></div>

# 2. Équipe projet et répartition des rôles

## 2.1. Présentation synthétique des compétences de l'équipe

L'équipe Garik réunit cinq profils complémentaires dont les expériences préalables en entreprise (alternances, stages et projets d'ingénierie) permettent de couvrir les différents aspects du projet ShopLoc :

| Membre de l'équipe | Rôle principal dans le projet | Formation | Atouts majeurs et compétences clés |
|---|---|---|---|
| **Khalil Bouchama** | Responsable Qualité & Déploiement | Master 2 MIAGE, Licence MIAGE, DUT Informatique | Diagnostic et tests chez Alstom Crespin (analyse ferroviaire), développement web full-stack chez Benzz Auto (React, Strapi, PostgreSQL). Rigueur en validation et conteneurisation Docker. |
| **Abdelkader Heddi** | Responsable Communication & Relations MOA | Master 2 MIAGE, Licence MIAGE | Analyse fonctionnelle chez AG2R La Mondiale, animation des rituels d'équipe, rédaction des synthèses et formalisation des besoins. Gestion de projets web collaboratifs. |
| **Gautam Demeulemeester** | Responsable Architecture Back-Office & Données | Master 2 MIAGE, Licence MIAGE | Gestion de projet marketplace et refonte comptable chez Damart, logistique des flux chez Mondial Relay. Solides compétences en modélisation relationnelle SQL et intégrité des stocks. |
| **Rayane Alli** | Spécialiste Outils & Ingénieur Logiciel | Master 2 MIAGE, Licence MIAGE | Conception d'applications de gestion d'inventaire, automatisation des tests et chaînes de compilation. Réalisation des simulateurs légers (bouchons) pour les services partenaires. |
| **Ilyas Ait Ali** | Responsable Architecture Front-Office & Ergonomie | Master 2 MIAGE, Licence MIAGE, L1/L2 Recherche | Développement d'entreprise chez Sopra Steria, traitement d'incidents chez AG2R La Mondiale. Maîtrise des interfaces réactives et forte sensibilisation à l'accessibilité numérique. |

*(Note : Les curricula vitæ complets et détaillés de chaque membre de l'équipe sont joints en annexe du dossier).*

<div style="page-break-after: always;"></div>

## 2.2. Répartition des rôles opérationnels du projet

Pour assurer une organisation claire et efficace, les responsabilités sont réparties entre les cinq membres de l'équipe de façon concrète et opérationnelle :

| Rôle dans le projet | Titulaire désigné | Responsabilités concrètes au sein de l'équipe |
|---|---|---|
| **1. Responsable de la Qualité** | **Khalil Bouchama** | Veille à la cohérence et à la clarté des livrables écrits, organise les relectures de code croisées entre collaborateurs, et s'assure de la présence de tests automatisés pertinents avant toute intégration de nouvelle fonctionnalité. |
| **2. Responsable de la Communication** | **Abdelkader Heddi** | Rédige les comptes-rendus des séances de travail, maintient à jour le journal de bord de l'équipe, prépare les ordres du jour et assure la liaison officielle avec la maîtrise d'ouvrage. |
| **3. Responsable du Déploiement** | **Khalil Bouchama** | Administre le dépôt de code de l'équipe, rédige la notice d'installation pas à pas et configure les fichiers Docker Compose pour permettre à la maîtrise d'ouvrage d'exécuter et valider la plateforme sans difficulté technique. |
| **4. Spécialiste Outils & Ingénieur Logiciel** | **Rayane Alli** | Met en place les environnements de travail communs, assiste l'équipe sur les configurations d'outils DevOps et développe les simulateurs légers simulant les services de la banque, des transports et de la voirie. |
| **5. Responsable Architecture Back-Office** | **Gautam Demeulemeester** | Conçoit le schéma relationnel de la base de données, met en œuvre la logique de réservation des commandes en deux temps pour éviter les ruptures de stock, et implémente les services métier côté serveur. |
| **6. Responsable Architecture Front-Office** | **Ilyas Ait Ali** | Élabore les maquettes d'écrans, développe l'interface web responsive adaptée aux mobiles et aux ordinateurs, et veille à proposer une ergonomie intuitive accessible aux usagers les moins à l'aise avec le numérique. |

## 2.3. Organisation du travail et principe du Scrum Master tournant

Pour favoriser l'implication de chacun et maintenir une bonne coordination, **notre équipe fonctionne selon une organisation collégiale et horizontale**. Nous nous appuyons sur les principes de la méthode Agile Scrum en confiant l'animation d'équipe (**Scrum Master tournant**) à tour de rôle à chaque jalon du projet :

- **Jalon R1 (18/09/2026) — Cadrage & Réponse à l'appel d'offres :** Coordination par **Khalil Bouchama** (restitution formelle et soutenance de cadrage le 21/09/2026).
- **Jalon R2 (12/10/2026) — Choix d'outillage & Socle technique :** Coordination par **Rayane Alli** (revue sur dossier technique d'ingénierie).
- **Jalon R3 (30/11/2026) — Analyse financière & Coûts complets :** Coordination par **Gautam Demeulemeester** (revue sur dossier financier et business plan).
- **Jalon R4 (18/12/2026) — Premier prototype logiciel & Architecture V1 :** Coordination par **Ilyas Ait Ali** (démonstration du prototype opérationnel le 04/01/2027).
- **Jalon R5 (19/03/2027) — Version complète V2 & Bilan d'exploitation :** Coordination par **Abdelkader Heddi** (recette finale et restitution de clôture le 22/03/2027).

Au quotidien, notre travail s'organise autour d'une réunion hebdomadaire de synchronisation d'une trentaine de minutes permettant de faire le point sur les avancées, de partager les difficultés éventuelles et de redistribuer les tâches en cas de besoin, garantissant un investissement équitable de chacun.

<div style="page-break-after: always;"></div>

# 3. Analyse fonctionnelle du sujet ShopLoc

## 3.1. Analyse du besoin et méthode APTE (Bête à cornes)

Pour appréhender objectivement la finalité de la plateforme ShopLoc, nous avons mis en œuvre la méthode d'analyse fonctionnelle du besoin APTE (norme AFNOR NF X 50-151) à travers l'outil de la « Bête à cornes » :

<div class="diagram-container" style="margin: 8pt 0; text-align: center;">
  <img src="figures/fig_1_1_bete_a_cornes.png" alt="Figure 3.1 — Bête à cornes APTE de la plateforme ShopLoc" style="width: 100%; max-width: 520px; height: auto; display: block; margin: 0 auto; border-radius: 4px;" />
  <div class="diagram-caption">Figure 3.1 — Expression du besoin fondamental (Bête à cornes APTE — Norme AFNOR NF X 50-151)</div>
</div>

Le système ShopLoc rend service à la fois aux **citoyens consommateurs**, aux **artisans et commerçants de proximité** et aux **collectivités territoriales**. Il agit directement sur **le dynamisme des cœurs de ville et les flux d'achats locaux**, dans le but de **revitaliser le commerce de proximité par des circuits courts, une visibilité numérique mutualisée et des avantages mobilité concrets**.

<div style="page-break-after: always;"></div>

## 3.2. Identification des acteurs et benchmark concurrentiel

Le déploiement de ShopLoc articule quatre catégories d'acteurs clés :
- **Commerçants et artisans indépendants :** Recherche d'une visibilité en ligne sans rogner leurs marges ni alourdir le travail en boutique (0% de commission marchande).
- **Citoyens consommateurs (habitants et actifs) :** Volonté de consommer localement via un panier unique Click & Collect gratuit et des gratifications régulières.
- **Collectivité territoriale (Mairie / DSI) :** Volonté de redynamiser les cœurs de ville, d'inciter aux mobilités douces et de suivre des indicateurs anonymisés (RGPD).
- **Partenaires délégués :** Réseaux de transports urbains (titres de bus) et voirie municipale (contrôle du stationnement par plaque minéralogique).

### Benchmark comparatif et positionnement différenciant
Notre étude de marché classe l'existant en trois familles : (1) **Plateformes globales (Amazon, Deliveroo)** à fortes commissions (15-30%) et livraisons motorisées délocalisées ; (2) **Marketplaces privées de proximité (Ollca, Epicery)** à commissions marchandes (8-15%) centrées sur la livraison à domicile ; (3) **Cartes de fidélité de ville (Proxity)** sans catalogue en ligne ni panier mutualisé.

ShopLoc investit un positionnement public vertueux : **0% de commission marchande**, **gratuité citoyenne**, **Click & Collect pédestre mutualisé** et **double fidélité territoriale** (cagnotte boutique et statut VFP mobilité financé par la ville).

<div class="diagram-container" style="margin: 6pt 0; text-align: center;">
  <img src="figures/fig_1_2_matrice_positionnement.png" alt="Figure 3.2 — Matrice de positionnement concurrentiel de ShopLoc" style="width: 100%; max-width: 480px; height: auto; display: block; margin: 0 auto; border-radius: 4px;" />
  <div class="diagram-caption">Figure 3.2 — Matrice de positionnement concurrentiel (Ancrage territorial vs. Équité du modèle économique)</div>
</div>

<div style="page-break-after: always;"></div>

## 3.3. Analyse des profils utilisateurs cibles (Personas)

L'étude des cas d'usage décrits dans le sujet d'appel d'offres permet d'identifier cinq profils types représentatifs des usagers et partenaires de la plateforme :
- **Pierre (74 ans) — Le senior fidèle de quartier :** Réalise quotidiennement sa tournée matinale chez les commerçants de proximité (Le Fournil, boucherie flamande, café des sports, tabac-presse). Même sans achat sur le web Click & Collect, la fréquence journalière de ses achats chez les partenaires lui permet d'obtenir rapidement le statut VFP et de débloquer la gratuité des transports en commun pour son trajet retour en bus.
- **Julie (31 ans) — La citadine active :** Consulte les horaires et commerces de son quartier sur le site web, commande ses articles en Click & Collect avec calcul du plus court chemin pour collecter ses achats, recharge sa carte en ligne par carte bleue (type Izli) et dépense ses points fidélité en avantages boutique (avec obligation d'achat antérieur et présentation de carte lors du paiement en cours).
- **Arthur (34 ans) — Le père de famille automobiliste :** Fréquente la boulangerie sur le chemin de l'école de son fils. Il s'abonne au service, renseigne sa plaque d'immatriculation dans son profil et active ses 20 minutes de stationnement offertes grâce au statut VFP pour effectuer ses courses en centre-ville.
- **Suzanne (22 ans) — La commerçante (Boulangerie Le Fournil) :** Met à jour son catalogue Click & Collect et ses stocks disponibles, paramètre les lots offerts dans le catalogue fidélité (tarte au maroilles, viennoiserie), scanne les cartes en caisse et consulte les statistiques de ventes associées au programme pour mesurer la rentabilité de sa participation.
- **Marius (27 ans) — Le gestionnaire municipal à la DSI :** Supervise le tableau de bord comparant le coût des avantages mobilité (partenariat Ilévia et parkings) au volume de vente généré, relance les usagers lors de la perte du statut VFP et diffuse des offres promotionnelles ou des sondages de satisfaction (QCM).

*(Note : Les fiches complètes et détaillées de ces personas, conçues lors de l'étude de cadrage ergonomique, sont jointes en annexe du dossier au format A4 paysage).*

## 3.4. Cartographie des récits utilisateurs (User Story Mapping)

Conformément à la méthode officielle de **User Story Mapping** ([guide de référence aha.io / Jeff Patton](https://www.aha.io/roadmapping/guide/release-management/what-is-user-story-mapping)), l'ensemble des exigences du projet est structuré selon une hiérarchie à trois niveaux :
1. **Activités utilisateurs (Backbone / User Activities) :** Les 5 grands thèmes structurant l'expérience : *1. Compte & Profils*, *2. Catalogue & Click & Collect*, *3. Caisse & Fidélité Boutique*, *4. Statut VFP & Mobilité*, *5. Pilotage & Supervision*.
2. **Étapes séquentielles du parcours (User Steps) :** Les étapes concrètes réalisées de gauche à droite sous chaque activité (ex. Inscription & Connexion, Profil & Plaque, Gestion Boutique & Articles, Commande & Trajet, Scan & Points, Lots & Cadeaux, Fréquence & VFP, Mobilité, Statistiques et Supervision).
3. **Découpage par Release (Tranches horizontales) :**
   - **Release 1 (MVP) :** Cœur contractuel obligatoire pour les jalons R4/R5 (création de compte, connexion sécurisée, consultation et gestion de fiche boutique, catalogue d'articles et gestion des stocks, commande Click & Collect, calcul du plus court chemin pédestre, scan en caisse, cumul de points boutique, conversion en lots/cadeaux, attribution du statut VFP, génération de ticket de bus dématérialisé, activation de 20 minutes de parking offert, tableaux de bord des ventes commerçant et supervision municipale DSI).
   - **Release 2 (Évolutions & Confort) :** Fonctionnalités complémentaires prévues pour enrichir l'expérience (recharge de carte en ligne type Izli, alertes automatiques de modification d'horaires et de seuil de stock pour le commerçant, suspension temporaire du statut VFP pendant les vacances scolaires, comparatif de rentabilité pour les commerçants, sondages municipaux courts par QCM et relances automatisées de la DSI).

<div class="landscape-page" style="display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 184mm; width: 100%; box-sizing: border-box; padding: 0; margin: 0;">
<!-- FIGURE 3.3 : GRILLE DE USER STORY MAPPING (CHARTE OFFICIELLE SHOPLOC) -->
<div class="figure-card" style="background:#FAF9F6; border:1px solid #DCD6CD; border-radius:14px; padding:14px 18px; margin: auto; width: 100%; box-sizing: border-box; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:14px; border-bottom:1px solid #DCD6CD; padding-bottom:10px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#C26750;"></span>
        <span style="font-size:11px; font-weight:700; color:#C26750; text-transform:uppercase; letter-spacing:0.08em;">Ingénierie des Exigences</span>
      </div>
      <h3 style="font-size:16px; font-weight:700; color:#243342; margin:0;">Figure 3.3 — Cartographie des Récits Utilisateurs (User Story Mapping)</h3>
    </div>
    <span style="font-size:11px; background:#FFFFFF; border:1px solid #DCD6CD; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600;">Modèle aha.io · Release 1 (MVP) &amp; Release 2</span>
  </div>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1520 860" width="100%" height="auto" style="display: block; width: 100%; height: auto; font-family: 'Poppins', sans-serif;">
  <defs>
    <style>@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');</style>
    <filter id="shadow-soft" x="-2%" y="-2%" width="104%" height="106%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#243342" flood-opacity="0.06"/>
    </filter>
    <filter id="shadow-card" x="-4%" y="-6%" width="108%" height="116%">
      <feDropShadow dx="0" dy="1.5" stdDeviation="2" flood-color="#243342" flood-opacity="0.04"/>
    </filter>
  </defs>

  <!-- FOND GLOBAL DE LA CARTE (LIN DOUX) -->
  <rect x="5" y="5" width="1510" height="850" rx="14" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1.2" filter="url(#shadow-soft)"/>

  <!-- ======================================================== -->
  <!-- EN-TÊTE PRINCIPAL DU DIAGRAMME                           -->
  <!-- ======================================================== -->
  <rect x="25" y="20" width="1470" height="50" rx="8" fill="#243342" />
  <rect x="38" y="31" width="28" height="28" rx="6" fill="#C26750" />
  <text x="52" y="50" text-anchor="middle" font-size="12" font-weight="800" fill="#FFFFFF">USM</text>
  <text x="78" y="44" font-size="14" font-weight="700" fill="#FFFFFF">Cartographie des Récits Utilisateurs — User Story Mapping (Modèle aha.io / Jeff Patton)</text>
  <text x="78" y="59" font-size="9.5" font-weight="400" fill="#EBF0F5">Activités Métier (Backbone) &gt; Étapes du Parcours (Steps) &gt; Récits Utilisateurs par Release</text>
  <text x="1480" y="49" text-anchor="end" font-size="11" font-weight="600" fill="#DCD6CD">ShopLoc · Master 2 MIAGE · Garik</text>

  <!-- ======================================================== -->
  <!-- NIVEAU 1 : ACTIVITÉS UTILISATEURS (USER ACTIVITIES)       -->
  <!-- ======================================================== -->
  <!-- Col 0 : Axe -->
  <rect x="25" y="80" width="115" height="42" rx="6" fill="#F5F2EB" stroke="#DCD6CD" stroke-width="1" />
  <text x="82" y="98" text-anchor="middle" font-size="10" font-weight="700" fill="#243342">ACTIVITÉS</text>
  <text x="82" y="112" text-anchor="middle" font-size="8.5" font-weight="600" fill="#5A6578">BACKBONE</text>

  <!-- Act 1 : Compte & Profils -->
  <rect x="150" y="80" width="260" height="42" rx="6" fill="#C26750" />
  <text x="280" y="98" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">1. COMPTE &amp; IDENTITÉ</text>
  <text x="280" y="112" text-anchor="middle" font-size="8.5" font-weight="500" fill="#FBEEEA">Inscription, connexion et profils</text>

  <!-- Act 2 : Catalogue & Click & Collect -->
  <rect x="420" y="80" width="260" height="42" rx="6" fill="#4A7A5B" />
  <text x="550" y="98" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">2. CATALOGUE &amp; CLICK &amp; COLLECT</text>
  <text x="550" y="112" text-anchor="middle" font-size="8.5" font-weight="500" fill="#EBF3ED">Articles, stocks, panier et trajet piéton</text>

  <!-- Act 3 : Caisse & Fidélité Boutique -->
  <rect x="690" y="80" width="260" height="42" rx="6" fill="#4A7A5B" />
  <text x="820" y="98" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">3. CAISSE &amp; FIDÉLITÉ BOUTIQUE</text>
  <text x="820" y="112" text-anchor="middle" font-size="8.5" font-weight="500" fill="#EBF3ED">Scan QR caisse, points et cadeaux</text>

  <!-- Act 4 : Programme VFP & Mobilité -->
  <rect x="960" y="80" width="260" height="42" rx="6" fill="#C48B28" />
  <text x="1090" y="98" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">4. STATUT VFP &amp; MOBILITÉ</text>
  <text x="1090" y="112" text-anchor="middle" font-size="8.5" font-weight="500" fill="#FEF7EB">Fréquence, bus offert et parking 20 min</text>

  <!-- Act 5 : Pilotage & Mairie -->
  <rect x="1230" y="80" width="265" height="42" rx="6" fill="#243342" />
  <text x="1362" y="98" text-anchor="middle" font-size="11" font-weight="700" fill="#FFFFFF">5. PILOTAGE &amp; SUPERVISION</text>
  <text x="1362" y="112" text-anchor="middle" font-size="8.5" font-weight="500" fill="#EBF0F5">Rentabilité Suzanne et métriques Marius</text>

  <!-- ======================================================== -->
  <!-- NIVEAU 2 : ÉTAPES UTILISATEURS (USER STEPS)               -->
  <!-- ======================================================== -->
  <!-- Col 0 : Axe -->
  <rect x="25" y="128" width="115" height="42" rx="6" fill="#F5F2EB" stroke="#DCD6CD" stroke-width="1" />
  <text x="82" y="146" text-anchor="middle" font-size="10" font-weight="700" fill="#243342">ÉTAPES</text>
  <text x="82" y="160" text-anchor="middle" font-size="8" font-weight="500" fill="#5A6578">PARCOURS</text>

  <!-- Steps Act 1 -->
  <rect x="150" y="128" width="125" height="42" rx="6" fill="#FBEEEA" stroke="#D88B77" stroke-width="1" />
  <text x="212" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#8E3D2A">1.1 Inscription &amp;</text>
  <text x="212" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#8E3D2A">Authentification</text>

  <rect x="285" y="128" width="125" height="42" rx="6" fill="#FBEEEA" stroke="#D88B77" stroke-width="1" />
  <text x="347" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#8E3D2A">1.2 Profil &amp;</text>
  <text x="347" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#8E3D2A">Immatriculation</text>

  <!-- Steps Act 2 -->
  <rect x="420" y="128" width="125" height="42" rx="6" fill="#EBF3ED" stroke="#7EA88D" stroke-width="1" />
  <text x="482" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2E583D">2.1 Fiche Boutique</text>
  <text x="482" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2E583D">&amp; Articles</text>

  <rect x="555" y="128" width="125" height="42" rx="6" fill="#EBF3ED" stroke="#7EA88D" stroke-width="1" />
  <text x="617" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2E583D">2.2 Commande C&amp;C</text>
  <text x="617" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2E583D">&amp; Trajet Piéton</text>

  <!-- Steps Act 3 -->
  <rect x="690" y="128" width="125" height="42" rx="6" fill="#EBF3ED" stroke="#7EA88D" stroke-width="1" />
  <text x="752" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2E583D">3.1 Scan Caisse &amp;</text>
  <text x="752" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2E583D">Crédit Points</text>

  <rect x="825" y="128" width="125" height="42" rx="6" fill="#EBF3ED" stroke="#7EA88D" stroke-width="1" />
  <text x="887" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2E583D">3.2 Déblocage</text>
  <text x="887" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#2E583D">Cadeaux Boutique</text>

  <!-- Steps Act 4 -->
  <rect x="960" y="128" width="125" height="42" rx="6" fill="#FEF7EB" stroke="#DCB162" stroke-width="1" />
  <text x="1022" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#845A11">4.1 Fréquence &amp;</text>
  <text x="1022" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#845A11">Obtention VFP</text>

  <rect x="1095" y="128" width="125" height="42" rx="6" fill="#FEF7EB" stroke="#DCB162" stroke-width="1" />
  <text x="1157" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#845A11">4.2 Usage Bus &amp;</text>
  <text x="1157" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#845A11">Parking 20 min</text>

  <!-- Steps Act 5 -->
  <rect x="1230" y="128" width="128" height="42" rx="6" fill="#EBF0F5" stroke="#8B9EAF" stroke-width="1" />
  <text x="1294" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#1C2D3D">5.1 Statistiques</text>
  <text x="1294" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#1C2D3D">Commerçant</text>

  <rect x="1367" y="128" width="128" height="42" rx="6" fill="#EBF0F5" stroke="#8B9EAF" stroke-width="1" />
  <text x="1431" y="145" text-anchor="middle" font-size="8.5" font-weight="700" fill="#1C2D3D">5.2 Supervision DSI</text>
  <text x="1431" y="159" text-anchor="middle" font-size="8.5" font-weight="700" fill="#1C2D3D">&amp; Sondages</text>

  <!-- ======================================================== -->
  <!-- SWIMLANE 1 : RELEASE 1 (MVP R4/R5 - MUST HAVE)           -->
  <!-- ======================================================== -->
  <rect x="25" y="180" width="1470" height="445" rx="10" fill="#FFFFFF" stroke="#243342" stroke-width="1.6" filter="url(#shadow-soft)"/>
  
  <!-- Bandeau Latéral Release 1 -->
  <path d="M 25 190 A 10 10 0 0 1 35 180 L 140 180 L 140 625 L 35 625 A 10 10 0 0 1 25 615 Z" fill="#EBF0F5" />
  <rect x="35" y="195" width="95" height="24" rx="5" fill="#243342" />
  <text x="82" y="211" text-anchor="middle" font-size="10" font-weight="700" fill="#FFFFFF">RELEASE 1</text>
  <text x="82" y="235" text-anchor="middle" font-size="11" font-weight="800" fill="#243342">MVP</text>
  <text x="82" y="252" text-anchor="middle" font-size="8.5" font-weight="600" fill="#4A7A5B">Cœur du sujet</text>
  <circle cx="82" cy="295" r="18" fill="#FFFFFF" stroke="#243342" stroke-width="1.5"/>
  <text x="82" y="301" text-anchor="middle" font-size="14" font-weight="800" fill="#243342">M</text>
  <text x="82" y="328" text-anchor="middle" font-size="8.5" font-weight="700" fill="#243342">MUST HAVE</text>
  <text x="82" y="344" text-anchor="middle" font-size="8" font-weight="500" fill="#5A6578">Évalué R4 / R5</text>
  <text x="82" y="585" text-anchor="middle" font-size="8.5" font-weight="700" fill="#243342">Socle Majeur</text>
  <text x="82" y="602" text-anchor="middle" font-size="10" font-weight="800" fill="#4A7A5B">Priorité 1</text>

  <!-- LIGNES SÉPARATRICES ACTIVITÉS MVP -->
  <line x1="415" y1="180" x2="415" y2="625" stroke="#EDE8E1" stroke-width="1" />
  <line x1="685" y1="180" x2="685" y2="625" stroke="#EDE8E1" stroke-width="1" />
  <line x1="955" y1="180" x2="955" y2="625" stroke="#EDE8E1" stroke-width="1" />
  <line x1="1225" y1="180" x2="1225" y2="625" stroke="#EDE8E1" stroke-width="1" />

  <!-- === CARTES RELEASE 1 (MVP) === -->
  
  <!-- Step 1.1 : Card US-01 (Inscription) -->
  <g transform="translate(150, 190)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#C26750" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#FBEEEA" stroke="#D88B77" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#8E3D2A">US-01</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#F5F2EB"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Citoyen</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Création Compte</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#C26750">Julie / Arthur</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que citoyen,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je crée mon compte avec</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">mes identifiants et j'obtiens</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">ma carte de fidélité.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Accès service garanti</text>
  </g>

  <!-- Step 1.1 : Card US-02 (Connexion) -->
  <g transform="translate(150, 405)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#C26750" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#FBEEEA" stroke="#D88B77" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#8E3D2A">US-02</text>
    <rect x="72" y="8" width="47" height="14" rx="3" fill="#F5F2EB"/>
    <text x="95" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Tous rôles</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Se Connecter</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#C26750">Tous profils</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant qu'utilisateur</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">(citoyen, commerçant,</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">admin mairie), je me</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">connecte à mon espace.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Authentification sécure</text>
  </g>

  <!-- Step 1.2 : Card US-04 (Plaque) -->
  <g transform="translate(285, 190)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#C26750" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#FBEEEA" stroke="#D88B77" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#8E3D2A">US-04</text>
    <rect x="68" y="8" width="51" height="14" rx="3" fill="#F5F2EB"/>
    <text x="93" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Automobile</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Saisie Plaque Auto</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#C26750">Arthur (Automobiliste)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant qu'automobiliste,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je renseigne mon numéro</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">de plaque dans mon profil</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">pour le parking offert.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Lien véhicule &lt;&gt; profil</text>
  </g>

  <!-- Step 2.1 : Card US-06 (Fiche boutique) -->
  <g transform="translate(420, 190)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#4A7A5B" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF3ED" stroke="#7EA88D" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#2E583D">US-06</text>
    <rect x="62" y="8" width="57" height="14" rx="3" fill="#F5F2EB"/>
    <text x="90" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Commerçant</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Horaires &amp; Boutique</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#4A7A5B">Suzanne (Fournil)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que commerçante,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je configure les horaires</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">d'ouverture et l'adresse</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">de ma boulangerie.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Fiche magasin publique</text>
  </g>

  <!-- Step 2.1 : Card US-07 (Gestion articles & stocks) -->
  <g transform="translate(420, 405)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#4A7A5B" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF3ED" stroke="#7EA88D" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#2E583D">US-07</text>
    <rect x="62" y="8" width="57" height="14" rx="3" fill="#F5F2EB"/>
    <text x="90" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Commerçant</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Articles &amp; Stocks</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#4A7A5B">Suzanne (Fournil)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que commerçante,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je saisis et modifie</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">facilement mes articles</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">et stocks Click &amp; Collect.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Stock en temps réel</text>
  </g>

  <!-- Step 2.2 : Card US-09 (Panier Julie) -->
  <g transform="translate(555, 190)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#4A7A5B" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF3ED" stroke="#7EA88D" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#2E583D">US-09</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#F5F2EB"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Citoyen</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Commander en Ligne</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#4A7A5B">Julie (Citadine)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que cliente,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je consulte les magasins,</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">sélectionne mes articles et</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">valide ma commande C&amp;C.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Réservation 2 phases</text>
  </g>

  <!-- Step 2.2 : Card US-11 (Plus court chemin) -->
  <g transform="translate(555, 405)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#4A7A5B" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF3ED" stroke="#7EA88D" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#2E583D">US-11</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#F5F2EB"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Citoyen</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Trajet le Plus Court</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#4A7A5B">Julie (Citadine)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que cliente,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je demande au système le</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">plus court chemin pour</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">collecter mes achats.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Calcul itinéraire piéton</text>
  </g>

  <!-- Step 3.1 : Card US-13 (Scan caisse & points) -->
  <g transform="translate(690, 190)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#4A7A5B" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF3ED" stroke="#7EA88D" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#2E583D">US-13</text>
    <rect x="62" y="8" width="57" height="14" rx="3" fill="#F5F2EB"/>
    <text x="90" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Commerçant</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Scan Caisse &amp; Points</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#4A7A5B">Pierre / Suzanne</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que commerçante,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je scanne la carte client</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">pour créditer les points</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">liés au montant dépensé.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Gain de points boutique</text>
  </g>

  <!-- Step 3.2 : Card US-15 (Catalogue cadeaux) -->
  <g transform="translate(825, 190)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#4A7A5B" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF3ED" stroke="#7EA88D" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#2E583D">US-15</text>
    <rect x="62" y="8" width="57" height="14" rx="3" fill="#F5F2EB"/>
    <text x="90" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Commerçant</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Catalogue Cadeaux</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#4A7A5B">Suzanne (Fournil)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que commerçante,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je paramètre les lots</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">offerts (tarte maroilles,</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">mini-viennoiserie).</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Offres partenaires</text>
  </g>

  <!-- Step 3.2 : Card US-16 (Déblocage cadeau) -->
  <g transform="translate(825, 405)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#4A7A5B" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF3ED" stroke="#7EA88D" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#2E583D">US-16</text>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Citoyen</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#F5F2EB"/>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Débloquer Cadeau</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#4A7A5B">Julie (Cliente)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que cliente,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">j'obtiens mon cadeau lors</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">d'un achat si j'ai au moins</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">un achat antérieur.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Règle anti-abus validée</text>
  </g>

  <!-- Step 4.1 : Card US-17 (Attribution VFP) -->
  <g transform="translate(960, 190)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#C48B28" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#FEF7EB" stroke="#DCB162" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#845A11">US-17</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#F5F2EB"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Citoyen</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Obtention Statut VFP</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#C48B28">Pierre / Arthur / Julie</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que client fidèle,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">j'obtiens le statut VFP</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">grâce à la fréquence de mes</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">achats hebdomadaires.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Calcul de fréquence auto</text>
  </g>

  <!-- Step 4.2 : Card US-19 (Bus Pierre) -->
  <g transform="translate(1095, 190)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#C48B28" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#FEF7EB" stroke="#DCB162" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#845A11">US-19</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#F5F2EB"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Mobilité</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Ticket Bus Offert</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#C48B28">Pierre (Senior)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que VFP,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je génère mon ticket de bus</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">gratuit quotidien avec QR code</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">à présenter au chauffeur.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Ticket mobilité actif</text>
  </g>

  <!-- Step 4.2 : Card US-20 (Parking Arthur) -->
  <g transform="translate(1095, 405)">
    <rect x="0" y="0" width="125" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="125" height="4" rx="2" fill="#C48B28" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#FEF7EB" stroke="#DCB162" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#845A11">US-20</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#F5F2EB"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Mobilité</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">20 min Parking Offert</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#C48B28">Arthur (Automobiliste)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que VFP,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">j'active mon forfait de 20 min</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">gratuites et je suis le</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">décompte en temps réel.</text>
    <rect x="6" y="180" width="113" height="18" rx="3" fill="#EBF3ED"/>
    <text x="62" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Stationnement synchronisé</text>
  </g>

  <!-- Step 5.1 : Card US-22 (Stats Suzanne) -->
  <g transform="translate(1230, 190)">
    <rect x="0" y="0" width="128" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="128" height="4" rx="2" fill="#243342" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF0F5" stroke="#8B9EAF" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#1C2D3D">US-22</text>
    <rect x="65" y="8" width="57" height="14" rx="3" fill="#F5F2EB"/>
    <text x="93" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Commerçant</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Ventes Boutique</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#243342">Suzanne (Fournil)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant que commerçante,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je consulte le volume des</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">ventes et achats C&amp;C</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">généré par les clients.</text>
    <rect x="6" y="180" width="116" height="18" rx="3" fill="#EBF3ED"/>
    <text x="64" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Mesure rentabilité</text>
  </g>

  <!-- Step 5.2 : Card US-24 (Tableau DSI Marius) -->
  <g transform="translate(1367, 190)">
    <rect x="0" y="0" width="128" height="205" rx="6" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="0" y="0" width="128" height="4" rx="2" fill="#243342" />
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF0F5" stroke="#8B9EAF" stroke-width="0.8"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#1C2D3D">US-24</text>
    <rect x="80" y="8" width="42" height="14" rx="3" fill="#F5F2EB"/>
    <text x="101" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Mairie DSI</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Tableau DSI Mairie</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#243342">Marius (DSI Ville)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">En tant qu'admin DSI,</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">je compare le coût des</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">avantages mobilité au</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">volume des ventes.</text>
    <rect x="6" y="180" width="116" height="18" rx="3" fill="#EBF3ED"/>
    <text x="64" y="192" text-anchor="middle" font-size="7" font-weight="600" fill="#2E583D">Rapport conseil municipal</text>
  </g>

  <!-- ======================================================== -->
  <!-- SWIMLANE 2 : RELEASE 2 (ÉVOLUTIONS & CONFORT - SHOULD HAVE) -->
  <!-- ======================================================== -->
  <rect x="25" y="635" width="1470" height="205" rx="10" fill="#FFFFFF" stroke="#8C96A5" stroke-width="1.2" stroke-dasharray="4 3" filter="url(#shadow-soft)"/>
  
  <!-- Bandeau Latéral Release 2 -->
  <path d="M 25 645 A 10 10 0 0 1 35 635 L 140 635 L 140 840 L 35 840 A 10 10 0 0 1 25 830 Z" fill="#F5F2EB" />
  <rect x="35" y="645" width="95" height="22" rx="5" fill="#5A6578" />
  <text x="82" y="660" text-anchor="middle" font-size="9.5" font-weight="700" fill="#FFFFFF">RELEASE 2</text>
  <text x="82" y="680" text-anchor="middle" font-size="10" font-weight="700" fill="#243342">Évolutions</text>
  <text x="82" y="695" text-anchor="middle" font-size="8" font-weight="600" fill="#C48B28">Confort usagers</text>
  <circle cx="82" cy="728" r="15" fill="#FFFFFF" stroke="#8C96A5" stroke-width="1"/>
  <text x="82" y="733" text-anchor="middle" font-size="11" font-weight="700" fill="#5A6578">S</text>
  <text x="82" y="755" text-anchor="middle" font-size="8" font-weight="600" fill="#5A6578">SHOULD HAVE</text>
  <text x="82" y="818" text-anchor="middle" font-size="8.5" font-weight="700" fill="#5A6578">Post-MVP</text>

  <!-- LIGNES SÉPARATRICES ACTIVITÉS R2 -->
  <line x1="415" y1="635" x2="415" y2="840" stroke="#EDE8E1" stroke-width="1" />
  <line x1="685" y1="635" x2="685" y2="840" stroke="#EDE8E1" stroke-width="1" />
  <line x1="955" y1="635" x2="955" y2="840" stroke="#EDE8E1" stroke-width="1" />
  <line x1="1225" y1="635" x2="1225" y2="840" stroke="#EDE8E1" stroke-width="1" />

  <!-- === CARTES RELEASE 2 (Évolutions) === -->
  <!-- Step 1.2 : US-05 (Recharge Izli) -->
  <g transform="translate(285, 645)">
    <rect x="0" y="0" width="125" height="185" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF0F5"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#5A6578">US-05</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#FFFFFF"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Citoyen</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Recharge Carte Izli</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#5A6578">Julie (Citadine)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">Chargement en ligne</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">d'une somme d'argent par</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">carte bleue pour petits</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">achats partenaires.</text>
    <rect x="6" y="160" width="113" height="18" rx="3" fill="#EBF0F5"/>
    <text x="62" y="172" text-anchor="middle" font-size="7" font-weight="600" fill="#243342">Porte-monnaie Izli</text>
  </g>

  <!-- Step 2.1 : US-08 (Alerte rupture stock) -->
  <g transform="translate(420, 645)">
    <rect x="0" y="0" width="125" height="185" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF0F5"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#5A6578">US-08</text>
    <rect x="62" y="8" width="57" height="14" rx="3" fill="#FFFFFF"/>
    <text x="90" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Commerçant</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Alerte Rupture Stock</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#5A6578">Suzanne (Fournil)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">Notification automatique</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">à la commerçante dès</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">qu'un article est épuisé.</text>
    <rect x="6" y="160" width="113" height="18" rx="3" fill="#EBF0F5"/>
    <text x="62" y="172" text-anchor="middle" font-size="7" font-weight="600" fill="#243342">Alerte commerçant</text>
  </g>

  <!-- Step 2.2 : US-12 (Notification horaires Julie) -->
  <g transform="translate(555, 645)">
    <rect x="0" y="0" width="125" height="185" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF0F5"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#5A6578">US-12</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#FFFFFF"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Citoyen</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Alerte Horaires</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#5A6578">Julie (Citadine)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">Notification courriel aux</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">clients quand les horaires</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">des magasins favoris</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">sont modifiés.</text>
    <rect x="6" y="160" width="113" height="18" rx="3" fill="#EBF0F5"/>
    <text x="62" y="172" text-anchor="middle" font-size="7" font-weight="600" fill="#243342">Suivi des commerces</text>
  </g>

  <!-- Step 4.1 : US-18 (Perte VFP Vacances Arthur) -->
  <g transform="translate(960, 645)">
    <rect x="0" y="0" width="125" height="185" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF0F5"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#5A6578">US-18</text>
    <rect x="76" y="8" width="43" height="14" rx="3" fill="#FFFFFF"/>
    <text x="97" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Citoyen</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Gestion Perte VFP</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#5A6578">Arthur (Vacances)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">Suspension temporaire</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">du statut VFP si la</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">fréquence d'achats baisse</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">(vacances scolaires).</text>
    <rect x="6" y="160" width="113" height="18" rx="3" fill="#EBF0F5"/>
    <text x="62" y="172" text-anchor="middle" font-size="7" font-weight="600" fill="#243342">Règle d'inactivité</text>
  </g>

  <!-- Step 5.1 : US-23 (Comparatif Suzanne) -->
  <g transform="translate(1230, 645)">
    <rect x="0" y="0" width="128" height="185" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF0F5"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#5A6578">US-23</text>
    <rect x="65" y="8" width="57" height="14" rx="3" fill="#FFFFFF"/>
    <text x="93" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Commerçant</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Comparatif Ventes</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#5A6578">Suzanne (Fournil)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">Indicateurs comparatifs</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">auprès des autres magasins</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">pour vérifier le gain</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">de participation.</text>
    <rect x="6" y="160" width="116" height="18" rx="3" fill="#EBF0F5"/>
    <text x="64" y="172" text-anchor="middle" font-size="7" font-weight="600" fill="#243342">Benchmark interne</text>
  </g>

  <!-- Step 5.2 : US-25 (Marius Relance & Sondages) -->
  <g transform="translate(1367, 645)">
    <rect x="0" y="0" width="128" height="185" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1" filter="url(#shadow-card)"/>
    <rect x="6" y="8" width="42" height="14" rx="3" fill="#EBF0F5"/>
    <text x="27" y="18" text-anchor="middle" font-size="7.5" font-weight="700" fill="#5A6578">US-25</text>
    <rect x="80" y="8" width="42" height="14" rx="3" fill="#FFFFFF"/>
    <text x="101" y="18" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">Mairie DSI</text>
    <text x="6" y="34" font-size="8.5" font-weight="700" fill="#1E252D">Sondages &amp; Relances</text>
    <text x="6" y="46" font-size="7.5" font-weight="600" fill="#5A6578">Marius (DSI)</text>
    <text x="6" y="60" font-size="7" font-weight="400" fill="#5A6578">Envoi de questionnaires</text>
    <text x="6" y="70" font-size="7" font-weight="400" fill="#5A6578">QCM de satisfaction et</text>
    <text x="6" y="80" font-size="7" font-weight="400" fill="#5A6578">relance des usagers lors</text>
    <text x="6" y="90" font-size="7" font-weight="400" fill="#5A6578">de la perte du statut VFP.</text>
    <rect x="6" y="160" width="116" height="18" rx="3" fill="#EBF0F5"/>
    <text x="64" y="172" text-anchor="middle" font-size="7" font-weight="600" fill="#243342">Animation &amp; Rétention</text>
  </g>
</svg>

</div>

</div>

## 3.5. Découpage modulaire du système

L'ensemble des exigences métier est structuré en quatre modules opérationnels :

- **Module A — Gestion des acteurs & conventionnement :**
  - *Adhésion commerçante conventionnée :* Compte professionnel unique par boutique, sous validation préalable de la collectivité.
  - *Fiches d'établissement & horaires :* Paramétrage des créneaux réguliers et alertes courriel automatiques aux clients favoris en cas de modification ponctuelle.

- **Module B — Marketplace locale & Click & Collect mutualisé :**
  - *Catalogue & synchronisation des stocks :* Réservation en deux temps évitant les ruptures avec les ventes physiques en boutique.
  - *Panier d'achat multi-boutiques & parcours piéton :* Commande groupée multi-commerçants et calcul de l'itinéraire de retrait pédestre le plus rapide.
  - *Délais de préparation & exclusion de livraison :* Respect des temps de confection artisanale ; livraison motorisée expressément exclue pour favoriser la marche en centre-ville.

- **Module C — Double système de fidélité & statut VFP :**
  - *Fidélité commerçante privée :* Cagnottage de points boutique convertibles en réductions ou cadeaux (avec règle anti-abus au passage en caisse).
  - *Fidélité territoriale citoyenne (statut VFP) :* 10 passages sur 15 jours glissants conférant un titre de transport ou 20 min de stationnement offert par la ville.
  - *Supports universels :* Carte physique plastifiée avec QR code pour les personnes non connectées, application web mobile et porte-monnaie d'appoint (type Izli).

- **Module D — Portail de supervision municipale & animation :**
  - *Tableau de bord de suivi économique :* Indicateurs d'activité en centre-ville, fréquentation par quartier et budget mobilité consommé.
  - *Animation locale & sondages (QCM) :* Diffusion de questionnaires courts de satisfaction et communication d'événements municipaux.
  - *Gestion des no-shows & conformité RGPD :* Remise en vente automatique des commandes non retirées, anonymisation stricte et aucun traçage de géolocalisation.

<div style="page-break-after: always;"></div>

# 4. Premiers choix justifiés d'outils logiciels

## 4.1. Architecture logicielle prévisionnelle et cadre méthodologique

Pour répondre avec réalisme aux exigences du projet, nous avons retenu une architecture applicative 3-tiers modulaire reposant sur des composants clairement isolés. Il s'agit d'une **proposition préliminaire de cadrage pour le jalon R1**, qui sera éprouvée par notre équipe et formellement validée lors du jalon R2.

Cette architecture s'articule autour de quatre niveaux opérationnels cohérents :
1. **Tier Clients & Interfaces Web (React 18 + TypeScript 5 + Tailwind CSS 3) :** Une application web responsive (PWA) offrant des interfaces dédiées pour les citoyens consommateurs (panier groupé, pass bi-média QR), les commerçants artisans (interface POS caisse, scan express < 3s) et les gestionnaires municipaux de la mairie (dashboard d'activité et k-anonymat RGPD).
2. **Tier Backend & Services Métier (Java 21 LTS + Spring Boot 3.3) :** Un serveur d'application modulaire articulé en contextes délimités (*Gestion des Profils & Sécurité JWT*, *Catalogue & Réservation Click & Collect 2PC*, *Double Moteur de Fidélité & Batch VFP nocturne*, *Tableau de bord municipal*), communiquant via des interfaces RESTful normalisées sous contrat **OpenAPI 3.1**.
3. **Tier Persistance & Données (PostgreSQL 16) :** Une base relationnelle assurant l'intégrité transactionnelle stricte (ACID) des commandes et des mouvements de points, persistée sur volume de données dédié (`pgdata`) avec isolation `READ COMMITTED` et index B-Tree.
4. **Tier Simulateurs Partenaires (Mocks REST OpenAPI 3.1) :** Des bouchons applicatifs légers conteneurisés simulant les échanges avec les services tiers (passerelle bancaire Izli avec scénarios 2PC, réseau de transport Ilévia Pass Pass, contrôle horodateur de stationnement municipal 20 min) pour garantir l'autonomie totale des tests en environnement d'intégration et de recette.

L'ensemble de ces briques est orchestré par **Docker Compose** et versionné sur la forge institutionnelle **GitLab de l'Université de Lille**, garantissant un déploiement reproductible en une commande unique (`docker compose up`).

La **Figure 4.1** ci-après synthétise l'agencement global de ces composants au sein d'une cartographie technique normalisée :

<div class="landscape-page" style="display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 184mm; width: 100%; box-sizing: border-box; padding: 0; margin: 0;">
<!-- FIGURE 4.1 : SCHÉMA D'ARCHITECTURE LOGICIELLE SHOPLOC -->
<div class="figure-card" style="background:#FAF9F6; border:1px solid #DCD6CD; border-radius:14px; padding:14px 18px; margin: auto; width: 100%; box-sizing: border-box; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; border-bottom:1px solid #DCD6CD; padding-bottom:8px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#243342;"></span>
        <span style="font-size:11px; font-weight:700; color:#243342; text-transform:uppercase; letter-spacing:0.08em; font-family: 'Poppins', sans-serif;">Ingénierie Logicielle &amp; DevOps</span>
      </div>
      <h3 style="font-size:16px; font-weight:700; color:#243342; margin:0; font-family: 'Poppins', sans-serif;">Figure 4.1 — Architecture Applicative Prévisionnelle (Jalon R1)</h3>
    </div>
    <span style="font-size:11px; background:#FFFFFF; border:1px solid #DCD6CD; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600; font-family: 'Poppins', sans-serif;">Architecture 3-Tiers Modulaire</span>
  </div>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 780" width="100%" height="auto" style="display: block; width: 100%; height: auto; font-family: 'Poppins', sans-serif;">
  <defs>
    <style>@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&amp;display=swap');</style>
    <filter id="shadow-soft" x="-2%" y="-2%" width="104%" height="106%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#243342" flood-opacity="0.06"/>
    </filter>
    <filter id="shadow-card" x="-4%" y="-6%" width="108%" height="116%">
      <feDropShadow dx="0" dy="1.5" stdDeviation="2" flood-color="#243342" flood-opacity="0.05"/>
    </filter>
  </defs>

  <!-- FOND GLOBAL -->
  <rect x="5" y="5" width="1430" height="770" rx="14" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1.2" filter="url(#shadow-soft)"/>

  <!-- EN-TÊTE -->
  <rect x="25" y="20" width="1390" height="52" rx="8" fill="#243342" />
  <rect x="38" y="32" width="28" height="28" rx="6" fill="#C26750" />
  <text x="52" y="51" text-anchor="middle" font-size="13" font-weight="800" fill="#FFFFFF">SL</text>
  <text x="78" y="44" font-size="14" font-weight="700" fill="#FFFFFF">Architecture Applicative Prévisionnelle (Jalon R1) — ShopLoc</text>
  <text x="78" y="59" font-size="10" font-weight="400" fill="#EBF0F5">Cartographie Technique 3-Tiers Découplée · Pile Technologique &amp; Protocoles d'Échange</text>
  <text x="1400" y="51" text-anchor="end" font-size="11" font-weight="600" fill="#DCD6CD">Master 2 MIAGE · Garik</text>

  <!-- ======================================================== -->
  <!-- TIER 1 : CLIENTS WEB & MOBILES                           -->
  <!-- ======================================================== -->
  <rect x="25" y="84" width="1390" height="135" rx="10" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1.2" filter="url(#shadow-card)"/>
  <rect x="25" y="84" width="1390" height="30" rx="10" fill="#EBF0F5" />
  <text x="45" y="104" font-size="11.5" font-weight="700" fill="#243342">TIER 1 — INTERFACES UTILISATEURS &amp; CLIENTS (Progressive Web App)</text>

  <!-- Badges technos Frontend -->
  <g transform="translate(980, 87)">
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="115" height="24" rx="12" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1"/>
      <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/react/react-original.svg" x="8" y="4" width="16" height="16" />
      <text x="30" y="16" font-size="10" font-weight="600" fill="#243342">React 18</text>
    </g>

    <g transform="translate(125, 0)">
      <rect x="0" y="0" width="135" height="24" rx="12" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1"/>
      <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/typescript/typescript-original.svg" x="8" y="4" width="16" height="16" />
      <text x="30" y="16" font-size="10" font-weight="600" fill="#243342">TypeScript 5</text>
    </g>

    <g transform="translate(270, 0)">
      <rect x="0" y="0" width="145" height="24" rx="12" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1"/>
      <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tailwindcss/tailwindcss-original.svg" x="8" y="4" width="16" height="16" />
      <text x="30" y="16" font-size="10" font-weight="600" fill="#243342">Tailwind CSS 3</text>
    </g>
  </g>

  <!-- Carte 1.1 : Espace Citoyen -->
  <g transform="translate(45, 122)">
    <rect x="0" y="0" width="425" height="84" rx="8" fill="#FBEEEA" stroke="#D88B77" stroke-width="1" />
    <circle cx="30" cy="28" r="15" fill="#C26750" />
    <text x="30" y="33" text-anchor="middle" font-size="13" fill="#FFFFFF">CIT</text>
    <text x="54" y="24" font-size="11" font-weight="700" fill="#8E3D2A">ESPACE CITOYEN (Consommateurs &amp; Seniors)</text>
    <text x="54" y="38" font-size="9" font-weight="600" fill="#C26750">PWA Mobile-First · Accessibilité RGAA (forts contrastes)</text>
    <line x1="14" y1="48" x2="411" y2="48" stroke="#E8B4A6" stroke-width="0.8" />
    <text x="14" y="66" font-size="9" font-weight="500" fill="#243342">Composants : Vitrines commerçantes, Panier multi-boutiques, Pass QR</text>
  </g>

  <!-- Carte 1.2 : Espace Commerçant -->
  <g transform="translate(508, 122)">
    <rect x="0" y="0" width="425" height="84" rx="8" fill="#EBF3ED" stroke="#7EA88D" stroke-width="1" />
    <circle cx="30" cy="28" r="15" fill="#4A7A5B" />
    <text x="30" y="33" text-anchor="middle" font-size="13" fill="#FFFFFF">COM</text>
    <text x="54" y="24" font-size="11" font-weight="700" fill="#2E583D">ESPACE COMMERÇANT (Artisans de quartier)</text>
    <text x="54" y="38" font-size="9" font-weight="600" fill="#4A7A5B">Web App POS Caisse · Scan express &lt; 3s</text>
    <line x1="14" y1="48" x2="411" y2="48" stroke="#A9C7B2" stroke-width="0.8" />
    <text x="14" y="66" font-size="9" font-weight="500" fill="#243342">Composants : Gestion catalogue &amp; stocks, Validation retraits C&amp;C</text>
  </g>

  <!-- Carte 1.3 : Portail DSI Mairie -->
  <g transform="translate(970, 122)">
    <rect x="0" y="0" width="425" height="84" rx="8" fill="#FEF7EB" stroke="#DCB162" stroke-width="1" />
    <circle cx="30" cy="28" r="15" fill="#C48B28" />
    <text x="30" y="33" text-anchor="middle" font-size="13" fill="#FFFFFF">DSI</text>
    <text x="54" y="24" font-size="11" font-weight="700" fill="#845A11">PORTAIL DSI MAIRIE &amp; COLLECTIVITÉ</text>
    <text x="54" y="38" font-size="9" font-weight="600" fill="#C48B28">Dashboard Décisionnel · Traçabilité anonymisée RGPD</text>
    <line x1="14" y1="48" x2="411" y2="48" stroke="#E6CB8F" stroke-width="0.8" />
    <text x="14" y="66" font-size="9" font-weight="500" fill="#243342">Composants : Indicateurs d'activité, Fréquentation piétonne, Sondages</text>
  </g>

  <!-- ======================================================== -->
  <!-- LIAISON TIER 1 -> TIER 2 : CONTRAT FORMEL D'INTERFACE    -->
  <!-- ======================================================== -->
  <line x1="720" y1="219" x2="720" y2="267" stroke="#243342" stroke-width="2" stroke-dasharray="4 3"/>
  <polygon points="720,271 715,261 725,261" fill="#243342"/>
  
  <g transform="translate(440, 226)">
    <rect x="0" y="0" width="560" height="38" rx="8" fill="#FFFFFF" stroke="#243342" stroke-width="1.2" filter="url(#shadow-soft)"/>
    <text x="280" y="16" text-anchor="middle" font-size="10.5" font-weight="700" fill="#243342">PROTOCOLE D'ÉCHANGE : HTTPS / RESTful · SPÉCIFICATION OPENAPI 3.1</text>
    <text x="280" y="30" text-anchor="middle" font-size="9" font-weight="500" fill="#5A6578">Authentification Stateless JWT Bearer · Routage Multi-Tenant : /api/v1/tenants/{tenant_id}/...</text>
  </g>

  <!-- ======================================================== -->
  <!-- TIER 2 : SERVEUR BACKEND APPLICATIF (SPRING BOOT 3.3)    -->
  <!-- ======================================================== -->
  <rect x="25" y="275" width="910" height="206" rx="10" fill="#FFFFFF" stroke="#8B9EAF" stroke-width="1.4" filter="url(#shadow-card)"/>
  <rect x="25" y="275" width="910" height="32" rx="10" fill="#243342" />
  <text x="45" y="296" font-size="11.5" font-weight="700" fill="#FFFFFF">TIER 2 — MONOLITHE MODULAIRE BACKEND (Spring Boot 3.3 / Java 21)</text>

  <!-- Badges technos Backend -->
  <g transform="translate(490, 279)">
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="125" height="24" rx="12" fill="#FFFFFF" stroke="#8B9EAF" stroke-width="1"/>
      <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg" x="8" y="4" width="16" height="16" />
      <text x="30" y="16" font-size="10" font-weight="600" fill="#243342">Java 21 LTS</text>
    </g>

    <g transform="translate(135, 0)">
      <rect x="0" y="0" width="145" height="24" rx="12" fill="#FFFFFF" stroke="#8B9EAF" stroke-width="1"/>
      <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/spring/spring-original.svg" x="8" y="4" width="16" height="16" />
      <text x="30" y="16" font-size="10" font-weight="600" fill="#243342">Spring Boot 3.3</text>
    </g>

    <g transform="translate(290, 0)">
      <rect x="0" y="0" width="125" height="24" rx="12" fill="#FFFFFF" stroke="#8B9EAF" stroke-width="1"/>
      <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/maven/maven-original.svg" x="8" y="4" width="16" height="16" />
      <text x="30" y="16" font-size="10" font-weight="600" fill="#243342">Maven 3.9</text>
    </g>
  </g>

  <!-- Carte 2.1 : Profils & Sécurité -->
  <g transform="translate(45, 317)">
    <rect x="0" y="0" width="415" height="72" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="14" y="24" font-size="11" font-weight="700" fill="#243342">Module Profils, Authentification &amp; RBAC</text>
    <line x1="14" y1="34" x2="401" y2="34" stroke="#E2DDD5" stroke-width="0.8" />
    <text x="14" y="54" font-size="9" font-weight="600" fill="#C26750">Techno : Spring Security 6 · JJWT (Java JWT) · Hachage SHA-256</text>
  </g>

  <!-- Carte 2.2 : Catalogue & Click & Collect -->
  <g transform="translate(495, 317)">
    <rect x="0" y="0" width="415" height="72" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="14" y="24" font-size="11" font-weight="700" fill="#243342">Module Catalogue, Stocks &amp; Réservation 2PC</text>
    <line x1="14" y1="34" x2="401" y2="34" stroke="#E2DDD5" stroke-width="0.8" />
    <text x="14" y="54" font-size="9" font-weight="600" fill="#4A7A5B">Techno : Spring Data JPA · Hibernate 6 · Jakarta Validation</text>
  </g>

  <!-- Carte 2.3 : Double Fidélité & VFP -->
  <g transform="translate(45, 399)">
    <rect x="0" y="0" width="415" height="72" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="14" y="24" font-size="11" font-weight="700" fill="#243342">Module Double Fidélité &amp; Moteur VFP</text>
    <line x1="14" y1="34" x2="401" y2="34" stroke="#E2DDD5" stroke-width="0.8" />
    <text x="14" y="54" font-size="9" font-weight="600" fill="#C48B28">Techno : Spring @Scheduled · Batch SQL glissant nocturne (15j)</text>
  </g>

  <!-- Carte 2.4 : Statistiques & RGPD -->
  <g transform="translate(495, 399)">
    <rect x="0" y="0" width="415" height="72" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="14" y="24" font-size="11" font-weight="700" fill="#243342">Module Reporting Municipal &amp; Conformité RGPD</text>
    <line x1="14" y1="34" x2="401" y2="34" stroke="#E2DDD5" stroke-width="0.8" />
    <text x="14" y="54" font-size="9" font-weight="600" fill="#243342">Techno : Requêtes SQL natives d'agrégation · k-anonymat strict</text>
  </g>

  <!-- ======================================================== -->
  <!-- LIAISON TIER 2 <-> TIER 3                                -->
  <!-- ======================================================== -->
  <line x1="935" y1="378" x2="965" y2="378" stroke="#243342" stroke-width="2"/>
  <polygon points="965,378 957,374 957,382" fill="#243342"/>
  <polygon points="935,378 943,374 943,382" fill="#243342"/>
  <text x="950" y="368" text-anchor="middle" font-size="8" font-weight="700" fill="#243342">JDBC</text>
  <text x="950" y="391" text-anchor="middle" font-size="7" font-weight="600" fill="#5A6578">HikariCP</text>

  <!-- ======================================================== -->
  <!-- TIER 3 : PERSISTANCE RELATIONNELLE (POSTGRESQL 16)       -->
  <!-- ======================================================== -->
  <rect x="965" y="275" width="450" height="206" rx="10" fill="#FFFFFF" stroke="#8B9EAF" stroke-width="1.4" filter="url(#shadow-card)"/>
  <rect x="965" y="275" width="450" height="32" rx="10" fill="#243342" />
  <text x="985" y="296" font-size="11.5" font-weight="700" fill="#FFFFFF">TIER 3 — PERSISTANCE RELATIONNELLE (ACID)</text>

  <g transform="translate(985, 317)">
    <rect x="0" y="0" width="410" height="154" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    
    <g transform="translate(178, 20)">
      <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg" x="0" y="0" width="54" height="54" />
    </g>
    
    <text x="205" y="100" text-anchor="middle" font-size="14" font-weight="700" fill="#243342">PostgreSQL 16 (SGBD-R)</text>
    <text x="205" y="122" text-anchor="middle" font-size="10" font-weight="600" fill="#2B5270">Intégrité Transactionnelle Strictement Garantie (ACID)</text>
  </g>

  <!-- ======================================================== -->
  <!-- LIAISON TIER 2 -> TIER 4 : APPELS CLIENTS HTTP           -->
  <!-- ======================================================== -->
  <line x1="720" y1="481" x2="720" y2="505" stroke="#243342" stroke-width="1.8" stroke-dasharray="3 2"/>
  <polygon points="720,509 716,500 724,500" fill="#243342"/>
  
  <g transform="translate(510, 485)">
    <rect x="0" y="0" width="420" height="18" rx="9" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="210" y="12" text-anchor="middle" font-size="8.5" font-weight="600" fill="#5A6578">Appels HTTP Clients (Spring RestClient) · Émulation des protocoles tiers</text>
  </g>

  <!-- ======================================================== -->
  <!-- TIER 4 : SIMULATEURS PARTENAIRES (MOCKS REST DOCKERISÉS) -->
  <!-- ======================================================== -->
  <rect x="25" y="510" width="1390" height="110" rx="10" fill="#FFFFFF" stroke="#DCD6CD" stroke-width="1.2" stroke-dasharray="4 3" filter="url(#shadow-card)"/>
  <rect x="25" y="510" width="1390" height="28" rx="10" fill="#F5F2EB" />
  <text x="45" y="529" font-size="11" font-weight="700" fill="#243342">TIER 4 — SIMULATEURS PARTENAIRES &amp; SYSTÈMES EXTERNES (Mocks REST OpenAPI 3.1)</text>
  <text x="1395" y="529" text-anchor="end" font-size="9.5" font-weight="500" fill="#5A6578">Bouchons Dockerisés Autonomes pour Environnement de Recette (Isolement Réseau)</text>

  <!-- Carte 4.1 : Mock Banque -->
  <g transform="translate(45, 546)">
    <rect x="0" y="0" width="425" height="64" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="14" y="22" font-size="11" font-weight="700" fill="#243342">Mock Passerelle Bancaire (Izli / Carte Bancaire)</text>
    <line x1="14" y1="31" x2="411" y2="31" stroke="#E2DDD5" stroke-width="0.8" />
    <text x="14" y="49" font-size="8.5" font-weight="500" fill="#334155">Rôle : Émulation pré-autorisation, débit global panier mutualisé &amp; rollback 2PC</text>
  </g>

  <!-- Carte 4.2 : Mock Mobilité -->
  <g transform="translate(508, 546)">
    <rect x="0" y="0" width="425" height="64" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="14" y="22" font-size="11" font-weight="700" fill="#243342">Mock Réseau de Transports Urbains (Ilévia Pass Pass)</text>
    <line x1="14" y1="31" x2="411" y2="31" stroke="#E2DDD5" stroke-width="0.8" />
    <text x="14" y="49" font-size="8.5" font-weight="500" fill="#334155">Rôle : Émission de titres de bus dématérialisés &amp; QR Code billettique VFP</text>
  </g>

  <!-- Carte 4.3 : Mock Voirie -->
  <g transform="translate(970, 546)">
    <rect x="0" y="0" width="425" height="64" rx="6" fill="#FAF9F6" stroke="#DCD6CD" stroke-width="1"/>
    <text x="14" y="22" font-size="11" font-weight="700" fill="#243342">Mock Stationnement Voirie (Horodateurs Municipaux)</text>
    <line x1="14" y1="31" x2="411" y2="31" stroke="#E2DDD5" stroke-width="0.8" />
    <text x="14" y="49" font-size="8.5" font-weight="500" fill="#334155">Rôle : Franchise de 20 minutes gratuites par lecture de plaque d'immatriculation</text>
  </g>

  <!-- ======================================================== -->
  <!-- SOCLE DEVOPS, CONTENEURISATION & QUALITÉ LOGICIELLE      -->
  <!-- ======================================================== -->
  <rect x="25" y="630" width="1390" height="130" rx="10" fill="#243342" filter="url(#shadow-card)"/>
  
  <text x="45" y="652" font-size="11.5" font-weight="700" fill="#FFFFFF">SOCLE DEVOPS, CONTENEURISATION &amp; QUALITÉ LOGICIELLE (JALONS R1 · R2)</text>

  <g transform="translate(45, 664)">
    <!-- Box 1 : Docker -->
    <rect x="0" y="0" width="425" height="82" rx="6" fill="#FAF9F6" />
    <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg" x="12" y="29" width="24" height="24" />
    <text x="44" y="24" font-size="10.5" font-weight="700" fill="#243342">Docker &amp; Docker Compose v2</text>
    <text x="44" y="44" font-size="8.5" font-weight="600" fill="#0284C7">Multi-conteneurs (Front, Back, DB, Mocks) · Réseau bridge</text>
    <text x="44" y="62" font-size="8.5" font-weight="400" fill="#5A6578">Déploiement reproductible en une commande : docker compose up</text>

    <!-- Box 2 : GitLab -->
    <rect x="463" y="0" width="425" height="82" rx="6" fill="#FAF9F6" />
    <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/gitlab/gitlab-original.svg" x="475" y="29" width="24" height="24" />
    <text x="507" y="24" font-size="10.5" font-weight="700" fill="#243342">GitLab Forge (Université de Lille)</text>
    <text x="507" y="44" font-size="8.5" font-weight="600" fill="#E24329">Pipelines CI/CD (.gitlab-ci.yml) · Tests unitaires JUnit 5</text>
    <text x="507" y="62" font-size="8.5" font-weight="400" fill="#5A6578">Versioning branches (main, develop), validation DoD &amp; Qualimétrie</text>

    <!-- Box 3 : OpenAPI -->
    <rect x="925" y="0" width="425" height="82" rx="6" fill="#FAF9F6" />
    <rect x="935" y="29" width="24" height="24" rx="4" fill="#4A7A5B" />
    <text x="947" y="45" text-anchor="middle" font-size="12" font-weight="700" fill="#FFFFFF">OA</text>
    <text x="967" y="24" font-size="10.5" font-weight="700" fill="#243342">Spécifications OpenAPI 3.1 &amp; Swagger-UI</text>
    <text x="967" y="44" font-size="8.5" font-weight="600" fill="#4A7A5B">Contrat d'interface formel partagé Front-End &amp; Back-End</text>
    <text x="967" y="62" font-size="8.5" font-weight="400" fill="#5A6578">Documentation interactive, DTOs normalisés et typage strict</text>
  </g>
</svg>

</div>
</div>

## 4.2. Choix de la pile technologique (Backend, Frontend, Données)

Les choix techniques présentés ci-dessous ont été guidés par trois critères simples : la fiabilité des technologies, la bonne maîtrise des outils par l'équipe et la simplicité de mise en œuvre :

- **Backend applicatif : Java (Spring Boot / J2E) avec Maven**
  - *Justification :* Java Spring Boot répond aux exigences du cahier des charges pour la mise en place d'une architecture orientée composants d'entreprise. Il assure une gestion transactionnelle robuste indispensable au protocole de réservation des stocks et à la cohérence de la fidélité, ainsi qu'une sécurité éprouvée (Spring Security pour les accès commerçants et municipaux). Maven garantit la reproductibilité des builds. Cette orientation préliminaire sera confrontée à une solution alternative légère lors des expérimentations du jalon R2.
- **Frontend utilisateur et commerçant : React avec TypeScript et Tailwind CSS**
  - *Justification :* React permet de construire des interfaces découpées en composants réutilisables, ce qui facilite la mise au point conjointe des écrans citoyens et commerçants. Conçu sous forme d'application web réactive (Progressive Web App), le service est directement utilisable depuis un navigateur mobile sans imposer aux usagers de télécharger une application dédiée sur les magasins d'applications.
- **Base de données relationnelle : PostgreSQL (version 16)**
  - *Justification :* Les transactions commerciales, les mouvements de stocks et les règles de fidélité nécessitent une intégrité relationnelle absolue (propriétés ACID). PostgreSQL constitue une référence éprouvée pour ce type d'usage, assurant une parfaite étanchéité des données et une gestion robuste des index.

## 4.3. Outillage collaboratif, intégration continue et simulateurs

- **Gestion de versions et forge logicielle : GitLab (Université de Lille)**
  - *Justification :* La forge institutionnelle de l'université centralise notre code source et garantit une traçabilité totale et un audit transparent de l'ensemble de nos travaux pour la maîtrise d'ouvrage. Nous adoptons une gestion de branches simple et lisible avec une branche principale stable (`main`), une branche de développement (`develop`) et des branches de fonctionnalités isolées.
- **Contrat d'interface formalisé : Spécification OpenAPI 3.1 (Swagger)**
  - *Justification :* Pour assurer une collaboration fluide entre l'architecture back-end (Gautam Demeulemeester) et l'architecture front-end (Ilyas Ait Ali), l'ensemble des points d'entrée d'API fera l'objet d'une documentation OpenAPI claire. Cela évite les malentendus techniques et permet de paralléliser les développements en toute confiance.
- **Conteneurisation et exécution : Docker & Docker Compose**
  - *Justification :* Docker permet d'encapsuler chaque composant (backend, frontend, base PostgreSQL et simulateurs) dans des environnements isolés et reproductibles. Ce choix garantit que la plateforme pourra être déployée et démarrée sur les postes de recette de la collectivité à l'aide d'une simple commande `docker compose up`, sans risque de conflits de versions logicielles.
- **Simulateurs de services partenaires (Mocks REST) :**
  - *Justification :* Ne pouvant pas nous connecter en direct aux infrastructures privées des banques (rechargement Izli), des réseaux de transport en commun (Ilévia) ou des serveurs de stationnement municipaux, ces briques seront simulées par des bouchons applicatifs légers intégrés dans l'environnement Docker, permettant de tester l'ensemble des parcours utilisateurs en parfaite autonomie.

<div style="page-break-after: always;"></div>

# 5. Diagramme de Gantt annuel prévisionnel

## 5.1. Calendrier des jalons contractuels officiels

Le calendrier de développement de ShopLoc est structuré sur sept mois, de septembre 2026 à mars 2027, en s'alignant sur les cinq jalons fixés par la maîtrise d'ouvrage :

| Jalon contractuel | Date de remise | Format de restitution | Livrables et objectifs attendus |
|---|---|---|---|
| **R1 — Cadrage & Appel d'offres** | 18 septembre 2026 (18h) | Dossier PDF & Soutenance le 21/09 (Amphi Turing) | Présentation de l'entreprise, CVs de l'équipe, analyse des besoins, premiers choix d'outils, Gantt et étude des coûts. |
| **R2 — Outillage & DevOps** | 12 octobre 2026 | Dossier technique d'outillage | Sélection et justification approfondie des outils, configuration du dépôt Git, conteneurs Docker et simulateurs partenaires. |
| **R3 — Viabilité financière** | 30 novembre 2026 | Dossier financier et étude de rentabilité | Étude économique complète basée sur la méthode des coûts complets, seuil de rentabilité et pérennité du modèle. |
| **R4 — Architecture V1 & Prototype** | 18 décembre 2026 (18h) | Dossier d'architecture, code & Soutenance le 04/01/2027 | Documentation d'architecture logicielle et premier démonstrateur opérationnel sous Docker (catalogue et réservation Click & Collect). |
| **R5 — Version complète V2** | 19 mars 2027 (18h) | Système complet & Soutenance le 22/03/2027 | Version finale intégrant la fidélité VFP, le portail municipal, les tests d'intégration complets et le bilan d'exploitation. |

## 5.2. Diagramme de Gantt prévisionnel sur l'année

Le diagramme ci-après retrace le cheminement chronologique des activités, en tenant compte des périodes de congés et des échéances pour sécuriser nos livraisons :

<div class="diagram-container" style="margin: 0; padding: 0; border: none; background: transparent;">
  <img src="figures/fig_5_1_gantt_annuel_officiel.png" alt="Figure 5.1 — Diagramme de Gantt annuel prévisionnel du projet ShopLoc" style="width: 100%; max-width: 100%; height: auto; display: block; margin: 0 auto; border-radius: 4px;" />
  <div class="diagram-caption" style="margin-top: 6pt;">Figure 5.1 — Diagramme de Gantt annuel prévisionnel du projet ShopLoc (Jalons officiels R1 à R5 — 2026-2027)</div>
</div>

Le projet s'organise autour de cinq phases de travail coordonnées :
- **Phase 1 (Septembre - Mi-octobre 2026) :** Réponse à l'appel d'offres, formalisation des exigences fonctionnelles et mise en place de la chaîne d'outils partagée (Jalons R1 et R2).
- **Phase 2 (Mi-octobre - Fin novembre 2026) :** Élaboration de l'étude financière par la méthode des coûts complets et conception préliminaire des schémas de données (Jalon R3).
- **Phase 3 (Décembre 2026 - Début janvier 2027) :** Développement du socle applicatif et du prototype fonctionnel Click & Collect mutualisé sous Docker (Jalon R4).
- **Phase 4 (Janvier - Mi-mars 2027) :** Implémentation du moteur de double fidélité, de l'espace de supervision municipal, des simulateurs de services et des tests de non-régression (Jalon R5).
- **Phase 5 (Fin mars 2027) :** Recette d'ensemble, rédaction de la documentation finale et soutenance de clôture du projet.

## 5.3. Dispositif de sécurisation des délais et gestion des risques

Pour prévenir les retards et assurer la régularité du travail, notre équipe met en place trois mesures d'organisation simples :
- **Estimation réaliste du temps de travail :** L'investissement de chaque membre est calibré à environ 6 à 8 heures de travail effectif par semaine sur les 25 semaines actives du projet, soit un volume global de 900 à 1 000 heures de travail sur l'ensemble de la réalisation.
- **Règle du gel des modifications (Buffer de 72 heures) :** Avant chaque échéance de remise contractuelle, un arrêt des ajouts fonctionnels est programmé 72 heures à l'avance. Cette période est exclusivement réservée à la relecture collective des documents, aux tests d'installation sur des ordinateurs témoins et à la préparation des présentations orales (15 minutes de présentation suivies de 5 minutes d'échanges).
- **Point hebdomadaire d'alerte :** Lors de notre réunion hebdomadaire animée par Abdelkader Heddi, tout retard sur une tâche est identifié immédiatement afin de réajuster la charge ou d'organiser un binôme d'entraide.

<div style="page-break-after: always;"></div>

# 6. Étude financière et méthode des coûts complets

Le modèle économique d'un système d'information territorial comme ShopLoc doit être calculé de façon rigoureuse et transparente. Conformément aux consignes de l'appel d'offres et aux principes de gestion financière (*La gestion stratégique des coûts*), notre chiffrage applique la **méthode des coûts complets** pour déterminer le coût de revient réel de la solution développée par Garik et justifier le tarif de l'abonnement annuel proposé à la collectivité.

## 6.1. Identification et sourçage des charges du projet

L'évaluation financière repose sur des charges réelles et documentées, découpées entre les charges directes de personnel et les charges indirectes de fonctionnement :

### Charges directes de personnel (Réalisation logicielle)
La phase de conception et de développement mobilise les 5 membres de Garik sur les 6 mois actifs du projet (septembre 2026 à février 2027 inclus). En phase de lancement, nous valorisons ce travail sur la base d'une indemnité mensuelle de **800,00 € par membre et par mois**, soit :
$$\text{Charge directe mensuelle de l'équipe} = 5 \times 800{,}00\text{ €} = 4\,000{,}00\text{ € / mois}$$
$$\text{Charge directe totale de réalisation (6 mois)} = 6 \times 4\,000{,}00\text{ €} = \mathbf{24\,000{,}00\text{ €}}$$

### Charges indirectes et frais externes sourcés
Les charges indirectes correspondent aux dépenses d'infrastructure technique, de communication et de fonctionnement nécessaires à l'exploitation du service :
- **Hébergement Cloud VPS dédié (OVHcloud, offre Comfort) :** Serveur sécurisé sous Linux (4 cœurs vCPU, 8 Go de mémoire vive, stockage 100 Go NVMe, bande passante 1 Gbps et sauvegardes quotidiennes automatisées) permettant d'isoler les conteneurs Docker de la collectivité : **35,00 € HT / mois**, soit **420,00 € HT / an**.
- **Nom de domaine territorial (OVHcloud) :** Réservation d'un nom de domaine institutionnel en `.fr` avec protection DNSSEC et gestion de la zone DNS : **10,00 € HT / an**.
- **Certificats de sécurité SSL/TLS (Let's Encrypt) :** Génération et renouvellement automatisé des certificats HTTPS de chiffrement : **0,00 €** (solution open-source).
- **Service d'envoi de courriels transactionnels (Brevo, ex-Sendinblue, plan Starter) :** Envoi des notifications de commande, alertes de rupture de stock aux commerçants et réinitialisation de mots de passe : **19,00 € HT / mois**, soit **228,00 € HT / an**.
- **Assurance Responsabilité Civile Professionnelle (RC Pro entreprise numérique) :** Couverture des risques d'exploitation et de responsabilité numérique : **350,00 € HT / an**.
- **Frais généraux d'outillage et amortissement matériel :** Amortissement partiel des postes de travail des cinq membres de l'équipe et licences : **500,00 € HT / an**.

Le montant global des charges indirectes s'élève donc à :
$$\text{Total des charges indirectes annuelles} = 420 + 10 + 0 + 228 + 350 + 500 = \mathbf{1\,508{,}00\text{ € HT / an}}$$

La masse totale des charges à répartir s'établit ainsi à :
$$\text{Masse totale des charges annuelles} = 24\,000{,}00 + 1\,508{,}00 = \mathbf{25\,508{,}00\text{ € HT}}$$

## 6.2. Découpage en centres d'analyse auxiliaires et principaux

Conformément à la méthode des coûts complets, l'activité de l'entreprise Garik est structurée en cinq centres d'analyse distincts :
1. **Centres auxiliaires (Centres de support interne) :**
   - **Administration & Direction de projet :** Pilotage global, gestion administrative, conventions et réunions d'équipe (4 500,00 € de charges réparties).
   - **Support Infrastructure & Outils :** Hébergement technique, administration des serveurs et maintenance de la forge logicielle (2 008,00 € comprenant les 1 508,00 € de frais externes et 500,00 € de travail technique interne).
2. **Centres principaux (Centres opérationnels) :**
   - **Vente & Relations Collectivités :** Prospection des municipalités, contractualisation tripartite et accompagnement institutionnel.
   - **Réalisation & Développement Logiciel :** Conception technique, développement frontend/backend, intégration des bases de données et tests.
   - **Maintenance & Support Utilisateurs :** Résolution d'anomalies, assistance technique auprès des commerçants et maintien en condition opérationnelle.

## 6.3. Tableau de répartition primaire et secondaire des charges

La répartition primaire affecte l'ensemble des charges directes et indirectes dans les cinq centres. La répartition secondaire déverse ensuite les coûts des centres auxiliaires vers les centres principaux selon des clés de répartition proportionnelles à l'activité :

- **Clé de déversement du centre Administration :** 20% vers le centre Vente, 50% vers le centre Réalisation, et 30% vers le centre Maintenance.
- **Clé de déversement du centre Support Infrastructure :** 10% vers le centre Vente, 60% vers le centre Réalisation, et 30% vers le centre Maintenance.

Le tableau ci-dessous détaille les calculs de répartition :

| Intitulé des centres d'analyse | Charges directes de personnel | Charges indirectes externes | Total Répartition Primaire | Déversement Administration | Déversement Infrastructure | Coût Total Après Répartition Secondaire |
|---|---|---|---|---|---|---|
| **Administration (Auxiliaire)** | 4 000,00 € | 500,00 € | 4 500,00 € | -4 500,00 € | — | **0,00 €** |
| **Infrastructure (Auxiliaire)** | 1 000,00 € | 1 008,00 € | 2 008,00 € | — | -2 008,00 € | **0,00 €** |
| **Vente & Collectivités (Principal)** | 3 000,00 € | — | 3 000,00 € | +900,00 € (20%) | +200,80 € (10%) | **4 100,80 €** |
| **Réalisation & Dev (Principal)** | 14 000,00 € | — | 14 000,00 € | +2 250,00 € (50%) | +1 204,80 € (60%) | **17 454,80 €** |
| **Maintenance & Support (Principal)** | 2 000,00 € | — | 2 000,00 € | +1 350,00 € (30%) | +602,40 € (30%) | **3 952,40 €** |
| **Total Général** | **24 000,00 €** | **1 508,00 €** | **25 508,00 €** | **0,00 €** | **0,00 €** | **25 508,00 €** |

## 6.4. Définition des unités d'œuvre et calcul des coûts unitaires

Pour chaque centre principal, nous définissons une Unité d'Œuvre (UO) représentative de son volume d'activité sur la première année d'exploitation de la plateforme :

| Centre d'analyse principal | Nature de l'Unité d'Œuvre (UO) | Volume prévisionnel d'UO (Année 1) | Formule de calcul du coût unitaire | Coût complet unitaire de l'UO |
|---|---|---|---|---|
| **Vente & Relations Collectivités** | Commune conventionnée déployée | 3 communes partenaires | 4 100,80 € / 3 communes | **1 366,93 € HT / commune** |
| **Réalisation & Développement** | Heure d'ingénierie logicielle | 800 heures de développement | 17 454,80 € / 800 heures | **21,82 € HT / heure de dev** |
| **Maintenance & Support** | Commerçant adhérent accompagné | 60 commerçants actifs | 3 952,40 € / 60 commerçants | **65,87 € HT / commerçant / an** |

Ces coûts unitaires reflètent le fonctionnement de notre structure : le coût d'une heure de développement (21,82 € HT) reste très accessible pour une commune tout en valorisant convenablement le travail accompli.

## 6.5. Déduction et justification du modèle économique SaaS

La méthode des coûts complets permet de calculer le coût de revient exact du déploiement de ShopLoc dans une commune moyenne (comptant environ 20 commerces partenaires la première année) :
- **Quote-part du centre Vente & Collectivités :** 1 366,93 € HT (frais d'adhésion et mise en place de la convention).
- **Amortissement de la réalisation logicielle :** La réalisation logicielle initiale (17 454,80 € HT) est conçue comme un investissement réutilisable amorti sur 3 ans et mutualisé entre 3 communes pilotes, soit une charge annuelle de :
$$\text{Quote-part annuelle de développement} = \frac{17\,454{,}80\text{ €}}{3\text{ ans} \times 3\text{ communes}} \approx \mathbf{1\,939{,}42\text{ € HT / commune / an}}$$
- **Quote-part de maintenance pour 20 commerçants :** $20 \times 65{,}87\text{ €} = \mathbf{1\,317{,}40\text{ € HT / an}}$.
- **Hébergement Cloud VPS dédié et nom de domaine communal :** $420 + 10 = \mathbf{430{,}00\text{ € HT / an}}$.

En additionnant ces composantes récurrentes à l'issue de la première phase de démarrage, le coût de revient annuel complet d'une collectivité s'établit à :
$$\text{Coût de revient complet annuel pour une commune} \approx 1\,939{,}42 + 1\,317{,}40 + 430{,}00 = \mathbf{3\,686{,}82\text{ € HT / an}}$$

### Tarification proposée et équité territoriale
Ce calcul objectif justifie pleinement la tarification forfaitaire que l'entreprise Garik soumet à la maîtrise d'ouvrage :
- **Abonnement annuel forfaitaire pour la collectivité :** **3 900,00 € HT / an** (soit seulement **325,00 € HT par mois** pour l'ensemble de la commune).
- Ce montant couvre l'intégralité des coûts d'exploitation et de maintenance, amortit le développement initial et dégage une marge de sécurité de gestion d'environ 5% (213,18 €/an) permettant de faire face aux imprévus techniques.
- Pour la municipalité, cet investissement reste modeste au regard de son budget global de développement économique, tout en garantissant un dispositif **entièrement gratuit pour les usagers** et **sans aucune commission prélevée sur les artisans et commerçants**.


