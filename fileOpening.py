#programme d'ouvertures des dossiers
import os

def dirCreation(name):
    path = os.getcwd() +"\\"+ name
    try :
        os.mkdir(path)
        with open(path +"\\"+ 'prjtset.json', "w") as file :
            pass
        with open(path +"\\"+ 'code.txt', "w") as file :
            pass
    except OSError as error :
        print("error raised : ", error)


def rmDirectory(name):
    path =  os.getcwd() +"\\"+ name
    rmFile(path)
    os.rmdir(path)


def emptyDir(path):
    if os.path.exists(path) :
        return True if os.listdir(path) == [] else False
    

def verifyDir(name):
    path = os.getcwd() +"\\"+ name
    if os.path.exists(path) :
        files = os.listdir(path)
        if "code.txt" in files and "prjtset.json" in files :
            return True
    return False


def addFiletoDir(path):
    files = os.listdir(path)
    if "code.txt" not in files :
        with open('code.txt', "w") as file :
            pass
    if "prjtset.json" not in files :
        with open('prjtset.json', "w") as file :
            pass


def rmFile(path):
    files_list = os.listdir(path)
    for files in files_list :
        os.remove(path + "\\" + files)