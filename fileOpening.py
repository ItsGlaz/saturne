#programme d'ouvertures des dossiers
from typing import *
import os
import json


def dirCreation(name : str):
    path = os.getcwd() +"\\"+ name
    try :
        os.mkdir(path)
        with open(path +"\\"+ 'prjtset.json', "w") as file :
            pass
        with open(path +"\\"+ 'code.txt', "w") as file :
            pass
        os.mkdir(path +"\\"+ "gtwids")
    except OSError as error :
        print("error raised : ", error)


def rmDirectory(name : str):
    path =  os.getcwd() +"\\"+ name
    rmFile(path)
    os.rmdir(path)


def emptyDir(path : str):
    if os.path.exists(path) :
        return True if os.listdir(path) == [] else False
    

def verifyDir(name : str):
    path = os.getcwd() +"\\"+ name
    if os.path.exists(path) :
        files = os.listdir(path)
        print(files)
        if "code.txt" in files and "prjtset.json" in files and "gtwids" in files :
            return True
    return False


def verifyDir(path : str):
    if os.path.exists(path) :
        files = os.listdir(path)
        print(files)
        if "code.txt" in files and "prjtset.json" in files and "gtwids" in files :
            return True
    return False


def addFiletoDir(path : str):
    files = os.listdir(path)
    if "code.txt" not in files :
        with open(path +"\\"+  'code.txt', "w") as file :
            pass
    if "prjtset.json" not in files :
        with open(path +"\\"+ 'prjtset.json', "w") as file :
            pass
    if "gtwids"not in files :
        os.mkdir(path +"\\"+ "gtwids")

def rmFile(path : str):
    files_list = os.listdir(path)
    for files in files_list :
        os.remove(path + "\\" + files)


def loadInfo(path : str = None, data : str = 'prjctInfo', widget : str = None):
    if data == 'prjctInfo' : 
        if verifyDir(path = path) :
            try : 
                with open(path +"\\"+ 'prjtset.json', "r") as file:
                    return json.load(file)
            except :
                return None
    if data == "widsets" :
        try : 
            with open('widgetInfo.json', "r") as file:
                return json.load(file)[widget]
        except :
            return None
    if data == 'setsinfo' :
        try : 
            with open('widParaInfo.json', "r") as file:
                return json.load(file)
        except :
            return None
            

def writeInfo(path : str, info: Union[dict, str], type : str):
    if type == "json" :
        with open(path, "w") as file :
            json.dump(info, file)
            
    
def createPath(target : str):
    return os.getcwd() +"\\"+ target


def verifyApp() -> Union[str, bool]:
    """verifyApp 
    fonction de vérification que tous les fichiers de l'applications sont présents

    Returns
    -------
    Union[str, bool]
        renvoie True si tous les fichiers sont présents, renvoie le nom du fichier manquant sinon
    """
    path = os.getcwd()
    cfiles = os.listdir(path)
    if 'addWidgetTool.py' not in cfiles :
        return 'addWidgetTool.py'
    if "fileManagemt.py" not in cfiles :
        return "fileManagemt.py"
    if "projectApp.py" not in cfiles :
        return "projectApp.py"
    if "settingsApp.py" not in cfiles :
        return "settingsApp.py"
    if "widgetApp.py" not in cfiles :
        return "widgetApp.py"
    if "tool_tip.py" not in cfiles :
        return "tool_tip.py"
    if 'projectInfoSave.json' not in cfiles :
        return "projectInfoSave.json"
    if "wdSettings.json" not in cfiles :
        return "wdSettings.json"
    if "widgetInfo.json" not in cfiles :
        return "widgetInfo.json"
    if "widgetRss.json" not in cfiles :
        return "widgetRss.json"
    if "widParaInfo.json" not in cfiles :
        return "widParaInfo.json"
    return True
