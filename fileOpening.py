#programme d'ouvertures des dossiers
import os

def directoryCreation(name):
    path = os.getcwd() +"\\"+ name
    try :
        os.mkdir(path)
    except OSError as error :
        print("error raised : ", error)


def rmDirectory(name):
    path =  os.getcwd() +"\\"+ name
    if emptyDir(path) and os.path.exists(path) :
        os.rmdir(path)


def emptyDir(path):
    return True if os.listdir(path) == [] else False