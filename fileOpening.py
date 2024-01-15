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
        if "code.txt" in files and "prjtset.json" in files :
            return True
    return False


def verifyDir(path : str):
    if os.path.exists(path) :
        files = os.listdir(path)
        print(files)
        if "code.txt" in files and "prjtset.json" in files :
            return True
    return False


def addFiletoDir(path : str):
    files = os.listdir(path)
    if "code.txt" not in files :
        with open('code.txt', "w") as file :
            pass
    if "prjtset.json" not in files :
        with open('prjtset.json', "w") as file :
            pass


def rmFile(path : str):
    files_list = os.listdir(path)
    for files in files_list :
        os.remove(path + "\\" + files)


def loadInfo(path : str, datatype : str):
    if datatype == 'json' : 
        if verifyDir(path = path) :
            try : 
                with open(path +"\\"+ 'prjtset.json', "r") as file:
                    return json.load(file)
            except :
                return None
            

def writeInfo(path : str, info: Union[dict, str], type : str):
    if type == "json" :
        with open(path, "w") as file :
            json.dump(info, file)
            
    
def createPath(target : str):
    return os.getcwd() +"\\"+ target
