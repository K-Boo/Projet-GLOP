# GUIDE D'ASSISTANCE & DE MONTÉE EN COMPÉTENCES FINANCIÈRES (SHOPLOC)
## UE Génie Logiciel par la Pratique (GLOP) — Master 2 MIAGE — Université de Lille

Ce guide est destiné aux 5 étudiants-ingénieurs de l'équipe ShopLoc. Il explique concrètement comment mobiliser l'**Agent de Gestion Financière et Stratégique** comme un assistant et tuteur expert, afin de comprendre chaque notion, co-construire les choix économiques et réussir les soutenances orales sans jamais subir une « boîte noire ».

---

## 1. Philosophie : L'Humain au Centre (Human-in-the-Loop)

Dans le projet ShopLoc, la gestion financière (chiffrage R1, rentabilité R3, calculs de coûts complets) est un élément déterminant de la notation.
* **Le piège à éviter** : Demander à une IA de générer un rapport financier tout fait. Devant les enseignants évaluateurs (Laurence Duchien, Anne Etien, François Secchi, Jérémy Woirhaye), vous seriez incapables d'expliquer l'origine des chiffres et les justifications méthodologiques.
* **La bonne approche** : Utiliser l'agent pour apprendre, poser des questions, tester des hypothèses et progresser pas-à-pas. Vous conservez 100 % du contrôle décisionnel, et vous ne déléguez les calculs lourds qu'une fois la logique comprise.

---

## 2. Les 4 Modes d'Intervention de l'Agent

Vous pouvez orienter le comportement de l'agent en ajoutant simplement un préfixe au début de votre message :

```text
[MODE: TUTEUR]     --> Pour comprendre un concept théorique ou une formule sans jargon
[MODE: COPILOTE]    --> (Par défaut) Pour réfléchir ensemble à une hypothèse ou un choix de tarif
[MODE: AUDITEUR]   --> Pour relire votre travail ou simuler les questions pièges du jury de soutenance
[MODE: EXECUTANT]  --> Pour lancer les calculs par script Python une fois vos chiffres arrêtés
```

### Mode 1 : Tuteur Pédagogique (`[MODE: TUTEUR]`)
L'agent n'écrit aucun livrable officiel et ne donne pas de chiffre brut. Il vous explique la méthode avec des analogies adaptées aux informaticiens (comparaisons avec les architectures logicielles, le devops ou les algorithmes) et vous pose des questions pour vous aider à trouver la solution par vous-même.

### Mode 2 : Copilote de Co-conception (`[MODE: COPILOTE]` — Mode Actif par Défaut)
C'est le mode de travail au quotidien. Vous avancez une idée ou un ordre de grandeur (ex. *"On pense facturer 5 000 € aux petites villes"*), l'agent calcule immédiatement l'impact économique (seuil de rentabilité, trésorerie), vous alerte sur les risques ou les oublis, et vous propose des pistes. La décision finale vous appartient toujours.

### Mode 3 : Auditeur Critique & Répétition d'Oral (`[MODE: AUDITEUR]` ou `[MODE: JURY]`)
L'agent endosse le costume d'un professeur examinateur exigeant. Il passe au crible vos arguments, challenge vos hypothèses et simule les questions déstabilisantes que le jury pourrait vous poser lors de la soutenance.

### Mode 4 : Exécutant Déterministe (`[MODE: EXECUTANT]`)
Une fois que vous maîtrisez la démarche et que l'équipe a validé ses chiffres réels, vous transmettez le fichier de configuration à l'agent. Il exécute le script `financial_engine.py` pour produire les tableaux et classeurs Excel avec des calculs exacts et certifiés, sans hallucination d'arrondi.

---

## 3. Les 4 Casquettes Métier Sollicitables

En complément du mode, vous pouvez préciser la spécialité attendue :
* **`[ROLE: COUTS]`** : Spécialiste de la méthode des coûts complets et partiels (support de cours MIAGE : chaîne de valeur ESN, répartition primaire/secondaire, unités d'œuvre, direct costing).
* **`[ROLE: CFO]`** : Spécialiste de la finance d'entreprise (compte de résultat P&L, bilan équilibré, trésorerie, actualisation VAN/TRI, payback).
* **`[ROLE: PRICING]`** : Spécialiste de la tarification communale (forfaits pour les 3 segments de villes, convention tripartite Mairie-Association-Commerçants ADR-004).
* **`[ROLE: JURY]`** : Entraînement oral pour la soutenance.

---

## 4. Dix Exemples de Requêtes Types pour l'Équipe

Voici des formulations prêtes à l'emploi que chaque membre de l'équipe peut copier-coller et adapter dans le chat :

### Compréhension Théorique & Méthodologie (Mode Tuteur)
* **Exemple 1 (Coûts complets)** :  
  `[MODE: TUTEUR] [ROLE: COUTS] Je ne comprends pas bien pourquoi le cours de MIAGE applique la méthode des coûts complets aux ESN. Peux-tu m'expliquer la chaîne de valeur de Michael Porter et comment elle s'applique concrètement à notre projet ShopLoc ?`
* **Exemple 2 (Répartition primaire et secondaire)** :  
  `[MODE: TUTEUR] [ROLE: COUTS] Peux-tu m'expliquer simplement la différence entre la répartition primaire et la répartition secondaire des charges indirectes ? Donne-moi une analogie simple avec l'informatique.`
* **Exemple 3 (Unités d'œuvre)** :  
  `[MODE: TUTEUR] [ROLE: COUTS] Qu'est-ce qu'une unité d'œuvre (UO) ? Pourquoi le choix de l'UO est-il crucial pour éviter les subventionnements croisés ? Quelles UO seraient pertinentes pour ShopLoc ?`
* **Exemple 4 (Direct costing & Point mort)** :  
  `[MODE: TUTEUR] [ROLE: COUTS] Peux-tu m'expliquer la différence entre marge sur coût variable (MCV) et résultat courant ? Comment calcule-t-on le seuil de rentabilité en euros et en nombre de jours ?`
* **Exemple 5 (VAN et TRI)** :  
  `[MODE: TUTEUR] [ROLE: CFO] Pourquoi doit-on actualiser les flux de trésorerie futurs avec un taux k pour calculer la VAN ? Pourquoi un euro dans 3 ans vaut-il moins qu'un euro aujourd'hui ?`

### Co-conception des Hypothèses Réelles (Mode Copilote)
* **Exemple 6 (Estimation du coût de build)** :  
  `[MODE: COPILOTE] [ROLE: CFO] Pour le livrable R1, on doit chiffrer la réalisation de ShopLoc par notre équipe de 5 étudiants. Comment doit-on valoriser notre temps de travail ? Doit-on compter un taux horaire junior ou des indemnités de stage ?`
* **Exemple 7 (Tarification communale)** :  
  `[MODE: COPILOTE] [ROLE: PRICING] La MOA nous demande un prix adapté aux 3 segments (petite, moyenne et grande ville). Quels ordres de grandeur de prix sont acceptables pour une association de commerçants subventionnée par la mairie ?`
* **Exemple 8 (Arbitrage Faire ou Faire-Faire)** :  
  `[MODE: COPILOTE] [ROLE: COUTS] On hésite entre héberger la plateforme sur un cloud mutualisé (type AWS/OVH) ou acheter notre propre serveur physique. Peux-tu nous guider avec la méthode du Direct Costing Évolué pour faire ce choix ?`

### Entraînement Oral & Revue Critique (Mode Auditeur)
* **Exemple 9 (Simulation de questions de soutenance)** :  
  `[MODE: AUDITEUR] [ROLE: JURY] Incarne l'un de nos professeurs évaluateurs lors de la soutenance R3. Pose-moi 3 questions difficiles et pièges sur notre stratégie financière et nos coûts pour tester mes connaissances.`

### Automatisation Outillée (Mode Exécutant)
* **Exemple 10 (Génération des calculs certifiés)** :  
  `[MODE: EXECUTANT] L'équipe a validé ses hypothèses réelles dans le fichier agent_projet/financials/hypotheses_equipe.json. Peux-tu exécuter le script financial_engine.py et vérifier que le bilan est parfaitement équilibré ?`

---

## 5. Aide-Mémoire Méthodologique des Formules Clés

| Concept Financier | Formule Mathématique | Interprétation pour ShopLoc |
|---|---|---|
| **Coût d'une Unité d'Œuvre (UO)** | $\frac{\text{Total charges indirectes après rép. secondaire}}{\text{Nombre total d'UO du centre}}$ | Coût unitaire d'imputation aux villes clientes (ex. coût par heure d'ingénieur ou par commune). |
| **Marge sur Coût Variable (MCV)** | $CA - CV$ | Ce qu'il reste du chiffre d'affaires après avoir payé les charges variables (serveurs volumétriques, SMS). |
| **Taux de MCV (TMCV)** | $\frac{MCV}{CA}$ | Pourcentage de chaque euro de CA qui contribue à couvrir les charges fixes. |
| **Seuil de Rentabilité (SR)** | $\frac{\text{Charges Fixes (CF)}}{TMCV}$ | Niveau de chiffre d'affaires minimum à atteindre pour ne faire ni perte ni bénéfice ($Résultat = 0$). |
| **Marge de Sécurité (MS)** | $CA - SR$ | Baisse maximale de chiffre d'affaires que ShopLoc peut supporter avant d'entrer en perte. |
| **Valeur Actuelle Nette (VAN)** | $\sum_{t=1}^{n} \frac{CF_t}{(1 + k)^t} - I_0$ | Gain net généré par le projet au-delà du taux de rentabilité exigé $k$. Si $VAN > 0$, le projet enrichit l'entreprise. |
| **Taux de Rentabilité Interne (TRI)** | Taux $r$ tel que $VAN(r) = 0$ | Taux de rentabilité maximal auquel ShopLoc pourrait emprunter sans perdre d'argent. |
| **Délai de Récupération (Payback)** | Période où $\sum CF_t = I_0$ | Moment où l'investissement initial est totalement remboursé. Doit intervenir avant 18 mois. |

---

## 6. Règles Fondamentales à Respecter

1. **Règle Zéro Invention** : Si vous ne disposez pas d'un chiffre réel, ne demandez pas à l'agent d'en inventer un. Travaillez sur des ordres de grandeur ou marquez la case `En attente d'arbitrage MOA`.
2. **Règle Zéro Emoji** : Aucun emoji ne doit figurer dans les notes, documents ou échanges formels (ADR-002).
3. **1 Session = 1 Tâche Atomique** : Ne mélangez pas la discussion sur le modèle financier avec la rédaction des User Stories ou l'architecture technique. Traitez un sujet à la fois pour économiser les quotas et préserver la clarté du projet.
