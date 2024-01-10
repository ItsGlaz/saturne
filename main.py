#fichier contenant l'interface graphique du programme
import customtkinter as ct
import json
import tool_tip as tl
import intermediateLayer
from app_editing_file import AppEditing
from widgetApp import *
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
        self.sideWidgetsUptdating()


    def createInterface(self) :
        
        #-------------------- création des frames --------------------
        
        self.main_frame = ct.CTkFrame(self)
        
        self.show_frame = ct.CTkFrame(self.main_frame, width=self.width*(50/100), height=self.height, border_width=2, border_color="#000000")
        self.edit_frame = ct.CTkFrame(self.main_frame, width=self.width*(30/100), height=self.height*(90/100))
        self.item_frame = ct.CTkFrame(self.main_frame, width=self.width*(20/100), height=self.height*(90/100), border_width=2, border_color="#000000")
        self.parameter_frame = ct.CTkFrame(self.main_frame, height = self.height*(10/100), width = self.width*(50/100))

        self.main_item_frame = ct.CTkScrollableFrame(self.item_frame, height = self.height*(90/100))


        self.main_frame.grid()

        self.show_frame.grid(rowspan = 2, column = 0)
        self.edit_frame.grid(row = 0, column = 1)
        self.item_frame.grid(row = 0, column = 2)
        
        self.main_item_frame.grid()
        self.parameter_frame.grid(row = 1,column =1, columnspan = 2 )
        

        #-------------------- création des widgets des paramètres --------------------


        self.parameter_button = ct.CTkButton(self.parameter_frame,  width= self.width*(10/100), height= self.height*(6/100), bg_color= 'transparent',
                                             text = "paramètres", font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command = lambda : self.openParameters())
        tl.CreateToolTip(self.parameter_button, text = "Bouton d'ouverture de la fenêtre de paramètres.")

        self.modify_button = ct.CTkButton(self.parameter_frame,  width= self.width*(10/100), height= self.height*(6/100), bg_color= 'transparent',
                                             text = "modifier", font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command = lambda : self.openProjectApp())
        tl.CreateToolTip(self.modify_button, text = "Bouton de modification des paramètres d'un widget.")

        self.delete_button = ct.CTkButton(self.parameter_frame,  width= self.width*(10/100), height= self.height*(6/100), bg_color= 'transparent',
                                             text = "supprimer", font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10)
        tl.CreateToolTip(self.delete_button, text = "Bouton de suppression d'un widget.")

        
        self.delete_button.place(x = self.width*(5/200), y = self.height*(3/200))
        self.modify_button.place(x = self.width*(35/200), y = self.height*(3/200))
        self.parameter_button.place(x = self.width*(70/200), y = self.height*(3/200))


    #-------------------- création des fonctions --------------------    


    def openParameters(self):
        if self.settings == None :
            self.settings = AppEditing(self.parameters)
            self.parameters = self.settings.get()
            self.settings = None
            self.getSettings()
            self.clear('all')
        else :
            print("fenêtre de paramètres déjà ouverte")
            self.settings.focus()


    def getSettings(self):
        with open("window_parameters.json", "r") as file :
            self.parameters = json.load(file)
        file.close()
        self.width = self.parameters["width"]
        self.height = self.parameters["height"]
        ct.set_default_color_theme(self.parameters["color"])
        ct.set_appearance_mode(self.parameters["theme"])
        
        self.geometry(f"{str(self.width)}x{str(self.height)}")
        self.minsize(self.width, self.height)


    def clear(self, mod):
        if mod == 'all' :
            liste = self.grid_slaves() + self.pack_slaves()
            print(liste)
            for element in liste :
                element.destroy()
            self.createInterface()
        if mod == 'itemFrame' :
            liste = self.main_item_frame.grid_slaves()
            for element in liste :
                element.destroy()


    def fileLoading(self):
        pass


    def sideWidgetsUptdating(self):
        self.clear('itemFrame')
        
        self.add_button = ct.CTkButton(self.main_item_frame, width= self.width*(18/100), height= self.height*(6/100), text = "ajouter", 
                                       font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command= lambda : self.widgetAdding())
        tl.CreateToolTip(self.add_button, text = "Bouton d'ajout de widgets dans le projet.")
        self.add_button.grid(padx = 5, pady = 5)

        for widgets in self.widgets_list :
            w_bt = ct.CTkButton(self.main_item_frame, text = widgets, width= self.width*(18/100), height= self.height*(6/100), 
                                font=ct.CTkFont(size=15, weight="bold"), corner_radius= 10, command = lambda w_id : self.widgetParametersFrame(w_id))
            w_bt.grid(padx = 5, pady = 5)


    def widgetAdding(self):
        if self.widgetapp == None :
            self.widgetapp = WidgetApp()
            self.widgets_list.append(self.widgetapp.get())
            self.widgetapp = None
            self.sideWidgetsUptdating()
        else :
            print("fenêtre d'ajout d'un widget déjà ouverte")
            self.widgetapp.focus()

        
    def widgetParametersFrame(self):
        pass


    def previewFrame(self):
        pass


    def openProjectApp(self):
        self.project_app = ProjectApp()

        

if __name__ == "__main__":
    app = interface()
    app.mainloop()
        
    