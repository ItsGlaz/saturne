#fichier gérant les interactions avec les fichiers de sauvegarde
import fileOpening as fileop

def modifyPrjtInfo(name : str, newinfo : dict):
    get_path = fileop.createPath(name) +"\\"+ 'prjtset.json'
    fileop.writeInfo(get_path, newinfo, "json")