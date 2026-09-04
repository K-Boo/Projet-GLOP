# Projet ShopLoc — Marketplace & Fidélisation de Centre-Ville
> **Master 2 MIAGE — UE Génie Logiciel par la Pratique (GLOP) 2026-2027**  
> Université de Lille — Faculté des Sciences et Technologies (FST)

---

## 1. Présentation du Projet

ShopLoc est une solution territoriale visant à revitaliser les commerces de centre-ville face aux grandes surfaces de périphérie. La plateforme intègre :
* Une **Marketplace Click & Collect multi-commerces** avec panier mutualisé.
* Un **programme de fidélité partagé** entre commerces avec compensation financière.
* L'interconnexion avec les **services municipaux de stationnement** (conversion des points en gratuité de stationnement).
* Des outils d'analyse et de synthèse pour l'association des commerçants et la Mairie (dans le respect strict du RGPD).
* Une ergonomie inclusive pensée pour tous les usagers (persona senior Pierre 74 ans, conformité RGAA).

---

## 2. Démarrage Rapide pour l'Équipe

L'ensemble de la configuration du projet, des directives de l'agent et des 40 compétences d'ingénierie logicielle est versionné sur ce dépôt.

### Étape 1 : Cloner le dépôt
```bash
git clone git@github.com:K-Boo/Projet-GLOP.git
cd Projet-GLOP
```

### Étape 2 : Ouvrir dans Antigravity
Ouvrez ce dossier dans votre IDE Antigravity. L'agent charge automatiquement les règles du projet et la boîte à outils.

### Étape 3 : Installer Google Drive pour ordinateur
Installez l'application officielle **Google Drive pour ordinateur** et connectez votre compte pour accéder au dossier partagé `Projet-GLOP`.

### Étape 4 : Laisser l'agent s'occuper du reste
Dans la discussion avec votre agent Antigravity, demandez-lui simplement :
> *« Aligne mon environnement sur la configuration d'équipe »*

L'agent lira automatiquement les directives d'équipe (`.antigravity/setup_equipe.md`), installera les dépendances nécessaires et configurera la liaison avec votre Google Drive de manière autonome.

---

## 3. Organisation du Dépôt : Deux Pôles Dédiés

Pour séparer nettement la phase de cadrage et de livrables de la phase d'implémentation logicielle, le projet est scindé en deux espaces :
* **`agent_projet/`** : Réservé à l'**Agent Projet & Livrables** (cadrage R1, étude financière R3, registres agiles `docs/`, logos `images/`, génération PDF et synchronisation Google Drive).
* **`agent_code/`** : Réservé à l'**Agent Ingénieur Logiciel & Code** (architecture backend/frontend `src/`, configurations `docker/` et tests).

---

## 4. Surveillance des Quotas, Routage LLM & Green FinOps

Pour suivre en direct la consommation de jetons de chaque requete, auditer le routage de modeles LLM et mesurer l'impact ecologique (energie et eau), un moniteur en ligne de commande sobre et 100% local est integre :

* **Sous Windows** : Double-cliquez directement sur `agent_projet/scripts/watch_tokens.bat`.
* **En ligne de commande** :
  ```bash
  # Mode tableau de bord en direct (actualise a chaque reponse de l'agent)
  python agent_projet/scripts/token_tracker.py --watch

  # Mode flux continu (journal defilant sans effacement d'ecran)
  python agent_projet/scripts/token_tracker.py --stream

  # Mode ponctuel (affichage instantane)
  python agent_projet/scripts/token_tracker.py
  ```

### Metriques Affichees :
* **Quotas Globaux** : Suivi du quota journalier (24h) et hebdomadaire (7 jours) avec jauges d'utilisation.
* **Derniere Requete** : Horodatage, prompt nettoye, modele LLM sollicite (Orchestrateur Flash, Sous-Agents Pro ou Flash Lite).
* **Jetons Consommes** : Jetons d'entree (In), de sortie (Out) et total unitaire.
* **Green AI / Impact Ecologique** : Estimation de la consommation d'energie electrique (Wh avec equivalence ampoule LED) et de l'empreinte eau (mL avec equivalence en gorgees d'eau).
* **Historique Recent** : Tableau recapitulatif des requetes precedentes.
