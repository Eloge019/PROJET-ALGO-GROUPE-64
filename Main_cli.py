main_cli.py

from directory_scanner import scanner_dossier, restaurer_fichiers, rechercher_fichier
from file_organizer import organiser_fichiers, creer_archives_zip
from logger import initialiser_journal, exporter_journal_csv
from stats_reporter import generer_statistiques, afficher_arborescence, exporter_csv

import os

def afficher_resultats_complets(fichiers_trouves, journal, dossiers_crees):
    total = len(journal['deplacements'])
   
    extensions = set(entree['extension'] for entree in journal['deplacements'])
   
    par_extension = {}
   
    for ext in extensions:
        par_extension[ext] = sum(1 for e in journal['deplacements'] if e['extension'] == ext)

    print("\n=== Résultats du classement de fichiers ===\n")
    # Liste complète des fichiers trouvés
    print("Liste complète des fichiers trouvés :")
    for f in fichiers_trouves:
        print(f" - {f}")
    print()
    # Nombre total de fichiers traités
    print(f"Nombre total de fichiers traités :{total}\n")
    # Liste des extensions détectées
    print("Extensions détectées :")
    print(". ".join(ext.upper() if ext else "SANS EXTENSION" for ext in extensions))
    print()
    # Nombre de fichiers par type
    print("Nombre de fichiers par type :")
    for ext, nb in par_extension.items():
        nom_ext = ext.upper() if ext else "SANS EXTENSION"
        print(f" - {nom_ext} : {nb}")
    print()
    # Arborescence des dossiers créés
    print("Arborescence des dossiers créés :")
    for d in sorted(dossiers_crees):
        print(f" - {d}/")
    print()
    # Chemin d'origine et de destination de chaque fichier déplacé
    print("Chemins d'origine et de destination :")
    for entree in journal['deplacements']:
        print(f" - {entree['nom']} :")
        print(f"  Origine   : {entree['source']}")
        print(f"  Destination : {entree['destination']}")
    print()
    # Statistiques globales en pourcentage
    print("Statistiques globales :")
    for ext, nb in par_extension.items():
        pourcentage = (nb / total) * 100 if total > 0 else 0
        nom_ext = ext.upper() if ext else "SANS EXTENSION"
        print(f" - {pourcentage:.1f}% des fichiers sont des {nom_ext}")
    print()
    # Liste des fichiers ignorés
    if journal['ignores']:
        print("Fichiers ignorés :")
        for f in journal['ignores']:
            print(f" - {f}")
    else:
        print("Aucun fichier ignoré.")
    print()
    if journal['renommes']:
        print("Fichiers renommés :")
        for ancien, nouveau in journal['renommes']:
            print(f" - {ancien} -> {nouveau}")
    else:
        print("Aucun fichier renommé.")
    print()

def main():
    chemin = input("Entrez le chemin du dossier à classer : ").strip()
    if not os.path.isdir(chemin):
        print("Chemin invalide.")
        return

    fichiers = scanner_dossier(chemin)
    journal = initialiser_journal()
    dossiers_crees = organiser_fichiers(chemin, fichiers, journal)
    afficher_resultats_complets(fichiers, journal, dossiers_crees)
    exporter_journal_csv(journal)
    stats = generer_statistiques(journal)
    exporter_csv(stats)
    creer_archives_zip(chemin, dossiers_crees)
    print("\n\033[92mArchives ZIP créées pour chaque type de fichier.\033[0m")
   
    if input("\nSouhaitez-vous effectuer une recherche de fichier ? (o/n) ").lower() == 'o':
        nom_recherche = input("Entrez le nom ou une partie du nom du fichier : ")
        resultats = rechercher_fichier(chemin, nom_recherche)
        if resultats:
            print("\nRésultats de recherche :")
            for r in resultats:
                print(f" - {r}")
        else:
            print("Aucun fichier correspondant trouvé.")
   
    if input("\nSouhaitez-vous réinitialiser et remettre les fichiers dans le dossier principal ? (o/n) ").lower() == 'o':
        restaurer_fichiers(chemin, journal)
        print("\n\033[92mLes fichiers ont été restaurés dans leur emplacement d'origine.\033[0m")


