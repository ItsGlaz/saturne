import customtkinter

window = customtkinter.CTk()









optionmenu1 = customtkinter.CTkOptionMenu(window, values = ["value1","value2"], command = lambda : commande(parametre))
optionmenu1.grid(sticky = 'W' )

