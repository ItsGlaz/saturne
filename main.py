#fichier contenant l'interface graphique du programme
import tkinter as tk
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
        self.settings = None
        self.widgetapp = None
        self.project_app = None
        self.getSettings()


        self.createInterface()


    def createInterface(self) :
        
        #-------------------- création des frames --------------------
        
        
        self.code_frame = ct.CTkFrame(self, width=self.width*(50/100), height=self.height, border_width=2, border_color="#000000")
        self.edit_frame = ct.CTkFrame(self, width=self.width*(30/100), height=self.height*(90/100))
        self.parameter_frame = ct.CTkFrame(self, height = self.height*(10/100), width = self.width*(50/100))

        self.main_item_frame = ct.CTkScrollableFrame(self, height = self.height*(85/100), width = self.width*(18/100), label_text = "widgets :")


        self.code_frame.grid(row =0, rowspan =2, column = 0)
        self.edit_frame.grid(row = 0, column = 1)
        
        self.main_item_frame.grid(row = 0, column = 2)
        self.parameter_frame.grid(row = 1,column =1, columnspan = 2 )


        #-------------------- création du menu --------------------


        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)

        self.fichier = tk.Menu(self.menubar, tearoff = False)
        self.fichier.add_command(label = "ouvrir un projet", command = lambda x = None : self.openProjectApp(x))
        self.fichier.add_command(label = "nouveau projet", command = lambda x = "new" : self.openProjectApp(x))
        self.fichier.add_separator() 
        self.fichier.add_command(label = "enregistrer", command = lambda : None)

        self.menubar.add_cascade(label = "fichiers", menu = self.fichier)
        

        #-------------------- création des widgets des paramètres --------------------


        self.parameter_button = ct.CTkButton(self.parameter_frame,  width= self.width*(10/100), height= self.height*(6/100),
                                             text = "paramètres", font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command = lambda : self.openParameters())
        tl.CreateToolTip(self.parameter_button, text = "Bouton d'ouverture de la fenêtre de paramètres.") if self.showtooltip == "Oui" else None

        self.modify_button = ct.CTkButton(self.parameter_frame,  width= self.width*(10/100), height= self.height*(6/100),
                                             text = "modifier", font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command = lambda : None)
        tl.CreateToolTip(self.modify_button, text = "Bouton de modification des paramètres d'un widget.") if self.showtooltip == "Oui" else None

        self.delete_button = ct.CTkButton(self.parameter_frame,  width= self.width*(10/100), height= self.height*(6/100),
                                             text = "supprimer", font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10)
        tl.CreateToolTip(self.delete_button, text = "Bouton de suppression d'un widget.") if self.showtooltip == "Oui" else None

        
        self.delete_button.place(x = self.width*(5/200), y = self.height*(3/200))
        self.modify_button.place(x = self.width*(35/200), y = self.height*(3/200))
        self.parameter_button.place(x = self.width*(70/200), y = self.height*(3/200))

        self.sideWidgetsUptdating()   


    def getSettings(self):

        with open("wdSettings.json", "r") as file :
            self.parameters = json.load(file)
        file.close()

        self.width       = self.parameters["width"]
        self.height      = self.parameters["height"]
        self.showtooltip = self.parameters["tooltip"]
        self.detail_lvl  = self.parameters["detail"]

        ct.set_default_color_theme(self.parameters["color"])
        ct.set_appearance_mode(self.parameters["theme"])
        
        self.geometry("500x300")
        self.minsize(self.width, self.height)


    def clear(self, mod):
        if mod == 'all' :
            liste = self.grid_slaves() + self.pack_slaves()
            for element in liste :
                element.destroy()
            self.createInterface()
        if mod == 'itemFrame' :
            liste = self.main_item_frame.grid_slaves()
            for element in liste :
                element.destroy()


    def fileLoading(self):
        #fonction d'envoi d'une requête au programme de gestion des fichiers
        pass


    def sideWidgetsUptdating(self):
        self.clear('itemFrame')
        
        self.add_button = ct.CTkButton(self.main_item_frame, width= self.width*(16/100), height= 40, text = "Ajouter", 
                                       font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command= lambda : self.widgetAdding())
        tl.CreateToolTip(self.add_button, text = "Bouton d'ajout de widgets dans le projet.")
        self.add_button.grid(padx = 5, pady = 5)

        for widgets in self.widgets_list :
            w_bt = ct.CTkButton(self.main_item_frame, text = widgets, width= self.width*(16/100), height= self.height*(6/100), 
                                font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command = lambda w_id : self.widgetParametersFrame(w_id))
            w_bt.grid(padx = 5, pady = 5)

        
    def widgetParametersFrame(self):
        #crée la fenêtre des paramètres du widget selectionné
        pass


    def codeFrame(self):
        #à voir si cette fonction est faite ou non
        #permet d'afficher l'interface à construire, peut être remplacée par une fenêtre à part
        pass


    def openProjectApp(self, mod = None):
        if self.project_app == None :
            self.project_app = ProjectApp(mod)
            self.project_app.grab_set()
            self.project_app.closed()
            self.project_app = None
        else :
            print("fenêtre de projets déjà ouverte")
            self.project_app.focus()


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
            self.settings.focus()


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
            self.widgetapp.focus()

        

if __name__ == "__main__":
    app = interface()
    app.mainloop()