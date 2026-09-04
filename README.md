# Projet ShopLoc — Marketplace & Fidélisation de Centre-Ville
> **Master 2 MIAGE — UE Génie Logiciel par la Pratique (GLOP) 2026-2027**  
> Université de Lille — Faculté des Sciences et Technologies (FST)

---

## 👥 Présentation du Projet

ShopLoc est une plateforme SaaS territoriale permettant de dynamiser le commerce de centre-ville face aux grandes zones commerciales périphériques. Elle réunit :
* Une **Marketplace Click & Collect multi-commerces** avec panier unifié.
* Un **programme de fidélité inter-commerces** avec compensation financière.
* L'interconnexion avec les **services municipaux de stationnement** (conversion de points en heures de parking gratuit).
* Des outils marketing et de reporting pour l'association des commerçants et la Mairie (respect strict du RGPD).
* Une ergonomie inclusive pensée pour tous les âges (persona Pierre 74 ans, normes RGAA).

---

## 🚀 Démarrage Rapide pour l'Équipe (Antigravity)

Ce dépôt contient l'ensemble de la **configuration partagée de l'agent Antigravity**, de la documentation de cadrage et des outils de compilation.

### 1. Cloner le dépôt
```bash
git clone git@github.com:K-Boo/Projet-GLOP.git
cd Projet-GLOP
```

### 2. Ouvrir dans Antigravity
Ouvrez simplement le dossier `Projet-GLOP` dans votre IDE Antigravity :
* L'agent détecte automatiquement les règles d'équipe dans `.antigravity/instructions.md` (rôles, personas, politique d'autonomie, nomenclature `[GLOP]`).
* L'agent charge automatiquement la bibliothèque de **40 skills** d'ingénierie logicielle située dans `.agents/skills/`.

### 3. Synchronisation Google Drive
Installez l'application **Google Drive pour ordinateur** et connectez votre compte Google partagé :
* Le dossier `Projet-GLOP` sur votre Google Drive sera automatiquement alimenté dès que des livrables (PDF, slides, vidéos) sont générés.
* Si votre lecteur Drive n'est pas sur `G:\`, vous pouvez définir la variable d'environnement :  
  `GLOP_DRIVE_DIR="<chemin_vers_votre_dossier_drive>"`

---

## 📁 Arborescence du Projet

```
Projet-GLOP/
├── .antigravity/                     # Directives d'équipe pour l'agent Antigravity
│   └── instructions.md               # Cadre GLOP, personas, rôles, sync Drive
├── .agents/                          # Customisations Antigravity découvertes automatiquement
│   └── skills/                       # 40 compétences techniques (RGAA, C4, Docker, BDD, etc.)
├── docs/                             # Documentation vivante et spécifications de cadrage
│   ├── assets/                       # Logos officiels (Université de Lille, FST Informatique)
│   ├── GLOSSAIRE.md                  # Glossaire métier vivant
│   ├── REPORTING_TEMPS.md            # Journal de suivi des heures par membre et par sprint
│   ├── DECISIONS.md                  # Registre des décisions d'architecture (ADRs)
│   ├── MODELE_DOCUMENT_LIVRABLE.md   # Modèle de mise en page documentaire
│   ├── QUESTIONNAIRE_METIER_DETAILLE.md # Questionnaire de cadrage (36 questions)
│   └── ShopLoc_Cadrage_Metier_Livrable_R1.pdf # Livrable R1 officiel A4
├── scripts/                          # Outils d'automatisation
│   ├── generate_pdf.py               # Générateur de PDF officiel au style LaTeX
│   └── drive_sync.py                 # Module de synchronisation automatique Google Drive
├── src/                              # Code source applicatif (réservé pour la phase de réalisation)
│   ├── backend/                      # API, services, base de données
│   └── frontend/                     # Applications Web & Mobile
├── .gitignore                        # Caches, fichiers temporaires et configs locales
└── README.md                         # Le présent guide d'accueil
```

---

## 🛠️ Commandes Utiles

* **Générer le PDF du questionnaire et synchroniser sur Drive** :
  ```bash
  python scripts/generate_pdf.py
  ```
* **Synchroniser manuellement un fichier sur Google Drive** :
  ```bash
  python scripts/drive_sync.py docs/mon_livrable.pdf
  ```

---

## 📋 Règles de Travail en Groupe (UE GLOP)

* **Gouvernance Agile** : Responsabilité de Scrum Master tournante à chaque sprint.
* **Tag de communication obligatoire** : Tout échange d'email officiel avec la MOA doit comporter le tag `[GLOP]` dans son objet.
* **Mise à jour continue des registres** : Reporter systématiquement ses heures dans `docs/REPORTING_TEMPS.md` et documenter les nouveaux termes dans `docs/GLOSSAIRE.md`.
