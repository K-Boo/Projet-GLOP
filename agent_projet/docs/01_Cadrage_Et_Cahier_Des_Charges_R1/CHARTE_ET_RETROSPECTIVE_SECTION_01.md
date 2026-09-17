# CHARTE DIRECTRICE, RÉTROSPECTIVE & RÈGLES DE CONCEPTION DES LIVRABLES (SECTION 01 & SUIVANTES)
**Master 2 MIAGE — Université de Lille — UE Génie Logiciel par la Pratique (2026-2027)**  
*Document de Référence pour l'Ensemble du Cahier des Charges (R1) et des Livrables Projet*

---

## 1. Contexte & Objectif de la Rétrospective

La finalisation de la **Section 01 : Cadrage Stratégique & Besoins** a fait l'objet d'itérations méthodiques approfondies entre l'équipe étudiante et les exigences de qualité du Master MIAGE.

Ce document consigne l'intégralité des choix, arbitrages et règles éditoriales, typographiques et graphiques validés. **Ces règles constituent la référence normative obligatoire** pour la rédaction, la mise en page et la compilation de l'ensemble des sections subséquentes du Cahier des Charges (Sections 02 à 11) ainsi que pour les livrables R3, R4 et R5.

---

## 2. Principes Éditoriaux & Style Rédactionnel

### Règle 2.1 — Ton Académique Étudiant Réaliste
* Le ton doit être **professionnel, structuré et rigoureux**, mais rester **proche de ce que produit une équipe d'étudiants de Master 2**.
* Éviter le verbiage excessif, le bavardage abstrait et le jargon artificiel propre aux réponses génériques d'IA (*AI slop*).
* Éviter les références prématurées à des corpus normatifs industriels trop lourds (ex. déclinaisons outrancières de normes AFNOR) non adaptés au niveau de cadrage initial.

### Règle 2.2 — Équilibre Subtil Puces / Prose (Anti-Bullet Explosion & Anti-Wall of Text)
* **Pas de pavés monolithiques** : Bannir les blocs de texte de plus de 8 lignes sans rupture visuelle ni structure interne.
* **Pas d'explosion de puces** : Interdiction d'empiler des listes de 15 à 20 puces plates qui détruisent la hiérarchie de l'information.
* **La structure idéale par catégorie** :
  - Une phrase introductive concise.
  - Des blocs thématiques distincts avec intitulé en gras.
  - Une structure en retrait : un **énoncé simple et clair**, suivi d'une **explication opérationnelle concise** (2 à 3 lignes).

### Règle 2.3 — Formulation des Objectifs Opérationnels au Format Analyste
Pour chaque objectif opérationnel du système :
1. **Catégorisation par profil d'acteur** (Citoyen & Consommateur, Commerçant & Artisan, Collectivité & Services Publics).
2. **Rappel explicite de la finalité d'usage principale** de l'acteur dans l'intitulé de catégorie.
3. **Format normé propre au métier d'analyste fonctionnel** :
   - `[Identifiant : Intitulé]` (ex. `OP-CIT-01 : Commande Click & Collect groupée et retrait pédestre`).
   - `*Énoncé :*` Définition de l'objectif en une phrase directe, simple et mesurable.
   - `*Explication :*` Détail opérationnel précisant les règles métier, contraintes techniques et délais cibles (ex. Two-Phase Commit, scan < 3s, fenêtres glissantes de 15 jours).

### Règle 2.4 — Périmètre Strict et Non-Redondance
* Chaque section du Cahier des Charges traite **exclusivement de son périmètre assigné** dans le Plan Directeur.
* **Aucun contenu technique prématuré** : L'architecture logicielle, les couches applicatives et les modèles d'interacteurs sont strictement réservés à la **Section 07 (Architecture & Composants)**.
* **Suppression des méta-données administratives redondantes** : Les cartouches lourds, informations documentaires répétées et mentions d'outillage sont exclus du corps de texte.

---

## 3. Charte Typographique & Mise en Page

### Règle 3.1 — Alignement au Fer à Gauche (`text-align: left`) Strict
* **Interdiction formelle de la justification pleine (`text-align: justify`)** :
  - La justification Chromium/CSS étire artificiellement les espaces entre les mots (« rivières de blanc ») et nuit gravement à la fluidité de lecture, particulièrement aux abords des figures, dans les listes et sur les écrans ou colonnes étroites.
* **Règle absolue** : L'ensemble du corps de texte, des paragraphes `<p>`, des listes `<li>` et des blocs de description est aligné **au fer à gauche (`text-align: left`)**, offrant une typographie en drapeau naturelle, aérée et moderne.
* Seuls les titres principaux (`.latex-main-title`), les légendes sous figures (`.diagram-caption`) et les badges d'axes sont centrés.

### Règle 3.2 — Zéro Emoji & Sobriété Visuelle
* **Interdiction absolue d'utiliser des émojis** dans tous les documents du projet (Markdown, PDF, HTML, CSS, SVG, commits).
* Les statuts, priorités et distinctions s'expriment exclusivement via des termes textuels académiques et des badges CSS sobres (`.badge-success`, `.badge-warning`, `.badge-brand`).

### Règle 3.3 — Règle « 1 Sujet Majeur = 1 Page A4 » (Page Budgeting)
* Le gabarit documentaire est conçu pour occuper l'espace A4 de manière dense et harmonieuse :
  - Chaque grande partie ou couple (explication + figure) forme une unité visuelle autonome sur **exactement une page**.
  - Utilisation contrôlée des sauts de page explicites `<div style="page-break-before: always;"></div>`.
  - Aucune figure orpheline sur une page sans son texte d'accompagnement.
  - Aucun paragraphe de 2 lignes rejeté sur une page blanche suivante.
* Utilisation du mode compact `--no-cartouche` dans `render_report.py` pour sanctuariser l'espace utile dès la première page.

---

## 4. Charte Graphique & Composants Visuels

### Règle 4.1 — Préservation Intégrale de l'Aspect Ratio (Zéro Déformation)
* Les figures PNG/SVG exportées conservent impérativement leur ratio d'origine (ex. ratio 2:1 pour la Bête à Cornes, 1.55:1 pour la Matrice 2 axes).
* Règle CSS obligatoire pour l'insertion des images :
  ```html
  <div class="diagram-container" style="margin: 6pt 0;">
    <img src="../figures/fig_X_X_nom.png" alt="..." style="width: 100%; max-width: 520px; height: auto; display: block; margin: 0 auto;" />
    <div class="diagram-caption">Figure X.X — Titre complet</div>
  </div>
  ```
* **Interdiction d'appliquer un `max-height` fixe en conflit avec `width: 100%`** qui écraserait ou déformerait le ratio naturel de l'image.

### Règle 4.2 — Détourage Précis du SVG Pur
* Les visuels sont extraits directement depuis le bloc `<svg>` calé sur sa `viewBox` intrinsèque via le script `export_diagram_svg_only.py`.
* Aucun cadre A4 résiduel, aucun fond blanc superflu ni bordure fantôme ne doit entourer la figure dans le fichier PNG.

### Règle 4.3 — Identité Visuelle Unique (Anti-Slop AI & Zéro Languette)
* **Bannissement définitif des « languettes » colorées latérales (`border-left: 3px solid ...`)**, signature visuelle classique des modèles d'IA par défaut.
* Structure des cartes : bordure continue très légère (`border: 1px solid #E8E6DF`), coins arrondis élégants (`14px` à `16px`), fond blanc pur avec ombre portée douce (`box-shadow: 0 4px 16px rgba(36,51,66,0.05)`).
* Typographie des schémas : police unique *Poppins*, contrastes forts et lisibles conformes au standard RGAA AA (texte ardoise `#243342` sur fond clair).

### Règle 4.4 — Légende Analytique & Benchmark des Acteurs Cités
* Tout visuel mentionnant des concurrents, partenaires ou services tiers (ex. Amazon, Deliveroo, Ollca, Epicery, Proxity) doit être **immédiatement suivi d'une légende analytique de benchmark**.
* Cette légende explicite :
  - Le périmètre de l'étude comparative menée sur le marché français.
  - Les forces et faiblesses observées (taux de commissionnement, mode de livraison, absence d'e-commerce).
  - La justification stratégique du positionnement cible de ShopLoc au regard de ce benchmark.

### Règle 4.5 — Calibrage Strict des Conteneurs Textuels & Anti-Débordement (Zero Text Overflow)
* **Principe d'Isolation Usager (1 Persona = 1 Document / 1 Pleine Page A4)** :
  - Chaque persona approfondi fait impérativement l'objet d'un **document ou d'une page pleine dédiée** (A4 Paysage ou Portrait).
  - Il est formellement interdit de comprimer 4 personas sur une seule planche A4 sous peine d'écrasement typographique et de collision de texte.
* **Marges de Sécurité Textuelle Obligatoires (Safety Margins)** :
  - Dans tout conteneur délimité (`<rect>`, carte, encart), une marge d'au moins **30px** doit sanctuariser l'espace entre la dernière ligne de texte et la bordure inférieure.
  - Tout intitulé, titre de poste ou sous-titre excédant 30 caractères doit être **découpé sur 2 lignes distinctes** pour éliminer tout risque de chevauchement avec les séparateurs verticaux, icônes ou badges de statut.
* **Largeur Confortable des Blocs de Texte** :
  - Les conteneurs textuels descriptifs doivent offrir une largeur minimale de **500px** en format paysage pour garantir une lecture fluide sans rupture intempestive de phrase.

---

## 5. Tableaux & Indicateurs de Performance (KPIs)

### Règle 5.1 — Standard Booktabs Académique
* Tous les tableaux comparatifs et périmètres utilisent le format typographique Booktabs :
  - Filet supérieur épais (`1.5pt solid var(--color-border-dark)`).
  - Filet d'en-tête intermédiaire (`0.75pt solid var(--color-border-dark)`).
  - Filet inférieur de clôture (`1.5pt solid var(--color-border-dark)`).
  - **Zéro filet vertical**, suppression des grilles de tableur.
  - En-têtes alignés à gauche en gras couleur ardoise institutionnelle.

### Règle 5.2 — Indicateurs Clés de Performance (KPIs)
* **Structure à double échelle obligatoire** :
  - *Scope 1 (Échelle Ville Pilote / Territoire)* : mesure de l'ancrage local (taux d'usagers réguliers VFP, taux de pénétration des commerçants du centre-ville).
  - *Scope 2 (Échelle Nationale SaaS)* : mesure du déploiement global (volume de collectivités conventionnées).
* **Sobriété et réalisme** :
  - Maximum 1 à 2 indicateurs par scope (lisibilité et pertinence).
  - Pas de valeurs chiffrées inventées ou d'exemples factices : mention explicite « *À déterminer* » en concertation avec les acteurs réels (phase d'étude financière R3).
  - Exclusion des KPIs d'exploitation purement techniques (SLA d'infrastructure, latence réseau), réservés au dossier technique d'architecture.

---

## 6. Synthèse de Répartition des Pages (Référence Gabarit)

| Page | Contenu Fonctionnel Maître | Composants & Visuels Clés |
|:---:|:---|:---|
| **P. 1** | **1.1 Présentation du Projet & Double Finalité**<br>**1.2 Expression du Besoin (Bête à Cornes)** | • Badges finalité commerciale / citoyenne<br>• Dimensions canoniques du besoin<br>• **Figure 1.1** : Bête à Cornes APTE (ratio 2:1) |
| **P. 2** | **1.3 Matrice de Positionnement Stratégique**<br>**Légende Analytique & Benchmark** | • Définition des 2 axes orthogonaux<br>• **Figure 1.2** : Matrice concurrentielle 4 quadrants<br>• Analyse benchmark des acteurs (Ollca, Epicery, Amazon, Proxity) |
| **P. 3** | **1.4 Objectifs du Projet**<br>(Format Analyste Métier) | • **Objectifs Stratégiques** : OS-01, OS-02, OS-03<br>• **Objectifs Opérationnels par profil** :<br>&nbsp;&nbsp;- Citoyen (OP-CIT-01, OP-CIT-02)<br>&nbsp;&nbsp;- Commerçant (OP-COM-01, OP-COM-02)<br>&nbsp;&nbsp;- Collectivité (OP-COL-01, OP-COL-02)<br>• Format normé : *Énoncé cible* + *Explication opérationnelle* |
| **P. 4** | **1.5 Périmètre Système In-Scope / Out-of-Scope**<br>**1.6 Gratuité Citoyenne & Inclusion Universelle** | • Tableau Booktabs à 6 lignes comparatives<br>• 3 principes d'équité sociale : Gratuité totale, inclusion seniors (persona Pierre 74 ans, RGAA AA, procuration) et RGPD |
| **P. 5** | **1.7 Indicateurs Clés de Performance (KPIs)** | • Scope 1 : Performance Locale (VFP, Pénétration locale)<br>• Scope 2 : Performance Nationale SaaS (Collectivités conventionnées)<br>• Cibles « À déterminer » en phase R3 |

---

## 7. Checklist d'Auto-Vérification pour les Prochaines Sections

Avant de déclarer une section du Cahier des Charges finalisée, l'agent ou le rédacteur doit valider les 10 critères suivants :

1. [ ] **Pagination maîtrisée** : La section commence sur une page propre et n'a aucune ligne isolée sur une page suivante.
2. [ ] **Zéro Justification** : Tous les paragraphes et listes sont en `text-align: left`.
3. [ ] **Zéro Emoji** : Aucun emoji présent dans le document.
4. [ ] **Format Objectifs Analyste** : Tout objectif opérationnel comporte un ID, son énoncé simple et son explication métier.
5. [ ] **Ratio des figures protégé** : Les figures utilisent `height: auto` et ne sont pas étirées.
6. [ ] **Visuel unique (Anti-AI Slop)** : Aucune languette latérale (`border-left`) sur les encarts.
7. [ ] **Benchmark explicité** : Toute référence à une solution existante est justifiée par une analyse comparative.
8. [ ] **Tableaux Booktabs** : Zéro filet vertical, bordures horizontales contrastées.
9. [ ] **Script de vérification exécuté** : `python agent_projet/scripts/verify_deliverables.py` retourne 0 violation.
10. [ ] **Synchronisation Google Drive** : Fichier synchronisé dans le dossier Drive de l'équipe.
