from typing import Optional, Tuple, Union
import customtkinter as ct

class ProjectApp(ct.CTkToplevel):

    def __init__(self):
        super().__init__()


        self.geometry("480x300")
        self.main_frame = ct.CTkFrame(self)
        self.side_frame = ct.CTkScrollableFrame(self.main_frame)
        self.work_frame = ct.CTkFrame(self.main_frame)

        self.main_frame.grid()
        self.side_frame.grid(row = 0, column =0)
        self.work_frame.grid(row =0, column = 1)


        self.add_button = ct.CTkButton(self.side_frame, text = 'ajouter un projet', width = 160, height = 30)
        self.add_button.grid(row = 0, column = 0, padx = 10, pady = 5)

