
import csv

def initialiser_journal():
    return {
        'deplacements': [],
        'renommes': [],
        'ignores': []
    }

def exporter_journal_csv(journal, nom_fichier="journal_operations.csv"):
    with open(nom_fichier, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # Écrire la liste des fichiers déplacés
        writer.writerow(["Fichiers déplacés"])
        writer.writerow(["Nom", "Extension", "Chemin origine", "Chemin destination"])
        for entree in journal['deplacements']:
            writer.writerow([
                entree['nom'],
                entree['extension'],
                entree['source'],
                entree['destination']
            ])

        writer.writerow([])  # Ligne vide

        # Écrire la liste des fichiers renommés
        writer.writerow(["Fichiers renommés"])
        writer.writerow(["Ancien nom", "Nouveau nom"])
        if journal['renommes']:
            for ancien, nouveau in journal['renommes']:
                writer.writerow([ancien, nouveau])
        else:
            writer.writerow(["Aucun fichier renommé"])

        writer.writerow([])  # Ligne vide

        # Écrire la liste des fichiers ignorés
        writer.writerow(["Fichiers ignorés"])
        if journal['ignores']:
            for fichier in journal['ignores']:
                writer.writerow([fichier])
        else:
            writer.writerow(["Aucun fichier ignoré"])
