#!/usr/bin/env python3
"""
Mise à jour intégrale de GARIK_GLOP-2026-ADDENDUM-R1.md :
1. Suppression absolue de tous les symboles et encodages LaTeX ($...$, \\ge, \\pm, etc.) -> typographie française propre.
2. Remplacement des diagrammes en tirets/ASCII par les 4 vrais schémas vectoriels SVG aux normes ShopLoc.
3. Intégration des pages A4 paysage (.landscape-page) pour la Pieuvre, les Use Cases UML, la Matrice des Risques et le Gantt.
4. Formatage ultra-lisible de la Matrice des 10 Risques réels avec cotations initiales et résiduelles claires.
5. Suppression du tableau WBS des 22 tâches redondant avec le Gantt.
"""

import os
import re

MD_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs", "01_Cadrage_Et_Cahier_Des_Charges_R1", "GARIK_GLOP-2026-ADDENDUM-R1.md"))

new_content = """# ADDENDUM DE CADRAGE & RÉFÉRENTIEL DES CORRECTIFS R1
## Projet ShopLoc — Master 2 MIAGE — UE Génie Logiciel par la Pratique (GLOP) 2026-2027
### Université de Lille — Faculté des Sciences et Technologies — Département Informatique

## Cadre de Mission & Contexte Pédagogique

Cet addendum constitue le référentiel contractuel d'ingénierie corrective pour le premier jalon (R1) de l'UE Génie Logiciel par la Pratique (GLOP), Master 2 MIAGE, Université de Lille. Il complète formellement le document initial `GARIK_GLOP-2026-LIVRABLE-R1.pdf` (Version officielle du 18/09/2026) évalué par la maîtrise d'ouvrage (Laurence Duchien, Anne Etien, François Secchi, Jérémy Woirhaye).

---

## Préambule & Objet de l'Addendum

Le présent document constitue l'**Addendum officiel de cadrage et de régularisation** du premier livrable (Jalon R1), émis suite à la soutenance orale du 21 septembre 2026 et à la synthèse d'évaluation transmise par la maîtrise d'ouvrage (MOA).

Conformément aux directives de l'équipe pédagogique, cet addendum ne reproduit pas les éléments validés du premier livrable (CVs de l'équipe, méthodologie Agile générale, modèle conceptuel de données Merise, etc.). Il se concentre **exclusivement et de manière approfondie sur les cinq axes majeurs ayant fait l'objet de demandes de corrections et d'enrichissements formels** :
1. **L'Analyse Fonctionnelle du Besoin APTE révisée** (Bête à cornes et Diagramme Pieuvre intégrant expressément la Mairie et l'Association des Commerçants).
2. **Le Cadre Institutionnel et la Gouvernance Contractuelle** (distinction juridique et opérationnelle stricte entre l'entreprise prestataire *Garik* et la solution progicielle *ShopLoc*, flux contractuels tripartites et matrice des 4 rôles d'administration RBAC).
3. **L'Approfondissement des Cas d'Utilisation UML** (diagramme global et 5 fiches détaillées au standard Cockburn / AFNOR incluant la gestion exhaustive des pannes et anomalies).
4. **Le Registre Formel des Risques Projet (Norme ISO 31000)** (cotation P × G, cartographie des aléas réels incluant le blocage du campus, la maladie, la recherche de CDI post-Master, et Plan de Continuité d'Activité).
5. **Le Recadrage du Périmètre de Décembre (Jalon R4) & le Diagramme de Gantt Opérationnel** (focalisation sur un seul composant vertical Panier 2PC sous TDD ≥ 80 %, sans tableau redondant).

*(Note contractuelle : La consolidation financière fait l'objet d'un livrable autonome dédié pour le Jalon R3 du 30 novembre 2026 et n'est pas traitée dans cet addendum).*

<div style="page-break-after: always;"></div>

# 1. Analyse Fonctionnelle du Besoin APTE Révisée (Norme NF X 50-151)

L'analyse préliminaire du premier livrable s'était focalisée sur le binôme usager « Citoyen - Commerçant ». Conformément aux exigences de la MOA, la méthode APTE est ici reformulée pour intégrer de façon centrale les deux acteurs institutionnels garants de la viabilité du dispositif : **la Mairie (Collectivité territoriale)** et **l'Association des Commerçants de Centre-Ville**.

## 1.1. Énonciation Canonique du Besoin : La Bête à Cornes Actualisée

La méthode APTE impose de répondre rigoureusement aux trois questions fondamentales définissant la raison d'être du système :

| Question Canonique APTE | Énonciation Normée & Complète du Système ShopLoc |
|---|---|
| **À qui le système rend-il service ?** | 1. **Aux Citoyens acheteurs** : valorisation de leur pouvoir d'achat par des avantages concrets et accès facilité à l'offre commerciale locale.<br>2. **Aux Artisans & Commerçants de centre-ville** : visibilité numérique accrue sans commission prédatrice et fidélisation de la clientèle physique.<br>3. **À la Mairie (Collectivité locale)** : revitalisation active de l'économie de proximité et incitation mesurable aux mobilités douces décarbonées.<br>4. **À l'Association des Commerçants** : tiers de confiance assurant l'animation du tissu commercial, l'adhésion des boutiques et la gestion mutualisée des récompenses. |
| **Sur quoi le système agit-il ?** | 1. **Sur les flux d'achats marchands physiques** et les commandes Click & Collect en cœur de ville.<br>2. **Sur les habitudes de mobilité urbaine** (report modal vers les transports en commun Ilévia et régulation du stationnement voirie).<br>3. **Sur la cohésion économique territoriale** via la mutualisation des avantages fidélité sans captation de marge par un intermédiaire externe. |
| **Dans quel but le système existe-t-il ?** | **Fédérer les acteurs locaux** (Citoyens, Commerçants, Mairie, Association) autour d'un écosystème numérique souverain, éthique et pérenne, dynamisant le commerce de centre-ville tout en encourageant les comportements écoresponsables. |

<div class="figure-card" style="background:#FAF9F6; border:1px solid #DCD6CD; border-radius:14px; padding:14px 18px; margin: 14pt auto; width: 100%; box-sizing: border-box; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; border-bottom:1px solid #DCD6CD; padding-bottom:8px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#C26750;"></span>
        <span style="font-size:11px; font-weight:700; color:#C26750; text-transform:uppercase; letter-spacing:0.08em; font-family: 'Poppins', sans-serif;">Méthode APTE · NF X 50-151</span>
      </div>
      <h3 style="font-size:15px; font-weight:700; color:#243342; margin:0; font-family: 'Poppins', sans-serif;">Figure 1.1 — Énonciation Canonique du Besoin (Bête à Cornes Révisée)</h3>
    </div>
    <span style="font-size:11px; background:#FFFFFF; border:1px solid #DCD6CD; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600; font-family: 'Poppins', sans-serif;">Cadrage Stratégique</span>
  </div>
  <img src="figures/fig_1_1_bete_a_cornes_revisee.svg" alt="Figure 1.1 — Bête à cornes révisée" style="width: 100%; max-width: 100%; height: auto; display: block; margin: 0 auto;" />
</div>

<div class="landscape-page" style="display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 184mm; width: 100%; box-sizing: border-box; padding: 0; margin: 0;">
<!-- FIGURE 1.2 : DIAGRAMME DES INTERACTEURS (PIEUVRE APTE RÉVISÉE) -->
<div class="figure-card" style="background:#FAF9F6; border:1px solid #DCD6CD; border-radius:14px; padding:14px 18px; margin: auto; width: 100%; box-sizing: border-box; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; border-bottom:1px solid #DCD6CD; padding-bottom:8px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#4A7A5B;"></span>
        <span style="font-size:11px; font-weight:700; color:#4A7A5B; text-transform:uppercase; letter-spacing:0.08em; font-family: 'Poppins', sans-serif;">Analyse Fonctionnelle Externe</span>
      </div>
      <h3 style="font-size:16px; font-weight:700; color:#243342; margin:0; font-family: 'Poppins', sans-serif;">Figure 1.2 — Diagramme des Interacteurs (Méthode APTE — Pieuvre Révisée)</h3>
    </div>
    <span style="font-size:11px; background:#FFFFFF; border:1px solid #DCD6CD; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600; font-family: 'Poppins', sans-serif;">Norme AFNOR NF X 50-151</span>
  </div>
  <img src="figures/fig_1_2_diagramme_pieuvre_revisee.svg" alt="Figure 1.2 — Diagramme Pieuvre Révisé APTE" style="width: 100%; max-width: 100%; height: auto; display: block; margin: 0 auto;" />
</div>
</div>

## 1.2. Matrice de Caractérisation des Fonctions de Service (FP & FC)

Le système ShopLoc satisfait aux trois fonctions principales d'interaction et aux quatre contraintes normées ci-après :

| Code | Type | Désignation de la Fonction | Critère d'Appréciation | Niveau d'Exigence | Flexibilité |
|---|---|---|---|---|---|
| **FP1** | Principale | Permettre à un Citoyen de commander en Click & Collect multi-commerces et de valoriser sa fidélité auprès des Commerçants adhérents. | - Taux de succès transactionnel 2PC<br>- Temps d'enregistrement en caisse | - 100 % d'intégrité ACID<br>- Moins de 3 secondes au scan optique | F0 (Impératif)<br>F1 (± 0,5 s) |
| **FP2** | Principale | Permettre à la Mairie d'encourager la fréquentation des commerces en récompensant la régularité d'achat par des titres de mobilité douce. | - Détection automatique de régularité (10 passages / 15j)<br>- Émission d'un voucher Ilévia ou 20 min parking | - 100 % des ayants droit VFP notifiés<br>- Plafond : 1 titre / 24h / citoyen | F0 (Impératif)<br>F0 (Impératif) |
| **FP3** | Principale | Permettre à l'Association des Commerçants d'enrôler les boutiques, d'administrer les lots cadeaux communs et d'animer le programme local. | - Délai d'onboarding d'un commerçant<br>- Étanchéité du catalogue de lots | - Moins de 24 heures après validation Kbis<br>- Zéro conflit sur les dotations | F1 (± 12 h)<br>F0 (Impératif) |
| **FC1** | Contrainte | **Secret des affaires & RGPD Mairie** : Garantir l'étanchéité des données marchandes et interdire tout profilage nominatif par la Mairie. | - Anonymisation des flux municipaux<br>- Cloisonnement inter-commerces | - Requêtes agrégées k-anonymisées (k ≥ 5)<br>- Isolation stricte par tenant_id | F0 (Impératif)<br>F0 (Impératif) |
| **FC2** | Contrainte | **Inclusion Senior & Accessibilité** : Permettre aux publics éloignés du numérique (Pierre, 74 ans) d'utiliser le système sans smartphone. | - Support bi-média universel<br>- Conformité accessibilité web | - Carte physique plastifiée QR code<br>- RGAA / WCAG 2.1 niveau AA | F0 (Impératif)<br>F1 (Partiel) |
| **FC3** | Contrainte | **Interopérabilité Partenaire** : S'interfacer avec les systèmes bancaires et opérateurs urbains via des API simulées conteneurisées. | - Disponibilité des mocks REST<br>- Simulation de scénarios d'erreurs | - 100 % sous Docker Compose dès R2<br>- Codes HTTP 200, 402, 503 simulés | F0 (Impératif)<br>F0 (Impératif) |
| **FC4** | Contrainte | **Frugalité & Éco-Conception** : Minimiser l'empreinte carbone et les coûts d'infrastructure par une architecture modulaire frugale. | - Empreinte mémoire à vide<br>- Score éco-index logiciel | - Moins de 1,5 Go RAM pour tout le socle<br>- Score Green IT grade B minimum | F1 (± 20 %)<br>F1 (Tolérance) |

<div style="page-break-after: always;"></div>

# 2. Cadre Institutionnel, Distinction Garik / ShopLoc & Gouvernance

La soutenance orale a mis en lumière une ambiguïté sur la nature de **ShopLoc** et de **Garik**. Cette section formalise sans équivoque les statuts respectifs, la chaîne contractuelle liant les quatre acteurs, et la matrice d'habilitation d'administration (RBAC).

## 2.1. Fiche Comparative : Entreprise Prestataire vs Produit Logiciel

| Dimension | Entreprise Garik | Plateforme ShopLoc |
|---|---|---|
| **Nature Juridique** | **Société d'ingénierie logicielle & ESN (Maître d'Œuvre - MOE)** créée par l'équipe des 5 élèves-ingénieurs Master 2 MIAGE. | **Solution logicielle progicielle SaaS territoriale & Marque commerciale** conçue, développée et exploitée par Garik. |
| **Mission / Rôle** | Répond à l'appel d'offres, détient la propriété intellectuelle du code, gère la forge GitLab, la CI/CD, l'hébergement et la maintenance. | Système d'Information déployé au profit des collectivités : catalogue Click & Collect, moteur de double fidélité et passerelles mobilité. |
| **Engagement** | Responsable légale et contractuelle de la réalisation des jalons R1 à R5, de la qualité du code et du respect des délais. | Actif technique multi-tenant instancié pour chaque ville cliente sous forme d'un espace applicatif isolé (`tenant_id`). |
| **Vocabulaire Strict** | On désigne Garik comme **« l'équipe prestataire »** ou **« la société titulaire du marché »**. | On désigne ShopLoc comme **« la plateforme logicielle »** ou **« le service SaaS territorial »**. |

<div style="page-break-after: always;"></div>

## 2.2. Gouvernance Contractuelle et Flux Financiers Tripartites

L'écosystème territorial repose sur une articulation tripartite rigoureuse prévenant toute prédation financière :

<div class="figure-card" style="background:#FAF9F6; border:1px solid #DCD6CD; border-radius:14px; padding:14px 18px; margin: 14pt auto; width: 100%; box-sizing: border-box; box-shadow:0 4px 16px rgba(36,51,66,0.06); page-break-inside: avoid; break-inside: avoid;">
  <div style="margin-bottom:12px; border-bottom:1px solid #DCD6CD; padding-bottom:8px;">
    <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
      <span style="width:8px; height:8px; border-radius:50%; background:#243342;"></span>
      <span style="font-size:11px; font-weight:700; color:#243342; text-transform:uppercase; letter-spacing:0.08em; font-family: 'Poppins', sans-serif;">Gouvernance &amp; Architecture Contractuelle</span>
    </div>
    <h3 style="font-size:15px; font-weight:700; color:#243342; margin:0; font-family: 'Poppins', sans-serif;">Figure 2.1 — Cartographie de la Gouvernance Tripartite &amp; Distinction Garik / ShopLoc</h3>
  </div>
  <img src="figures/fig_2_1_gouvernance_tripartite.svg" alt="Figure 2.1 — Gouvernance Tripartite Garik ShopLoc" style="width: 100%; max-width: 100%; height: auto; display: block; margin: 0 auto;" />
</div>

* **Le client contractuel direct de Garik est l'Association des Commerçants** : Garik facture son abonnement annuel d'exploitation SaaS à l'Association, laquelle est financée par la subvention municipale fléchée.
* **Les Commerçants ne paient aucune commission sur les ventes** : Seule l'adhésion annuelle à l'Association des commerçants est requise pour ouvrir sa boutique sur ShopLoc, préservant ainsi l'intégralité de leurs marges.
* **Les Citoyens bénéficient d'une gratuité absolue** : Aucun surcoût n'est appliqué aux articles commandés en ligne par rapport aux prix pratiqués en boutique physique.

<div style="page-break-after: always;"></div>

## 2.3. Matrice d'Habilitation et d'Administration RBAC (4 Niveaux Étanches)

Pour lever toute ambiguïté sur les profils d'administration, le modèle de sécurité implémente un contrôle d'accès basé sur les rôles (*Role-Based Access Control* - RBAC) articulé en quatre niveaux étanches :

| Rôle RBAC | Titulaire & Entité | Périmètre d'Action & Droits Accordés | Interdictions Strictes (Garde-fous RGPD & Concurrence) |
|---|---|---|---|
| `ROLE_SUPER_ADMIN` | **Ingénieurs Garik**<br>(Exploitant SaaS) | - Provisionnement multi-tenant d'une nouvelle commune (`tenant_id`).<br>- Supervision de l'infrastructure Docker et des métriques JVM/PostgreSQL.<br>- Configuration des passerelles API simulateurs (banque, voirie, bus). | Interdiction formelle de modifier les prix des articles ou d'interférer dans les transactions commerciales des boutiques. |
| `ROLE_CITY_ADMIN` | **DSI Mairie**<br>(Persona Marius) | - Paramétrage des plafonds budgétaires mobilité (enveloppes tickets Ilévia).<br>- Consultation des tableaux de bord macroscopiques agrégés et k-anonymisés.<br>- Validation des conventions annuelles de revitalisation urbaine. | **Interdiction absolue d'accéder aux tickets de caisse nominatifs**, aux paniers des usagers et au chiffre d'affaires individuel des boutiques (secret des affaires). |
| `ROLE_ASSOCIATION_ADMIN` | **Bureau Association**<br>(Tiers de confiance) | - Instruction des dossiers d'adhésion commerçants (contrôle Kbis).<br>- Activation, suspension ou radiation des boutiques sur la marketplace.<br>- Administration du catalogue des lots et cadeaux communs de la ville. | Aucune visibilité sur les données bancaires privées des commerçants ni sur les flux d'authentification citoyens. |
| `ROLE_MERCHANT_ADMIN` | **Gérant de Boutique**<br>(Persona Suzanne) | - Gestion exclusive de sa fiche boutique, de ses horaires et de son stock C&C.<br>- Validation des retraits Click & Collect et scan caisse express.<br>- Consultation de ses propres statistiques de ventes et fidélité boutique. | **Étanchéité totale inter-commerces** : interdiction d'accéder aux données, stocks, tarifs ou clients d'un commerçant confrère. |

<div class="landscape-page" style="display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 184mm; width: 100%; box-sizing: border-box; padding: 0; margin: 0;">
<!-- FIGURE 3.1 : DIAGRAMME GLOBAL DES CAS D'UTILISATION UML -->
<div class="figure-card" style="background:#FAF9F6; border:1px solid #DCD6CD; border-radius:14px; padding:14px 18px; margin: auto; width: 100%; box-sizing: border-box; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; border-bottom:1px solid #DCD6CD; padding-bottom:8px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#243342;"></span>
        <span style="font-size:11px; font-weight:700; color:#243342; text-transform:uppercase; letter-spacing:0.08em; font-family: 'Poppins', sans-serif;">Ingénierie des Exigences UML</span>
      </div>
      <h3 style="font-size:16px; font-weight:700; color:#243342; margin:0; font-family: 'Poppins', sans-serif;">Figure 3.1 — Diagramme Global des Cas d'Utilisation UML du Système ShopLoc</h3>
    </div>
    <span style="font-size:11px; background:#FFFFFF; border:1px solid #DCD6CD; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600; font-family: 'Poppins', sans-serif;">Standards Cockburn / AFNOR</span>
  </div>
  <img src="figures/fig_3_1_use_cases_uml.svg" alt="Figure 3.1 — Diagramme Global des Cas d'Utilisation UML" style="width: 100%; max-width: 100%; height: auto; display: block; margin: 0 auto;" />
</div>
</div>

# 3. Cas d'Utilisation UML Approfondis (Standards Cockburn / AFNOR)

L'ingénierie fonctionnelle est ici formalisée selon le standard international Alistair Cockburn (recommandé par l'AFNOR). Les cas d'usage nominaux ainsi que l'ensemble des scénarios dégradés et d'exception sont rigoureusement documentés.

## 3.1. Fiche UC-01 : Passer une Commande Click & Collect Multi-Commerces sous Protocole 2PC

* **Identifiant :** `UC-01`
* **Titre :** Passer une commande groupée multi-boutiques avec réservation transactionnelle en deux phases (2PC).
* **Niveau d'objectif :** Niveau utilisateur (valeur métier directe).
* **Acteur principal :** Citoyen acheteur (authentifié ou invité avec saisie coordonnées).
* **Acteurs secondaires :** Commerçants concernés (notification), Simulateur Bancaire (mock de paiement).
* **Préconditions :** Le citoyen a constitué un panier contenant des articles d'au moins deux commerces distincts ; les commerces sont conventionnés actifs (`STATUS_ACTIVE`).
* **Déclencheur :** Le citoyen clique sur « Confirmer et Payer ma commande ».

### Scénario Nominal (Pas-à-pas)
1. Le citoyen soumet son panier multi-commerces.
2. Le système initie une transaction globale orchestrée sous protocole Two-Phase Commit (2PC).
3. **Phase 1 du 2PC (Prepare & Hold) :**
   * Le système vérifie en base PostgreSQL la disponibilité des stocks pour chaque article chez Suzanne et chez les confrères concernés.
   * Le système pose un verrou pessimiste temporaire (`SELECT FOR UPDATE`) et décrémente les stocks en statut réservé temporaire (`STOCK_HOLD` pendant 15 minutes).
4. Le système appelle le simulateur bancaire pour solliciter l'autorisation de débit du montant total de la commande.
5. Le simulateur bancaire répond avec un accord d'autorisation (Code HTTP 200).
6. **Phase 2 du 2PC (Commit définitif) :**
   * Le système valide définitivement la commande globale et génère un identifiant unique `order_id`.
   * Le système éclate la commande en sous-commandes marchandes étanches (`merchant_order_id`) associées à chaque boutique concernée.
   * Les stocks passent définitivement de l'état `STOCK_HOLD` à l'état `STOCK_COMMITTED`.
7. Le système transmet par notification asynchrone le bon de préparation à chaque commerçant avec son créneau de retrait individualisé.
8. Le système affiche à l'usager son récapitulatif de commande avec les QR codes de retrait Click & Collect.

### Scénarios Alternatifs & d'Exception (Pannes et Anomalies)
* **Exception 3a (Rupture de stock concurrente chez l'un des commerçants) :**
  * *Condition :* Un autre client a validé le dernier article d'une boutique pendant la constitution du panier.
  * *Traitement :* La Phase 1 échoue sur la boutique concernée. Le système interrompt immédiatement le protocole 2PC, libère l'ensemble des verrous posés chez les autres commerçants, notifie l'usager de l'article indisponible et conserve le reste du panier éditable sans aucun débit bancaire.
* **Exception 5a (Rejet ou échec du paiement bancaire) :**
  * *Condition :* Le simulateur bancaire retourne un refus de paiement (Code HTTP 402 ou timeout réseau 504).
  * *Traitement :* Le système déclenche l'étape de compensation (**Rollback 2PC**) : annulation de la transaction, libération immédiate des réservations de stock (`STOCK_HOLD` remis à disposition de la boutique) et affichage d'un message d'erreur invitant l'usager à réitérer son paiement.
* **Exception 7a (Défaut de retrait par le client - Cas de "No-Show") :**
  * *Condition :* Le citoyen ne se présente pas en boutique à l'issue de la date limite de retrait (48 heures).
  * *Traitement :* Le commerçant valide le statut « Non retiré ». Les produits non périssables sont réintégrés manuellement au stock de la boutique ; les produits périssables (produits frais) restent acquis financièrement au commerçant conformément aux règles de commerce de bouche.

* **Postconditions de succès :** La commande est enregistrée en 3NF ; les stocks sont à jour ; le citoyen dispose de ses preuves de retrait ; chaque commerçant ne voit que sa propre sous-commande.

## 3.2. Fiche UC-02 : Enregistrer un Passage en Caisse Physique & Créditer la Double Fidélité

* **Identifiant :** `UC-02`
* **Titre :** Scanner le QR code client lors d'un achat physique en caisse et créditer la double fidélité (Boutique + Ville).
* **Niveau d'objectif :** Sous-fonction métier (opération de caisse express).
* **Acteur principal :** Commerçant / Artisan (Persona Suzanne, Boulangère).
* **Acteur secondaire :** Citoyen acheteur (présente sa carte physique ou son smartphone).
* **Préconditions :** Le commerçant est connecté sur son terminal POS ou smartphone ; l'achat physique est supérieur au montant plancher (1,00 €).
* **Déclencheur :** Le commerçant vise le QR code du client avec la caméra du terminal de vente.

### Scénario Nominal (Pas-à-pas)
1. Le client présente son QR code universel (affiché sur PWA ou imprimé sur sa carte physique distribuée par l'Association).
2. Le commerçant scanne le QR code via l'application ShopLoc Caisse (temps de lecture optique inférieur à 1,5 seconde).
3. Le système décode le jeton cryptographique pérenne du citoyen et valide son identité.
4. Le commerçant saisit le montant total de l'achat (ex. 14,50 €) et valide.
5. Le système applique en une transaction atomique le **moteur de double fidélité territoriale** :
   * **Cagnotte Commerçant :** Crédite 1 point par euro dépensé sur le compte exclusif de la boulangerie de Suzanne.
   * **Cagnotte Territoire Ville :** Incrémente de +1 le compteur d'actes d'achats physiques du citoyen sur la commune de Lille.
6. Le terminal émet un signal sonore de validation et affiche le nouveau solde de points du client.

### Scénarios Alternatifs & d'Exception
* **Exception 2a (QR code illisible ou smartphone citoyen déchargé) :**
  * *Traitement :* Le commerçant bascule en saisie manuelle de secours : recherche du citoyen par son numéro de téléphone ou son identifiant court à 6 chiffres.
* **Exception 5a (Réseau Internet de la boutique temporairement indisponible) :**
  * *Traitement :* L'application web progressive (PWA) bascule en **mode hors-ligne dégradé (Service Worker & IndexedDB)** : le passage en caisse est horodaté et signé cryptographiquement en local. La synchronisation bidirectionnelle avec le serveur central PostgreSQL s'opère automatiquement dès le rétablissement de la connexion 4G/WiFi.

* **Postconditions de succès :** Les deux cagnottes sont créditées ; l'acte d'achat est tracé pour le calcul de régularité nocturne ; aucun ticket papier n'est gaspillé.

## 3.3. Fiche UC-03 : Activer un Titre Mobilité Urbaine (Ticket Bus Ilévia & Parking Voirie)

* **Identifiant :** `UC-03`
* **Titre :** Convertir son statut de fidélité citoyenne en avantage de mobilité douce décarbonée.
* **Niveau d'objectif :** Niveau utilisateur (bénéfice citoyen direct).
* **Acteur principal :** Citoyen acheteur éligible (statut régulier actif).
* **Acteurs secondaires :** API Simulateur Mobilité Pass Pass Ilévia, API Horodateur Parking Municipal.
* **Préconditions :** Le citoyen détient le statut de régularité commerciale validé par le système.
* **Déclencheur :** Le citoyen clique sur « Activer mon avantage mobilité du jour ».

### Scénario Nominal (Pas-à-pas)
1. Le citoyen choisit la nature de l'avantage souhaité : Ticket de transport en commun ou Franchise stationnement.
2. **Branchement A — Option Transport en commun (Ticket de Bus) :**
   * Le citoyen sélectionne « Ticket 1 Trajet Réseau Ilévia ».
   * Le système ShopLoc interroge l'API du simulateur Ilévia en transmettant le numéro d'identifiant usager.
   * Le simulateur répond avec un code-barres 2D sécurisé et horodaté (valable 1 heure dès première validation).
   * Le titre dématérialisé s'affiche immédiatement dans la PWA du citoyen avec mention « Prêt à badger ».
3. **Branchement B — Option Stationnement Voirie (Franchise 20 minutes) :**
   * Le citoyen renseigne sa plaque d'immatriculation (ex. `AB-123-CD`) ou sélectionne son véhicule enregistré.
   * Le système ShopLoc émet un appel REST vers le simulateur d'horodateur municipal pour déclarer une session de stationnement gratuite de 20 minutes.
   * L'API municipale confirme la prise en compte : le véhicule est immunisé contre tout avis d'amende forfaitaire (FPS) pendant le créneau accordé pour retirer ses commandes.

### Scénarios Alternatifs & d'Exception
* **Exception 2a (Plafond journalier de mobilité déjà atteint) :**
  * *Condition :* Le citoyen a déjà émis un titre de transport au cours des dernières 24 heures.
  * *Traitement :* Le système bloque l'émission, rappelle la règle d'équité (1 titre par tranche de 24h) et informe l'usager de l'heure exacte de réactivation de son droit.
* **Exception 3a (Panne du service tiers de voirie municipale) :**
  * *Traitement :* Si le mock de voirie retourne une erreur HTTP 503, le système génère un reçu numérique de secours infalsifiable avec QR code horodaté certifié par Garik, servant de justificatif opposable.

## 3.4. Fiche UC-04 : Calculer la Cohorte de Régularité & Notifier les Usagers (Batch Nocturne)

* **Identifiant :** `UC-04`
* **Titre :** Traitement par lots automatisé réévaluant l'éligibilité aux avantages et générant les relances incitatives.
* **Niveau d'objectif :** Tâche système automatisée (sans intervention humaine directe).
* **Acteur principal :** Planificateur de tâches Quartz / Spring Scheduled (horloge système).
* **Acteurs secondaires :** Moteur de notification push / SMS, Tableau de bord DSI Mairie (récepteur des métriques).
* **Préconditions :** Le serveur d'application est actif ; l'horloge indique 02:00 du matin (créneau creux).
* **Déclencheur :** Déclenchement du cron nocturne quotidien.

### Scénario Nominal (Pas-à-pas)
1. Le job batch extrait de la base PostgreSQL l'ensemble des passages en caisse physiques et commandes C&C validés.
2. Pour chaque citoyen actif, le système calcule le nombre d'actes d'achats distincts réalisés sur la **fenêtre glissante exacte des 15 derniers jours calendaires** (J-15 à J).
3. **Cas 1 : Citoyen atteignant ou maintenant le seuil de régularité (≥ 10 passages) :**
   * Le système positionne son statut à `STATUS_ACTIVE`.
   * Le système reconduit ses droits mobilité pour une durée de 15 jours calendaires supplémentaires.
4. **Cas 2 : Citoyen passant sous le seuil critique (< 10 passages) :**
   * Le système rétrograde le statut à `STATUS_STANDARD`.
   * Le système programme une notification douce personnalisée : *« Plus que 2 passages chez vos commerçants pour débloquer vos titres de transport offerts par la Ville ! »*.
5. Le système compile les métriques de la nuit et génère les indicateurs k-anonymisés pour le tableau de bord DSI de la Mairie.

### Scénarios Alternatifs & d'Exception
* **Exception 1a (Interruption ou échec en cours de calcul batch) :**
  * *Traitement :* Le calcul SQL est optimisé par partitionnement mensuel de la table des passages et utilisation d'une vue matérialisée rafraîchie de façon incrémentale, garantissant un temps de calcul inférieur à 60 secondes même sur 100 000 usagers. En cas d'exception non gérée, une alerte est transmise au canal de support Garik et le calcul est relancé à 05:00 sans impact sur la journée d'exploitation.

## 3.5. Fiche UC-05 : Conventionner une Commune & Onboarder une Boutique Adhérente

* **Identifiant :** `UC-05`
* **Titre :** Enrôler une nouvelle commune et déployer les commerçants de l'association locale.
* **Niveau d'objectif :** Niveau administratif et paramétrage multi-tenant.
* **Acteurs principaux :** Administrateur Association des Commerçants, Super-Admin Garik.
* **Acteurs secondaires :** Gérant de Boutique (Suzanne), API INSEE (vérification SIRET).
* **Préconditions :** La Mairie a voté la convention territoriale cadre et versé la subvention d'amorçage.
* **Déclencheur :** L'Association soumet le dossier d'adhésion d'une nouvelle boutique.

### Scénario Nominal (Pas-à-pas)
1. L'administrateur de l'Association saisit le numéro SIRET de l'artisan boulanger dans l'interface de gestion.
2. Le système appelle automatiquement l'API Sirene INSEE pour contrôler l'existence légale et le code NAF/APE du commerce.
3. Le système envoie un lien sécurisé d'activation de compte au commerçant.
4. Le commerçant Suzanne crée ses identifiants personnels sécurisés (`ROLE_MERCHANT_ADMIN`).
5. Le commerçant configure sa fiche publique (nom, spécialité, horaires d'ouverture, coordonnées) et charge son premier catalogue d'articles éligibles au Click & Collect.
6. L'Association valide la mise en ligne : la boutique devient visible et commandable par les citoyens de la commune.

### Scénarios Alternatifs & d'Exception
* **Exception 1a (Dossier Kbis non conforme ou radiation associative) :**
  * *Traitement :* L'administrateur de l'association rejette la demande avec motif. Si un commerçant quitte l'association en cours d'année, sa boutique bascule en statut `SUSPENDED` : le catalogue n'est plus commandable, mais l'historique comptable est conservé pour les garanties légales.

<div style="page-break-after: always;"></div>

# 4. Registre Formel des Risques Projet (Norme ISO 31000) & PCA

Pour corriger l'absence constatée lors du premier rendu, la gestion des risques est ici modélisée selon les exigences de la norme internationale **ISO 31000**. Elle prend en compte l'ensemble des contraintes techniques du système, ainsi que la réalité opérationnelle et humaine de l'équipe étudiante de Master 2.

## 4.1. Cadre Méthodologique & Grille de Cotation de la Criticité

Chaque risque est évalué selon deux grandeurs discrètes graduées de 1 à 5 :
* **Probabilité d'occurrence (P)** : 1 (Très improbable, < 5 %) | 2 (Faible, 5-20 %) | 3 (Moyenne, 20-50 %) | 4 (Forte, 50-80 %) | 5 (Quasi-certaine, > 80 % ou en cours).
* **Gravité de l'impact (G)** : 1 (Négligeable, simple gêne interne) | 2 (Faible, solution de contournement aisée) | 3 (Modérée, impact sur une tâche secondaire) | 4 (Majeure, menace sur un jalon contractuel) | 5 (Critique, blocage total du projet ou faute juridique).
* **Indice de Criticité (C = P × G)** :
  * **1 à 4 : Risque Mineur (Zone Verte)** — Surveillance périodique standard.
  * **5 à 9 : Risque Modéré (Zone Jaune)** — Traitement par l'application des bonnes pratiques d'ingénierie.
  * **10 à 15 : Risque Majeur (Zone Orange)** — Plan d'action et mesures de mitigation obligatoires.
  * **16 à 25 : Risque Critique (Zone Rouge)** — Menace directe sur le projet ; plan de contingence immédiat.

<div class="landscape-page" style="display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 184mm; width: 100%; box-sizing: border-box; padding: 0; margin: 0;">
<!-- TABLEAU 4.1 : MATRICE DES 10 RISQUES PROJET RÉELS ISO 31000 -->
<div class="figure-card" style="background:#FAF9F6; border:1px solid #DCD6CD; border-radius:14px; padding:12px 16px; margin: auto; width: 100%; box-sizing: border-box; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:10px; border-bottom:1px solid #DCD6CD; padding-bottom:8px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#B44C43;"></span>
        <span style="font-size:11px; font-weight:700; color:#B44C43; text-transform:uppercase; letter-spacing:0.08em; font-family: 'Poppins', sans-serif;">Maîtrise des Risques &amp; Qualité Logicielle</span>
      </div>
      <h3 style="font-size:15px; font-weight:700; color:#243342; margin:0; font-family: 'Poppins', sans-serif;">Tableau 4.1 — Matrice et Registre Exhaustif des 10 Risques Projet Réels (Norme ISO 31000)</h3>
    </div>
    <span style="font-size:11px; background:#FFFFFF; border:1px solid #DCD6CD; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600; font-family: 'Poppins', sans-serif;">Échelle Criticité : Rouge (≥12) · Jaune (6-10) · Vert (1-5)</span>
  </div>

| Réf. | Catégorie | Description de l'Aléa (Cause → Événement → Impact) | Cotation Initiale | Dispositif de Mitigation d'Ingénierie &amp; Plan de Contingence (Parade) | Cotation Résiduelle | Resp. Garik |
|:---:|:---:|---|:---:|---|:---:|:---:|
| **R-01** | Technique | **Désynchronisation 2PC sur Panier Multi-Commerces** : Panne réseau ou rupture concurrente pendant la commande → Incohérence des stocks ou débit orphelin. | P=3, G=4<br><span class="badge badge-error">C = 12 (Élevée)</span> | Protocole transactionnel Two-Phase Commit avec verrous pessimistes PostgreSQL (`SELECT FOR UPDATE`), compensation automatique (*Rollback*) et tests TDD avec Testcontainers dès le Sprint 3. | P=1, G=3<br><span class="badge badge-success">C = 3 (Faible)</span> | Gautam (Back) &amp; Rayane |
| **R-02** | Partenaire | **Indisponibilité des API externes réelles** : Impossibilité de tester le paiement bancaire ou les tickets de bus → Blocage de la chaîne d'intégration. | P=5, G=4<br><span class="badge badge-error">C = 20 (Critique)</span> | Découplage total dès le Jalon R2 via des simulateurs (mocks REST OpenAPI 3.1 conteneurisés sous Docker Compose) simulant les pannes (HTTP 402, 503). | P=1, G=2<br><span class="badge badge-success">C = 2 (Faible)</span> | Rayane (DevOps) |
| **R-03** | Terrain | **Friction commerçante en caisse (Suzanne)** : Complexité de saisie des stocks ou lenteur du scan → Rejet du système par les artisans de bouche. | P=4, G=4<br><span class="badge badge-error">C = 16 (Critique)</span> | Mode « caisse express » ultra-frugal : scan optique en moins de 2 secondes sans clic de confirmation ; saisie des stocks limitée aux articles C&amp;C. | P=2, G=2<br><span class="badge badge-success">C = 4 (Faible)</span> | Ilyas (Front) &amp; Abdelkader |
| **R-04** | Usager | **Illectronisme &amp; Exclusion des seniors (Pierre)** : Usagers sans smartphone incapables d'utiliser les applications mobiles → Échec d'adoption territoriale. | P=4, G=3<br><span class="badge badge-error">C = 12 (Élevée)</span> | Dispositif bi-média universel : carte physique plastifiée avec QR code pérenne distribuée par l'Association ; portail web accessible conforme RGAA AA. | P=1, G=2<br><span class="badge badge-success">C = 2 (Faible)</span> | Ilyas (Accessibilité) |
| **R-05** | Sécurité | **Fuite du secret des affaires inter-commerces &amp; RGPD** : Accès non autorisé aux chiffres d'un confrère ou profilage nominatif par la Mairie → Sanction CNIL. | P=2, G=5<br><span class="badge badge-warning">C = 10 (Modérée)</span> | Cloisonnement strict multi-tenant par `tenant_id` au niveau SQL ; interdiction d'accès aux flux marchands pour la Mairie ; requêtes k-anonymisées (k ≥ 5). | P=1, G=4<br><span class="badge badge-success">C = 4 (Faible)</span> | Gautam (Sécurité) &amp; Khalil |
| **R-06** | Calendrier | **Dérive des délais sur le Jalon R4 (Décembre)** : Masse de développement irréaliste sur 7 semaines → Sanction académique de fin de S3. | P=4, G=4<br><span class="badge badge-error">C = 16 (Critique)</span> | Recentrage formel de R4 sur un seul composant vertical (Panier 2PC) ; sanctuarisation de la règle du Code Freeze à J-3 (15 décembre) sans ajout fonctionnel. | P=2, G=2<br><span class="badge badge-success">C = 4 (Faible)</span> | Ilyas (Scrum Master) |
| **R-07** | Académique | **Blocage de l'université suite à mouvement social &amp; bascule visio** : Fermeture des locaux de cours et amphis → Perte des créneaux présentiels. | P=5, G=3<br><span class="badge badge-error">C = 15 (Élevée)</span> | Stack 100 % reproductible sur PC personnels sous Docker Desktop (zéro dépendance aux salles TP) ; rituels maintenus en visio ; traçabilité GitLab asynchrone. | P=2, G=1<br><span class="badge badge-success">C = 2 (Faible)</span> | Abdelkader (Coordination) |
| **R-08** | Humain | **Indisponibilité imprévue d'un équipier (Maladie, isolement)** : Absence soudaine d'un développeur sur le chemin critique → Goulot d'étranglement (*Bus Factor* = 1). | P=3, G=4<br><span class="badge badge-error">C = 12 (Élevée)</span> | Règle du binômage systématique (*Pair Programming*) sur chaque brique (Gautam+Rayane au Back, Ilyas+Abdelkader au Front, Khalil en QA) garantissant un *Bus Factor* ≥ 2. | P=1, G=2<br><span class="badge badge-success">C = 2 (Faible)</span> | Khalil (Qualité &amp; RH) |
| **R-09** | Carrière | **Recherche de potentiel CDI post-Master (Préparation &amp; Entretiens)** : Sollicitation intense par les recruteurs au S3/S4 → Emploi du temps haché, fatigue. | P=4, G=3<br><span class="badge badge-error">C = 12 (Élevée)</span> | Découpage atomique des tâches en tickets de moins de 4 heures pour travail asynchrone autonome ; agenda partagé sanctuarisant les créneaux d'entretiens déclarés. | P=2, G=2<br><span class="badge badge-success">C = 4 (Faible)</span> | Collectif Garik |
| **R-10** | Matériel | **Défaillance machine d'un membre (Crash PC / Disque dur)** : Ordinateur portable hors-service en plein sprint → Perte de code local ou indisponibilité 48h. | P=3, G=3<br><span class="badge badge-warning">C = 9 (Modérée)</span> | Zéro stockage local exclusif : obligation de commit/push quotidien sur GitLab ; guide d'installation multi-OS permettant de remonter un environnement en moins de 30 min. | P=1, G=2<br><span class="badge badge-success">C = 2 (Faible)</span> | Rayane (Support Outils) |

</div>
</div>

## 4.2. Plan de Continuité d'Activité (PCA) & Protocole d'Escalade sous 24h

Pour garantir que l'équipe Garik conserve une capacité de réaction immédiate face aux aléas majeurs, le protocole d'escalade suivant est instauré :
1. **Seuil d'alerte sous 24 heures :** Dès qu'une tâche du chemin critique accuse un retard estimé supérieur à 48 heures ou qu'un membre signale une indisponibilité (maladie, entretien CDI bloquant), le Scrum Master du jalon convoque un point de crise exceptionnel de 20 minutes en visio.
2. **Mécanisme d'arbitrage MoSCoW :** En cas d'aléa temporel avéré, la règle de dé-scopage s'applique sans délai : seules les fonctionnalités *Must Have* sont maintenues dans le sprint en cours. Les fonctionnalités *Should Have* sont automatiquement basculées sur le sprint suivant.
3. **Escalade transparente vers la MOA sous 48 heures :** Si un aléa majeur (ex. blocage universitaire prolongé affectant les modalités d'évaluation) est susceptible d'impacter le livrable officiel, un mémo d'ingénierie formel est transmis aux enseignants-tuteurs (Laurence Duchien, Anne Etien, François Secchi, Jérémy Woirhaye) sous 48h ouvrées.

<div style="page-break-after: always;"></div>

# 5. Recadrage du Périmètre de Décembre (R4) & Gantt Opérationnel

Le présent chapitre formalise la réponse au commentaire central de la MOA : *« Première release très ambitieuse pour décembre. Il faut être plus précis et réaliste. »*.

## 5.1. Découpage Réaliste par Release (R4 vs R5)

L'engagement initial prévoyant la livraison des 10 User Stories du MVP dès décembre a été révoqué conformément à l'arbitrage `ADR-020`. Le calendrier d'ingénierie se restructure en deux tranches contractuelles étanches :

### Jalon R4 — 18 Décembre 2026 : Release V1 (Composant Vertical Panier 2PC & Archi C4)
Conformément à la consigne contractuelle de l'UE GLOP (*« Réaliser un au choix des composants logiciels jusqu'au déploiement et aux tests »*), les 7 semaines de développement effectif (mi-octobre à mi-décembre 2026) sont dédiées à 100 % à l'excellence technique d'un composant vertical complet :
* **Dossier d'Architecture Logicielle 4+1 C4 exhaustif** : Vue Contexte, Conteneurs, Composants et Code ; modélisation du domaine métier et schéma relationnel PostgreSQL 16 normalisé en 3NF.
* **Composant logiciel unique déployé de bout en bout : Commande & Panier Multi-Commerces Click & Collect sous protocole Two-Phase Commit (2PC)** :
  * Backend Java 21 / Spring Boot 3.3 implémentant la réservation temporaire de stock et l'orchestration transactionnelle 2PC.
  * Persistance PostgreSQL 16 avec gestion de concurrence stricte (`SELECT FOR UPDATE`).
  * Simulateur bancaire conteneurisé (Mock OpenAPI 3.1) validant les cas nominaux et les compensations (*rollback*).
  * Interface frontend réactive React / TypeScript pour la consultation du catalogue et la validation du panier.
  * Couverture de tests automatisés unitaires et d'intégration TDD ≥ 80 %.
  * Déploiement clé en main via `docker compose up`.

### Jalon R5 — 19 Mars 2027 : Release V2 (Système Industriel Complet)
Le Semestre 4 intègre les composants complémentaires planifiés de janvier à mars 2027 :
* Moteur batch SQL de fidélité VFP sur fenêtre glissante de 15 jours consécutifs.
* Interface de caisse express marchande (moins de 3s) et catalogue cadeaux.
* Module d'émission des vouchers mobilité (Bus Ilévia et franchise 20 min parking).
* Portail de supervision municipale DSI k-anonymisé (Persona Marius).
* Campagne d'homologation, tests de charge Gatling et audit d'éco-conception Green IT.

<div class="landscape-page" style="display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 184mm; width: 100%; box-sizing: border-box; padding: 0; margin: 0;">
<!-- FIGURE 5.1 : DIAGRAMME DE GANTT ANNUEL OFFICIEL (PLEINE PAGE PAYSAGE) -->
<div class="figure-card" style="background:#FAF9F6; border:1px solid #DCD6CD; border-radius:14px; padding:14px 18px; margin: auto; width: 100%; box-sizing: border-box; box-shadow:0 4px 16px rgba(36,51,66,0.06);">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; border-bottom:1px solid #DCD6CD; padding-bottom:8px;">
    <div>
      <div style="display:inline-flex; align-items:center; gap:8px; margin-bottom:4px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#243342;"></span>
        <span style="font-size:11px; font-weight:700; color:#243342; text-transform:uppercase; letter-spacing:0.08em; font-family: 'Poppins', sans-serif;">Planification &amp; Ordonnancement</span>
      </div>
      <h3 style="font-size:16px; font-weight:700; color:#243342; margin:0; font-family: 'Poppins', sans-serif;">Figure 5.1 — Diagramme de Gantt Annuel Officiel du Projet ShopLoc (2026-2027)</h3>
    </div>
    <span style="font-size:11px; background:#FFFFFF; border:1px solid #DCD6CD; padding:4px 12px; border-radius:9999px; color:#5A6578; font-weight:600; font-family: 'Poppins', sans-serif;">Jalons R1 à R5 · Recadrage R4</span>
  </div>
  <img src="figures/fig_5_1_gantt_annuel_officiel.png" alt="Figure 5.1 — Diagramme de Gantt annuel officiel" style="width: 100%; max-height: 172mm; object-fit: contain; display: block; margin: 0 auto; border-radius: 4px;" />
  <div class="diagram-caption" style="margin-top: 6pt;">Vue synoptique annuelle intégrant le chemin critique, le recadrage réaliste du jalon R4 de Décembre 2026 (Composant Panier 2PC) et les rituels de livraison.</div>
</div>
</div>

---

## Conclusion & Engagement Contractuel

Le présent addendum corrige et complète formellement le livrable R1 conformément à l'intégralité des observations de la maîtrise d'ouvrage. 

L'équipe d'ingénierie Garik s'engage sur ce référentiel unifié :
1. Les choix d'outillage validés au jalon R2 (12 octobre) soutiennent directement cette architecture.
2. Les calculs financiers détaillés (coûts complets, compte de résultat 3 ans, VAN, TRI) seront remis au jalon dédié R3 (30 novembre).
3. Le prototype opérationnel démontrable du **Composant Panier & Réservation 2PC sous TDD ≥ 80 %** et le dossier C4 complet seront livrés au jalon R4 le 18 décembre 2026.
"""

with open(MD_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"[OK] Fichier actualisé avec succès : {MD_PATH}")
