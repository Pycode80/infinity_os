import os
import platform

# Utilisez la fonction listdir() de os pour obtenir la liste des fichiers et dossiers du répertoire courant
contenu_repertoire = os.listdir()

# Utilisez la variable platform.system() pour déterminer si l'utilisateur est sous Windows ou Linux
if platform.system() == "Windows":
    separateur = "\\"
else:
    separateur = "/"

# Parcourez la liste des fichiers et dossiers du répertoire courant et affichez-les
for element in contenu_repertoire:
    if os.path.isdir(element):
        # Si l'élément est un dossier, affichez le nom du dossier entre crochets
        print(f"[{element}]")
    else:
        # Si l'élément est un fichier, affichez le nom du fichier
        print(element)
