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
        self.getSettings()
        self.createInterface()
        if self.actual_widget != None :
            self.widgetParametersFrame(self.actual_widget)
        self.openProjectApp()


    def createInterface(self) :
        
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
        self.fichier.add_command(label = "ouvrir un projet", command = lambda x = None : self.openProjectApp(x))
        self.fichier.add_command(label = "nouveau projet", command = lambda x = "new" : self.openProjectApp(x))
        self.fichier.add_separator() 
        self.fichier.add_command(label = "enregistrer", command = lambda : None)
        self.fichier.add_command(label='vérifier les fichiers', command = lambda : self.verifyFiles())

        self.menubar.add_cascade(label = "fichiers", menu = self.fichier)
        

        #-------------------- création des widgets des paramètres --------------------


        self.createActionBt()

        self.sideWidgetsUptdating()   
            

    def createActionBt(self):
        self.parameter_button = ct.CTkButton(self.parameter_frame,  width= self.width*(10/100), height= self.height*(6/100),
                                             text = "paramètres", font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command = lambda : self.openParameters())
        tl.CreateToolTip(self.parameter_button, text = "Bouton d'ouverture de la fenêtre de paramètres.") if self.showtooltip == "Oui" else None

        self.modify_button = ct.CTkButton(self.parameter_frame,  width= self.width*(10/100), height= self.height*(6/100),
                                             text = "modifier", font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command = lambda : self.modifyWid())
        tl.CreateToolTip(self.modify_button, text = "Bouton de modification des paramètres d'un widget.") if self.showtooltip == "Oui" else None
        self.modify_button.configure(state = "disabled") if self.actual_widget == None else None

        self.delete_button = ct.CTkButton(self.parameter_frame,  width= self.width*(10/100), height= self.height*(6/100),
                                             text = "supprimer", font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10)
        tl.CreateToolTip(self.delete_button, text = "Bouton de suppression d'un widget.") if self.showtooltip == "Oui" else None
        self.delete_button.configure(state = "disabled") if self.actual_widget == None else None
        
        self.delete_button.place(x = self.width*(5/200), y = self.height*(3/200))
        self.modify_button.place(x = self.width*(35/200), y = self.height*(3/200))
        self.parameter_button.place(x = self.width*(70/200), y = self.height*(3/200))
    

    def getSettings(self):

        with open("rssDir\wdSettings.json", "r") as file :
            self.parameters = json.load(file)
        file.close()

        self.width       = self.parameters["width"]
        self.height      = self.parameters["height"]
        self.showtooltip = self.parameters["tooltip"]
        self.detail_lvl  = self.parameters["detail"]

        ct.set_default_color_theme(self.parameters["color"])
        ct.set_appearance_mode(self.parameters["theme"])
        
        self.title("Saturne")
        self.geometry("500x300")
        self.minsize(self.width, self.height)


    def clear(self, mod : str):
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


    def prjctInfoLoading(self, event):
        #fonction d'envoi d'une requête au programme de gestion des fichiers
        if event == "widnamelist" :
            self.widgets_list = interl.getWidNameListReq(self.actual_project)
            self.clear("itemFrame")
            self.sideWidgetsUptdating()


    def sideWidgetsUptdating(self):
        self.clear('itemFrame')
        
        self.add_button = ct.CTkButton(self.main_item_frame, width= self.width*(16/100), height= 40, text = "Ajouter",border_width= 2, border_color = "#FFFFFF",
                                       font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command= lambda : self.widgetAdding())
        tl.CreateToolTip(self.add_button, text = "Bouton d'ajout de widgets dans le projet.") if self.showtooltip == "Oui" else None
        self.add_button.configure(state = "disabled") if self.actual_project == None else None
        self.add_button.grid(padx = 5, pady = 5)
        for widgets in self.widgets_list :
            w_bt = ct.CTkButton(self.main_item_frame, text = widgets, width= self.width*(16/100), height= self.height*(6/100), 
                                font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command = lambda w_id = widgets : self.widgetParametersFrame(w_id))
            w_bt.grid(padx = 5, pady = 5)


    def modifyWid(self):
        pass

        
    def widgetParametersFrame(self, widget):
        self.clear("sets")
        self.actual_widget = widget
        self.createActionBt()
        self.column_num = 1 if self.width*(30/100) < 400 else 3
        row = 2
        column = 0
        loading = True
        try :
            setsinfo = interl.getSetsInfoRqst()
            widsets = interl.getWidSetsRqst(widget)
        except setsinfo == None or widsets == None :
            loading = False
            messagebox.showwarning("Fichier introuvable", "Une erreur est survenue lors du chargement des données.")

        if loading == True  : 
            self.overal_lbl = ct.CTkLabel(self.edit_frame, text = "",font=ct.CTkFont(size=25, weight="bold"))
            self.widnamelbl = ct.CTkLabel(self.edit_frame, text = "Nom du widget :",font=ct.CTkFont(size=15, weight="bold"))
            self.widname = ct.CTkEntry(self.edit_frame, width= 150, height = 40,font=ct.CTkFont(weight="bold"))

            self.overal_lbl.grid(column = 0, row = 0, columnspan = 4, pady = 15)
            self.widnamelbl.grid(row = 1, column = 0, columnspan = 2, pady = 20, sticky = 'e')
            self.widname.grid(row = 1, column = 2, columnspan = 2, pady = 20)
            detail_dico = {"Simple" : (0,1), "Normal" : (1,2), "Complet" : (1,2,3)}
            try :
                #-------------------- création entrées de modification des paramètres --------------------

                for parameter in widsets["parameters"]:
                    if setsinfo[parameter][1] in detail_dico[self.detail_lvl] :
                        
                        lbl = ct.CTkLabel(self.edit_frame, text = parameter + " :", font=ct.CTkFont(size=15, weight="bold"))
                        if parameter in ["font", "hover", "round_width_to_even_numbers", "round_height_to_even_numbers", "image"]:
                            entry = ct.CTkCheckBox(self.edit_frame, text = "")
                        elif parameter in ["state", "anchor", "compound", "justify"]:
                            entry = ct.CTkOptionMenu(self.edit_frame, values = setsinfo[parameter][3])      
                        else :
                            entry = ct.CTkEntry(self.edit_frame, width = 130,font=ct.CTkFont(weight="bold"))
                        self.actual_sets.append((entry, parameter))
                        tl.CreateToolTip(lbl, setsinfo[parameter][2])
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


    def openProjectApp(self, mod = None):
        if self.project_app == None :
            self.project_app = ProjectApp(mod)
            self.project_app.grab_set()
            self.actual_project = self.project_app.closed()
            self.project_app = None
            if self.actual_project != None :
                self.title(f"Saturne : {self.actual_project}")
                self.prjctInfoLoading(event = "widnamelist")
            else :
                self.title("Saturne")
                self.resetAttr()
        else :
            print("fenêtre de projets déjà ouverte")
        self.clear('all')


    def openParameters(self):
        if self.settings == None :
            self.settings = AppEditing(self.parameters)
            self.settings.grab_set()
            self.parameters = self.settings.get()
            self.settings = None
            self.getSettings()
            self.clear('all')
        else :
            print("fenêtre de paramètres déjà ouverte")


    def widgetAdding(self):
        if self.widgetapp == None :
            self.widgetapp = WidgetApp()
            self.widgetapp.grab_set()
            newwidget = self.widgetapp.get()
            if newwidget != None :
                self.widgets_list.append(newwidget)
            self.widgetapp = None
            self.sideWidgetsUptdating()
        else :
            print("fenêtre d'ajout d'un widget déjà ouverte")


    def verifyFiles(self):
        verify =interl.verifyFilesRqst()
        if verify[0] != True :
            messagebox.showwarning("Fichier manquant", f"Un fichier ou dossier est manquant \nname : {verify[0]}; class : {verify[1]}")
        else :
            messagebox.showinfo("Fichiers complets", "Tous les fichiers sont présents")
        

    def resetAttr(self):
        if self.actual_project == None :
            self.widgets_list = []
            self.actual_widget = None

if __name__ == "__main__":
    app = interface()
    app.mainloop()