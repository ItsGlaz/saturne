from typing import Optional, Tuple, Union
import customtkinter as ct
from tkinter import messagebox
import json
import intermediateLayer as interl

class ProjectApp(ct.CTkToplevel):

    def __init__(self, mod = None):
        super().__init__()

        self.newprojectname = None
        self.main_frame = ct.CTkFrame(self)
        self.side_frame = ct.CTkScrollableFrame(self.main_frame, height = 300, width = 180)
        self.work_frame = ct.CTkFrame(self.main_frame, height = 300, width=600)

        self.main_frame.grid()
        self.side_frame.grid(row = 0, column =0)
        self.work_frame.grid(row =0, column = 1)
        self.actual_prjt = None
        
        self.sideFrameUpdating()
        self.workFrameCreation()


    def workFrameCreation(self):
        self.clear("workFrame")
        
        self.project_label = ct.CTkLabel(self.work_frame, text = "Créer un nouveau projet", width=600)
        self.entry = ct.CTkEntry(self.work_frame, width=200)
        self.content_valid_bt = ct.CTkButton(self.work_frame, text = "valider", height = 30, width=200, command = lambda : self.addProject())

        self.project_label.grid(row = 0, column = 0, pady = 15)
        self.entry.grid(row = 1, column = 0, pady = 15)
        self.content_valid_bt.grid(row =2, column = 0, pady = 15)


    def modifyFrame(self, project):
        self.clear("workFrame")

        self.actual_prjt = project
        dico = self.loadPrjctInfo()


        #-------------------- création des frames -------------------- 


        self.upper_frame = ct.CTkFrame(self.work_frame)
        self.lower_frame = ct.CTkFrame(self.work_frame)

        self.upper_frame.grid(row = 0, column = 0)
        self.lower_frame.grid(row =1, column = 0)


        #-------------------- création des labels -------------------- 


        self.inter_name_lbl = ct.CTkLabel(self.upper_frame, text = "nom de l'interface :", width = 180)
        self.inter_height_lbl = ct.CTkLabel(self.upper_frame, text = "hauteur :", width = 90)
        self.inter_width_lbl = ct.CTkLabel(self.upper_frame, text = "largeur :", width = 90)

        self.inter_name_lbl.grid(row = 0, column =0, padx = 10, pady = 10)
        self.inter_height_lbl.grid(row = 0, column =1, padx = 5, pady = 10)
        self.inter_width_lbl.grid(row = 1, column =1, padx = 5, pady = 10)


        #-------------------- création des entrées -------------------- 


        self.interface_name = ct.CTkEntry(self.upper_frame, width = 180)
        self.interface_name.insert(0, dico['Name'] if dico != None else "")

        self.interface_height = ct.CTkEntry(self.upper_frame, width=90)
        self.interface_height.insert(0, dico["height"] if dico != None else "")

        self.interface_width = ct.CTkEntry(self.upper_frame, width=90)
        self.interface_width.insert(0, dico["width"] if dico != None else "")


        self.interface_name.grid(row = 1, column = 0, padx = 10)
        self.interface_height.grid(row = 0, column =2, padx = 5)
        self.interface_width.grid(row = 1, column =2, padx = 5, pady = 10)


        #-------------------- création des boutons -------------------- 


        self.del_bt = ct.CTkButton(self.lower_frame, text = "supprimer", height = 30, width=130, command = lambda : self.delProject(project))
        self.modify_bt = ct.CTkButton(self.lower_frame, text = "modifier", height = 30, width=130, command = lambda :self.modifyInfo())
        self.open_bt = ct.CTkButton(self.lower_frame, text = "ouvrir", height = 30, width=130, command = lambda : self.destroy())

        self.del_bt.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.modify_bt.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.open_bt.grid(row = 0, column = 2, padx = 10, pady = 10)


    def loadPrjctInfo(self):
        dico =  interl.getPrjtSetRqst(self.actual_prjt)
        print(dico)
        return dico
            

    def modifyInfo(self):
        
        dico = {}
        try :
            dico["Name"]        = self.interface_name.get()
            dico["height"]      = int(self.interface_height.get())
            dico["width"]       = int(self.interface_width.get())
            interl.modidyPrjctRqst(self.actual_prjt, dico)
        except :
            messagebox.showerror('entrées invalides', "données entrées ivalides")

    
    def openProjectInfo(self):
        with open("rssDir\prjctNameSave.txt", "r", encoding= 'utf8') as file :
            self.project_info = file.read().split(",")
        file.close()


    def sideFrameUpdating(self):
        self.openProjectInfo()
        self.clear("sideFrame")
        self.add_button = ct.CTkButton(self.side_frame, text = 'ajouter un projet', width = 160, height = 30, command = lambda : self.workFrameCreation())
        self.add_button.grid(padx = 10, pady = 5)

        for projects in self.project_info:
            if projects != "":
                bt = ct.CTkButton(self.side_frame, text = projects, width = 160, height = 30, command = lambda : self.modifyFrame(projects))
                bt.grid(padx = 10, pady = 5)


    def addProject(self):
        self.newprojectname = self.entry.get()
        self.project_info.append(self.newprojectname)
        converted_info = ",".join(self.project_info)

        
        with open("rssDir\prjctNameSave.txt", "w", encoding= 'utf8') as file :
            file.write(converted_info)
        file.close()
        
        if self.newprojectname != None and type(self.newprojectname) == str :
            interl.newPrjctRqst(self.newprojectname)
        
        self.clear("sideFrame")
        self.clear("workFrame")
        self.sideFrameUpdating()
        self.modifyFrame(self.newprojectname)


    def delProject(self, project):
        try : 
            if type(project) == str :
                interl.rmproject(project)
            del self.project_info[self.project_info.index(project)]
            converted_info = ",".join(self.project_info)
            with open("rssDir\prjctNameSave.txt", "w", encoding= 'utf8') as file :
                file.write(converted_info)
            file.close()
            
            self.clear("workFrame")
            self.clear("sideFrame")
            self.sideFrameUpdating()
        except :
            messagebox.showerror("Suppression impossible", "Une erreur est survenue lors de la suppresion du projet.")


    def clear(self, choice):
        if choice == "sideFrame":
            liste = self.side_frame.grid_slaves()
        if choice =='workFrame':
            liste = self.work_frame.grid_slaves()
        for widgets in liste :
            widgets.destroy()
    

    def closed(self):
        self.master.wait_window(self)
        return self.actual_prjt
        

if __name__ == "__main__" :
    testapp = ProjectApp()
    testapp.mainloop()