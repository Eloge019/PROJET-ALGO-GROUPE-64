import os
import shutil
import re
import zipfile


def nettoyer_nom_fichier(nom):
    nom_sans_espace = nom.strip().replace(' ', '_')
    return re.sub(r'[^a-zA-Z0-9_.()-]', '', nom_sans_espace)

def generer_nom_unique(chemin_dossier, nom_fichier):
    base, ext = os.path.splitext(nom_fichier)
    compteur = 1
    nouveau_nom = nom_fichier
    while os.path.exists(os.path.join(chemin_dossier, nouveau_nom)):
        nouveau_nom = f"{base}({compteur}){ext}"
        compteur += 1
    return nouveau_nom

def organiser_fichiers(chemin, fichiers, journal):
    arbre = set()
    for fichier in fichiers:
        chemin_complet = os.path.join(chemin, fichier)
        nom_nettoye = nettoyer_nom_fichier(fichier)
        ext = os.path.splitext(fichier)[1].lower()
        dossier_cible = ext[1:].upper() if ext else 'SANS_EXTENSION'

        chemin_destination = os.path.join(chemin, dossier_cible)
        if not os.path.exists(chemin_destination):
            os.makedirs(chemin_destination)
        arbre.add(dossier_cible)

        nom_final = generer_nom_unique(chemin_destination, nom_nettoye)
        chemin_final = os.path.join(chemin_destination, nom_final)

        try:
            shutil.move(chemin_complet, chemin_final)
            journal['deplacements'].append({
                'nom': nom_nettoye,
                'extension': ext[1:] if ext else '',
                'source': chemin_complet,
                'destination': chemin_final
            })
            if nom_nettoye != nom_final:
                journal['renommes'].append((nom_nettoye, nom_final))
        except Exception as e:
            journal['ignores'].append(fichier)

    return arbre

def creer_archives_zip(chemin, dossiers):
    for dossier in dossiers:
        dossier_complet = os.path.join(chemin, dossier)
        if os.path.isdir(dossier_complet):
            zip_path = os.path.join(chemin, f"{dossier.lower()}.zip")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(dossier_complet):
                    for file in files:
                        full_path = os.path.join(root, file)
                        arcname = os.path.relpath(full_path, start=dossier_complet)
                        zipf.write(full_path, arcname)
