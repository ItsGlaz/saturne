from typing import Optional, Tuple, Union
import customtkinter as ct
import json

class ProjectApp(ct.CTkToplevel):

    def __init__(self):
        super().__init__()

        self.newprojectname = None

        self.geometry("480x300")
        self.main_frame = ct.CTkFrame(self)
        self.side_frame = ct.CTkScrollableFrame(self.main_frame, height = 300, width = 180)
        self.work_frame = ct.CTkFrame(self.main_frame, height = 300, width=300)

        self.main_frame.grid()
        self.side_frame.grid(row = 0, column =0)
        self.work_frame.grid(row =0, column = 1)

        self.sideFrameUpdating()


    def workFrameCreation(self):
        self.project_label = ct.CTkLabel(self.work_frame, text = "Créer un nouveau projet")
        self.entry = ct.CTkEntry(self.work_frame, width=200)
        self.content_valid_bt = ct.CTkButton(self.work_frame, text = "valider", height = 30, width=160, command = lambda : self.addProject())

        self.project_label.grid(row = 0, column = 0, pady = 15)
        self.entry.grid(row = 1, column = 0, pady = 15)
        self.content_valid_bt.grid(row =2, column = 0, pady = 15)

    
    def openProjectInfo(self):
        with open("projectInfoSave.json", "r") as file :
            self.project_info = json.load(file)
        file.close()


    def sideFrameUpdating(self):
        self.openProjectInfo()
        self.clear("sideFrame")
        self.add_button = ct.CTkButton(self.side_frame, text = 'ajouter un projet', width = 160, height = 30, command = lambda : self.workFrameCreation())
        self.add_button.grid(padx = 10, pady = 5)

        for projects in self.project_info.keys():
            bt = ct.CTkButton(self.side_frame, text = projects, width = 160, height = 30)
            bt.grid(padx = 10, pady = 5)


    def addProject(self):
        self.newprojectname = self.entry.get()
        self.project_info[self.newprojectname] = []
        with open("projectInfoSave.json", "w") as file :
            json.dump(self.project_info, file)
        file.close()
        self.clear("sideFrame")
        self.sideFrameUpdating()


    def clear(self, choice):
        if choice == "sideFrame":
            liste = self.side_frame.grid_slaves()
            for widgets in liste :
                widgets.destroy()

    
    def get(self):
        self.master.wait_window(self)
        return self.newprojectname