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
        with open(path +"\\"+ 'widNmeList.txt', "w") as file :
            pass
    except OSError as error :
        print("error raised : ", error)


def rmDirectory(name : str):
    path =  os.getcwd() +"\\"+ name
    rmFiles(path)
    os.rmdir(path)


def emptyDir(path : str):
    if os.path.exists(path) :
        return True if os.listdir(path) == [] else False
    

def verifyDir(name : str):
    path = os.getcwd() +"\\"+ name
    if os.path.exists(path) :
        files = os.listdir(path)
        print(files)
        if "code.txt" in files and "prjtset.json" in files and "widNmeList.txt" in files :
            return True
        else :
            addFiletoDir(path)
            return True


def verifyDir(path : str):
    if os.path.exists(path) :
        files = os.listdir(path)
        print(files)
        if "code.txt" in files and "prjtset.json" in files and "widNmeList.txt" in files :
            return True
        else :
            addFiletoDir(path)
            return True


def addFiletoDir(path : str):
    files = os.listdir(path)
    if "code.txt" not in files :
        with open(path +"\\"+  'code.txt', "w") as file :
            pass
    if "prjtset.json" not in files :
        with open(path +"\\"+ 'prjtset.json', "w") as file :
            pass
    if "widNmeList.txt" not in files :
        with open(path +"\\"+ 'widNmeList.txt', "w") as file :
            pass


def rmFiles(path : str):
    files_list = os.listdir(path)
    for files in files_list :
        try: 
            os.remove(path + "\\" + files)
        except : 
            os.rmdir()


def rmFile(path : str):
    os.remove(path)

def rmWid(widget : str, project : str) : 
    path = createPath(project)
    os.remove(path + "\\" + widget + ".json")
    with open(path + "\widNmeList.txt", 'r', encoding= 'utf8') as file :
        data = file.read().split(",")
        del data[data.index(widget)]
    with open(path + "\widNmeList.txt", 'w', encoding= 'utf8') as file :
        file.write(data)

def loadInfo(path : str = None, data : str = 'prjctInfo', widget : str = None):
    if data == "widsets" :
        try : 
            with open('rssDir\widgetInfo.json', "r", encoding= 'utf8') as file:
                return json.load(file)[widget]
        except :
            return None
    if data == 'setsinfo' :
        try : 
            with open('rssDir\widParaInfo.json', "r", encoding= 'utf8') as file:
                return json.load(file)
        except :
            return None
    if data == 'prjctInfo' : 
        if verifyDir(path = path) :
            try : 
                with open(path + '\\prjtset.json', "r", encoding= 'utf8' ) as file:
                    return json.load(file)
            except :
                return None
    if data == "widNameList" :
        try :
            with open(path + "\widNmeList.txt", 'r', encoding= 'utf8') as file :
                widsaved = file.read().split(",")
            file.close()
            return widsaved
        except :
            return []
    if data == "actualwidSet" :
        try :
            with open(path, 'r', encoding= 'utf8') as file :
                return json.load(file)
        except :
            return False
            

def writeInfo(path : str, info: Union[dict, str], type : str):
    if type == "json" :
        with open(path, "w", encoding= 'utf8') as file :
            json.dump(info, file)
            
    
def createPath(target : str):
    return os.getcwd() +"\\"+ target


def cWSF(path : str, name : str, settings : dict):
    with open(path + "\\" + name + ".json", "w", encoding= 'utf8') as file :
        json.dump(settings, file)
    with open(path + "\widNmeList.txt", 'a', encoding= 'utf8') as file :
        file.write("," + name)
    

def mWS(path : str, newname : str, oldname : str, settings : dict) :
    with open(path + "\\" + newname + ".json", "w", encoding= 'utf8') as file :
        json.dump(settings, file)
    if newname != oldname :
        with open(path + "\widNmeList.txt", 'r', encoding= 'utf8') as file :
            data = file.read().split(',')
            print(data)
            data.insert(data.index(oldname), newname)
            del data[data.index(oldname)]
            print(data)
            data = ','.join(data)
        with open(path + "\widNmeList.txt", 'w', encoding= 'utf8') as file :
            file.write(data)

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
    cfiles =os.listdir(path + "\\" + "rssDir")
    if 'prjctNameSave.txt' not in cfiles :
        return "prjctNameSave.txt"
    if "wdSettings.json" not in cfiles :
        return "wdSettings.json"
    if "widgetInfo.json" not in cfiles :
        return "widgetInfo.json"
    if "widgetRss.json" not in cfiles :
        return "widgetRss.json"
    if "widParaInfo.json" not in cfiles :
        return "widParaInfo.json"
    return True


if __name__ == "__main__" :
    print(verifyApp())