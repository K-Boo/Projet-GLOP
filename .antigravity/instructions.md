# DIRECTIVES GÉNÉRALES & ORCHESTRATION DU WORKSPACE (.antigravity/instructions.md)

Ce fichier est le point d'entrée principal pour tout agent Antigravity opérant sur ce workspace.
Il définit l'orchestration entre les deux domaines spécialisés du projet : **Gestion de Projet & Livrables** et **Ingénierie Logicielle & Code**.

---

## 1. Organisation Bimodale du Workspace

Le projet est strictement partitionné en deux sous-espaces de travail complémentaires :

```text
ShopLoc/
├── agent_projet/                  # [PÔLE PROJET & LIVRABLES]
│   ├── AGENTS.md                  # Règles locales pour les livrables
│   ├── docs/                      # Cadrage R1, glossaire, reporting temps, ADRs
│   ├── images/                    # Logos officiels Université de Lille & Faculté
│   └── scripts/                   # Compilation PDF (generate_pdf.py) & Drive sync
│
├── agent_code/                    # [PÔLE INGÉNIERIE & CODE]
│   ├── AGENTS.md                  # Règles locales pour le développement
│   ├── src/backend/               # Services API, logique métier, modèles BDD
│   ├── src/frontend/              # Interfaces web/mobiles accessibles RGAA
│   ├── docker/                    # Dockerfile, docker-compose, configs infra
│   └── tests/                     # Tests d'intégration et mocks
│
├── .antigravity/
│   ├── instructions.md            # Ce fichier (routeur d'orchestration)
│   ├── agent_projet.md            # Directives détaillées de l'Agent Projet
│   ├── agent_code.md              # Directives détaillées de l'Agent Code
│   └── setup_equipe.md            # Directive d'alignement d'environnement équipe
│
└── .agents/skills/                # 40 compétences d'ingénierie logicielle
```

---

## 2. Aiguillage des Requêtes Utilisateur

Dès réception d'une instruction utilisateur, l'agent identifie le domaine concerné et applique la directive appropriée :

### Cas A : Demande liée au Projet, aux Livrables ou à la Gouvernance
- **Exemples** : Rédaction ou modification de livrables (R1, R3, R4/R5), cadrage métier, questionnaires MOA, étude financière, reporting de temps, mise à jour du glossaire, diaporamas PPTX, vidéos de démonstration, synchronisation Google Drive.
- **Règle à appliquer** : Se conformer impérativement à [`.antigravity/agent_projet.md`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/.antigravity/agent_projet.md) et aux règles locales [`agent_projet/AGENTS.md`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/agent_projet/AGENTS.md).
- **Emplacement des fichiers** : Opérer exclusivement dans `agent_projet/`.

### Cas B : Demande liée au Code, à l'Architecture ou aux Tests
- **Exemples** : Écriture de code Java/TypeScript, création d'APIs REST, modélisation SQL PostgreSQL, cycle TDD, composants React accessibles RGAA, conteneurs Docker, tests de charge, Green IT.
- **Règle à appliquer** : Se conformer impérativement à [`.antigravity/agent_code.md`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/.antigravity/agent_code.md) et aux règles locales [`agent_code/AGENTS.md`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/agent_code/AGENTS.md).
- **Emplacement des fichiers** : Opérer exclusivement dans `agent_code/`.

---

## 3. Autonomie Opérationnelle & Gestion des Permissions

1. **Haute Autonomie sur l'Exploration, la Lecture et les Tests** :
   - L'agent exécute **en totale autonomie et sans solliciter de permission** toutes les opérations de diagnostic, lecture de fichiers, recherches grep, compilation de tests ou vérifications d'état.
2. **Arrêt et Demande de Validation (Stop & Wait) STRICTEMENT Réservés aux Actes Majeurs** :
   - L'agent **ne doit solliciter la validation explicite de l'utilisateur QUE dans les 3 cas suivants** :
     1. **Modification ou suppression** de code source ou de données existantes du projet.
     2. **Génération ou modification d'un livrable officiel** (cahier des charges R1, étude financière R3, dossiers techniques R4/R5, diaporama de soutenance).
     3. **Arbitrage structurant** (choix technologique majeur, validation d'hypothèse métier auprès de la MOA, arbitrage d'architecture).

---

## 4. Économie de Quota & Hygiène de Conversation

1. **Principe 1 Session = 1 Tâche Atomique** :
   - Clôturer le chat dès qu'une tâche est achevée et ouvrir une nouvelle session pour la suivante.
   - La mémoire pérenne du projet réside dans les fichiers Markdown de `agent_projet/docs/` et `agent_code/`.
2. **Méthode Avant Code (Planning Mode)** :
   - Toujours formaliser le plan (schémas, signatures d'API, entités) avant d'écrire du code de grande envergure.

---

## 5. Synchronisation Google Drive Automatique

- Tout livrable officiel produit dans `agent_projet/` doit être synchronisé dans le dossier Google Drive partagé de l'équipe (`G:\Mon Drive\Projet-GLOP` ou chemin configuré) en appelant :
  ```bash
  python agent_projet/scripts/drive_sync.py <fichier>
  ```
- Les sous-dossiers cibles sont :
  - `01_Cadrage_Metier_R1/`
  - `02_Etude_Financiere_R3/`
  - `03_Architecture_Technique_R4_R5/`
  - `04_Presentations_Diaporamas/`
  - `05_Demonstrations_Videos/`

---

## 6. Alignement Automatique de l'Environnement Équipe

Tout agent Antigravity opérant sur ce projet doit appliquer le protocole d'alignement défini dans [`.antigravity/setup_equipe.md`](file:///c:/Users/hpome/Documents/M2_MIAGE/GLOP/ShopLoc/.antigravity/setup_equipe.md). Dès qu'un membre de l'équipe demande de vérifier, aligner ou synchroniser sa configuration, l'agent exécute automatiquement :
```bash
python agent_projet/scripts/setup_env.py
```
