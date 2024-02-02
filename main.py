#fichier contenant l'interface graphique du programme
from typing import Union
import tkinter as tk
from tkinter import messagebox
import customtkinter as ct
import json
import tool_tip as tl
import intermediateLayer as interl
from settingsApp import AppEditing
from widgetApp import WidgetApp
from projectApp import ProjectApp

class interface(ct.CTk):

    def __init__(self) -> None:
        super().__init__()
        
        self.widgets_list = []
        self.actual_sets = []
        self.settings = None
        self.widgetapp = None
        self.project_app = None
        self.actual_widget = None
        self.actual_project = None
        self.widget_id = None

        self.getSettings()
        self.createInterface()
        if self.actual_widget != None :
            self.widgetParametersFrame(self.actual_widget)
        self.openProjectApp()


    #-------------------- fonctions de création de la fenêtres --------------------
        

    def createInterface(self) -> None:
        """createInterface
        Fonction de création du corps de l'interface
        """
        #-------------------- création des frames --------------------
        
        
        self.code_frame = ct.CTkFrame(self, width=self.width*(45/100), height=self.height, border_width=2, border_color="#000000")
        self.edit_frame = ct.CTkScrollableFrame(self, width=self.width*(35/100), height=self.height*(90/100))
        self.parameter_frame = ct.CTkFrame(self, height = self.height*(10/100), width = self.width*(55/100))

        self.main_item_frame = ct.CTkScrollableFrame(self, height = self.height*(85/100), width = self.width*(18/100), label_text = "widgets :")


        self.code_frame.grid(row =0, rowspan =2, column = 0)
        self.edit_frame.grid(row = 0, column = 1, sticky = "e")
        
        self.main_item_frame.grid(row = 0, column = 2, sticky = "e")
        self.parameter_frame.grid(row = 1,column =1, columnspan = 2 )


        #-------------------- création du menu --------------------


        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)

        self.fichier = tk.Menu(self.menubar, tearoff = False)
        self.fichier.add_command(label = "Ouvrir un projet", command = lambda x = None : self.openProjectApp(x))
        self.fichier.add_command(label = "Nouveau projet", command = lambda x = "new" : self.openProjectApp(x))
        self.fichier.add_separator()
        self.fichier.add_command(label = "Enregistrer", command = lambda : None)
        self.fichier.add_command(label='Vérifier les fichiers', command = lambda : self.verifyFiles())
        self.fichier.add_separator() 
        self.fichier.add_command(label='Quitter', command = lambda : self.on_quit())
        self.menubar.add_cascade(label = "fichiers", menu = self.fichier)
        

        #-------------------- création des widgets et des boutons d'actions --------------------


        self.createActionBt()

        self.sideWidgetsUptdating()   
            

    def createActionBt(self) -> None:
        """createActionBt 
        fonction de création des boutons d'actions ( bouton de suppression et de modification de widget, et bouton d'ouverture des paramètres)
        """
        self.parameter_button = ct.CTkButton(self.parameter_frame,  width= self.width*(10/100), height= self.height*(6/100),
                                             text = "paramètres", font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command = lambda : self.openParameters())
        tl.CreateToolTip(self.parameter_button, text = "Bouton d'ouverture de la fenêtre de paramètres.") if self.showtooltip == "Oui" else None

        self.modify_button = ct.CTkButton(self.parameter_frame,  width= self.width*(10/100), height= self.height*(6/100),
                                             text = "modifier", font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command = lambda : self.modifyWid())
        tl.CreateToolTip(self.modify_button, text = "Bouton de modification des paramètres d'un widget.") if self.showtooltip == "Oui" else None
        self.modify_button.configure(state = "disabled") if self.actual_widget == None else None

        self.delete_button = ct.CTkButton(self.parameter_frame,  width= self.width*(10/100), height= self.height*(6/100),
                                             text = "supprimer", font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command = lambda : self.delWid())
        tl.CreateToolTip(self.delete_button, text = "Bouton de suppression d'un widget.") if self.showtooltip == "Oui" else None
        self.delete_button.configure(state = "disabled") if self.actual_widget == None else None
        
        self.delete_button.place(x = self.width*(5/200), y = self.height*(3/200))
        self.modify_button.place(x = self.width*(35/200), y = self.height*(3/200))
        self.parameter_button.place(x = self.width*(70/200), y = self.height*(3/200))


    def sideWidgetsUptdating(self) -> None:
        """sideWidgetsUptdating
        Fonction de création des boutons pour les widgets, sur le coté droit de la fenêtre
        """
        self.clear('itemFrame')
        
        self.add_button = ct.CTkButton(self.main_item_frame, width= self.width*(16/100), height= 40, text = "Ajouter",border_width= 2, border_color = "#FFFFFF",
                                       font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command= lambda : self.widgetAdding())
        tl.CreateToolTip(self.add_button, text = "Bouton d'ajout de widgets dans le projet.") if self.showtooltip == "Oui" else None
        self.add_button.configure(state = "disabled") if self.actual_project == None else None
        self.add_button.grid(padx = 5, pady = 5)
        for widgets in self.widgets_list :
            if widgets != "" :
                w_bt = ct.CTkButton(self.main_item_frame, text = widgets, width= self.width*(16/100), height= self.height*(6/100), 
                                    font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command = lambda w_id = widgets : self.widgetParametersFrame(w_id))
                w_bt.grid(padx = 5, pady = 5)
            else : pass


    def widgetParametersFrame(self, widget : str)  -> None:
        """widgetParametersFrame 
        fonction de création de la frame de paramètres du widget

        Parameters
        ----------
        widget : str
            widget dont la fonction doit afficher les paramètres, et leurx valeurs respectives
        """
        self.clear("sets")
        self.actual_widget = widget
        #on configue les boutons d'action pour les rendre actifs
        self.createActionBt()
        #on configure la disposition des paramètres selon la largeur de la fenêtre
        self.column_num = 1 if self.width*(30/100) < 470 else 3
        row = 2
        column = 0
        loading = True

        try :
            #on récupère les données du widget, les données associées à chaque paramètre, et les paramètre par défaut du widget
            actualwidset = self.fLoadFunct("getWidSet")
            self.widget_id = actualwidset["ID"]
            setsinfo = self.fLoadFunct("getSetsInfo")
            widsets = self.fLoadFunct("getWidInfo")
        except any as error :
            print(error)
            loading = False
            messagebox.showwarning("Fichier introuvable", "Une erreur est survenue lors du chargement des données.")

        if loading == True :
            try :
                #-------------------- création des entrées de modification des paramètres --------------------

                #on crée le label titre, ainsi que l'entrée permettant de renseigner le nom du widget
                self.overal_lbl = ct.CTkLabel(self.edit_frame, text = actualwidset["name"],font=ct.CTkFont(size=25, weight="bold"))
                self.widnamelbl = ct.CTkLabel(self.edit_frame, text = "Nom du widget :",font=ct.CTkFont(size=15, weight="bold"))
                self.widname = ct.CTkEntry(self.edit_frame, width= 150, height = 40,font=ct.CTkFont(weight="bold"))
                tl.CreateToolTip(self.widnamelbl, "Nom du widget, attention ce nom sera aussi utilisé comme nom de variable dans le code.") if self.showtooltip == "Oui" else None
                self.widname.insert(0, actualwidset["name"])

                self.overal_lbl.grid(column = 0, row = 0, columnspan = 4 if self.column_num == 3 else 2 , pady = 15)
                self.widnamelbl.grid(row = 1, column = 0, columnspan = 2 if self.column_num == 3 else 1, 
                                     pady = 20, sticky = 'e')
                self.widname.grid(row = 1, column = 2 if self.column_num == 3 else 1, 
                                  columnspan = 2 if self.column_num == 3 else 1 , padx = 15, pady = 20)
                
                detail_dico = {"Simple" : (0,1), "Normal" : (1,2), "Complet" : (1,2,3)}
                
                #on crée le reste des paramètres, selon le type ( soit une entrée texte, un menu, ou un switch)
                for parameter in widsets["parameters"]:
                    
                    if setsinfo[parameter][1] in detail_dico[self.detail_lvl] :
                        lbl = ct.CTkLabel(self.edit_frame, text = parameter + " :", font=ct.CTkFont(size=15, weight="bold"))
                        
                        if parameter in ["font", "hover", "round_width_to_even_numbers", "round_height_to_even_numbers", "image"]:
                            entry = ct.CTkSwitch(self.edit_frame, text = "", onvalue="1", offvalue="0", switch_width= 48,switch_height= 18)
                            entry.select() if actualwidset[parameter] == 1 else None
                        
                        elif parameter in ["state", "anchor", "compound", "justify"]:
                            entry = ct.CTkOptionMenu(self.edit_frame, values = setsinfo[parameter][3])    
                            entry.set(actualwidset[parameter])  
                        
                        else :
                            entry = ct.CTkEntry(self.edit_frame, width = 130,font=ct.CTkFont(weight="bold"))
                            entry.insert(0, actualwidset[parameter])
                        self.actual_sets.append((entry, parameter))
                        tl.CreateToolTip(lbl, setsinfo[parameter][2]) if self.showtooltip == "Oui" else None
                        
                        lbl.grid(row = row, column = column, padx = 5, pady = 10, sticky = 'n')
                        column = column + 1 if column < self.column_num else 0
                        row += 1 if column == 0 else 0
                        
                        entry.grid(row = row, column = column, padx = 5, pady = 10, sticky = 'n')
                        column = column + 1 if column < self.column_num else 0
                        row += 1 if column == 0 else 0
            except any as error :
                print(error)
                messagebox.showwarning("Erreur de chargement", "Une erreur est survenue lors de l'affichage des données")


    def codeFrame(self):
        #permet d'afficher le code de l'interface
        pass


    #-------------------- fonctions de gestions des évènements --------------------
                 

    def clear(self, mod : str) -> None:
        """clear 
        fonction de destruction de widgets

        Parameters
        ----------
        mod : str
            défini les widgets à détruire :
            -all : détruit tous les widgets de l'interface ( frames comprises )
            -itemFrame : détruit les boutons associés aux widgets
            -sets : détruit les labels et entrées de paramètres d'un widget
        """
        if mod == 'all' :
            liste = self.grid_slaves() + self.pack_slaves()
            for element in liste :
                element.destroy()
            self.createInterface()
            if self.actual_widget != None :
                self.widgetParametersFrame(self.actual_widget)
            self.sideWidgetsUptdating()
        if mod == 'itemFrame' :
            liste = self.main_item_frame.grid_slaves()
            for element in liste :
                element.destroy()
        if mod == 'sets':
            liste = self.edit_frame.grid_slaves()
            for element in liste :
                element.destroy()


    def fLoadFunct(self, event : str, *dico : dict) -> Union[None, dict]:
        """fLoadFunct _summary_
        fonction d'envoi de requêtes de chargement/envoi de données

        Parameters
        ----------
        event : str
            décrit l'action à réaliser :
            -widnamelist : récupère la liste des widgets du projet, et actualise la frame des widget
            -getWidSet : récupère les données d'un widget ciblé            ( fichier "[nom du projet]\[nom du widget].json")
            -modifyWidSet : modifie les données d'un widget ciblé          ( fichier "[nom du projet]\[nom du widget].json")
            -getSetsInfo : récupère les données des paramètres des widgets ( fichier "widParaInfo.json")
            -getSetsInfo : récupères les données de base du widget ciblé   ( fichier "widgetInfo.json")
        Returns
        -------
        Union[None, dict]
            renvoie None dans la plupart des cas, 
            renvoie un dictionnaire si l'appel est lié à l'obtention des données d'un widget
        """
        if event == "widnamelist" :
            self.widgets_list = interl.getWidNameListReq(self.actual_project)
            self.sideWidgetsUptdating()
        if event == "getWidSet" :
            return interl.getWidSetReq(self.actual_widget, self.actual_project)
        if event == 'modifyWidSet' :
            interl.modifyWidSetReq(self.widget_id, self.actual_widget, dico[0], self.actual_project)
        if event == "getSetsInfo" :
            return interl.getSetsInfoRqst()
        if event == "getWidInfo" :
            return interl.getMainWidSetsRqst(self.widget_id)


    def modifyWid(self) -> None:
        """modifyWid 
        fonction de modification des paramètres d'un widget,
        appele la fonction de chargement/envoi de données (fLoadFunct)
        """
        dico = {}
        dico['ID'] = self.widget_id
        #on vérifie que le nom de widget donné respecte les règles de typage pour une variable
        if interl.tryWN(self.widname.get()) == True :
            dico["name"] = self.widname.get() 
        else :
            messagebox.showerror("Nom de widget invalide", "Le nom du widget est invalide.")
            dico["name"] = self.actual_widget
            #on supprime le nom invalide dans l'entrée associée et le remplace par le précédent nom
            self.widname.delete()
            self.widname.insert(0, self.actual_widget)
        
        for element in self.actual_sets :
            dico[element[1]] = element[0].get()
        self.fLoadFunct("modifyWidSet", dico)
        self.fLoadFunct("widnamelist")
        self.overal_lbl.configure(text = dico["name"])
        self.actual_widget = dico["name"]


    def getSettings(self) -> None:
        """getSettings 
        fonction de récupération des paramètres de l'application,
        attribue les paramètres chargé aux variable de l'application
        """

        with open("rssDir\wdSettings.json", "r") as file :
            self.parameters = json.load(file)
        file.close()
        if self.parameters["fullscreen"]: 
            self.width   = self.winfo_screenwidth() -10
            self.height  = self.winfo_screenheight() -10
            self.attributes('-fullscreen', True)
        else : 
            self.attributes('-fullscreen', False)
            self.width   = self.parameters["width"]
            self.height  = self.parameters["height"]
        self.showtooltip = self.parameters["tooltip"]
        self.detail_lvl  = self.parameters["detail"]

        ct.set_default_color_theme(self.parameters["color"])
        ct.set_appearance_mode(self.parameters["theme"])
        
        self.title("Saturne")
        self.geometry("500x300")
        self.minsize(self.width, self.height)


    def verifyFiles(self) -> None:
        """verifyFiles 
        Fonction de vérification des fichiers de l'application
        """
        verify =interl.verifyFilesRqst()
        if verify[0] != True :
            messagebox.showwarning("Fichier manquant", f"Un fichier ou dossier est manquant \nname : {verify[0]}; class : {verify[1]}")
        else :
            messagebox.showinfo("Fichiers complets", "Tous les fichiers sont présents")
        

    def resetAttr(self) -> None:
        """resetAttr 
        Fonction de réinitialisation de certaines variables de l'application,
        utilisé lorsque l'application est lancé sans projet ouvert
        """
        if self.actual_project == None :
            self.widgets_list = []
            self.actual_widget = None


    def delWid(self):
        """delWid 
        Fonction de suppression d'un widget.
        """
        interl.delWidReq(self.actual_widget, self.actual_project)
        self.fLoadFunct('widnamelist')
        self.clear("sets")
        self.actual_widget = None
        self.widget_id = None
        self.widgets_list = []
        self.createActionBt()

    
    def on_quit(self):
        """on_quit 
        Détruit la fenêtre lorsque le bouton "Quitter" du menu est pressé
        """
        self.destroy()

#-------------------- fonctions de création de fenêtres enfant --------------------
    

    def openProjectApp(self) -> None:
        """openProjectApp 
        Fonction d'ouverture de la fenêtre de projets,
        modifie le nom de l'application si un projet est ouvert
        """
        if self.project_app == None :
            self.project_app = ProjectApp()
            self.project_app.grab_set()
            self.actual_project = self.project_app.closed()
            self.project_app = None
            if self.actual_project != None :
                self.title(f"Saturne : {self.actual_project}")
                self.fLoadFunct(event = "widnamelist")
            else :
                self.title("Saturne")
                self.resetAttr()
        else :
            print("fenêtre de projets déjà ouverte")
        self.clear('all')


    def openParameters(self) -> None:
        """openParameters 
        fonction d'ouverture des paramètres, 
        appele la fonction "getSettings" à l'issue
        """
        if self.settings == None :
            self.settings = AppEditing(self.parameters)
            self.settings.grab_set()
            self.parameters = self.settings.get()
            self.settings = None
            self.getSettings()
            self.clear('all')
        else :
            print("fenêtre de paramètres déjà ouverte")


    def widgetAdding(self)  -> None:
        """widgetAdding 
        Fonction d'ouverture de la fenêtre d'ajout de Widgets
        """
        if self.widgetapp == None :
            self.widgetapp = WidgetApp()
            self.widgetapp.grab_set()
            newwidget = self.widgetapp.get()
            if newwidget != None :
                newwidget = interl.createWidSetFileReq(newwidget, self.actual_project)
                self.widgets_list.append(newwidget)

            self.widgetapp = None
            self.sideWidgetsUptdating()
        else :
            print("fenêtre d'ajout d'un widget déjà ouverte")


if __name__ == "__main__":
    app = interface()
    app.mainloop()