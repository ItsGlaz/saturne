#programme d'ajout de widget, permet de gagner du temps
from typing import Optional, Tuple, Union
import customtkinter as ct
import json 


class AddWidgetTool(ct.CTk):

    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        with open("WidgetRss.json", "r",) as file :
            self.validparameters = json.load(file)
            file.close()
        self.entries = [] 

        self.upper_frame = ct.CTkFrame(self)
        self.lower_frame = ct.CTkFrame(self) 

        self.upper_frame.grid(row =0, column = 0)    
        self.lower_frame.grid(row = 1, column = 0)  
        
        self.framecreation()


    def framecreation(self):
        self.entry_name = ct.CTkEntry(self.upper_frame, width=200)
        self.entry_name.insert(0, 'nom du widget')
        self.entry_id = ct.CTkEntry(self.upper_frame, width=200)
        self.entry_id.insert(0, 'id du widget')
        self.entry_name.grid(row = 0, column =0)
        self.entry_id.grid (row = 0, column = 1)
        
        
        row =0
        column =0
        for parameters in self.validparameters[1].keys():
        
            check = ct.CTkCheckBox(self.lower_frame, text = parameters)
            self.entries.append(check)

            check.grid(row = row, column = column, padx= 5, pady = 5)
            
            column = column + 1 if column < 5 else 0
            row += 1 if column == 0 else 0



    def addWidgetParameter(self):
        for entries in self.entries :
            pass


if __name__ == "__main__" :
    app = AddWidgetTool()
    app.mainloop()