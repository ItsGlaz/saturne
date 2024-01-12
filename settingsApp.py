#fichier pour l'interface de paramètres
#ajouter le dimensionnement de l'intefaces ( via des dimensions pré-définies)
#ajouter l'apparition des tooltip ou non
#ajouter le niveau de détail des paramètres des widgets

from typing import Optional, Tuple, Union
from copy import deepcopy
import customtkinter as ct 
import json

class AppEditing(ct.CTkToplevel):

    def __init__(self, parameters : dict ):
        super().__init__()
        
        self.parameters = deepcopy(parameters)
        self.color = ct.StringVar()
        self.theme = ct.StringVar()
        self.theme_translation = {"eng-fra" : {"green" : "Vert", "dark-blue" : "Bleu foncé", "blue" : "Bleu", "system" : "Système", "dark" : "Sombre", "light" : "Clair"}, 
                                  "fra-eng" : {"Vert" : "green", "Bleu" : "blue", "Bleu foncé" : "dark-blue", "Système" : "system", "Sombre" : "dark", "Clair" : "light"}}
         
        self.main_frame = ct.CTkFrame(self)

        self.sub_main_frame = ct.CTkFrame(self.main_frame)
        self.bottom_frame = ct.CTkFrame(self.main_frame)

        self.main_frame.pack()
        self.sub_main_frame.grid(row = 1, column =0, pady = 10)
        self.bottom_frame.grid(row = 2, column = 0, pady = 5)


        self.general_label = ct.CTkLabel(self.main_frame, text = "Générals", font=ct.CTkFont(size=25, weight="bold"))
        self.color_theme_change_label = ct.CTkLabel(self.sub_main_frame, text = "Couleur", font=ct.CTkFont(size=15, weight="bold"))
        self.color_theme_change_option = ct.CTkOptionMenu(self.sub_main_frame, values = ["Bleu foncé", "Bleu", "Vert"], variable=self.color)
        self.color_theme_change_option.set(self.theme_translation["eng-fra"][self.parameters["color"]])

        self.theme_change_label = ct.CTkLabel(self.sub_main_frame, text = "Thème", font=ct.CTkFont(size=15, weight="bold"))
        self.theme_change_option = ct.CTkOptionMenu(self.sub_main_frame, values = ["Système", "Sombre", "Clair"], variable=self.theme)
        self.theme_change_option.set(self.theme_translation["eng-fra"][self.parameters["theme"]])

        
        self.general_label.grid(row = 0, column = 0, pady = 10, columnspan = 2, sticky="w")

        self.color_theme_change_label.grid(column =0, row = 0, pady =5, padx = 10)
        self.color_theme_change_option.grid(row = 0, column = 1, pady =5, padx = 10)

        self.theme_change_label.grid(row = 1, column = 0, pady = 5)
        self.theme_change_option.grid(row = 1, column = 1, pady = 5)

        self.apply_button = ct.CTkButton(self.bottom_frame, text = "confirmer", font=ct.CTkFont(size=15, weight="bold") , command = lambda : self.applySettings())
        self.return_button = ct.CTkButton(self.bottom_frame, text = "fermer", font=ct.CTkFont(size=15, weight="bold") , command = lambda : self.quitSettings())


        self.return_button.grid(row = 0, column = 0, padx = 10)
        self.apply_button.grid(row = 0, column =1)


    def quitSettings(self):
        self.destroy()


    def applySettings(self):
        self.parameters["color"] = self.theme_translation["fra-eng"][self.color.get()]
        self.parameters["theme"] = self.theme_translation["fra-eng"][self.theme.get()] 
        with open("window_parameters.json", "w") as file:
            json.dump(self.parameters, file)
        file.close()
        self.destroy()


    def get(self):
        self.master.wait_window(self)
        return self.parameters