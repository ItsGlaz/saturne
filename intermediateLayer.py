#fichier gérant les interactions entre l'interface et les fichiers fonctionnels
import fileOpening as fileop
import fileManagemt as flmngt
import json 
from typing import *

def newPrjctRqst(name : str): 
    """newPrjctRequest 
    fonction de transition entre le programme de l'interface et le programme de gestions des fichiers

    Parameters
    ----------
    name : str
        nom du dossier à créer
    """
    fileop.dirCreation(name)


def rmproject(name : str):
    fileop.rmDirectory(name)


def modidyPrjctRqst(name : str, dico : dict):
    flmngt.modifyPrjtInfo(name, dico)
    

# def ctrlMod(
#         info : Union[dict, str, int, list], 
#         validtype : str = 'int'
#         ):

#     match validtype :
        
#         case 'int' :
#             try :
#                 info = int(info)
#                 return info
#             except :
#                 return False


def getPrjtSetRqst(name : str) -> dict:
    path = fileop.createPath(name)
    print(path)
    return fileop.loadInfo(path = path)


def getWidSetsRqst(widget) -> dict:
    return fileop.loadInfo(data = "widsets", widget = widget)

def getSetsInfoRqst() -> dict:
    return fileop.loadInfo(data = 'setsinfo')


def verifyFilesRqst()-> list:
    path = fileop.createPath("rssDir")
    with open(path + "\\" + "prjctNameSave.txt", 'r') as file :
        prjts = file.read()
        prjts.split(",")
    file.close()
    for projects in prjts :
        print(projects)
        if not  fileop.verifyDir(fileop.createPath(projects)) :
            return [projects, 'project']
    return [fileop.verifyApp(), 'file']