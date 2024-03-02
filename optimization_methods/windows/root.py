import customtkinter as c
import tkinter

class App(c.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(6, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)




