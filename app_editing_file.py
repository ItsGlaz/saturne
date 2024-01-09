#fichier pour l'interface de paramètres
from typing import Optional, Tuple, Union
import customtkinter as ct 

class AppEditing(ct.CTk):

    def __init__(self, parameters : dict ):
        super().__init__()

        self.main_frame = ct.CTkFrame()

