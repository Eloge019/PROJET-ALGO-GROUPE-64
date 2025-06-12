import os

# ==========================
# MODULE 1 – EXPLORATION DE DOSSIER
# ==========================

def get_directory_path():
    """
    Demande à l'utilisateur de saisir un chemin de dossier.
    Vérifie si le dossier existe.
    """
    path = input("📁 Entrez le chemin du dossier à classer : ").strip()
    if not os.path.isdir(path):
        raise ValueError("❌ Chemin invalide ou dossier introuvable.")
    return os.path.abspath(path)


def list_files(path):
    """
    Liste tous les fichiers à la racine du dossier donné (ignore les sous-dossiers).
    """
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


def get_extension(file_name):
    """
    Retourne l'extension du fichier en majuscules (sans le point).
    Si le fichier n’a pas d’extension, retourne None.
    """
    if '.' not in file_name or file_name.startswith('.'):
        return None
    return file_name.split('.')[-1].upper()


def should_ignore(file_name):
    """
    Retourne True si le fichier doit être ignoré (ex : fichiers cachés commençant par un point).
    """
    return file_name.startswith('.')


# ==========================
# APPEL DE TEST – EXÉCUTION LOCALE
# ==========================

if __name__ == "__main__":
    try:
        # Demander le chemin du dossier à classer
        chemin = get_directory_path()

        # Lister les fichiers dans le dossier
        fichiers = list_files(chemin)

        if not fichiers:
            print("ℹ️ Aucun fichier trouvé dans ce dossier.")
        else:
            print("\n📂 Fichiers détectés :")
            for fichier in fichiers:
                extension = get_extension(fichier)
                ignore = should_ignore(fichier)
                print(f"- {fichier} | Extension : {extension if extension else 'Aucune'} | Ignoré ? {'Oui' if ignore else 'Non'}")

            print(f"\n✅ Total : {len(fichiers)} fichier(s) analysé(s).")

    except Exception as e:
        print(f"\n❌ Erreur : {e}")

