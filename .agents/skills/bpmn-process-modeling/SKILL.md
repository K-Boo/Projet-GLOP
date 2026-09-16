---
name: bpmn-process-modeling
description: "Model business processes using BPMN 2.0 standard with swimlanes, events, tasks, and gateways. Generates vector SVG diagrams conforming to ShopLoc pastel design tokens."
risk: safe
source: project-tailored
tags: [bpmn, processes, workflows, swimlanes, modeling, svg]
---

# BPMN 2.0 Business Process Modeling

Ce skill fournit les directives et modèles pour formaliser l'ensemble des processus métiers du projet ShopLoc conformément à la norme internationale BPMN 2.0 (ISO/IEC 19510) et aux exigences du Master 2 MIAGE.

## Quand utiliser ce skill
- Modélisation des processus métiers de la Section 03 du Cahier des Charges R1 (Processus P1 à P5).
- Formalisation des parcours transactionnels entre le citoyen, le commerçant, la plateforme et les partenaires.
- Conception des flux de messages et des cinématiques de commandes (réservation 2PC, no-show, annulations).

## Standards & Règles de Conception BPMN 2.0

### 1. Structuration en 4 Couloirs (Swimlanes)
Chaque diagramme de processus ShopLoc doit être structuré en couloirs horizontaux étanches :
1. **Couloir 1 : Citoyen (Client / Usager)** — Teinte vert amande pastel (`#DCFCE7`, bordure `#22C55E`, texte `#15803D`).
2. **Couloir 2 : Plateforme ShopLoc (Cœur applicatif Monolithe)** — Teinte bleu ciel pastel (`#E0F2FE`, bordure `#0284C7`, texte `#0369A1`).
3. **Couloir 3 : Commerçant Partenaire** — Teinte pêche pastel (`#FFEDD5`, bordure `#F97316`, texte `#C2410C`).
4. **Couloir 4 : Services Partenaires (Mobilité / Banque / Mairie)** — Teinte lavande pastel (`#EDE9FE`, bordure `#8B5CF6`, texte `#6D28D9`).

### 2. Sémantique des Nœuds BPMN
- **Événement de début** : Cercle simple à contour fin vert (`#15803D`).
- **Événement de fin** : Cercle à contour épais (vert pour fin nominale `#15803D`, rouge `#B91C1C` pour fin en anomalie/rejet).
- **Tâche / Activité** : Rectangle à coins arrondis contenant un verbe d'action à l'infinitif.
- **Passerelle exclusive (XOR)** : Losange contenant un « X », avec conditions mutuellement exclusives sur chaque branche sortante (ex : `[Stock disponible]`, `[Stock épuisé]`).
- **Flux de séquence** : Flèche pleine continue (`stroke="#334155"`).
- **Flux de message** : Flèche en pointillés (`stroke-dasharray="3,3"`).

### 3. Les 5 Processus Majeurs ShopLoc à Modéliser
1. **P1 — Conventionnement communal et adhésion commerçante** (Processus administratif tripartite).
2. **P2 — Commande Click & Collect, réservation 2PC et retrait boutique** (Processus transactionnel nominal et rupture).
3. **P3 — Enregistrement de passage en caisse et calcul VFP** (Double moteur : points boutique décentralisés et compteur 10 passages / 15 jours).
4. **P4 — Conversion de l'avantage fidélité en mobilité urbaine** (Ticket de bus dématérialisé ou 20 min de stationnement).
5. **P5 — Traitement des anomalies, no-show et annulations** (Règle des 24h et libération de stock).

## Format de Sortie
Le skill génère du code SVG vectoriel pur autonome ou injectable directement dans le gabarit [`agent_projet/templates/components/bpmn_swimlane_template.html`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/agent_projet/templates/components/bpmn_swimlane_template.html), visualisable en local et imprimable en PDF sans perte de netteté.
