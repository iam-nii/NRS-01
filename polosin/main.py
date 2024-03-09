import customtkinter as c
import tkinter
from utilities import User,Database,EncDecPass
from CTkMenuBar import *

width = 1028
height = 800

def file_click():
    print("file")

def change_user():
    print("change user")

def help():
    print("Help")


root = c.CTk()
root.geometry(f"{width}x{height}")
root.configure(title='Main window',fg_color='#232E33', padx=0)

menu = CTkMenuBar(master=root)

file = menu.add_cascade("File")
file.configure(command=file_click)

change_user = menu.add_cascade("Change user")
change_user.configure(command=change_user)

help = menu.add_cascade("Help")
help.configure(command=help)

root.mainloop()