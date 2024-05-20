import traceback

import customtkinter as c
import tkinter as tk
from tkinter import filedialog
import polosin.windows.Login as Login
from polosin.public.Database_root import Database
from polosin.public.Tables import *
import polosin.public.PasswordGen as PasswordGen
from polosin.public.databases import User, Material, MathModel, ProcessParams
from polosin.public.Tables import *
from polosin.public.Encryption import EncDecPass

def donothing():
    pass

# self.database = Database()



# Main window
class Admin(c.CTk):
    def __init__(self,database):
        super().__init__()
        self.database = database
        # Geometry and window config
        self.main_width = 1028
        self.main_height = 800
        self.geometry(f"{self.main_width}x{self.main_height}")
        self.configure(title='Окно администратора', fg_color='#232E33', padx=0)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(2, weight=1)

        # Create the menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Create the file menu
        filemenu = tk.Menu(menubar, tearoff=0)

        # Add menu items to the file menu
        filemenu.add_command(label="Сменить пользователя", command=self.change_user_click, font=('Arial', 20, 'normal'))
        filemenu.add_command(label="Создать резервную копию", command=self.create_reserve_copy, font=('Arial', 20, 'normal'))
        filemenu.add_command(label="Восстановить базу данных", command=self.restore_database, font=('Arial', 20, 'normal'))
        filemenu.add_separator()
        filemenu.add_command(label="Выход", command=self.quit, font=('Arial', 20, 'normal'))

        # Add the file menu to the menu bar
        menubar.add_cascade(label="Меню", menu=filemenu, font=('Arial', 20, 'normal'))

        # Create the table selection menu
        tables_menu = tk.Menu(menubar,tearoff=0)

        # Add the tables to the file menu
        tables_list = self.database.get_tables()

        tables_dict = {
            table:self.tables_select for table in tables_list
        }
        print(tables_dict)
        self.table_frame = c.CTkFrame(self)
        # self.table_frame.pack(pady=30)
        # for each element and functio in the tables dictionary, pass they key string as a paramenter to the function
        for table,func in tables_dict.items():
            tables_menu.add_command(label=f"{table}",command=lambda t = table:func(t,self.table_frame)
                                    ,font=('Arial', 20, 'normal'))

        menubar.add_cascade(label="Выбрать таблицу", menu=tables_menu,font=('Arial', 20, 'normal'))

        # User Edit frame
        self.user_edit_frame = c.CTkFrame(self, fg_color='#1C414D', width=100)

        self.table_id = c.CTkLabel(self.user_edit_frame, fg_color='#D9D9D9', text=' '
                                   , width=150, text_color='black')
        self.table_id.pack(pady=10, padx=30)

        self.table_username = c.CTkEntry(self.user_edit_frame, fg_color='#D9D9D9', corner_radius=0,
                                         border_width=0, border_color='black', placeholder_text='Логин', width=150,
                                         text_color='black')
        self.table_username.pack(pady=10, padx=30)

        self.table_password = c.CTkEntry(self.user_edit_frame, fg_color='#D9D9D9', placeholder_text='Пароль', corner_radius=0,
                                         border_width=0, border_color='black', width=150, text_color='black')
        self.table_password.pack(pady=10, padx=30)

        # Buttons
        self.user_edit_button = c.CTkButton(self.user_edit_frame, width=150, text='ОБНОВИТЬ', fg_color='#238FB1',
                                            command=self.on_edit_user_click)
        self.user_delete_button = c.CTkButton(self.user_edit_frame, width=150, text='УДАЛИТЬ', fg_color='#FB5757',
                                              command=self.on_delete_user_click)
        self.user_add_button = c.CTkButton(self.user_edit_frame, width=150, text='ДОБАВИТЬ', fg_color='#6CD63C',
                                           command=self.user_on_add_click)
        self.user_edit_button.pack(pady=10, padx=30)
        self.user_delete_button.pack(pady=10, padx=30)
        self.user_add_button.pack(pady=10, padx=30)

        # # Chanel Edit frame
        # self.chanel_edit_frame = c.CTkFrame(self, fg_color='#1C414D', width=100)
        #
        # self.chanel_id = c.CTkLabel(self.chanel_edit_frame, fg_color='#D9D9D9', text=' '
        #                            , width=150, text_color='black')
        # self.chanel_id.pack(pady=10, padx=30)
        #
        # self.chanel_width = c.CTkEntry(self.chanel_edit_frame, fg_color='#D9D9D9', corner_radius=0,
        #                                  border_width=0, border_color='black', placeholder_text='Ширина', width=150,
        #                                  text_color='black')
        # self.chanel_width.pack(pady=10, padx=30)
        #
        # self.chanel_depth = c.CTkEntry(self.chanel_edit_frame, fg_color='#D9D9D9', placeholder_text='Глубина', corner_radius=0,
        #                              border_width=0, border_color='black', width=150, text_color='black')
        # self.chanel_depth.pack(pady=10, padx=30)
        #
        # self.chanel_length = c.CTkEntry(self.chanel_edit_frame, fg_color='#D9D9D9', placeholder_text='Длина',
        #                              corner_radius=0,
        #                              border_width=0, border_color='black', width=150, text_color='black')
        # self.chanel_length.pack(pady=10, padx=30)
        #
        # # Buttons
        # self.chanel_edit_button = c.CTkButton(self.chanel_edit_frame, width=150, text='ОБНОВЛЯТЬ', fg_color='#238FB1')
        # self.chanel_delete_button = c.CTkButton(self.chanel_edit_frame, width=150, text='УДАЛИТЬ', fg_color='#FB5757')
        # self.chanel_add_button = c.CTkButton(self.chanel_edit_frame, width=150, text='ДОБАВИТЬ', fg_color='#6CD63C',
        #                                      command=self.chanel_edit_on_add_click)
        # self.chanel_edit_button.pack(pady=10, padx=30)
        # self.chanel_delete_button.pack(pady=10, padx=30)
        # self.chanel_add_button.pack(pady=10, padx=30)

        # Material Edit frame
        self.material_edit_frame = c.CTkFrame(self, fg_color='#1C414D', width=100)

        self.material_id = c.CTkLabel(self.material_edit_frame, fg_color='#D9D9D9', text=' '
                                    , width=150, text_color='black')
        self.material_id.pack(pady=10, padx=30)

        self.material_name = c.CTkEntry(self.material_edit_frame, fg_color='#D9D9D9', corner_radius=0,
                                       border_width=0, border_color='black', placeholder_text='Материал', width=150,
                                       text_color='black')
        self.material_name.pack(pady=10, padx=30)

        self.material_density = c.CTkEntry(self.material_edit_frame, fg_color='#D9D9D9', placeholder_text='Плотность',
                                       corner_radius=0,
                                       border_width=0, border_color='black', width=150, text_color='black')
        self.material_density.pack(pady=10, padx=30)

        self.material_heat_capacity = c.CTkEntry(self.material_edit_frame, fg_color='#D9D9D9', placeholder_text='Удельная теплоемкость',
                                        corner_radius=0,
                                        border_width=0, border_color='black', width=150, text_color='black')
        self.material_heat_capacity.pack(pady=10, padx=30)

        self.material_melting_temp = c.CTkEntry(self.material_edit_frame, fg_color='#D9D9D9',
                                          placeholder_text='Температура плавления',
                                          corner_radius=0,
                                          border_width=0, border_color='black', width=150, text_color='black')
        self.material_melting_temp.pack(pady=10, padx=30)

        self.input_warning = c.CTkLabel(master=None,text_color='red', text='Вводимые числа должны быть больше 0')

        # Buttons
        self.material_edit_button = c.CTkButton(self.material_edit_frame, width=150, text='ОБНОВИТЬ', fg_color='#238FB1',
                                                command=self.on_edit_material_click)
        self.material_delete_button = c.CTkButton(self.material_edit_frame, width=150, text='УДАЛИТЬ', fg_color='#FB5757',
                                                  command=self.on_delete_material_click)
        self.material_add_button = c.CTkButton(self.material_edit_frame, width=150, text='ДОБАВИТЬ', fg_color='#6CD63C',
                                               command=self.material_on_add_click)
        self.material_edit_button.pack(pady=10, padx=30)
        self.material_delete_button.pack(pady=10, padx=30)
        self.material_add_button.pack(pady=10, padx=30)

        # Math model params Edit frame
        self.math_model_params_edit_frame = c.CTkFrame(self, fg_color='#1C414D', width=100)

        self.math_model_params_id = c.CTkLabel(self.math_model_params_edit_frame, fg_color='#D9D9D9', text=' '
                                      , width=150, text_color='black')
        self.math_model_params_id.pack(pady=10, padx=30)

        self.math_model_params_consistency_coeff = c.CTkEntry(self.math_model_params_edit_frame, fg_color='#D9D9D9', corner_radius=0,
                                        border_width=0, border_color='black', placeholder_text='Коэффициент консистенции...', width=150,
                                        text_color='black')
        self.math_model_params_consistency_coeff.pack(pady=10, padx=30)

        self.math_model_params_temp_coeff = c.CTkEntry(self.math_model_params_edit_frame, fg_color='#D9D9D9', placeholder_text='Температурный коэффициент...',
                                           corner_radius=0,
                                           border_width=0, border_color='black', width=150, text_color='black')
        self.math_model_params_temp_coeff.pack(pady=10, padx=30)

        self.math_model_params_casting_temp = c.CTkEntry(self.math_model_params_edit_frame, fg_color='#D9D9D9',
                                                 placeholder_text='Температура приведения',
                                                 corner_radius=0,
                                                 border_width=0, border_color='black', width=150, text_color='black')
        self.math_model_params_casting_temp.pack(pady=10, padx=30)

        self.math_model_params_flow_index = c.CTkEntry(self.math_model_params_edit_frame, fg_color='#D9D9D9',
                                                 placeholder_text='Индекс течения материала',
                                                 corner_radius=0,
                                                 border_width=0, border_color='black', width=150, text_color='black')
        self.math_model_params_flow_index.pack(pady=10, padx=30)

        self.math_model_params_cover_heat_trans = c.CTkEntry(self.math_model_params_edit_frame, fg_color='#D9D9D9',
                                                 placeholder_text='Коэффициент теплоотдачи...',
                                                 corner_radius=0,
                                                 border_width=0, border_color='black', width=150, text_color='black')
        self.math_model_params_cover_heat_trans.pack(pady=10, padx=30)

        self.math_model_material_id = c.CTkEntry(self.math_model_params_edit_frame, fg_color='#D9D9D9',
                                                       placeholder_text='ID материала',
                                                       corner_radius=0,
                                                       border_width=0, border_color='black', width=150,
                                                       text_color='black')
        self.math_model_material_id.pack(pady=10, padx=30)

        # Buttons
        self.math_model_params_edit_button = c.CTkButton(self.math_model_params_edit_frame, width=150, text='ОБНОВИТЬ',
                                                fg_color='#238FB1',command=self.on_edit_mathModel_click)
        self.math_model_params_delete_button = c.CTkButton(self.math_model_params_edit_frame, width=150, text='УДАЛИТЬ',
                                                  fg_color='#FB5757',command=self.on_delete_mathModel_click)
        self.math_model_params_add_button = c.CTkButton(self.math_model_params_edit_frame, width=150, text='ДОБАВИТЬ', fg_color='#6CD63C',
                                                        command=self.math_model_params_on_add_click)
        self.math_model_params_edit_button.pack(pady=10, padx=30)
        self.math_model_params_delete_button.pack(pady=10, padx=30)
        self.math_model_params_add_button.pack(pady=10, padx=30)




        # Process params Edit frame
        self.process_params_edit_frame = c.CTkFrame(self, fg_color='#1C414D', width=100)

        self.process_params_id = c.CTkLabel(self.process_params_edit_frame, fg_color='#D9D9D9', text=' '
                                            , width=150, text_color='black')
        self.process_params_id.pack(pady=10, padx=30)

        self.cover_speed = c.CTkEntry(self.process_params_edit_frame, fg_color='#D9D9D9', corner_radius=0,
                                              border_width=0, border_color='black', placeholder_text='Скорость крышки',
                                              width=150,
                                              text_color='black')
        self.cover_speed.pack(pady=10, padx=30)

        self.cover_temperature = c.CTkEntry(self.process_params_edit_frame, fg_color='#D9D9D9',
                                                 placeholder_text='Температтура  крышки',
                                                 corner_radius=0,
                                                 border_width=0, border_color='black', width=150, text_color='black')
        self.cover_temperature.pack(pady=10, padx=30)

        # Buttons
        self.process_params_edit_button = c.CTkButton(self.process_params_edit_frame, width=150, text='ОБНОВИТЬ',
                                                      fg_color='#238FB1',command=self.on_edit_process_params)
        self.process_params_delete_button = c.CTkButton(self.process_params_edit_frame, width=150, text='УДАЛИТЬ',
                                                        fg_color='#FB5757',command=self.on_delete_process_params_click)
        self.process_params_add_button = c.CTkButton(self.process_params_edit_frame, width=150, text='ДОБАВИТЬ',
                                                     fg_color='#6CD63C',
                                                     command=self.process_params_on_add_click)
        self.process_params_edit_button.pack(pady=10, padx=30)
        self.process_params_delete_button.pack(pady=10, padx=30)
        self.process_params_add_button.pack(pady=10, padx=30)

        self.success = c.CTkLabel(master=None,text="Таблица успешно обновлена", text_color='green')

    def tables_select(self,choice, frame: c.CTkFrame):
        match choice:
            case 'users':
                try:
                    for widget in frame.winfo_children():
                        widget.destroy()
                    # self.chanel_edit_frame.grid_forget()
                    self.material_edit_frame.grid_forget()
                    self.process_params_edit_frame.grid_forget()
                    self.math_model_params_edit_frame.grid_forget()

                except Exception as e:
                    print(e)
                else:
                    result = self.database.get_users()
                    table = result[0]
                    columns = result[1]

                    table = User_Table(frame, table, columns)
                    frame.grid(row=0, column=1, pady=30, columnspan=3)
                    # self.user_edit_frame = c.CTkFrame(self, fg_color='#1C414D', width=100)
                    self.user_edit_frame.grid(row=0, column=0, pady=10, padx=20)
                    # self.left_frame.grid(row=0, column=0, pady=30, padx=20, rowspan=3)
            # case 'chanel':
            #     try:
            #         for widget in frame.winfo_children():
            #             widget.destroy()
            #         self.user_edit_frame.grid_forget()
            #         self.material_edit_frame.grid_forget()
            #         self.process_params_edit_frame.grid_forget()
            #         self.math_model_params_edit_frame.grid_forget()
            #
            #
            #     except Exception as e:
            #         print(e)
            #     else:
            #         result = self.database.get_chanel_params()
            #         table = result[0]
            #         columns = result[1]
            #         print(table)
            #
            #         table = Chanel_Table(frame, table, columns)
            #         frame.grid(row=0, column=1, pady=30, columnspan=3)
            #
            #         self.chanel_edit_frame.grid(row=0, column=0, pady=10, padx=20)
            case 'material':
                try:
                    for widget in frame.winfo_children():
                        widget.destroy()
                    # self.chanel_edit_frame.grid_forget()
                    self.user_edit_frame.grid_forget()
                    self.process_params_edit_frame.grid_forget()
                    self.math_model_params_edit_frame.grid_forget()


                except Exception as e:
                    print(e)
                else:
                    result = self.database.get_materials()
                    print("Material results")
                    print(result)
                    table = result[0]
                    columns = result[1]

                    table = Material_Table(frame, table, columns)
                    frame.grid(row=0, column=1, pady=30, columnspan=3)

                    self.material_edit_frame.grid(row=0, column=0, pady=10, padx=20)

            case 'math_model':
                try:
                    for widget in frame.winfo_children():
                        widget.destroy()
                    # self.chanel_edit_frame.grid_forget()
                    self.user_edit_frame.grid_forget()
                    self.material_edit_frame.grid_forget()
                    self.process_params_edit_frame.grid_forget()

                except Exception as e:
                    print(e)
                else:
                    result = self.database.get_math_module()
                    table = result[0]
                    columns = result[1]

                    table = MathModel_Table(frame, table, columns)
                    frame.grid(row=0, column=1, pady=30, columnspan=3)

                    self.math_model_params_edit_frame.grid(row=0, column=0, pady=10, padx=20)

            case 'process_params':
                try:
                    for widget in frame.winfo_children():
                        widget.destroy()
                    # self.chanel_edit_frame.grid_forget()
                    self.user_edit_frame.grid_forget()
                    self.material_edit_frame.grid_forget()
                    self.math_model_params_edit_frame.grid_forget()

                except Exception as e:
                    print(e)
                else:
                    result = self.database.get_process_params()
                    table = result[0]
                    columns = result[1]

                    table = ProcessParams_Table(frame, table, columns)
                    frame.grid(row=0, column=1, pady=30, columnspan=3)

                    self.process_params_edit_frame.grid(row=0, column=0, pady=10, padx=20)

    # Edit tables
    def on_edit_user_click(self):
        id = int(self.table_id.cget('text'))
        username = self.table_username.get()
        password = self.table_password.get()

        try:
            user_to_update = self.database.session.query(User).filter(User.id == id).first()
            user_to_update.username = username
            user_to_update.password = EncDecPass().encrypt_password(password)
            self.database.session.commit()
            self.success.pack(in_=self.user_edit_frame)
        except Exception as e:
            print(e,': on_edit_user_click')
            print(traceback.print_exc())

    def on_edit_material_click(self):
        try:
            id = int(self.material_id.cget('text'))
            material = self.material_name.get()
            density = float(self.material_density.get())
            heat_capacity = float(self.material_heat_capacity.get())
            melting_temp = float(self.material_melting_temp.get())

            if density <=0 or heat_capacity <= 0 or melting_temp <= 0:
                raise Exception("Не может быть 0")
        except Exception as e:
            print(e)
            self.input_warning.pack(in_=self.material_edit_frame)
        try:
            material_to_update = self.database.session.query(Material).filter(Material.id == id).first()
            material_to_update.material = material
            material_to_update.density = density
            material_to_update.heat_capacity = heat_capacity
            material_to_update.melting_tempterature = melting_temp

            self.database.session.commit()
            self.success.pack(in_=self.material_edit_frame)
        except Exception as e:
            print(e)

    def on_edit_mathModel_click(self):
        try:
            id = int(self.math_model_params_id.cget('text'))
            consistency_coeff = float(self.math_model_params_consistency_coeff.get())
            temp_visc_coeff = float(self.math_model_params_temp_coeff.get())
            casting_temp = float(self.math_model_params_casting_temp.get())
            flow_index = float(self.math_model_params_flow_index.get())
            cover_heat_trans_coeff = float(self.math_model_params_cover_heat_trans.get())
            material_id = int(self.math_model_material_id.get())

            if consistency_coeff <=0 or temp_visc_coeff <= 0 or casting_temp <= 0 or flow_index <= 0 or cover_heat_trans_coeff <=0:
                raise Exception("Не может быть 0")

        except Exception as e:
            print(e)
            self.input_warning.configure(master=self.math_model_params_edit_frame)
        try:
            # material_to_update = self.database.session.query(Material).filter(Material.id == id).first()
            try:
                material = self.database.session.query(Material).filter(Material.id == material_id).first()
                if material is not None:
                    mathModel_update = self.database.session.query(MathModel).filter(MathModel.id == id).first()
                    mathModel_update.consistency_coefficient = consistency_coeff
                    mathModel_update.temp_viscosity_coefficient = temp_visc_coeff
                    mathModel_update.casting_temperature = casting_temp
                    mathModel_update.flow_index = flow_index
                    mathModel_update.cover_heat_transfer_coefficient = cover_heat_trans_coeff
                    mathModel_update.material_id = material_id

                    self.database.session.commit()
                    self.success.pack(in_=self.math_model_params_edit_frame)
                else:
                    raise Exception(f"Материала с id:{material_id} не существует")

            except Exception as e:
                self.input_warning.configure(text=f"Материала с id:{material_id} не существует")
                self.input_warning.pack(in_=self.math_model_params_edit_frame)
                print(f'{e} in edit math model')
        except Exception as e:
            print(e)
            self.input_warning.configure(text="Ошибка обновления параметров математической модели")
            self.input_warning.pack(in_=self.math_model_params_edit_frame)

    def on_edit_process_params(self):
        try:
            id = int(self.process_params_id.cget('text'))
            consistency_coeff = float(self.math_model_params_consistency_coeff.get())
            cover_speed = float(self.cover_speed.get())
            cover_temp = float(self.cover_temperature.get())

            if cover_speed <= 0 or cover_temp <= 0:
                raise Exception("Не может быть 0")

        except Exception as e:
            print(e)
            self.input_warning.configure(master=self.math_model_params_edit_frame)
        try:
            # material_to_update = self.database.session.query(Material).filter(Material.id == id).first()

            process_params_update = self.database.session.query(ProcessParams).filter(ProcessParams.id == id).first()
            process_params_update.cover_speed = cover_speed
            process_params_update.cover_temperature = cover_temp
            self.database.session.commit()
            self.success.pack(in_=self.process_params_edit_frame)
        except Exception as e:
            print(e)
            self.input_warning.configure(text="Ошибка обновления параметров процесса")
            self.input_warning.pack(in_=self.process_params_edit_frame)

    # Deleting records from tables
    def on_delete_user_click(self):
        id = int(self.table_id.cget('text'))
        try:
            delete_user = self.database.session.query(User).filter(User.id == id).first()
            self.database.session.delete(delete_user)
            self.database.session.commit()
            self.success.configure(text="Пользователь успешно удален")
            self.success.pack(in_=self.user_edit_frame)
        except Exception as e:
            print(e)
            self.input_warning.configure(text="Ошибка удаления пользователя")
            self.input_warning.pack(in_=self.user_edit_frame)
    def on_delete_material_click(self):
        id = int(self.material_id.cget('text'))
        try:
            delete_material = self.database.session.query(Material).filter(Material.id == id).first()
            self.database.session.delete(delete_material)
            self.database.session.commit()
            self.success.configure(text="Материал успешно удален")
            self.success.pack(in_=self.material_edit_frame)
        except Exception as e:
            print(e)
            self.input_warning.configure(text="Ошибка удаления материала")
            self.input_warning.pack(in_=self.material_edit_frame)
    def on_delete_mathModel_click(self):
        id = int(self.math_model_params_id.cget('text'))
        try:
            delete_math_model = self.database.session.query(MathModel).filter(MathModel.id == id).first()
            self.database.session.delete(delete_math_model)
            self.database.session.commit()
            self.success.configure(text="Параметры математической модели успешно удалены")
            self.success.pack(in_=self.math_model_params_edit_frame)
        except Exception as e:
            print(e)
            self.input_warning.configure(text="Ошибка удаления параметров математической модели")
            self.input_warning.pack(in_=self.math_model_params_edit_frame)
    def on_delete_process_params_click(self):
        id = int(self.process_params_id.cget('text'))
        try:
            delete_process_params = self.database.session.query(ProcessParams).filter(ProcessParams.id == id).first()
            self.database.session.delete(delete_process_params)
            self.database.session.commit()
            self.success.configure(text="Параметры процесса успешно удалены")
            self.success.pack(in_=self.process_params_edit_frame)
        except Exception as e:
            print(e)
            self.input_warning.configure(text="Ошибка удаления параметров процесса")
            self.input_warning.pack(in_=self.process_params_edit_frame)

    # Adding data to the database
    def user_on_add_click(self):
        # Top level window
        self.add_user_window = c.CTkToplevel(self,fg_color="#232E33")
        self.add_user_window.geometry('400x250')
        self.add_user_window.title('Добавить нового пользователя')
        self.add_user_window.resizable(False,False)
        self.add_user_window.attributes('-topmost', 'true')

        # Username
        self.new_username = c.CTkEntry(master=self.add_user_window,placeholder_text='Логин',width=200)
        # Role
        self.combobox_var = c.StringVar(value="Роль")
        self.new_role = c.CTkComboBox(self.add_user_window, values=["Администратор", "Исследователь"], corner_radius=10,
                                      fg_color='#D9D9D9', variable=self.combobox_var, width=200,
                                      text_color='#000000', state='readonly', height=40, dropdown_font=('', 20))

        # Password
        self.new_password = c.CTkEntry(master=self.add_user_window,width=200)
        self.new_password.delete(0,c.END)
        self.new_password.insert(0,PasswordGen.generate_password())

        # Add button
        self.new_add_button = c.CTkButton(master=self.add_user_window, text='ДОБАВИТЬ', fg_color='#6CD63C', command=self.on_new_user_add_click)

        # Warning
        self.warning = c.CTkLabel(master=self.add_user_window,text='Ошибка добавления нового пользователя',text_color='red')

        # Success
        self.success = c.CTkLabel(master=self.add_user_window,text='Пользователь успешно добавлен',text_color='green')
        # self.success.pack(pady=10)
        # self.success.pack_forget()

        # Pack elements
        self.new_username.pack(pady=10)
        self.new_role.pack(pady=10)
        self.new_password.pack(pady=10)
        self.new_add_button.pack(pady=10)
    def math_model_params_on_add_click(self):
        # Top level window
        self.add_mathModel_window = c.CTkToplevel(self, fg_color="#232E33")
        self.add_mathModel_window.geometry('450x500')
        self.add_mathModel_window.title('Добавить новые параметры математической модели')
        self.add_mathModel_window.resizable(False, False)
        self.add_mathModel_window.attributes('-topmost', 'true')

        # Коэффициент консистен-ции материала при темпе-ратуре приведения
        self.new_consistency_coefficient = c.CTkEntry(master=self.add_mathModel_window, placeholder_text='Коэффициент консистенции...', width=400)

        # Температурный коэффи-циент вязкости материала
        self.new_temp_visc_coeff = c.CTkEntry(master=self.add_mathModel_window, placeholder_text='Температурный коэффициент...', width=300)

        # Температура приведения
        self.new_casting_temp = c.CTkEntry(master=self.add_mathModel_window, placeholder_text='Температура приведения...',
                                            width=300)

        # Индекс течения материала
        self.new_flow_index = c.CTkEntry(master=self.add_mathModel_window, placeholder_text='Индекс течения материала',
                                           width=250)

        # Коэффициент теплоотдачи от крышки канала к материалу
        self.new_cover_heat_trans_coeff = c.CTkEntry(master=self.add_mathModel_window, placeholder_text='Коэффициент теплоотдачи...',
                                     width=250)
        self.new_material_id = c.CTkEntry(master=self.add_mathModel_window,
                                                 placeholder_text='Id Материала',
                                                 width=250)

        # Add button
        self.new_add_button = c.CTkButton(master=self.add_mathModel_window, text='Добавить', fg_color='#6CD63C',
                                          command=self.on_new_mathModel_add_click)

        # Warning
        self.warning = c.CTkLabel(master=self.add_mathModel_window, text='Ошибка добавления новой математической модели', text_color='red')

        # Success
        self.success = c.CTkLabel(master=self.add_mathModel_window, text='Математическая модель успешно добавлена',
                                  text_color='green')
        # self.success.pack(pady=10)
        # self.success.pack_forget()

        # Pack elements
        self.new_consistency_coefficient.pack(pady=10)
        self.new_temp_visc_coeff.pack(pady=10)
        self.new_casting_temp.pack(pady=10)
        self.new_flow_index.pack(pady=10)
        self.new_cover_heat_trans_coeff.pack(pady=10)
        self.new_material_id.pack(pady=10)
        self.new_add_button.pack(pady=10)
    def material_on_add_click(self):
        # Top level window
        self.add_material_window = c.CTkToplevel(self, fg_color="#232E33")
        self.add_material_window.geometry('450x300')
        self.add_material_window.title('Добавить новый материал')
        self.add_material_window.resizable(False, False)
        self.add_material_window.attributes('-topmost', 'true')

        # Материал
        self.new_material = c.CTkEntry(master=self.add_material_window, placeholder_text='Материал', width=200)

        # Плотность
        self.new_density = c.CTkEntry(master=self.add_material_window, placeholder_text='Плотность', width=200)

        # Удельная теплоемкость
        self.new_heat_capacity = c.CTkEntry(master=self.add_material_window, placeholder_text='Удельная теплоемкость', width=250)

        # Температура плавления
        self.new_melting_temp = c.CTkEntry(master=self.add_material_window, placeholder_text='Температура плавления',
                                            width=250)

        # Add button
        self.new_add_button = c.CTkButton(master=self.add_material_window, text='ДОБАВИТЬ', fg_color='#6CD63C',
                                          command=self.on_new_material_add_click)

        # Warning
        self.warning = c.CTkLabel(master=self.add_material_window, text='Ошибка добавления нового материала', text_color='red')

        # Success
        self.success = c.CTkLabel(master=self.add_material_window, text='Материал успешно добавлен', text_color='green')
        # self.success.pack(pady=10)
        # self.success.pack_forget()

        # Pack elements
        self.new_material.pack(pady=10)
        self.new_density.pack(pady=10)
        self.new_heat_capacity.pack(pady=10)
        self.new_melting_temp.pack(pady=10)
        self.new_add_button.pack(pady=10)

        self.math_model_params_on_add_click()
    def process_params_on_add_click(self):
        # Top level window
        self.add_process_params_window = c.CTkToplevel(self, fg_color="#232E33")
        self.add_process_params_window.geometry('450x250')
        self.add_process_params_window.title('Добавить новые параметры процесса')
        self.add_process_params_window.resizable(False, False)
        self.add_process_params_window.attributes('-topmost', 'true')

        # Материал
        self.new_cover_speed = c.CTkEntry(master=self.add_process_params_window, placeholder_text='Скорость крышки', width=250)

        # Плотность
        self.new_cover_temperature = c.CTkEntry(master=self.add_process_params_window, placeholder_text='Температура крышки', width=250)

        # Add button
        self.new_add_button = c.CTkButton(master=self.add_process_params_window, text='ДОБАВИТЬ', fg_color='#6CD63C',
                                          command=self.on_new_process_params_add_click)

        # Warning
        self.warning = c.CTkLabel(master=self.add_process_params_window, text='Добавить новые параметры процесса', text_color='red')

        # Success
        self.success = c.CTkLabel(master=self.add_process_params_window, text='Параметры процесса успешно добавлены',
                                  text_color='green')
        # self.success.pack(pady=10)
        # self.success.pack_forget()

        # Pack elements
        self.new_cover_speed.pack(pady=10)
        self.new_cover_temperature.pack(pady=10)
        self.new_add_button.pack(pady=10)


    def on_new_user_add_click(self):
        username = self.new_username.get()
        password = self.new_password.get()
        role = self.new_role.get()
        print((username, password, role))
        user = User(username, password, role)
        try:

            self.database.session.add(user)
            self.database.session.commit()
            print('Пользователь добавлен успешно...')
            self.success.pack()

        except Exception:
            print(Exception)
            self.warning.pack()
    def on_new_material_add_click(self):
        try:
            material = self.new_material.get()
            density = float(self.new_density.get())
            heat_capacity = float(self.new_heat_capacity.get())
            melting_temp = float(self.new_melting_temp.get())
            if density or heat_capacity or melting_temp <=0:
                raise Exception("Не может быть 0")
        except Exception as e:
            print(e)
            self.warning.configure(text="Вводимое число должно быть больше 0")
        print((material, density, heat_capacity,melting_temp))

        material = Material(material,density,heat_capacity,melting_temp)
        try:

            self.database.session.add(material)
            self.database.session.commit()
            print('Material successfully added...')
            self.success.pack()
            # self.add_user_window.after(200,self.success.pack_forget())

        except Exception:
            print(Exception)
            self.warning.pack()
            # self.add_user_window.after(1000, self.warning.destroy())
    def on_new_mathModel_add_click(self):
        try:
            consistency_coeff = float(self.new_consistency_coefficient.get())
            temp_visc_coeff = float(self.new_temp_visc_coeff.get())
            casting_temp = float(self.new_casting_temp.get())
            flow_index = float(self.new_flow_index.get())
            cover_heat_transfer_coeff = float(self.new_cover_heat_trans_coeff.get())
            material_id = float(self.new_material_id.get())

            if consistency_coeff <= 0 or temp_visc_coeff <= 0 or casting_temp <= 0 or flow_index <= 0 or cover_heat_transfer_coeff <= 0 or material_id <= 0:
                raise Exception("Cannot be zero")
        except Exception as e:

            self.warning.configure(text="Вводимое число должно быть больше 0")
            self.success.pack_forget()
            print(e)
        # print((consistency_coeff, temp_visc_coeff, casting_temp, flow_index, cover_heat_transfer_coeff,material_id))

        math_model = MathModel(consistency_coeff, temp_visc_coeff,casting_temp,flow_index,cover_heat_transfer_coeff,material_id)
        # print(math_model)
        try:
            material = self.database.get_materials(material_id)
            print(material)
            if  material[0] != None:
                print("Material with id exists")
                self.database.session.add(math_model)
                self.database.session.commit()
                print('Math Model successfully added...')
                self.success.pack()
            else:
                self.success.pack_forget()
                self.warning.configure(text="Не существует материал с таким id")
                self.warning.pack()
            # self.add_user_window.after(200,self.success.pack_forget())

        except Exception as e:
            print(traceback.print_exc())
            self.warning.pack()
            # self.add_user_window.after(1000, self.warning.destroy())
    def on_new_process_params_add_click(self):
        try:
            cover_speed = float(self.new_cover_speed.get())
            cover_temp = float(self.new_cover_temperature.get())
            print(cover_speed <=0)
            print(cover_temp <=0)
            if cover_temp <= 0 or cover_speed <= 0:
                raise Exception("Cannot be zero")
        except Exception as e:
            self.warning.configure(text="Вводимое число должно быть больше 0")
            self.warning.pack()
            print(e)
            return
        # print((consistency_coeff, temp_visc_coeff, casting_temp, flow_index, cover_heat_transfer_coeff,material_id))

        process_params = ProcessParams(cover_speed,cover_temp)
        print(process_params)
        try:
            self.database.session.add(process_params)
            self.database.session.commit()
            print('Process params successfully added...')
            self.success.pack()
            # self.add_user_window.after(200,self.success.pack_forget())

        except Exception:
            print(Exception)
            self.warning.pack()
            # self.add_user_window.after(1000, self.warning.destroy())


    def change_user_click(self):
        print('change user')
        self.destroy()
        login = Login.Login(self.database)
        login.mainloop()
    def create_reserve_copy(self):
        print('creating reserved copy...')
        try:
            result = self.database.create_reserve_copy()
        except Exception as e:
            print(e)
        else:
            # Top level window
            self.result_window = c.CTkToplevel(self, fg_color="#232E33")
            self.result_window.geometry('450x250')
            self.result_window.title('Резервная копия')
            self.result_window.resizable(False, False)
            self.result_window.attributes('-topmost', 'true')

            self.label = c.CTkLabel(master=self.result_window,text=result)
            self.label.pack()

    def restore_database(self):
        print("restoring self.database...")
        # Create a Tkinter window
        root = tk.Tk()
        root.withdraw()

        # Create a file dialog box
        file_path = filedialog.askopenfilename(title="Выбрать базу данных", filetypes=[("Database files", "*.db")])

        # Pass the file path to a variable
        selected_file = file_path

        # Show the selected file path in a message box
        print(f"Selected file: {selected_file}")
        try:
            result = self.database.restore_from_reserve_copy(selected_file)
        except Exception as e:
            print(e)
        else:
            # Top level window
            self.result_window = c.CTkToplevel(self, fg_color="#232E33")
            self.result_window.geometry('450x250')
            self.result_window.title('Восстановление базы данных')
            self.result_window.resizable(True, False)
            self.result_window.attributes('-topmost', 'true')

            self.label = c.CTkLabel(master=self.result_window, text=result)
            self.label.pack()

