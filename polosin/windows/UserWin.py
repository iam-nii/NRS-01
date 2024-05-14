import math
from polosin.public.Save_to_excel import Save_to_excel
import tkinter as tk
from polosin.public.results import Results
import customtkinter as c
import numpy
import polosin.windows.Login as Login
from polosin.public.Database_root import Database
from polosin.windows.Params.geometric_values import Geometric
from polosin.windows.Params.materials_values import Material_values
from polosin.windows.Params.math_model_values import Math_model_values
from polosin.windows.Params.process_params import Process_values
from polosin.windows.Params.solution_method_params import Solution_method_values
import psutil
import time
import os
import asyncio


# database = Database()

# Import the materials from the database

# print(materials_list)

# Create a font object
FONT = ("MS Serif", 20)
ENTRY_FONT = ("Arial", 18)

DATA = {
    'density': '',
    'heat_capacity':'',
    'melting_temperature':'',
    'cover_speed':'1.5',
    'cover_temperature':'180',
    'width':'0.2',
    'depth':'0.003',
    'length':'7.5',
    'consistency_coefficient':'1500',
    'temp_viscosity_coefficient':'0.015',
    'casting_temperature':'185',
    'flow_index':'0.38',
    'cover_heat_transfer_coefficient':'1500',
    "step": '0.1',
    "material": ''
}
data_report = {
    "Производительность": '',
    "Температура продукта": '',
    "Вязкость продукта": '',
    "Память": '',
    "Время рассчета":"",
    "Количество операций": '',
}

class UserWin(c.CTk):
    def __init__(self,database):
        super().__init__()
        self.database = database
        # Geometry and window config
        self.main_width = 1028
        self.main_height = 820
        self.title('Окно исследователя')
        self.geometry(f"{self.main_width}x{self.main_height}")
        self.configure(fg_color='#F5F5F5', padx=0)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(2, weight=1)
        self.coordinates = []
        self.T = []
        self.viscosity = []

        self.materials_list = [
            {
                'id':material.id,
                'material':str(material.material),
                'density':material.density,
                'heat_capacity':material.heat_capacity,
                'melting_temperature':material.melting_temperature,
            }
            for material in self.database.get_materials()[0]
        ]




        # Create the menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Create the file menu
        filemenu = tk.Menu(menubar, tearoff=0)

        # Add menu items to the file menu
        filemenu.add_command(label="Сменить пользователя", command=self.change_user_click, font=('Arial', 20, 'normal'))
        filemenu.add_command(label="Сохранить данные", command=self.save_data_click, font=('Arial', 20, 'normal'))
        filemenu.add_command(label="Справка", command=self.help_click, font=('Arial', 20, 'normal'))
        filemenu.add_separator()
        filemenu.add_command(label="Выход", command=self.quit, font=('Arial', 20, 'normal'))

        # Add the file menu to the menu bar
        menubar.add_cascade(label="Меню", menu=filemenu, font=('Arial', 20, 'normal'))



        # Creating the tabs
        TABS = c.CTkTabview(
            master=self,
            segmented_button_selected_color='grey',
            width=900,
            height=700,
            fg_color='white',
            text_color="black"
        )
        TABS.pack()
        self.params = TABS.add('Входные параметры')
        self.results = TABS.add('Результаты')
        self.graph = TABS.add('График')

        # Temperature and viscosity graph tabs
        self.temp_visco_tab =c.CTkTabview(
            master=self.graph,
            segmented_button_selected_color='grey',
            width=800,
            height=600,
            fg_color='white',
            text_color="black"
        )
        self.temp_visco_tab.pack()
        self.temp_tab = self.temp_visco_tab.add('Температура')
        self.visco_tab = self.temp_visco_tab.add('Вязкость')

        self.parameters: [dict] = []

        # Params tab
        # Materials combobox
        material_menu_list = [material['material'] for material in self.materials_list]
        materials = c.CTkOptionMenu(self.params, values=material_menu_list,
                                    command=self.print_materials)
        materials.set("Материалы")
        materials.grid(column=1, row=0, padx=5, pady=5, sticky="E")

        # ------------------------Geometric values-------------------------------------#
        self.geometric_values = Geometric(self.params, DATA)
        self.divider = c.CTkFrame(self.params, fg_color="white")
        self.divider.grid(row=2, column=0, padx=5, pady=10)
        # ---------------------------Process Parameters-----------------------------------#
        self.process_values = Process_values(self.divider, DATA)
        # ---------------------------Solution method parameters-----------------------------------#
        self.solution_method_values = Solution_method_values(self.divider, DATA)
        # # Calculation step
        # self.calculation_step_frame = c.CTkFrame(master=self.divider, fg_color='#070809')
        # self.calculation_step_frame.grid(row=1, column=0, sticky=tk.W, pady=10, padx=5)
        # # Label
        # self.calculation_step_label = c.CTkLabel(master=self.calculation_step_frame,
        #                                          text='Шаг расчёта по длине канала  : ',
        #                                          text_color='#D6D7D8',
        #                                          font=FONT, justify='right', width=250, anchor='e')
        # self.calculation_step_label.grid(row=0, column=0, padx=5, sticky='e')
        # # Entry
        # self.calculation_step_entry = c.CTkEntry(master=self.calculation_step_frame, fg_color='#1F2022',
        #                                          font=ENTRY_FONT,
        #                                          # validate="key",
        #                                          # validatecommand=(params.register(validate_float), "%S"),
        #                                          text_color='#D6D7D8', width=60)
        # self.calculation_step_entry.grid(row=0, column=1, padx=5)

        # ----------------------------------------Math Model------------------------------------#
        self.math_model_values = Math_model_values(self.params, DATA)


        calculate = c.CTkButton(master=self.params, text='Расчёт', fg_color='#214569', command=self.run_calculate)
        calculate.grid(column=1, row=3, padx=5, pady=5, sticky="E")

        # self.message = c.CTkLabel(master=self.params, text='Invalid inputs, all fields must be floating numbers',
        #                           anchor='w', text_color='red')
        self.message = c.CTkLabel(master=self.params, anchor='w',text=' ')
        self.message.grid(row=3, column=0, sticky=tk.W, pady=10, padx=5)

    def run_calculate(self):
        asyncio.run(self.calculate())

    def print_materials(self, choice):
        id = 0
        for material in self.materials_list:
            if material['material'] == choice:
                DATA['material'] = choice
                id = material['id']
                # Material parameters
                DATA['density'] = material['density']
                DATA['heat_capacity'] = material['heat_capacity']
                DATA['melting_temperature'] = material['melting_temperature']

        # Process parameters
        # process_params = self.database.get_process_params(id)[0]
        # DATA['cover_speed'] = process_params.cover_speed,
        # DATA['cover_temperature'] = process_params.cover_temperature

        # Chanel parameters
        # chanel_params = database.get_chanel_params(id)[0]
        # DATA['width'] = chanel_params.width
        # DATA['depth'] = chanel_params.depth
        # DATA['length'] = chanel_params.length

        # Math Model parameters
        # math_model_params = self.database.get_math_module(id)[0]
        # DATA['consistency_coefficient'] = math_model_params.consistency_coefficient
        # DATA['temp_viscosity_coefficient'] = math_model_params.temp_viscosity_coefficient
        # DATA['casting_temperature'] = math_model_params.casting_temperature
        # DATA['flow_index'] = math_model_params.flow_index
        # DATA['cover_heat_transfer_coefficient'] = math_model_params.cover_heat_transfer_coefficient

        print(DATA)



        # ---------------------------Materials-----------------------------------#
        self.material_values = Material_values(self.params, DATA)




    async def calculate(self):
        # Get the data from the entries

        # self.table_result = None
        # self.temp_graph_result = None
        # self.viscosity_graph_result = None
        # gc.collect()

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

        # Solution method params
        self.solution_method_values_dict = self.solution_method_values.get_values()
        self.parameters.append(self.solution_method_values_dict)
        print(self.solution_method_values_dict)



        # Math model
        self.math_model_dict = self.math_model_values.get_values()
        self.parameters.append(self.materials_dict)
        print(self.math_model_dict)

        # # Check for valid data
        # for model in self.parameters:
        #     for key, value in model.items():
        #         try:
        #             float(value)
        #         except Exception as e:
        #             self.message.configure(text='Invalid inputs, all fields must be floating numbers',text_color='red')
        #         else:
        #             self.message.configure(text='Success',text_color='green')


        # Process the data received
        try:
            params = []
            H = float(self.geometric_dict['depth'])
            params.append(H)
            W = float(self.geometric_dict['width'])
            params.append(W)
            L = float(self.geometric_dict['length'])
            params.append(L)
            p = float(self.materials_dict['density'])
            params.append(p)
            c = float(self.materials_dict['heat_capacity'])
            params.append(c)
            Uo = float(self.math_model_dict['consistency_coefficient'])
            params.append(Uo)
            n = float(self.math_model_dict['flow_index'])  # flow index
            params.append(n)
            Vu = float(self.process_values_dict['cover_speed'])
            params.append(Vu)
            au = float(self.math_model_dict['heat_transfer'])
            params.append(au)
            b = float(self.math_model_dict['temp_viscosity_coeff'])
            params.append(b)
            Tu = float(self.process_values_dict['cover_temperature'])
            params.append(Tu)
            Tr = float(self.math_model_dict['casting_temp'])
            params.append(Tr)
            To = float(self.materials_dict['melting_temperature'])
            params.append(To)
            step = float(self.solution_method_values_dict['step'])

            if step == 0.01:
                step = round(step, 2)

            if step < 0.1 and step >= 0.009:
                step = round(step, 2)

            params.append(step)

            for param in params:
                if param == 0:
                    raise Exception("Input cannot be 0")

        except Exception as e:
            print(e)
            self.message.configure(text='Invalid inputs, all fields must be filled, floating numbers and not 0', text_color='red')
        else:
            self.message.configure(text='Success', text_color='green')
            start = time.time()
            shear_rate = Vu / H
            count = 1

            q_shear_rate = H * W * Uo * (shear_rate ** (n + 1))
            count+=5

            q_a = W * au * ((b ** -1) - Tu + Tr)
            count+=5

            F = 0.125 * ((H / W) ** 2) - 0.625 * (H / W) + 1
            count+=7

            Qch = ((H * W * Vu) / 2) * F
            count+=4



            # self.T = [
            #     round(Tr + 1 / b * (math.log(
            #         (((b * q_shear_rate) + (W * au)) / (b * q_a)) *
            #         (1 - math.exp(-(b * q_a) * z / (p * c * Qch))) + (
            #             math.exp(b * (To - Tr - z * (q_a / (p * c * Qch))))
            #         ))), 2)
            #     for z in numpy.arange(0, L + step, step)
            # ]
            self.T = []
            for z in numpy.arange(0, L + step, step):
                self.T.append(round(Tr + 1 / b * (math.log(
                    (((b * q_shear_rate) + (W * au)) / (b * q_a)) *
                    (1 - math.exp(-(b * q_a) * z / (p * c * Qch))) + (
                        math.exp(b * (To - Tr - z * (q_a / (p * c * Qch))))
                    ))), 2))
                count += 27

            print(self.T)

            # material_temperature = float(self.math_model_dict['casting_temp']) + 1/
            # self.viscosity = [
            #     round(Uo * math.exp(-b * (temp - Tr)) * (shear_rate ** (n - 1)), 2)
            #     for temp in self.T
            # ]
            self.viscosity = []
            for temp in self.T:
                self.viscosity.append(round(Uo * math.exp(-b * (temp - Tr)) * (shear_rate ** (n - 1)), 2))
                count+=7

            print(self.viscosity)

            # Channel output
            Q = p * Qch * 3600
            count+=3
            print(f'Производительность: {round(Q, 2)}')

            # Product Temperature and viscosity
            Tp = self.T[-1]
            print(f'Температура продукта: {round(Tp, 2)}')

            Viscosity_p = self.viscosity[-1]
            print(f'Вязкость продукта: {round(Viscosity_p, 2)}')

            end = time.time()
            calc_time = (end - start) * 1000
            memory_usage = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2

            data_report["Производительность"] = Q
            data_report["Температура продукта"] = Tp
            data_report["Вязкость продукта"] = Viscosity_p
            data_report["Память"] = memory_usage
            data_report["Время рассчета"] = calc_time
            data_report["Количество операций"] = count


            # Generate the table and graphs
            self.coordinates = [round(n * step, 1) for n in range(len(self.T))]
            self.table_result = Results(self.results)
            # process = psutil.Process(os.getpid())

            prod_temp_visc = [
                f'Производительность : {round(Q, 2)} [кг/ч]\n',
                f'Температура продукта: {round(Tp, 2)} [°C]\n',
                f'Вязкость продукта: {round(Viscosity_p, 2)} [Па*с]\n',
                f'Память: {round(memory_usage,2)} [Мбайт]\n ',
                f'Время рассчета: {round(calc_time,4)} [мc]\n',
                f'Количество операций: {count}'
            ]
            # table_result.create_result_table(self.T, self.viscosity, self.coordinates, prod_temp_visc)

            # def create_result_graph(self, frame, prop: list, coordinates: list, title: str):

            # temp_graph_result = Results(self.results)
            #
            # temp_graph = temp_graph_result.create_result_graph(frame=self.temp_tab, prop=self.T, title_main='температуры, °C',
            #                                         title_y='Температура, °C',
            #                                         coordinates=self.coordinates)
            # viscosity_graph_result = Results(self.results)
            # viscosity_graph = viscosity_graph_result.create_result_graph(frame=self.visco_tab, prop=self.viscosity,
            #                                              title_main='вязкости, Па*с',title_y='Вязкость, Па*с',
            #                                              coordinates=self.coordinates)


            # update the table with the new data


            self.table_result.create_result_table(self.T, self.viscosity, self.coordinates, prod_temp_visc)

            # update the temperature graph with the new data
            self.temp_graph_result = Results(self.results)
            self.temp_graph_result.create_result_graph(frame=self.temp_tab, prop=self.T, title_main='температуры, °C',
                                                  title_y='Температура, °C',
                                                  coordinates=self.coordinates)

            # update the viscosity graph with the new data
            self.viscosity_graph_result = Results(self.results)
            self.viscosity_graph_result.create_result_graph(frame=self.visco_tab, prop=self.viscosity,
                                                       title_main='вязкости, Па*с', title_y='Вязкость, Па*с',
                                                       coordinates=self.coordinates)


            return

    def save_data_click(self):
        # Top level window
        self.save_to_file_window = c.CTkToplevel(self, fg_color="#F5F5F5")
        self.save_to_file_window.geometry('400x250')
        self.save_to_file_window.title(' Сохранить в Excel')
        self.save_to_file_window.resizable(False, False)
        self.save_to_file_window.attributes('-topmost', 'true')

        # Filename
        self.filename = c.CTkEntry(master=self.save_to_file_window, placeholder_text='Имя файла', width=200)

        # Save button
        self.save_button = c.CTkButton(master=self.save_to_file_window, text='СОХРАНИТЬ', fg_color='#6CD63C',
                                          command=self.on_save_click)

        # Pack elements
        self.filename.pack(pady=10)
        self.save_button.pack(pady=10)

    def on_save_click(self):
        # Save Temperature
        save = Save_to_excel(list1=self.coordinates, list2=self.T, list3=self.viscosity, file_name=self.filename.get(),
                             DATA=DATA, prod_temp_visc=data_report)


    def change_user_click(self):
        self.destroy()
        login = Login.Login(self.database)
        login.mainloop()

    def help_click(self):
        print('help')


# win = UserWin()
# win.mainloop()
