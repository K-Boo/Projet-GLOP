# Partie 6 : Analyse des Coûts Complets (Projet ShopLoc)

**Contexte**
L'entreprise étudiante Garik déploie la plateforme SaaS ShopLoc pour redynamiser les centres-villes. La direction souhaite calculer le coût de revient détaillé et la rentabilité globale du projet ShopLoc sur sa première année. 
Conformément aux exigences, **ce coût détaillé du projet comprend sa réalisation initiale (Build), mais également son exploitation et sa maintenance (Run)**. La méthode employée est celle des coûts complets par centres d'analyse.

---

## 1. Charges directes du projet

| Élément | Projet Global ShopLoc |
| :--- | :---: |
| Heures de développeurs (MOD - Réalisation, Exploitation & Maintenance) | 480 h |
| Taux horaire chargé de l'équipe d'ingénierie | 25 €/h |
| Achats directs (Hébergement Cloud VPS, domaine, licences spécifiques) | 2 400 € |
| Heures commerciales (Avant-vente et relations collectivités) | 60 h |
| **Prix de vente facturé (Chiffre d'affaires global de l'année)** | **88 000 €** |

*Les heures de l'équipe d'ingénierie dédiées au projet et les achats d'infrastructures (serveurs) constituent des charges directes affectables sans ambiguïté au coût du projet.*

---

## 2. Charges indirectes de la période

Le tableau de répartition ci-dessous concerne l'ensemble des charges indirectes de l'entreprise (36 000 € au total : locaux, assurances, direction, outils transverses), ventilées en 4 centres d'analyse personnalisés pour l'activité de Garik.

### 2.1 Répartition primaire

| Centre | % de répartition primaire | Montant |
| :--- | :---: | :---: |
| Administration générale & Gouvernance (auxiliaire) | 33,33 % | 12 000 € |
| Support Infra & Outillage DevOps (auxiliaire) | 16,67 % | 6 000 € |
| Commercial & Déploiement (principal) | 16,67 % | 6 000 € |
| Production (Réalisation, Exploitation & Maintenance) (principal) | 33,33 % | 12 000 € |
| **Total** | **100 %** | **36 000 €** |

### 2.2 Répartition secondaire (cession des centres auxiliaires)

Les centres auxiliaires cèdent la totalité de leurs charges aux autres centres selon les clés suivantes :

**Administration générale & Gouvernance** se répartit sur :
* Support Infra & Outillage DevOps : 10 %
* Commercial & Déploiement : 30 %
* Production (Réal., Exploit. & Maint.) : 60 %

**Support Infra & Outillage DevOps** (charges propres + charges reçues de l'Administration) se répartit sur :
* Commercial & Déploiement : 20 %
* Production (Réal., Exploit. & Maint.) : 80 %

**Tableau de calcul de la répartition secondaire :**

| Centres | Administration | Support Infra | Commercial | Production |
| :--- | :---: | :---: | :---: | :---: |
| **Totaux primaires** | **12 000 €** | **6 000 €** | **6 000 €** | **12 000 €** |
| Cession Administration | - 12 000 € | + 1 200 € | + 3 600 € | + 7 200 € |
| Cession Support Infra | | - 7 200 € | + 1 440 € | + 5 760 € |
| **Totaux secondaires** | **0 €** | **0 €** | **11 040 €** | **24 960 €** |

*(Le total des charges indirectes après répartition secondaire est bien de 11 040 € + 24 960 € = 36 000 €)*

### 2.3 Unités d'œuvre des centres principaux

| Centre principal | Unité d'œuvre (UO) | Nombre total d'UO du projet | Coût de l'Unité d'Œuvre |
| :--- | :--- | :--- | :--- |
| Commercial & Déploiement | l'heure commerciale | 60 h | **184,00 €** / h |
| Production (Réalisation, Exploitation & Maintenance) | l'heure de développeur facturable | 480 h | **52,00 €** / h |

<div align="center">
  <img src="https://latex.codecogs.com/png.latex?\bg_white&space;\text{Cout&space;UO&space;Commercial}=\frac{11040}{60}=184\text{\euro/h}" alt="Calcul UO Commercial" />
  <br/><br/>
  <img src="https://latex.codecogs.com/png.latex?\bg_white&space;\text{Cout&space;UO&space;Production}=\frac{24960}{480}=52\text{\euro/h}" alt="Calcul UO Production" />
</div>

---

## 3. Coût de revient complet du Projet ShopLoc

Pour obtenir le coût de revient détaillé et complet du projet, nous additionnons ses charges directes (hébergement, développement) et ses charges indirectes imputées via les UO.

| Élément | Détail du Calcul | Montant imputé |
| :--- | :--- | :---: |
| **Charges directes** | | |
| Heures de développeurs (MOD - Réal, Exploit & Maint) | 480 h × 25 € | 12 000 € |
| Achats directs (Cloud, Domaines) | | 2 400 € |
| **Charges indirectes** | | |
| Centre Commercial & Déploiement | 60 h × 184 € | 11 040 € |
| Centre Production (Réalisation, Exploitation & Maintenance) | 480 h × 52 € | 24 960 € |
| **COÛT DE REVIENT COMPLET** | | **50 400 €** |

---

## 4. Résultat analytique du Projet

### 4.1 Calcul du résultat et commentaires

<div align="center">
  <img src="https://latex.codecogs.com/png.latex?\bg_white&space;\text{Resultat}=\text{Chiffre&space;d'Affaires}-\text{Cout&space;de&space;Revient}" alt="Formule Résultat" />
</div>
<br/>

**Résultat ShopLoc** = 88 000 € - 50 400 € = **+ 37 600 €**

**Commentaire :** Le projet ShopLoc (couvrant tout le cycle de réalisation, d'exploitation et de maintenance) dégage un résultat analytique très positif de 37 600 €. La marge bénéficiaire s'élève à 42,7 % du chiffre d'affaires, confirmant la pertinence économique du modèle SaaS retenu.

### 4.2 Contrôle de reconstitution des charges

<div align="center">
  <img src="https://latex.codecogs.com/png.latex?\bg_white&space;\text{Total&space;Cout&space;de&space;Revient}=14400&space;\text{(Dir.)}&space;+&space;36000&space;\text{(Indir.)}=50400&space;\text{\euro}" alt="Reconstitution des charges" />
</div>

Le coût de revient détaillé (50 400 €) correspond parfaitement à l'absorption complète des charges directes de l'entreprise sur ce projet (14 400 €) et de ses charges indirectes (36 000 €).

### 4.3 Simulation d'un prix de vente (PV) pour une rentabilité cible de 15%

Si la direction avait souhaité fixer un prix de vente assurant un résultat de très exactement 15% du Chiffre d'Affaires (PV) :
* Résultat attendu = 15% du PV
* Coût de revient complet = 85% du PV

<div align="center">
  <img src="https://latex.codecogs.com/png.latex?\bg_white&space;\text{Prix&space;de&space;Vente&space;Cible}=\frac{\text{Cout&space;de&space;Revient}}{0,85}=\frac{50400}{0,85}=59294,12&space;\text{\euro}" alt="Calcul du Prix Cible" />
</div>
<br/>

**Prix de vente ciblé : 59 294,12 €**
*(Le projet a donc été facturé à un montant nettement supérieur à ce seuil de rentabilité minimum).*
