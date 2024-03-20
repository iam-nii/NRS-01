import customtkinter as c
import tkinter
from utilities import User, Database, EncDecPass
from CTkMenuBar import *
from auth import Login

width = 1028
height = 800


def file_click():
    print("file")


def change_user_click():
    root.destroy()
    login = Login()
    login.mainloop()


def help_click():
    print("Help")


root = c.CTk()
root.geometry(f"{width}x{height}")
root.configure(title='Main window', fg_color='#232E33', padx=0)
root.rowconfigure(2, weight=1)
root.columnconfigure(2, weight=1)

menu_frame = c.CTkFrame(root, width=width, height=25)
menu_frame.grid(column=0, row=0, columnspan=3)

menu = CTkMenuBar(master=menu_frame)
menu.pack(fill=c.X)

file = menu.add_cascade("File")
file.configure(command=file_click)

change_user = menu.add_cascade("Change User")
change_user.configure(command=change_user_click)

help = menu.add_cascade("Help")
help.configure(command=help_click)

# Left
left_frame = c.CTkFrame(master=root, bg_color='white', fg_color='white', height=(height - 100))
left_frame.grid(row=1, column=1, pady=30, padx=30)

root.mainloop()
