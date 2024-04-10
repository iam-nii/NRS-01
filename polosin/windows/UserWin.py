import customtkinter as c
import tkinter as tk
from polosin.public.Database_root import Database
import polosin.windows.Login as Login
from polosin.public.databases import Chanel,Material,MathModel,ProcessParams
from polosin.windows.Params.geometric_values import Geometric
from polosin.windows.Params.materials_values import Material_values
from polosin.windows.Params.process_params import Process_values
from polosin.windows.Params.math_model_values import Math_model_values

database = Database(window='User')


# Create a font object
FONT = ("MS Serif",20)
ENTRY_FONT = ("Arial",18)
def print_materials(choice):
    print("Selected material:", choice)
class UserWin(c.CTk):
    def __init__(self):
        super().__init__()
        # Geometry and window config
        self.main_width = 1028
        self.main_height = 820
        self.title('Research window')
        self.geometry(f"{self.main_width}x{self.main_height}")
        self.configure(fg_color='#232E33', padx=0)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(2, weight=1)

        # Create the menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Create the file menu
        filemenu = tk.Menu(menubar, tearoff=0)

        # Add menu items to the file menu
        filemenu.add_command(label="Change User", command=self.change_user_click, font=('Arial', 20, 'normal'))
        filemenu.add_command(label="Help", command=self.help_click, font=('Arial', 20, 'normal'))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit, font=('Arial', 20, 'normal'))

        # Add the file menu to the menu bar
        menubar.add_cascade(label="Tools", menu=filemenu, font=('Arial', 20, 'normal'))

        # Import the materials from the database
        materials_list = [str(material.material) for material in database.get_materials()[0]]
        print(materials_list)

        materials = c.CTkOptionMenu(self, values=materials_list,
                                                 command=print_materials)
        materials.set("Materials")
        materials.pack(anchor='w')

        # Creating the tabs
        TABS = c.CTkTabview(
            master=self,
            segmented_button_selected_color='grey',
            width=900,
            height=700,
            fg_color='#070809'
        )
        TABS.pack()
        params = TABS.add('Входные параметры')
        results = TABS.add('Результаты')
        graph = TABS.add('График')


        self.parameters:[dict] = []

        # Params tab
        # ------------------------Geometric values-------------------------------------#
        geometric_values = Geometric(params)
        geometric_dict = geometric_values.get_values()
        self.parameters.append(geometric_dict)

        # ---------------------------Materials-----------------------------------#
        material_values = Material_values(params)
        materials_dict = material_values.get_values()
        self.parameters.append(materials_dict)

        # ---------------------------Process Parameters-----------------------------------#
        process_values = Process_values(params)
        process_values_dict = process_values.get_values()
        self.parameters.append(process_values_dict)

        # ----------------------------------------Math Model------------------------------------#
        math_model_values = Math_model_values(params)
        math_model_dict = math_model_values.get_values()
        self.parameters.append(materials_dict)

        calculate = c.CTkButton(master=params,text='Расчёт',fg_color='#214569',command=self.calculate)
        calculate.grid(row=2, column=1, padx=5, pady=10,sticky=tk.E)

        self.warning = c.CTkLabel(master=params,text='Invalid inputs, all fields must be floating numbers',
                                  anchor='w',text_color='red')



    def calculate(self):
        # Check for valid data
        for model in self.parameters:
            for key,value in model.items():
                try:
                    float(value)
                except:
                    self.warning.grid(row=2,column=0,sticky=tk.W,pady=10,padx=5)
                else:
                    self.warning.grid_forget()



        # Process the data received


        return
    def change_user_click(self):
        self.destroy()
        login = Login.Login()
        login.mainloop()

    def help_click(self):
        print('help')



win = UserWin()
win.mainloop()