---
name: strategic-cost-accounting
description: "Master strategic cost accounting and financial planning for software engineering. Covers Full Costing (coûts complets, centres d'analyse, unités d'œuvre), Direct Costing, 3-year P&L, balance sheets, and ROI/NPV/IRR models."
risk: safe
source: project-tailored
tags: [finance, full-costing, couts-complets, p-and-l, business-plan, roi, npv, r3]
---

# Contrôle de Gestion Stratégique & Analyse des Coûts Complets

Ce skill implémente la méthodologie financière universitaire de référence (conforme au support de cours officiel *« La gestion stratégique des coûts 2026.pdf »*) pour la Section 09 du Cahier des Charges R1 et l'Étude Financière approfondie du Livrable R3.

## Quand utiliser ce skill
- Chiffrage financier préliminaire et justification tarifaire dans la Section 09 du Cahier des Charges R1.
- Élaboration complète de l'Étude Financière R3 (Compte de Résultat prévisionnel 3 ans, Bilan d'ouverture et de clôture, Tableau des Flux de Trésorerie).
- Détermination du coût de revient d'une collectivité et calcul des indicateurs de rentabilité (VAN, TRI, Seuil de Rentabilité, Payback).

## Principes Méthodologiques Majeurs

### 1. La Méthode des Coûts Complets (Centres d'Analyse)
- **Charges Directes** : Affectées sans ambiguïté à un produit ou service (ex : temps de développement dédié, hébergement spécifique d'un tenant).
- **Charges Indirectes** : Transitent obligatoirement par des **Centres d'Analyse** avant imputation :
  - **Centres Auxiliaires** : Gestion des infrastructures, administration générale, outillage FinOps (leurs coûts sont déversés sur les centres principaux via des clés de répartition primaire et secondaire).
  - **Centres Principaux** :
    1. *Centre Build (Ingénierie & Développement)* — Unité d'Œuvre (UO) : Jour/Homme de développement.
    2. *Centre Run (Exploitation & Cloud)* — UO : Nombre de transactions ou volume de données hébergées.
    3. *Centre Support & Relation Clients* — UO : Nombre de tickets commerçants/villes traités.
    4. *Centre Déploiement Territorial* — UO : Nombre de commerces raccordés.

### 2. Le Direct Costing & Seuil de Rentabilité
- Séparation stricte entre **Charges Variables** (proportionnelles au volume de villes ou de commerces) et **Charges Fixes** (salaires structurels, amortissement du socle logiciel, licences).
- Calcul de la **Marge sur Coût Variable (MCV)** : `MCV = Chiffre d'Affaires - Charges Variables`.
- Taux de MCV : `Taux MCV = MCV / Chiffre d'Affaires`.
- **Seuil de Rentabilité (SR en valeur)** : `SR = Charges Fixes / Taux MCV` (point mort en jours : `(SR / CA) * 360`).

### 3. Modélisation Pluriannuelle & Rigueur Comptable (Livrable R3)
- **Compte de Résultat (P&L 3 ans)** :
  - Produits d'exploitation (subventions municipales tripartites + adhésions annuelles commerçants à l'association).
  - Charges d'exploitation (charges de personnel, sous-traitance, hébergement Docker/PostgreSQL, amortissements).
  - Résultat d'exploitation, résultat financier, résultat exceptionnel et résultat net.
- **Bilan Équilibré** : Égalité comptable absolue `Actif = Passif` (Actif immobilisé, actif circulant, trésorerie vs Capitaux propres, dettes financières, dettes d'exploitation).
- **Critères d'Investissement** :
  - **VAN (Valeur Actuelle Nette)** à un taux d'actualisation explicite (ex : 8%).
  - **TRI (Taux de Rentabilité Interne)**.
  - **Délai de Récupération du Capital Investi (Payback)**.

## Règle Anti-Invention Inviolable
Toutes les données chiffrées doivent provenir exclusivement d'hypothèses réelles validées avec l'équipe ou du moteur arithmétique déterministe [`financial_engine.py`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/agent_projet/scripts/financial_engine.py). Aucune valeur spéculative n'est injectée de manière autonome par l'IA.
