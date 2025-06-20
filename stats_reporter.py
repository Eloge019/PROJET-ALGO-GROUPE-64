import csv
from collections import defaultdict

def generer_statistiques(journal):
    stats = {
        'total': len(journal['deplacements']),
        'extensions': set(),
        'par_extension': defaultdict(int)
    }
    for entree in journal['deplacements']:
        ext = entree['extension']
        stats['extensions'].add(ext)
        stats['par_extension'][ext] += 1
    return stats

def afficher_arborescence(dossiers):
    for d in sorted(dossiers):
        print(f"  - {d}/")

def exporter_csv(statistiques, nom_fichier="statistiques.csv"):
    with open(nom_fichier, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Extension", "Nombre de fichiers"])
        for ext, nb in statistiques['par_extension'].items():
            writer.writerow([ext, nb])
