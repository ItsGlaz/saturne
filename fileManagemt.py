#fichier gérant les interactions avec les fichiers de sauvegarde
import fileOpening as fileop

def modifyPrjtInfo(name : str, newinfo : dict):
    get_path = fileop.createPath(name) +"\\"+ 'prjtset.json'
    fileop.writeInfo(get_path, newinfo, "json")


def cNWSF(widget, project):
    """cNWSF : Create New Widget Settings File

    Parameters
    ----------
    widget : _type_
        _description_
    project : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    sets = fileop.loadInfo(data = "widsets", widget = widget)
    setvalues = fileop.loadInfo(data = "setsinfo")

    path = fileop.createPath(project)
    widnameused = fileop.loadInfo(path = path,data = "widNameList")
    flag = False
    incr = 1
    while flag == False :
        if widget + str(incr) not in widnameused :
            flag = True
            newname = widget + str(incr)
        else : incr += 1
    dico = {}
    dico["name"] = newname
    dico["ID"] = widget
    for values in sets["parameters"]:
        dico [values] = setvalues[values][0]
    fileop.cWSF(path, newname, dico)
    return newname 


def uWS(widid : str, widname : str, dico : dict, project : str) -> None:
    """uWS : Update Widget Settings

    Parameters
    ----------
    wid : str
        _description_
    dico : dict
        _description_
    """
    datasets = {}
    datasets["name"] = dico["name"]
    datasets["ID"] = dico["ID"]
    sets = fileop.loadInfo(data = "widsets", widget = widid)
    setvalues = fileop.loadInfo(data = "setsinfo")
    for settings in sets["parameters"] :
        if settings in dico :
            datasets[settings] = dico[settings]
        else :
            datasets[settings] = setvalues[settings][0]
    print(datasets)
    path = fileop.createPath(project)
    fileop.rmFile(path + "\\" + widname + '.json')
    fileop.mWS(path, dico["name"], widname, datasets)
