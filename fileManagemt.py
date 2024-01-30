#fichier gérant les interactions avec les fichiers de sauvegarde
import fileOpening as fileop

def modifyPrjtInfo(name : str, newinfo : dict):
    get_path = fileop.createPath(name) +"\\"+ 'prjtset.json'
    fileop.writeInfo(get_path, newinfo, "json")


def CreateNewWidSetFile(widget, project):
    sets = fileop.loadInfo(data = "widsets", widget = widget)
    setvalues = fileop.loadInfo(data = "setsinfo")

    path = fileop.createPath(project)
    widnameused = fileop.loadInfo(path = path,data = "widNameList")
    dico = {}
    dico["name"] = ""
    dico["ID"] = widget
    for values in sets["parameters"]:
        dico [values] = setvalues[values][0]
    flag = False
    incr = 1
    while flag == False :
        if widget + str(incr) not in widnameused :
            flag = True
            newname = widget + str(incr)
        else : incr += 1
    
    #créer le fichier
    fileop.cWSF(path, newname, dico)
    #renvoyer le l'ID du widget
    return newname 