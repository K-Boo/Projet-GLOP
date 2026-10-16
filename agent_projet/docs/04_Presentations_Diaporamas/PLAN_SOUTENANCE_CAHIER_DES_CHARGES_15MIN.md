# PLAN DE PRÉSENTATION ORALE (15 MIN) — SOUTENANCE DU CAHIER DES CHARGES REMIS (R1)

## Société d'Ingénierie Logicielle Garik — Université de Lille — M2 MIAGE GLOP

---

### Fiche Signalétique de l'Épreuve

| Paramètre | Valeur de référence |
|---|---|
| **Document support officiel** | Cahier des Charges R1 remis (`CAHIER_DES_CHARGES_R1.md` / `ShopLoc_Cahier_des_Charges_Livrable_R1.pdf`) |
| **Durée totale de parole** | 15 minutes strictes (suivies de 5 à 10 minutes de questions/réponses) |
| **Nombre d'intervenants** | 5 membres (temps de parole équitable : **3 minutes par personne**) |
| **Auditoire / Jury** | Maîtrise d'Ouvrage (Professeurs évaluateurs de l'UE GLOP) |
| **Posture professionnelle** | Société d'ingénierie Garik répondant à un appel d'offres territorial |

---

### 1. Vue d'Ensemble & Chronométrie de la Présentation

Le plan de présentation suit rigoureusement les **6 sections du Cahier des Charges remis**, réparties de façon cohérente selon les responsabilités opérationnelles des 5 équipiers :

```text
[00:00 - 03:00] Khalil Bouchama       : Section 1 (Entreprise Garik) & Section 2 (Équipe & Rôles) + APTE
[03:00 - 06:00] Abdelkader Heddi      : Section 3 (Acteurs, Benchmark Concurrentiel, Personas & Cas d'Usage)
[06:00 - 09:00] Gautam Demeulemeester : Section 3 (User Story Mapping aha.io & Découpage en 4 Modules)
[09:00 - 12:00] Rayane Alli           : Section 4 (Architecture 3-Tiers, Pile Tech, Mocks REST & Docker)
[12:00 - 15:00] Ilyas Ait Ali         : Section 5 (Gantt, Jalons, Risques) & Section 6 (Coûts Complets, SaaS)
```

---

### 2. Déroulé Détaillé par Intervenant (3 Minutes par Personne)

#### Intervenant 1 : Khalil Bouchama
- **Rôles officiels** : Scrum Master R1, Responsable Qualité & Déploiement
- **Sections couvertes** : Section 1 (Entreprise Garik), Section 2 (Équipe projet) et début Section 3 (Besoin APTE)
- **Minutage** : 00:00 à 03:00 (3 minutes)

| Temps | Contenu et messages clés à délivrer |
|---|---|
| **00:00 - 00:50** | **Section 1 : Présentation de l'entreprise Garik & Vision territoriale**<br>- Création de la société Garik par 5 ingénieurs MIAGE : double compétence technique et gestion de projet.<br>- Réponse à l'appel d'offres ShopLoc face à la dévitalisation des cœurs de ville face aux géants du e-commerce.<br>- Les 3 piliers éthiques : **gratuité citoyenne**, **0 % de commission marchande** (préservation intégrale des marges des artisans) et **financement communal mutualisé**. |
| **00:50 - 01:45** | **Section 2 : Compétences de l'équipe, rôles et gouvernance Agile**<br>- 5 profils complémentaires issus d'expériences en entreprise (Alstom, AG2R La Mondiale, Damart, Mondial Relay, Sopra Steria).<br>- Répartition des 6 rôles recommandés par l'UE GLOP (Qualité, Communication, Déploiement, Outils, Archi Back-Office, Archi Front-Office).<br>- Organisation collégiale avec **Scrum Master tournant** à chaque jalon (R1 Khalil, R2 Rayane, R3 Gautam, R4 Ilyas, R5 Abdelkader). |
| **01:45 - 02:45** | **Section 3.1 : Analyse fonctionnelle du besoin (Méthode APTE)**<br>- Présentation de la Bête à cornes (Figure 3.1, norme AFNOR NF X 50-151).<br>- À qui le système rend service (citoyens, commerçants, collectivité), sur quoi il agit (dynamisme des cœurs de ville) et sa finalité (revitalisation locale sans livraison motorisée). |
| **02:45 - 03:00** | **Passage de relais verbal :**<br>*« Pour vous présenter la confrontation au marché, l'écosystème d'acteurs et les profils types issus de notre cadrage, je passe la parole à Abdelkader. »* |

---

#### Intervenant 2 : Abdelkader Heddi
- **Rôle officiel** : Responsable Communication & Relations MOA
- **Sections couvertes** : Section 3.2 (Acteurs & Benchmark) et Section 3.3 (Personas cibles)
- **Minutage** : 03:00 à 06:00 (3 minutes)

| Temps | Contenu et messages clés à délivrer |
|---|---|
| **03:00 - 03:50** | **Section 3.2 : Les 4 acteurs clés de l'écosystème ShopLoc**<br>- *Commerçants & artisans de proximité* : visibilité en ligne sans frais ni lourdeur de gestion.<br>- *Citoyens consommateurs* : achats locaux simplifiés, panier multi-boutiques et gratifications régulières.<br>- *Collectivité territoriale (Mairie / DSI)* : dynamisation du centre-ville, incitation aux mobilités douces, tableau de bord anonymisé (RGPD).<br>- *Partenaires délégués* : réseau de transports en commun (titres Ilévia) et voirie municipale (contrôle du stationnement 20 min). |
| **03:50 - 04:45** | **Section 3.2 : Benchmark comparatif et positionnement différenciant (Figure 3.2)**<br>- Confrontation de ShopLoc face à l'existant :<br>  1. *Plateformes globales (Amazon, Deliveroo)* : commissions prédatrices (15-30 %) et livraison motorisée délocalisée.<br>  2. *Marketplaces de proximité privées (Ollca, Epicery)* : commissions marchandes (8-15 %) et livraison à domicile.<br>  3. *Cartes de fidélité de ville (Proxity)* : pas de catalogue en ligne ni de panier d'achat mutualisé.<br>- Positionnement souverain de ShopLoc : ancrage physique piétonnier, gratuité pour l'usager, 0 % de commission, double fidélité. |
| **04:45 - 05:45** | **Section 3.3 : Les personas cibles du projet**<br>- Présentation concise des cas d'usage réels du sujet :<br>  - *Pierre (74 ans)* : senior fidèle de quartier, achats réguliers débloquant le bus gratuit pour son retour, carte physique QR code.<br>  - *Julie (31 ans)* : citadine active, panier Click & Collect avec calcul de trajet pédestre, recharge en ligne (type Izli).<br>  - *Arthur (34 ans)* : père de famille automobiliste, 20 minutes de parking offertes par le statut VFP pour ses achats.<br>  - *Suzanne (22 ans)* : commerçante Le Fournil, gestion simplifiée du catalogue et scan caisse express.<br>  - *Marius (27 ans)* : gestionnaire municipal DSI, supervision de l'impact économique et mobilité. |
| **05:45 - 06:00** | **Passage de relais verbal :**<br>*« Afin de détailler l'ingénierie des exigences avec notre cartographie des récits utilisateurs et le découpage modulaire du système, je cède la parole à Gautam. »* |

---

#### Intervenant 3 : Gautam Demeulemeester
- **Rôle officiel** : Responsable Architecture Back-Office & Données
- **Sections couvertes** : Section 3.4 (User Story Mapping) et Section 3.5 (Découpage Modulaire)
- **Minutage** : 06:00 à 09:00 (3 minutes)

| Temps | Contenu et messages clés à délivrer |
|---|---|
| **06:00 - 07:15** | **Section 3.4 : Cartographie des récits utilisateurs — User Story Mapping (Figure 3.3)**<br>- Application rigoureuse de la méthode officielle aha.io / Jeff Patton.<br>- Les 5 activités clés du Backbone :<br>  1. *Compte & Identité* (inscription, connexion, profils et plaque minéralogique).<br>  2. *Catalogue & Click & Collect* (fiche boutique, catalogue, panier groupé et calcul de trajet pédestre).<br>  3. *Caisse & Fidélité Boutique* (scan QR code, crédit de points et déblocage de cadeaux marchands).<br>  4. *Statut VFP & Mobilité* (comptabilisation de fréquence, ticket de bus et stationnement 20 min).<br>  5. *Pilotage & Supervision* (statistiques de ventes commerçant et indicateurs municipaux DSI).<br>- Découpage par release : **Release 1 (MVP R4/R5)** concentrée sur le cœur contractuel indispensable face à la **Release 2** d'évolutions. |
| **07:15 - 08:45** | **Section 3.5 : Découpage modulaire du système ShopLoc**<br>- Structuration en 4 modules opérationnels clairs :<br>  - *Module A — Gestion des acteurs & conventionnement* : validation mairie, comptes commerçants, fiches et horaires.<br>  - *Module B — Marketplace & Click & Collect mutualisé* : réservation des stocks en deux temps évitant les ruptures physiques, panier multi-boutiques, trajet piétonnier le plus court, exclusion stricte de la livraison à domicile.<br>  - *Module C — Double fidélité & statut VFP* : découplage strict entre la cagnotte privée du commerçant et la fidélité territoriale citoyenne VFP (règle des 10 passages sur 15 jours glissants).<br>  - *Module D — Portail de supervision municipale* : tableau de bord d'activité, animation locale par sondages QCM, gestion des no-shows et respect strict du RGPD. |
| **08:45 - 09:00** | **Passage de relais verbal :**<br>*« Pour vous présenter les choix d'architecture logicielle, les technologies retenues et les simulateurs d'intégration, je laisse la parole à Rayane. »* |

---

#### Intervenant 4 : Rayane Alli
- **Rôle officiel** : Spécialiste Outils & Ingénieur Logiciel
- **Sections couvertes** : Section 4 (Premiers choix justifiés d'outils logiciels)
- **Minutage** : 09:00 à 12:00 (3 minutes)

| Temps | Contenu et messages clés à délivrer |
|---|---|
| **09:00 - 10:15** | **Section 4.1 : Architecture applicative 3-tiers modulaire (Figure 4.1)**<br>- Proposition préliminaire pour le jalon R1 organisée en 4 niveaux étanches :<br>  1. *Tier Clients (Frontend)* : PWA responsive React 18, TypeScript 5, Tailwind CSS 3 (interfaces adaptées citoyens, commerçants et mairie).<br>  2. *Tier Backend & Services Métier* : Java 21 LTS et Spring Boot 3.3, architecture modulaire en contextes délimités (Profils, Click & Collect 2PC, Double Fidélité VFP, Dashboard).<br>  3. *Tier Données & Persistance* : PostgreSQL 16 garantissant les transactions ACID et la consistance des stocks.<br>  4. *Tier Simulateurs Partenaires* : Mocks REST OpenAPI 3.1 conteneurisés.<br>- Contrat d'interface documenté sous spécification **OpenAPI 3.1**. |
| **10:15 - 11:00** | **Section 4.2 : Justification des choix technologiques**<br>- Robustesse et typage de Java/Spring Boot et TypeScript pour sécuriser les flux de réservation et le calcul des règles de fidélité.<br>- Performance et fiabilité transactionnelle de PostgreSQL face aux besoins d'intégrité des commandes.<br>- Frugalité opérationnelle : absence de sur-ingénierie et adéquation parfaite avec les exigences du projet. |
| **11:00 - 11:45** | **Section 4.3 : Outillage collaboratif, simulateurs et Docker**<br>- Forge GitLab Université de Lille et pipeline d'intégration continue GitLab CI.<br>- **Simulateurs de services tiers (Mocks REST)** : simulation autonome des systèmes bancaires (rechargement Izli 2PC), transports Ilévia et horodateurs municipaux.<br>- Déploiement reproductible clé en main sous **Docker Compose** en une seule commande (`docker compose up`). |
| **11:45 - 12:00** | **Passage de relais verbal :**<br>*« Afin de clore cette présentation sur notre planification prévisionnelle de Gantt et l'étude financière par coûts complets, je donne la parole à Ilyas. »* |

---

#### Intervenant 5 : Ilyas Ait Ali
- **Rôle officiel** : Responsable Architecture Front-Office & Ergonomie
- **Sections couvertes** : Section 5 (Diagramme de Gantt) et Section 6 (Étude financière par coûts complets)
- **Minutage** : 12:00 à 15:00 (3 minutes)

| Temps | Contenu et messages clés à délivrer |
|---|---|
| **12:00 - 12:50** | **Section 5 : Planification annuelle, jalons contractuels & maîtrise des risques**<br>- Calendrier des 5 jalons contractuels du projet (R1 Cadrage 18/09, R2 Outillage 12/10, R3 Finance 30/11, R4 Proto V1 18/12, R5 Version finale 19/03).<br>- Présentation du Diagramme de Gantt annuel (Figure 5.1).<br>- Mesures de sécurisation des délais : volume réaliste de 6 à 8 h/semaine par équipier (~950 h au total), **buffer de 72 heures de gel des modifications** avant chaque livraison, réunion d'alerte hebdomadaire. |
| **12:50 - 14:00** | **Section 6 : Étude financière par la méthode des coûts complets**<br>- Application rigoureuse de la méthode enseignée (*La gestion stratégique des coûts*) :<br>  - *Charges directes* : 14 400 € (480 h de Main d'Œuvre Directe à 25 €/h + 2 400 € d'achats informatiques et hébergement Cloud VPS).<br>  - *Charges indirectes* : 36 000 € réparties en 4 centres d'analyse (Administration, Support Infra, Commercial, Production), avec déversement secondaire complet des centres auxiliaires.<br>  - *Coût des Unités d'Œuvre* : 184 € / heure commerciale (60 h) et 52 € / heure de dev (480 h).<br>  - *Coût de revient complet* : **50 400,00 € HT**.<br>  - *Marge bénéficiaire cible de 20 %* : 10 080,00 € HT, soit un Chiffre d'Affaires cible de **60 480,00 € HT**. |
| **14:00 - 14:40** | **Section 6.5 : Modèle économique retenu : Le forfait SaaS communal**<br>- Comparatif des 3 modèles (Licence logicielle on-premise, Commission transactionnelle, Forfait annuel SaaS).<br>- Rejet formel de la commission (contraire aux valeurs du projet et rejetée par les commerçants).<br>- Choix de **l'abonnement forfaitaire annuel SaaS** payé par la commune : revenus prévisibles, gratuité usagers, 0 % commission artisans. Coût mutualisé très accessible d'environ **3 900 € HT / an par commune** (soit seulement **325 € HT / mois**). |
| **14:40 - 15:00** | **Conclusion collective & Clôture :**<br>- Affirmation de l'engagement et de la cohésion de l'équipe Garik pour réussir les jalons à venir.<br>- Remerciement formel des membres du jury et ouverture de la séance de questions/réponses. |

---

### 3. Matrice de Répartition du Diaporama (12 Diapositives Recommandées)

Ce gabarit respecte un rythme d'environ **1 diapositive toutes les 1 minute 15**, idéal pour maintenir l'attention sans surcharger visuellement l'écran :

| N° | Titre de la diapositive | Orateur | Visuel officiel extrait du Cahier des Charges |
|---|---|---|---|
| **01** | Société Garik & Projet ShopLoc | Khalil | Cartouche officiel, logo Garik / ShopLoc, trombinoscope de l'équipe |
| **02** | Positionnement & Valeurs Fondamentales | Khalil | Les 3 piliers (gratuité, 0% commission, modèle communal) |
| **03** | Expression du Besoin Fondamental | Khalil | Diagramme Bête à cornes APTE (Figure 3.1) |
| **04** | Acteurs Clés & Benchmark Concurrentiel | Abdelkader | Matrice de positionnement concurrentiel 2 axes (Figure 3.2) |
| **05** | Profils Utilisateurs & Cas d'Usage Réels | Abdelkader | Synthèse visuelle des 5 personas (Pierre, Julie, Arthur, Suzanne, Marius) |
| **06** | Cartographie des Récits Utilisateurs | Gautam | Grille de User Story Mapping aha.io (Figure 3.3 en A4 paysage) |
| **07** | Découpage Modulaire du Système | Gautam | Schéma des 4 modules (Acteurs, Marketplace C&C, Double fidélité, DSI) |
| **08** | Architecture Applicative 3-Tiers Modulaire | Rayane | Cartographie technique normalisée 4 Tiers (Figure 4.1 avec logos) |
| **09** | Environnement DevOps, Simulateurs & Docker | Rayane | Schéma des mocks REST OpenAPI (Banque, Ilévia, Parking) et Docker Compose |
| **10** | Planification Annuelle & Jalons Contractuels | Ilyas | Diagramme de Gantt officiel R1 à R5 (Figure 5.1) et buffer 72h |
| **11** | Étude Financière : Coûts Complets & UO | Ilyas | Tableaux des centres d'analyse, calcul des UO et coût de revient (50 400 €) |
| **12** | Modèle SaaS Communal & Conclusion | Ilyas | Comparatif des modèles, forfait à 325 €/mois, conclusion et remerciements |

---

### 4. Protocole d'Aiguillage des Questions du Jury (Q&A)

Pendant les 5 à 10 minutes d'échange, le passage de parole doit refléter l'organisation professionnelle de l'équipe :

1. **Modération par le Scrum Master (Khalil)** :
   - Khalil accuse réception de la question du professeur, remercie brièvement et oriente vers le référent naturel du sujet.
2. **Attribution thématique des questions** :
   - *Expression des besoins, personas, dialogue MOA, positionnement* : **Abdelkader**
   - *Règles de gestion métier, déblocage VFP, User Story Mapping, modules fonctionnels* : **Gautam**
   - *Architecture logicielle, choix de stack (Spring/React/Postgres), simulateurs partenaires, Docker* : **Rayane**
   - *Planning de Gantt, gestion des risques, calculs des coûts complets, rentabilité, modèle SaaS* : **Ilyas**
   - *Gouvernance d'équipe, démarche qualité, conformité du livrable, méthode Scrum* : **Khalil**
3. **Règle de réponse collective** :
   - Une réponse doit être concise (30 à 45 secondes maximum).
   - Un autre membre peut intervenir en complément pour illustrer l'esprit d'équipe, sans jamais contredire son collègue.
