
import os
import shutil

# Dictionnaire contenant les types de fichiers et leurs extensions associées
EXTENSIONS_SPECIALES = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'documents': ['.txt', '.doc', '.docx', '.odt'],
    'pdf': ['.pdf'],
    'tableurs': ['.xls', '.xlsx', '.ods'],
    'archives': ['.zip', '.rar', '.tar', '.gz'],
}

def scanner_dossier(chemin):
    """
    Scanne le dossier spécifié et retourne la liste des fichiers qu'il contient.
    
    Args:
        chemin (str): Chemin du dossier à scanner.
        
    Returns:
        list: Liste des noms de fichiers présents dans le dossier (hors fichiers cachés).
    """
    fichiers = []
    for item in os.listdir(chemin):
        chemin_complet = os.path.join(chemin, item)
        # On vérifie si c'est un fichier (pas un dossier) et s'il n'est pas caché
        if os.path.isfile(chemin_complet) and not item.startswith('.'):
            fichiers.append(item)
    return fichiers

def restaurer_fichiers(chemin, journal):
    """
    Restaure les fichiers déplacés à leurs emplacements d'origine en utilisant un journal.
    
    Args:
        chemin (str): Chemin du dossier de base.
        journal (dict): Journal contenant l'historique des déplacements avec la clé 'deplacements'.
    """
    for entree in journal['deplacements']:
        chemin_actuel = entree['destination']  # Emplacement actuel du fichier déplacé
        chemin_initial = os.path.join(chemin, entree['nom'])  # Emplacement d'origine
        try:
            shutil.move(chemin_actuel, chemin_initial)  # Déplacement du fichier vers son emplacement d'origine
        except Exception as e:
            print(f"Erreur lors de la restauration de {chemin_actuel} : {e}")

def rechercher_fichier(chemin, nom_partiel):
    """
    Recherche récursivement des fichiers contenant une partie spécifique de leur nom.
    
    Args:
        chemin (str): Dossier de base où effectuer la recherche.
        nom_partiel (str): Chaîne partielle à rechercher dans les noms de fichiers.
        
    Returns:
        list: Liste des chemins complets des fichiers correspondant à la recherche.
    """
    resultats = []
    for dossier, sous_dossiers, fichiers in os.walk(chemin):
        for f in fichiers:
            # Si le nom partiel est contenu dans le nom du fichier (insensible à la casse)
            if nom_partiel.lower() in f.lower():
                resultats.append(os.path.join(dossier, f))
    return resultats
