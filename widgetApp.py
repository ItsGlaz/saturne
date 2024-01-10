#fichier contenant les widgets à créer
from typing import Optional, Tuple, Union
import customtkinter as ct

class WidgetApp(ct.CTkToplevel):

    def __init__(self):
        super().__init__()

        self.choice = None

        self.main_frame = ct.CTkScrollableFrame(self, width=360, height = 150)
        self.main_frame.grid()

        self.frame_button = ct.CTkButton(self.main_frame, text = "Frame", font=ct.CTkFont(size=15, weight="bold"), width=160,height = 40, command = lambda x="Frame" : self.choiceDone(x))
        self.label_button = ct.CTkButton(self.main_frame, text = "Label", font=ct.CTkFont(size=15, weight="bold"), width=160, height = 40, command = lambda x="Label" : self.choiceDone(x))
        self.entry_button = ct.CTkButton(self.main_frame, text = "Entrée", font=ct.CTkFont(size=15, weight="bold"), width=160, height = 40, command = lambda x="Entry" : self.choiceDone(x))
        self.button_button = ct.CTkButton(self.main_frame, text = "Bouton", font=ct.CTkFont(size=15, weight="bold"), width=160, height = 40, command = lambda x="Button" : self.choiceDone(x))
        self.checkbox_button = ct.CTkButton(self.main_frame, text = "Case à cocher", font=ct.CTkFont(size=15, weight="bold"), width=160, height = 40, command = lambda x="Checkbox" : self.choiceDone(x))
        self.list_button = ct.CTkButton(self.main_frame, text = "Liste", font=ct.CTkFont(size=15, weight="bold"), width=160, height = 40, command = lambda x="Listbox" : self.choiceDone(x))

        self.frame_button.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.label_button.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.entry_button.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.button_button.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.checkbox_button.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.list_button.grid(row = 2, column = 1, padx = 10, pady = 10)
        


    def choiceDone(self, choice):
        self.choice = choice
        self.destroy()


    def get(self):
        self.master.wait_window(self)
        return self.choice


