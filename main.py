#fichier contenant l'interface graphique du programme
import customtkinter as ct
import json
import tool_tip as tl

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



        #--------- création des frames --------------------
        
        
        self.show_frame = ct.CTkFrame(self, width=self.width*(50/100), height=self.height)
        self.edit_frame = ct.CTkFrame(self, width=self.width*(30/100), height=self.height)
        self.item_frame = ct.CTkFrame(self, width=self.width*(20/100), height=self.height)

        self.show_frame.grid(row = 0, column = 0)
        self.edit_frame.grid(row = 0, column = 1)
        self.item_frame.grid(row = 0, column = 2)


if __name__ == "__main__":
    app = interface()
    app.mainloop()
        
    