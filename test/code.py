import customtkinter

window = customtkinter.CTk()









optionmenu1 = customtkinter.CTkOptionMenu(window, values = ["value1","value2"], command = lambda : commande(parametre))
optionmenu1.grid(sticky = 'W' )

label1 = customtkinter.CTkLabel(window, text = "entrez \'", image = 0, wraplength = 0)
label1.grid(sticky = 'W' )


