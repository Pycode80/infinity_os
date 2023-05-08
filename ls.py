import os
import platform




def ls():
    contenu_repertoire = os.listdir()
    if platform.system() == "Windows":
        separateur = "\\"
    else:
        separateur = "/"
    for element in contenu_repertoire:
        if os.path.isdir(element):
            print(f"[{element}]")
        else:
            print(element)