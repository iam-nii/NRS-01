import math
import tkinter as tk

import customtkinter as c
import numpy
import polosin.windows.Login as Login
from polosin.public.Database_root import Database
from polosin.windows.Params.geometric_values import Geometric
from polosin.windows.Params.materials_values import Material_values
from polosin.windows.Params.math_model_values import Math_model_values
from polosin.windows.Params.process_params import Process_values

database = Database(window='User')

# Create a font object
FONT = ("MS Serif", 20)
ENTRY_FONT = ("Arial", 18)


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

        self.parameters: [dict] = []

        # Params tab
        # ------------------------Geometric values-------------------------------------#
        self.geometric_values = Geometric(params)


        # ---------------------------Materials-----------------------------------#
        self.material_values = Material_values(params)


        # ---------------------------Process Parameters-----------------------------------#
        self.process_values = Process_values(params)


        # ----------------------------------------Math Model------------------------------------#
        self.math_model_values = Math_model_values(params)


        calculate = c.CTkButton(master=params, text='Расчёт', fg_color='#214569', command=self.calculate)
        calculate.grid(row=2, column=1, padx=5, pady=10, sticky=tk.E)

        self.warning = c.CTkLabel(master=params, text='Invalid inputs, all fields must be floating numbers',
                                  anchor='w', text_color='red')

    def calculate(self):
        # Get the data from the entries

        # Geometry
        self.geometric_dict = self.geometric_values.get_values()
        self.parameters.append(self.geometric_dict)
        print(self.geometric_dict)


        # Materials
        self.materials_dict = self.material_values.get_values()
        self.parameters.append(self.materials_dict)
        print(self.materials_dict)

        # Process parameters
        self.process_values_dict = self.process_values.get_values()
        self.parameters.append(self.process_values_dict)
        print(self.process_values_dict)


        # Math model
        self.math_model_dict = self.math_model_values.get_values()
        self.parameters.append(self.materials_dict)
        print(self.math_model_dict)

        # Check for valid data
        for model in self.parameters:
            for key, value in model.items():
                try:
                    float(value)
                except:
                    self.warning.grid(row=2, column=0, sticky=tk.W, pady=10, padx=5)
                else:
                    self.warning.grid_forget()

        # Process the data received
        H = float(self.geometric_dict['depth'])
        W = float(self.geometric_dict['width'])
        L = float(self.geometric_dict['length'])
        p = float(self.materials_dict['density'])
        c = float(self.materials_dict['heat_capacity'])
        Uo = float(self.math_model_dict['consistency_coefficient'])
        n = float(self.math_model_dict['flow_index'])  # flow index
        Vu = float(self.process_values_dict['cover_speed'])
        au = float(self.math_model_dict['heat_transfer'])
        b = float(self.math_model_dict['temp_viscosity_coeff'])
        Tu = float(self.process_values_dict['cover_temperature'])
        Tr = float(self.math_model_dict['casting_temp'])
        To = float(self.materials_dict['melting_temperature'])
        step = float(self.process_values_dict['step'])

        shear_rate = Vu / H

        q_shear_rate = H * W * Uo * (shear_rate ** (n + 1))

        q_a = W * au * ((b ** -1) - Tu + Tr)

        F = 0.125 * ((H / W) ** 2) - 0.625 * (H / W) + 1

        Qch = ((H * W * Vu) / 2) * F

        T = [
            round(Tr + 1 / b * (math.log(
                (((b * q_shear_rate) + (W * au)) / (b * q_a)) *
                (1 - math.exp(-(b * q_a) * z / (p * c * Qch))) + (
                    math.exp(b * (To - Tr - z * (q_a / (p * c * Qch))))
                ))),4)
            for z in numpy.arange(0, L, step)
        ]
        print(T)

        # material_temperature = float(self.math_model_dict['casting_temp']) + 1/
        viscosity = [
            round(Uo * math.exp(-b * (temp - Tr)) * (shear_rate ** (n - 1)),4)
            for temp in T
        ]
        print(viscosity)

        # Channel output
        Q = p * Qch
        print(f'Channel output: {round(Q,2)}')

        # Product Temperature and viscosity
        Tp = T[-1]
        print(f'product temperature: {round(Tp,2)}')

        # Generate the table

        return

    def change_user_click(self):
        self.destroy()
        login = Login.Login()
        login.mainloop()

    def help_click(self):
        print('help')


win = UserWin()
win.mainloop()
