# DIRECTIVE D'ALIGNEMENT DE L'ENVIRONNEMENT D'ÉQUIPE (.antigravity/setup_equipe.md)

Cette instruction s'adresse à tout agent Antigravity opérant sur la machine d'un membre de l'équipe (Master 2 MIAGE - UE GLOP).
Elle décrit l'état de référence du projet et la procédure d'auto-configuration à exécuter pour que la machine locale soit 100% conforme à l'environnement de référence de l'équipe.

---

## 1. Contexte & Environnement de Référence

L'environnement de référence du projet (initialisé par Khalil) repose sur :
1. **Dépôt Git distant** : `git@github.com:K-Boo/Projet-GLOP.git` (branche principale : `main`).
2. **Bibliothèque de 40 compétences Antigravity** : Située dans `.agents/skills/` à la racine (détectée automatiquement par Antigravity).
3. **Synchronisation Google Drive** : Application officielle *Google Drive pour ordinateur* installée, connectée au compte partagé d'équipe.
   - Dossier racine du projet sur Drive : `Projet-GLOP`.
   - Sur la machine de référence, ce dossier est monté sous : `G:\Mon Drive\Projet-GLOP`.
   - Il contient les 5 sous-dossiers de livrables :
     - `01_Cadrage_Metier_R1/`
     - `02_Etude_Financiere_R3/`
     - `03_Architecture_Technique_R4_R5/`
     - `04_Presentations_Diaporamas/`
     - `05_Demonstrations_Videos/`
4. **Moteur d'outillage & PDF** :
   - Python 3.10+ avec les bibliothèques : `pymupdf`, `reportlab`, `pypdf`, `pillow`.
   - Moteur Chromium / Edge headless pour le rendu PDF vectoriel A4.

---

## 2. Procédure d'Auto-Configuration par l'Agent

Dès qu'un collègue demande à son agent de vérifier son poste ou de se configurer, l'agent doit exécuter les étapes suivantes de manière totalement autonome :

### Étape 1 : Exécuter le script d'alignement
L'agent doit lancer la commande :
```bash
python scripts/setup_env.py
```
Ce script réalise automatiquement :
- La détection et l'installation des dépendances Python manquantes (`pymupdf`, `reportlab`, `pypdf`, `pillow`).
- La vérification du moteur headless Chromium/Edge.
- La détection de Google Drive pour ordinateur et la création automatique des 5 sous-dossiers de livrables si nécessaires.
- La création du fichier de configuration local `config.local.json` si le Drive est monté sur une autre lettre que `G:\`.
- Le contrôle du remote Git `origin`.

### Étape 2 : Cas particuliers Google Drive
Si `scripts/setup_env.py` indique que Google Drive n'est pas détecté :
1. L'agent doit inviter l'utilisateur à installer l'application officielle **Google Drive pour ordinateur** et à synchroniser le dossier partagé `Projet-GLOP`.
2. Si le collègue a son Google Drive sur un chemin personnalisé (ex : `D:\Google Drive\Projet-GLOP` ou sous macOS/Linux `~/Google Drive/Projet-GLOP`), l'agent doit créer ou mettre à jour le fichier `config.local.json` à la racine du projet :
   ```json
   {
     "drive_path": "<chemin_absolu_vers_Projet-GLOP>"
   }
   ```
   *(Ce fichier est ignoré par Git via le `.gitignore` et reste propre à chaque poste).*

### Étape 3 : Production et Synchronisation des Livrables
L'agent ne doit **JAMAIS** demander à l'utilisateur de synchroniser manuellement ses fichiers :
- Dès qu'un livrable officiel est généré (ex: `python scripts/generate_pdf.py`), le script appelle automatiquement `scripts/drive_sync.py` qui pousse le fichier dans le dossier Google Drive de l'équipe.
- Si l'agent produit un autre livrable (diaporama `.pptx`, vidéo `.mp4`, tableur `.xlsx`), l'agent doit lui-même exécuter :
  ```bash
  python scripts/drive_sync.py <chemin_du_fichier>
  ```

---

## 3. Règle d'Action de l'Agent

Si un collègue dit à son agent Antigravity :
*« Configure mon environnement »*, *« Synchronise ma machine »*, ou *« Est-ce que mon setup est identique à l'équipe ? »*,
l'agent doit immédiatement lire ce fichier, exécuter `python scripts/setup_env.py`, appliquer les ajustements nécessaires et lui confirmer le résultat sans lui demander d'étapes manuelles complexes.
