# Projet ShopLoc — Marketplace & Fidélisation de Centre-Ville
> **Master 2 MIAGE — UE Génie Logiciel par la Pratique (GLOP) 2026-2027**  
> Université de Lille — Faculté des Sciences et Technologies (FST)

---

## 👥 Présentation du Projet

ShopLoc est une solution territoriale visant à revitaliser les commerces de centre-ville face aux grandes surfaces de périphérie. La plateforme intègre :
* Une **Marketplace Click & Collect multi-commerces** avec panier mutualisé.
* Un **programme de fidélité partagé** entre commerces avec compensation financière.
* L'interconnexion avec les **services municipaux de stationnement** (conversion des points en gratuité de stationnement).
* Des outils marketing et de reporting pour l'association des commerçants et la Mairie (dans le respect strict du RGPD).
* Une ergonomie inclusive pensée pour tous les usagers (persona senior Pierre 74 ans, conformité RGAA).

---

## 🚀 Démarrage Rapide pour l'Équipe

L'ensemble de la configuration du projet, des directives de l'agent et des 40 skills d'ingénierie logicielle est versionné sur ce dépôt.

### 1. Cloner le dépôt
```bash
git clone git@github.com:K-Boo/Projet-GLOP.git
cd Projet-GLOP
```

### 2. Ouvrir dans Antigravity
Ouvrez simplement ce dossier dans votre IDE Antigravity. L'agent charge automatiquement les règles du projet et la boîte à outils.

### 3. Installer Google Drive pour ordinateur
Installez l'application officielle **Google Drive pour ordinateur** et connectez votre compte pour accéder au dossier partagé `Projet-GLOP`.

### 4. Laisser l'agent s'occuper du reste
Dans la discussion avec votre agent Antigravity, demandez-lui simplement :
> *« Aligne mon environnement sur la configuration d'équipe »*

L'agent lira automatiquement les directives d'équipe (`.antigravity/setup_equipe.md`), installera les dépendances nécessaires et configurera la liaison avec votre Google Drive de manière autonome.

---

## 🏛️ Organisation du Dépôt : Deux Pôles Dédiés

Pour séparer nettement la phase de cadrage/livrables de la future phase d'implémentation logicielle, le projet est scindé en deux espaces :
* 📂 **`agent_projet/`** : Réservé à l'**Agent Projet & Livrables** (cadrage R1, étude financière R3, registres agiles `docs/`, logos `images/`, génération PDF et synchronisation Google Drive).
* 📂 **`agent_code/`** : Réservé à l'**Agent Ingénieur Logiciel & Code** (architecture backend/frontend `src/`, configurations `docker/` et tests).
