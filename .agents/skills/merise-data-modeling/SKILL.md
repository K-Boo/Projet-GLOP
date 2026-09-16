---
name: merise-data-modeling
description: "Design conceptual data models (MCD) using Merise notation and derive normalized relational dictionaries (MLD) in PostgreSQL. Formats entities, verbal associations, cardinalities, and Booktabs tables."
risk: safe
source: project-tailored
tags: [merise, mcd, mld, database, postgresql, data-dictionary, cardinalities]
---

# Modélisation Conceptuelle des Données (Méthode Merise & MLD)

Ce skill formalise l'ingénierie des données du projet ShopLoc conformément aux normes académiques françaises Merise et aux meilleures pratiques de modélisation relationnelle (3NF / BCNF) pour PostgreSQL 16.

## Quand utiliser ce skill
- Élaboration du Modèle Conceptuel de Données (MCD) pour la Section 04 du Cahier des Charges R1.
- Rédaction du Dictionnaire Formel des Données (Attributs, types logiques, règles de gestion).
- Dérivation en Modèle Logique de Données (MLD) relationnel pour l'architecture PostgreSQL (Section 07).

## Standards & Règles de Modélisation

### 1. Formalisme du Modèle Conceptuel (MCD)
- **Entité** :
  - Rectangle à coins arrondis avec cartouche d'en-tête contenant le nom de l'entité en majuscules (ex : `CITOYEN`, `COMMERCE`, `COMMANDE`).
  - Séparation horizontale par un trait net.
  - Clé primaire soulignée et préfixée par `#` (ex : `# id_citoyen (UUID)`).
  - Liste typée des attributs descriptifs.
- **Association / Relation** :
  - Ovale ou rectangle très arrondi contenant un verbe d'action à l'infinitif (ex : `Passer`, `Composer`, `Déclencher`).
  - Éventuels attributs portés par la relation (ex : `quantite`, `prix_unitaire_facture` sur l'association `Composer`).
- **Cardinalités Explicites** :
  - `0,1` : Participation optionnelle, au plus une occurrence.
  - `1,1` : Participation obligatoire, exactement une occurrence.
  - `0,n` : Participation optionnelle, plusieurs occurrences possibles.
  - `1,n` : Participation obligatoire, au moins une occurrence.

### 2. Dictionnaire de Données Normalisé (Format Booktabs)
Chaque entité et association fait l'objet d'une documentation tabulaire rigoureuse :
- **Entité / Association** : Nom canonique.
- **Attribut** : Identifiant technique SQL.
- **Libellé métier** : Description fonctionnelle intelligible.
- **Type Logique** : `UUID`, `VARCHAR(n)`, `INTEGER`, `DECIMAL(10,2)`, `TIMESTAMP`, `BOOLEAN`, `ENUM`.
- **Nullabilité & Contraintes** : `NOT NULL`, `UNIQUE`, `CHECK`, `DEFAULT`.
- **Règle de gestion / RGPD** : Justification métier, pseudonymisation ou règles de rétention.

### 3. Règles d'Architecture Spécifiques à ShopLoc
- **Découplage strict des deux moteurs** : Aucun lien de jointure direct entre les points marchands (décentralisés par boutique) et le statut communal VFP (fondé sur les passages temporels).
- **Pseudonymisation RGPD native** : Pas de stockage en clair des emails ou noms dans les tables transactionnelles ; hachage salé et identifiants non séquentiels UUIDv4.
- **Partitionnement territorial** : Présence systématique d'une clé de partitionnement communal `code_commune` pour garantir l'étanchéité multi-tenant.

## Format de Sortie
Génération de schémas vectoriels SVG purs stylisés selon les Design Tokens pastel du projet, complétés par des tableaux Booktabs compatibles avec [`render_report.py`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/agent_projet/scripts/render_report.py).
