# 🗂️ Classificateur de Fichiers par Extension

## 📌 Description du Projet

Ce projet Python a pour but de **trier automatiquement les fichiers** d’un dossier selon leur extension (ex : `.pdf`, `.jpg`, `.txt`, etc.). Il facilite l’organisation des fichiers en les plaçant dans des sous-dossiers dédiés (Images, Documents, Archives, etc.) tout en :
- nettoyant les noms,
- gérant les doublons,
- générant des **statistiques complètes**,
- et en proposant des **fonctionnalités bonus** comme la **réinitialisation** ou la création de **fichiers ZIP**.

---

## 👥 Membres du Projet

| Nom                | Rôle                                      |
|--------------------|-------------------------------------------|
| Étudiant 2         | Interface CLI & Orchestration générale     |
| Étudiant 2         | Exploration de dossier & extraction       |
| Étudiant 3         | Déplacement & gestion des conflits         |
| Étudiant 4         | Journalisation & statistiques              |
| Étudiant 5         | ZIP, export CSV, et recherche de fichiers |

---

## 🗃️ Structure du Projet

```
file_sorter/
├── main_cli.py
├── directory_scanner.py
├── file_organizer.py
├── logger.py
├── stats_reporter.py
├── logs/
│   └── operations.csv
├── sorted/
│   └── ... (fichiers triés par type)
├── README.md
```

---

## ⚙️ Fonctionnalités Principales

- Lecture de tous les fichiers dans un dossier donné
- Identification des extensions
- Déplacement des fichiers dans des sous-dossiers :
  - `TXT/`, `PDF/`, `JPG/`, etc.
  - `SANS_EXTENSION/` pour les fichiers sans extension
- Nettoyage des noms de fichiers (caractères spéciaux supprimés)
- Gestion des conflits de nom (`nom(1).txt`)
- Journalisation détaillée (`operations.csv`)
- Affichage de statistiques :
  - Noms et chemins des fichiers déplacés
  - Nombre de fichiers par type
  - Pourcentage de fichiers par catégorie
  - Fichiers renommés ou ignorés
- BONUS :
  - Création de fichiers `.zip` par type (ex: `images.zip`)
  - Réinitialisation (remettre tous les fichiers à leur place d’origine)
  - Recherche dans les fichiers classés

---

## 🔧 Installation

### 1. Prérequis

- Python 3.8+
- Aucun module externe requis (utilise `os`, `shutil`, `csv`, `zipfile`)

### 2. Clonage du projet

```bash
git clone https://github.com/votre-utilisateur/file_sorter.git
cd file_sorter
```

---

## 🚀 Lancement

```bash
python main_cli.py
```

Suivez les instructions à l’écran pour :
- Entrer le dossier à classer,
- Choisir les options avancées,
- Lire les statistiques et les logs.

---

## 🧪 Exemples de Résultat CLI

```
✅ 52 fichiers trouvés dans /home/user/Documents
📦 12 fichiers déplacés vers PDF/
🖼️ 10 fichiers déplacés vers JPG/
📄 18 fichiers déplacés vers TXT/
📁 3 fichiers sans extension déplacés vers SANS_EXTENSION/

📊 Statistiques :
- 52 fichiers traités
- 4 types d’extension détectés
- 🔁 2 fichiers renommés
- 📂 Arborescence créée : PDF/, JPG/, TXT/, SANS_EXTENSION/
- 📌 34% des fichiers sont des documents (.txt)
```

---

## 📤 Exports

- `operations.csv` : journal de toutes les opérations
- `*.zip` : archives générées par type de fichier (bonus)

---

## 🔁 Fonctionnalités Bonus

- **Réinitialisation** : remet tous les fichiers dans le dossier d’origine
- **Recherche** : permet de rechercher un fichier par nom dans tous les sous-dossiers
- **Export CSV** : statistiques exportables en tableur

---


Projet académique - Université Don Bosco Lubumbashi

