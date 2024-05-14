import customtkinter as c
from polosin.public.databases import User,Material,ProcessParams,MathModel


class App(c.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(7, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

ROLE = ''
# DATABASES = {
#     'users': User,
#     'chanel': Chanel,
#     'material': Material,
#     'math_model': MathModel,
#     'process_params': ProcessParams,
# }
# database = Database()

def clear_frames(tables:list[c.CTkFrame]):
    if len(tables) != 0:
        for frame in tables:
            frame.pack_forget()
    print(f'tables:{len(tables)}')

tables_list:list[c.CTkFrame] = []


def donothing():
    pass

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)








