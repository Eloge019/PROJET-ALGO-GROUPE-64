import os
import zipfile
import csv
from collections import defaultdict
from pathlib import Path

def generate_statistics(directory: str, log_file: str):
    """
    Analyse les fichiers dans le répertoire donné, génère des statistiques et crée des archives ZIP par type de fichier.
    """
    # Initialisation des structures de données
    file_types = defaultdict(int)
    file_details = []
    zip_files = defaultdict(list)

    # Lecture du fichier journal
    with open(log_file, 'r') as log:
        for line in log:
            if line.startswith("Déplacement:"):
                parts = line.split(" ")
                file_name = parts[1]
                file_extension = file_name.split('.')[-1] if '.' in file_name else 'SANS_EXTENSION'
                file_types[file_extension] += 1
                file_details.append((file_name, file_extension))
                zip_files[file_extension].append(file_name)

    # Génération des statistiques
    total_files = sum(file_types.values())
    file_type_percentages = {ext: (count / total_files) * 100 for ext, count in file_types.items()}

    # Création des archives ZIP par type de fichier
    for ext, files in zip_files.items():
        zip_filename = f"{ext}.zip"
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for file in files:
                zipf.write(file, os.path.basename(file))

    # Export des statistiques au format CSV
    with open('file_statistics.csv', 'w', newline='') as csvfile:
        fieldnames = ['Extension', 'Nombre de fichiers', 'Pourcentage']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for ext, count in file_types.items():
            writer.writerow({'Extension': ext, 'Nombre de fichiers': count, 'Pourcentage': file_type_percentages.get(ext, 0)})

    # Affichage des statistiques
    print(f"Total de fichiers traités : {total_files}")
    for ext, count in file_types.items():
        print(f"{ext}: {count} fichiers ({file_type_percentages.get(ext, 0):.2f}%)")

    return file_details, file_type_percentages