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

## 3. Architecture Bi-Depots : Cockpit Projet & Code Evalue

Pour garantir une etancheite totale entre les livrables d'ingenierie/gouvernance et le code source remis aux professeurs, l'infrastructure est scindee en deux depots distincts :

1. **Depot Principal (GitHub `Projet-GLOP`) — Ce Depot** :
   * Espace de gouvernance d'equipe, cadrage metier R1, etude financiere R3, dossiers d'architecture R4/R5, diaporamas PPTX et synchronisation Google Drive.
   * Cockpit interne d'orchestration agentique et suivi Green FinOps.

2. **Depot Applicatif (GitLab Univ-Lille `projet-glop-app`) — Remis aux Evaluateurs** :
   * Depot officiel public consulte et evalue par les professeurs : `git@gitlab-ssh.univ-lille.fr:khalil.bouchama.etu/projet-glop-app.git`.
   * Reserve exclusivement au code source applicatif, aux tests unitaires TDD, a la conteneurisation Docker et a la CI/CD.
   * **Zero trace agentique** : aucun fichier d'instruction d'agent, aucun script FinOps ni mention d'IA ne figure sur ce depot. Tous les commits y sont signes au format conventionnel avec l'identite etudiante officielle.
   * Le depot reste vide jusqu'a la validation du cadrage (R1) et de la stack technique.

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
