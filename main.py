#fichier contenant l'interface graphique du programme
import customtkinter as ct
import json
import tool_tip as tl
import intermediateLayer

class interface(ct.CTk):

    def __init__(self) -> None:
        super().__init__()

        ct.set_default_color_theme("dark-blue")  #Themes: "blue" (standard), "green", "dark-blue"
        with open("window_parameters.json", "r") as file :
            parameters = json.load(file)

        self.width = parameters["width"]
        self.height = parameters["height"]
        ct.set_default_color_theme(parameters["theme"])

        self.geometry("1080x720")
        self.minsize(self.width, self.height)



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


        self.add_button = ct.CTkButton(self.main_item_frame,  width= self.width*(15/100), height= self.height*(6/100), text = "ajouter", font = ("arial", 15), corner_radius= 10, anchor = "center")
        tl.CreateToolTip(self.add_button, text = "Bouton d'ajout de widgets dans le projet.")

        self.parameter_button = ct.CTkButton(self.parameter_frame,  width= self.width*(10/100), height= self.height*(6/100), bg_color= 'transparent',
                                             text = "paramètres", font = ("arial", 15), corner_radius= 10)
        tl.CreateToolTip(self.parameter_button, text = "Bouton d'ouverture de la fenêtre de paramètres.")

        self.modify_button = ct.CTkButton(self.parameter_frame,  width= self.width*(10/100), height= self.height*(6/100), bg_color= 'transparent',
                                             text = "modifier", font = ("arial", 15), corner_radius= 10)
        tl.CreateToolTip(self.modify_button, text = "Bouton de modification des paramètres d'un widget.")

        self.delete_button = ct.CTkButton(self.parameter_frame,  width= self.width*(10/100), height= self.height*(6/100), bg_color= 'transparent',
                                             text = "supprimer", font = ("arial", 15), corner_radius= 10)
        tl.CreateToolTip(self.delete_button, text = "Bouton de suppression d'un widget.")

        
        
        self.add_button.grid(ipadx = 20)
        self.delete_button.place(x = self.width*(5/200), y = self.height*(3/200))
        self.modify_button.place(x = self.width*(35/200), y = self.height*(3/200))
        self.parameter_button.place(x = self.width*(70/200), y = self.height*(3/200))


    #-------------------- création des fonctions --------------------    


    def openParameters(self):
        pass


    def fileLoading(self):
        pass


    def sideWidgetsUptdating(self):
        pass


    def widgetAdding(self):
        pass

        
    def widgetParametersFrame(self):
        pass


    def previewFrame(self):
        pass
        

if __name__ == "__main__":
    app = interface()
    app.mainloop()
        
    