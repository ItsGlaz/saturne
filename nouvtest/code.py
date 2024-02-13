from tkinter import *

window = Tk()

window.title("mini jeu")
window.geometry("720x144")
window.minsize(720, 144)
window.config(background='#37678D')

main_entry_frame = Frame(window, bg = '#37678D')
auxiliary_entry_frame = Frame(window, bg = '#37678D')
confirm_button_frame = Frame(window, bg = '#37678D')
main_entry_frame.pack(side = TOP)
auxiliary_entry_frame.pack(side= TOP)
confirm_button_frame.pack(side= TOP)

value_entry = StringVar()
value_entry.set("chercher un contact")
primary_entry = Entry(main_entry_frame, textvariable=value_entry, width= 80,font=("Arial", 15), bg = '#2F2F2F', fg = '#5494C6')
primary_entry.pack(side = BOTTOM, pady= 10, padx = 10 )

value_name = StringVar()
value_name.set("prénom et nom du contact")
name_entry = Entry(auxiliary_entry_frame, textvariable=value_name, width= 20,font=("Arial", 15), bg = '#2F2F2F', fg = '#5494C6')
name_entry.grid(row = 0, column= 0, pady= 10, padx = 10 )

value_age = StringVar()
value_age.set("âge")
age_entry = Entry(auxiliary_entry_frame, textvariable=value_age, width= 10,font=("Arial", 15), bg = '#2F2F2F', fg = '#5494C6')
age_entry.grid(row = 0, column= 1, pady= 10, padx = 10 )

value_tel = StringVar()
value_tel.set("numéro de télephone")
tel_entry = Entry(auxiliary_entry_frame, textvariable=value_tel, width= 20,font=("Arial", 15), bg = '#2F2F2F', fg = '#5494C6')
tel_entry.grid(row = 0, column= 2, pady= 10, padx = 10 )

confirm_button = Button(confirm_button_frame, text="valider",font=("Arial", 15), fg = '#5494C6', bg='#2F2F2F', bd=1, relief=SUNKEN, command=None)
confirm_button.pack(fill=X,pady=10)


window.mainloop()
