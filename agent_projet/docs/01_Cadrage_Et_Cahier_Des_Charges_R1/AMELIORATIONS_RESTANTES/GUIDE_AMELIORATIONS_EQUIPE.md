# FEUILLE DE ROUTE & AMÉLIORATIONS DU CAHIER DES CHARGES R1

Ce document récapitule l'ensemble des points d'amélioration identifiés sur le Cahier des Charges R1 (*ShopLoc_Cahier_des_Charges_Livrable_R1.pdf* / *CAHIER_DES_CHARGES_R1.md*). Il est destiné à guider les membres de l'équipe Garik pour la finalisation du livrable avant la soutenance.

---

## 1. Diagramme d'Architecture Technique (Figure 4.1 / Section 4)

### Constats actuels
- Le schéma actuel comporte **trop de blocs de texte denses** qui nuisent à l'impact visuel.
- La typographie et les contrastes de couleurs ne respectent pas parfaitement la charte UI officielle du projet (*Plus Jakarta Sans*, contrastes pastel doux, lisibilité immédiate).
- Le niveau de détail doit être recentré sur l'essentiel pour un prototype de Master 2.

### Actions à réaliser par l'équipe
1. **Refonte visuelle orientée "Icônes & Logos"** :
   - Remplacer les longs paragraphes par des cartes épurées avec les logos officiels (React, TypeScript, Spring Boot, PostgreSQL, Docker, GitLab).
   - Minimiser le texte descriptif dans le diagramme : n'afficher que les noms des couches, des composants et les flux de communication essentiels.
2. **Conformité stricte à la charte UI ShopLoc** :
   - Fond lin doux (`#FAF9F6`), bordures subtiles (`#DCD6CD`), typographie harmonisée (*Plus Jakarta Sans*).
   - Utilisation des codes couleurs métier ShopLoc : Ardoise (`#243342`), Terracotta (`#C26750` - Citoyen), Sauge (`#4A7A5B` - Commerçant), Miel (`#C48B28` - Mairie).
   - Assurer un niveau de contraste élevé et agréable pour l'impression A4 et la lecture écran.
3. **Maintien du format A4 Paysage** :
   - Conserver l'intégration dans une page dédiée A4 paysage (`.landscape-page`) pour une lisibilité maximale.

---

## 2. Diagramme de Gantt Annuel (Figure 5.1 / Section 5)

### Constats actuels
- Le modèle de Gantt actuel manque de clarté et comporte des phases trop génériques ou déconnectées des contraintes réelles du sujet.

### Actions à réaliser par l'équipe
1. **Ancrage exclusif sur les jalons contractuels de l'UE GLOP** :
   - **Jalon R1 (18/09/2026)** : Cadrage & Réponse à l'appel d'offres (Soutenance le 21/09).
   - **Jalon R2 (12/10/2026)** : Choix d'outillage & Socle technique.
   - **Jalon R3 (30/11/2026)** : Analyse financière & Coûts complets.
   - **Jalon R4 (18/12/2026)** : Premier prototype logiciel & Architecture V1 (Soutenance le 04/01/2027).
   - **Jalon R5 (19/03/2027)** : Version complète V2 & Bilan d'exploitation (Soutenance le 22/03/2027).
2. **Prise en compte du calendrier universitaire réel** :
   - Intégrer explicitement les périodes de vacances (Toussaint, Noël, Hiver) et les périodes d'examens/partiels universitaires.
   - Positionner clairement les périodes de gel de code / relecture collective (buffer de 72h avant chaque rendu).
3. **Suppression de toute tâche inventée** :
   - Structurer les barres du diagramme uniquement autour des livrables et activités réels du projet ShopLoc.

---

## 3. Calcul des Coûts par la Méthode des Coûts Complets (Section 6)

### Constats actuels
- La structure de calcul est trop alambiquée et certaines formules KaTeX / Markdown présentent des erreurs de rendu ou d'alignement.

### Actions à réaliser par l'équipe
1. **Simplification de la structure de calcul** :
   - Partir sur une présentation simple et didactique des deux grandes masses :
     * **Charges directes** : Indemnités de stage/alternance des 5 étudiants sur les mois actifs du projet.
     * **Charges indirectes** : Frais d'infrastructure sourcés (VPS OVHcloud, nom de domaine, services de mails, assurances, amortissement matériel).
2. **Correction et clarté des affichages mathématiques** :
   - Vérifier et corriger le formatage des calculs KaTeX (espacements, symboles monétaires `€`, équations en blocs centrés `$$...$$`).
   - Présenter les tableaux récapitulatifs de manière aérée et sans surcharge pour faciliter la lecture des évaluateurs.

---

## 4. Annexes : CVs et Personas Complets au Format A4

### Constats actuels
- Les CVs et fiches personas complètes doivent être intégrés proprement en annexes et reliés depuis le corps du texte.

### Actions à réaliser par l'équipe
1. **Intégration des CVs réels** :
   - Insérer les 5 CVs complets des membres du groupe (Khalil Bouchama, Abdelkader Heddi, Gautam Demeulemeester, Rayane Alli, Ilyas Ait Ali) dans le dossier d'annexes.
2. **Intégration des fiches Personas au format A4 Paysage** :
   - Insérer les fiches personas complètes et détaillées générées lors du cadrage ergonomique en fin de document.
3. **Vérification des liens et références** :
   - Vérifier que toutes les références textuelles dans les sections 2.1 (CVs) et 3.3 (Personas) pointent de manière exacte et fonctionnelle vers leurs annexes respectives.

---

## 5. Renforcement de la Section 6.5 : Choix du Business Model & Rentabilité de Garik

### Constats actuels
- La section 6.5 ne valorise pas suffisamment la viabilité économique et les perspectives de gain de l'entreprise Garik.
- Garik est une société d'ingénierie logicielle qui doit dégager un bénéfice net pour pérenniser son activité, investir dans sa R&D et rémunérer ses associés fondateurs.

### Actions à réaliser par l'équipe
1. **Justification rigoureuse du choix de modèle économique** :
   - Établir le modèle tarifaire sur la base du coût de revient unitaire issu du calcul des coûts complets.
   - Justifier pourquoi le modèle de licence/abonnement annuel par collectivité territoriale (SaaS communal) est le plus protecteur et vertueux par rapport aux modèles à commission marchande.
2. **Hypothèses explicites de chiffre d'affaires et de rentabilité** :
   - Définir des hypothèses de déploiement réalistes (ex. 1 ville pilote en Année 1, puis 3 à 5 villes moyennes en Année 2 et 3).
   - Intégrer un **pourcentage de marge bénéficiaire cible** (ex. 15% à 25% de marge commerciale) appliqué sur le coût de revient complet.
   - Calculer le bénéfice net projeté de Garik permettant de financer le développement de nouvelles fonctionnalités (V2/V3) et de constituer des réserves de trésorerie.

---

## 6. Synthèse des Priorités pour l'Équipe

| Priorité | Sujet | Responsable suggéré | Livrable attendu |
|---|---|---|---|
| **P1** | Architecture technique épurée & logos UI | Ilyas Ait Ali / Gautam Demeulemeester | Nouveau composant `tech_choices_diagram.html` et image HD A4 paysage |
| **P2** | Diagramme de Gantt recalibré R1-R5 | Khalil Bouchama / Rayane Alli | Nouveau script Gantt et image HD conforme |
| **P3** | Coûts complets simplifiés & correction KaTeX | Gautam Demeulemeester / Khalil Bouchama | Section 6.1 à 6.4 révisée dans `CAHIER_DES_CHARGES_R1.md` |
| **P4** | Section 6.5 : Business model, marge & rentabilité | Abdelkader Heddi / Gautam Demeulemeester | Section 6.5 enrichie avec hypothèses de gains et taux de marge |
| **P5** | Assemblage annexes (CVs + Personas A4) & liens | Khalil Bouchama / Ilyas Ait Ali | Annexes intégrées et compilation PDF finale |
