---
name: apte-functional-analysis
description: "Perform functional requirements engineering using APTE method (Bête à cornes and Pieuvre diagrams). Formulates Main Functions (FP) and Constraint Functions (FC) conforming to AFNOR NF X 50-151."
risk: safe
source: project-tailored
tags: [apte, functional-analysis, requirements, bete-a-cornes, pieuvre, cdc]
---

# Analyse Fonctionnelle du Besoin (Méthode APTE)

Ce skill guide l'expression canonique et formelle des exigences du système ShopLoc selon la méthode APTE (norme AFNOR NF X 50-151) pour la Section 01 du Cahier des Charges R1.

## Quand utiliser ce skill
- Formalisation du besoin initial et du périmètre fonctionnel dans la Section 01 du Cahier des Charges.
- Définition du graphe des interactions entre le système et ses milieux extérieurs.
- Dérivation des Fonctions Principales (FP) en User Stories et des Fonctions Contraintes (FC) en exigences non-fonctionnelles.

## Démarche Méthodologique APTE

### 1. Saisir le Besoin : La Bête à Cornes
Le diagramme Bête à cornes répond obligatoirement aux trois questions canoniques :
1. **À qui le produit rend-il service ?**
   - Aux citoyens acheteurs, aux commerçants de centre-ville et aux collectivités locales partenaires.
2. **Sur quoi agit-il ?**
   - Sur les flux d'achats physiques en boutique et sur les habitudes de mobilité urbaine décarbonée.
3. **Dans quel but ?**
   - Revitaliser le tissu commercial de proximité et renforcer la cohésion urbaine sans prédation financière.

### 2. Énoncer les Fonctions : Le Diagramme Pieuvre
Le système ShopLoc est placé au centre des éléments de son environnement extérieur :
- **Fonctions Principales (FP)** — Relient deux éléments du milieu extérieur à travers le système :
  - `FP1` : Permettre à un citoyen d'effectuer des achats Click & Collect et de valoriser sa fidélité auprès des commerçants adhérents.
  - `FP2` : Permettre à la collectivité municipale d'encourager la fréquentation des commerces locaux en récompensant la régularité d'achat par des avantages de mobilité douce.
- **Fonctions Contraintes (FC)** — Relient le système à un seul élément du milieu extérieur (adaptation ou contrainte réglementaire/technique) :
  - `FC1 (RGPD & Souveraineté)` : Garantir l'anonymisation des données d'achat et le respect strict du RGPD vis-à-vis de la collectivité.
  - `FC2 (Inclusion Senior RGAA)` : Assurer une accessibilité universelle pour les publics non-connectés (carte physique QR, contrastes élevés).
  - `FC3 (Frugalité Économique)` : Minimiser les coûts d'exploitation (Run) par une architecture modulaire mutualisée.
  - `FC4 (Interopérabilité Partenaire)` : S'interfacer avec les services de voirie et de transport via des API REST mockées.

### 3. Matrice de Caractérisation des Fonctions
Pour chaque fonction (FP ou FC), le skill produit une fiche normalisée :
- **Critère d'appréciation** (grandeur mesurable, ex : temps de traitement, taux de contraste).
- **Niveau d'exigence** (valeur seuil, ex : `< 3 secondes`, `contraste >= 4.5:1`).
- **Flexibilité** (F0 = impératif strict, F1 = tolérance faible, F2 = négociable).

## Format de Sortie
Génération de diagrammes SVG vectoriels purs prêts pour l'intégration dans [`agent_projet/templates/components/apte_pieuvre.html`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/agent_projet/templates/components/apte_pieuvre.html).
