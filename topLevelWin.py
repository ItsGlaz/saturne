from typing import Tuple
import customtkinter as ct
from copy import deepcopy

class TextTopLevelWin(ct.CTkToplevel):

    def __init__(self, *args, text : str = "", fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)

        self.choice = ""

        self.label = ct.CTkLabel(self, text = "Texte :", font= ct.CTkFont(family = "arial", size=25, weight="bold"))
        self.text_input = ct.CTkEntry(self, height= 30, width=250, font= ct.CTkFont(family = "arial", size=12, weight="bold"))
        self.text_input.insert(0, text)
        self.validate_bt = ct.CTkButton(self, text = "Valider", font= ct.CTkFont(family = "arial", size=15, weight="bold"), width= 100, command = lambda : self.contentValidation())
        self.cancel_bt = ct.CTkButton(self, text = "Annuler", font= ct.CTkFont(family = "arial", size=15, weight="bold"), width= 100, command = lambda : self.on_quit())


        self.label.grid(row = 0, column =0, columnspan = 2, padx = 10, pady = 10, sticky = "w")
        self.text_input.grid(row = 1, column =0, columnspan = 2, padx = 10, pady = 10)
        self.validate_bt.grid(row = 2, column =0, padx = 10, pady = 10)
        self.cancel_bt.grid(row = 2, column =1, padx = 10, pady = 10)


    def on_quit(self):
        self.destroy()


    def contentValidation(self):
        self.choice = self.text_input.get()
        self.destroy()
        

    def contentGet(self):
        self.wait_window()
        return self.choice


class ValuesTopLevelWin(ct.CTkToplevel):

    def __init__(self, values : list = [], *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)

        self.values = deepcopy(values)
        self.return_values = []
        self.entries = []
        self.max_row =len(self.values) +1

        self.add_bt = ct.CTkButton(self, text = "Ajouter un widget", font= ct.CTkFont(family = "arial", size=15, weight="bold"), width= 200, command = lambda : self.addValue())
        self.add_bt.grid(column =0, row = 0, padx = 5, pady = 10, columnspan =2)

        self.validate_bt = ct.CTkButton(self, text = "Valider", font= ct.CTkFont(family = "arial", size=15, weight="bold"), width= 65, command = lambda : self.contentValidation())
        self.cancel_bt = ct.CTkButton(self, text = "Annuler", font= ct.CTkFont(family = "arial", size=15, weight="bold"), width= 65, command = lambda : self.on_quit())

        
        if len(self.values) > 1 :
            for i in range(len(self.values)):
                entry = ct.CTkEntry(self, height= 30, width=200, font= ct.CTkFont(family = "arial", size=15, weight="bold"))
                entry.insert(0, self.values[i])
                cross_bt = ct.CTkButton(self, text = "X", font= ct.CTkFont(family = "arial", size=15, weight="bold"), text_color="#FC2626", width= 20, 
                                        command= lambda x = i : self.delValue(x))
                self.entries.append((entry, cross_bt))
                entry.grid(column =0, row = i +1, padx = 5, pady = 5, columnspan =2)
                cross_bt.grid(column = 2, row = i + 1, padx = 5, pady = 5, sticky = "w")

        self.validate_bt.grid(row = self.max_row, column =0, padx = 5, pady = 5)
        self.cancel_bt.grid(row = self.max_row, column =1, padx = 5, pady = 5)


    def addValue(self):
        entry = ct.CTkEntry(self, height= 30, width=200, font= ct.CTkFont(family = "arial", size=15, weight="bold"))
        cross_bt = ct.CTkButton(self, text = "X", font= ct.CTkFont(family = "arial", size=15, weight="bold"), text_color="#FC2626", width= 20,
                                command= lambda x = self.max_row -1 : self.delValue(x))
        
        self.entries.append((entry, cross_bt))
        
        entry.grid(column =0, row = self.max_row, padx = 5, pady = 5, columnspan =2)
        cross_bt.grid(column = 2, row = self.max_row, padx = 5, pady = 5, sticky = "w")
        self.max_row += 1
        self.validate_bt.grid_configure(row = self.max_row)
        self.cancel_bt.grid_configure(row = self.max_row)

    
    def delValue(self, rank):
        self.entries[rank][0].destroy()
        self.entries[rank][1].destroy()
        del self.entries[rank]


    def on_quit(self):
        self.destroy()

 
    def contentValidation(self):
        for entry in self.entries :
            self.return_values.append(entry[0].get())
        self.destroy()


    def contentGet(self):
        self.wait_window()
        return self.return_values
    

if __name__ == "__main__":
    values = ["val1", "val2", "val3"]
    app = ValuesTopLevelWin(values = values)
    values = app.contentGet()
    print(values)

