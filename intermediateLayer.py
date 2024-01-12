#fichier gérant les interactions entre l'interface et les fichiers fonctionnels
import fileOpening as fileop

def newPrjctRequest(name : str): 
    """newPrjctRequest 
    fonction de transition entre le programme de l'interface et le programme de gestions des fichiers

    Parameters
    ----------
    name : str
        nom du dossier à créer
    """
    fileop.directoryCreation(name)