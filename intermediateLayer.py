#fichier gérant les interactions entre l'interface et les fichiers fonctionnels
import fileOpening as fileop
import fileManagemt as flmngt
from typing import *

def newPrjctRqst(name : str) -> None: 
    """newPrjctRequest 
    fonction de transition entre le programme de l'interface et le programme de gestions des fichiers
    envoie une requête de création d'un dossier pour un nouveau projet

    Parameters
    ----------
    name : str
        nom du dossier à créer
    """
    fileop.dirCreation(name)


def rmproject(name : str) -> None:
    fileop.rmDirectory(name)


def modidyPrjctRqst(name : str, dico : dict) -> None:
    flmngt.modifyPrjtInfo(name, dico)


def getPrjtSetRqst(name : str) -> dict:
    path = fileop.createPath(name)
    print(path)
    return fileop.loadInfo(path = path)


def getMainWidSetsRqst(widget : str) -> dict:
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


def getWidNameListReq(project : str) -> list:
    path = fileop.createPath(project)
    return fileop.loadInfo(path, data = "widNameList")


def getWidSetReq(widname : str, project : str) -> dict:
    path = fileop.createPath(project + "\\" + widname + ".json")
    return fileop.loadInfo(path, "actualwidSet")


def createWidSetFileReq(newwidget : str, project : str) -> str:
    return flmngt.cNWSF(newwidget, project)


def modifyWidSetReq(widget : str, widname : str, dico : str, project : str) -> None:
    flmngt.uWS(widget,widname, dico, project)


def delWidReq(widget : str, project : str) -> None:
    fileop.rmWid(widget, project)


def tryWN(name : str) -> bool:
    allowedchar = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'
    ]
    for letters in name :
        if letters not in allowedchar :
            return False
    if name[0] in allowedchar[26:-2]:
        return False
    return True
        

#possibilité de lancer le programme seul, à des fins de débogage
if __name__ == "__main__" :
    name = input("nom : ")
    print(tryWN(name))