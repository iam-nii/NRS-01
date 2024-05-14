import customtkinter as c


class User_Table:
    def __init__(self, root,table,columns:int):

        self.root = root

        # Header row
        self.label = c.CTkLabel(self.root, width=100, height=30, text='id', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=0, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=300, height=30, text='Логин', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=1, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=300, height=30, text='Роль', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=2, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=300, height=30, text='ID материала', fg_color='black',
                                text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=3, padx=1, pady=1)  # position the entry within the frame

        self.users_dict = {}
        username_label_list: list[c.CTkLabel] = []
        role_label_list: list[c.CTkLabel] = []
        id_label_list: list[c.CTkLabel] = []
        material_id_list:list[c.CTkLabel] = []

        # code for creating table
        for i in range(len(table)):
            for j in range(columns + 2):
                if j == 1:
                    self.label1 = c.CTkLabel(root, width=300, height=30,text=f'{table[i].username}', fg_color='grey',
                                          text_color='white',font=('Arial', 16, 'bold'))
                    self.label1.grid(row=i+1, column=j, padx=1, pady=1)  # position the entry within the frame
                    username_label_list.append(self.label1)
                elif j == 2:
                    self.label2 = c.CTkLabel(root, width=300, height=30, text=f'{table[i].role}',fg_color='grey',
                                          text_color='white',font=('Arial', 16, 'bold'))
                    self.label2.grid(row=i+1, column=j, padx=1, pady=1)  # position the entry within the frame
                    role_label_list.append(self.label2)
                elif j == 3:
                    self.label2 = c.CTkLabel(root, width=300, height=30, text=f'{table[i].material_id}',fg_color='grey',
                                          text_color='white',font=('Arial', 16, 'bold'))
                    self.label2.grid(row=i+1, column=j, padx=1, pady=1)  # position the entry within the frame
                    material_id_list.append(self.label2)
                else:
                    self.label3 = c.CTkLabel(root, width=100, height=30, text=f'{i+1}', fg_color='black',
                                          text_color='white', font=('Arial', 16, 'bold'))
                    self.label3.grid(row=i+1, column=j, padx=1, pady=1)  # position the entry within the frame
                    id_label_list.append(self.label3)

        for i in range(len(username_label_list)):
            self.users_dict[i] = {
                'username': username_label_list[i].cget('text'),
                'role': role_label_list[i].cget('text'),
                'material_id':material_id_list[i].cget('text'),
                'id':id_label_list[i].cget('text'),
            }
        print(self.users_dict)

        for label in username_label_list:
            label.bind('<Button-1>',lambda e,label = label: self.on_label_click(label))

    def on_label_click(self,label:c.CTkLabel):
        username = label.cget('text')
        material_id = ''
        role = ' '
        id = ' '
        print(username)
        for key in self.users_dict:
            value = self.users_dict[key]
            if value['username'] == username:
                id = value['id']
                role = value['role']
                material_id = value['material_id']


        self.root.winfo_toplevel().table_id.configure(text=id, text_color='black')
        # Username
        entry:c.c.CTkEntry = self.root.winfo_toplevel().table_username
        entry.delete(0,c.END)
        entry.insert(0,username)

        # # role
        # role_entry:c.c.CTkEntry = self.root.winfo_toplevel().table_role
        # role_entry.delete(0,c.END)
        # role_entry.insert(0,role)


        # self.root.winfo_toplevel().table_username.configure(text=username, text_color='black',width=100)
        # self.root.winfo_toplevel().table_role.configure(text=role, text_color='black',width=100)


# class Chanel_Table:
#     def __init__(self, root,table,columns:int):
#         self.root = root
#         width_label_list: list[c.CTkLabel] = []
#         depth_label_list: list[c.CTkLabel] = []
#         length_label_list: list[c.CTkLabel] = []
#         id_label_list: list[c.CTkLabel] = []
#         self.chanels_dict = {}
#
#         # Header row
#         self.label = c.CTkLabel(self.root, width=100, height=30, text='id', fg_color='black',
#                               text_color='white', font=('Arial', 16, 'bold'))
#         self.label.grid(row=0, column=0, padx=1, pady=1)  # position the entry within the frame
#
#         self.label = c.CTkLabel(self.root, width=300, height=30, text='width', fg_color='black',
#                               text_color='white', font=('Arial', 16, 'bold'))
#         self.label.grid(row=0, column=1, padx=1, pady=1)  # position the entry within the frame
#
#         self.label = c.CTkLabel(self.root, width=300, height=30, text='depth', fg_color='black',
#                               text_color='white', font=('Arial', 16, 'bold'))
#         self.label.grid(row=0, column=2, padx=1, pady=1)  # position the entry within the frame
#
#         self.label = c.CTkLabel(self.root, width=300, height=30, text='length', fg_color='black',
#                               text_color='white', font=('Arial', 16, 'bold'))
#         self.label.grid(row=0, column=3, padx=1, pady=1)  # position the entry within the frame
#
#         # code for creating table
#         for i in range(len(table)):
#             for j in range(columns + 1):
#                 if j == 1:
#                     self.label1 = c.CTkLabel(self.root, width=300, height=30, text=f'{table[i].width}', fg_color='grey',
#                                              text_color='white', font=('Arial', 16, 'bold'))
#                     self.label1.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
#                     width_label_list.append(self.label1)
#                 elif j == 2:
#                     self.label2 = c.CTkLabel(self.root, width=300, height=30, text=f'{table[i].depth}', fg_color='grey',
#                                              text_color='white', font=('Arial', 16, 'bold'))
#                     self.label2.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
#                     depth_label_list.append(self.label2)
#                 elif j == 3:
#                     self.label2 = c.CTkLabel(self.root, width=300, height=30, text=f'{table[i].length}', fg_color='grey',
#                                              text_color='white', font=('Arial', 16, 'bold'))
#                     self.label2.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
#                     length_label_list.append(self.label2)
#
#                 else:
#                     self.label3 = c.CTkLabel(self.root, width=100, height=30, text=f'{i + 1}', fg_color='black',
#                                              text_color='white', font=('Arial', 16, 'bold'))
#                     self.label3.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
#                     id_label_list.append(self.label3)
#
#         for i in range(len(width_label_list)):
#             self.chanels_dict[i] = {
#                 'width': width_label_list[i].cget('text'),
#                 'depth': depth_label_list[i].cget('text'),
#                 'length': length_label_list[i].cget('text'),
#                 'id': id_label_list[i].cget('text'),
#             }
#         print(self.chanels_dict)
#
#         for label in width_label_list:
#             label.bind('<Button-1>', lambda e, label=label: self.on_label_click(label))
#     def on_label_click(self,label:c.CTkLabel):
#         width = label.cget('text')
#         depth = ' '
#         length = ' '
#         id = ' '
#         print(width)
#         for key in self.chanels_dict:
#             value = self.chanels_dict[key]
#             if value['width'] == width:
#                 depth = value['depth']
#                 length = value['length']
#                 id = value['id']
#
#
#         self.root.winfo_toplevel().chanel_id.configure(text=id, text_color='black')
#         # Width
#         entry:c.c.CTkEntry = self.root.winfo_toplevel().chanel_width
#         entry.delete(0,c.END)
#         entry.insert(0,width)
#
#         # depth
#         depth_entry:c.c.CTkEntry = self.root.winfo_toplevel().chanel_depth
#         depth_entry.delete(0,c.END)
#         depth_entry.insert(0,depth)
#
#         # length
#         length_entry: c.c.CTkEntry = self.root.winfo_toplevel().chanel_length
#         length_entry.delete(0, c.END)
#         length_entry.insert(0, length)

class Material_Table:
    def __init__(self, root, table, columns: int):

        self.root = root
        self.materials_dict = {}
        material_label_list: list[c.CTkLabel] = []
        density_label_list: list[c.CTkLabel] = []
        heat_capacity_label_list: list[c.CTkLabel] = []
        melting_temperature_label_list: list[c.CTkLabel] = []
        id_label_list: list[c.CTkLabel] = []

        # Header row
        self.label = c.CTkLabel(self.root, width=100, height=30, text='id', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=0, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=200, height=30, text='Материал', fg_color='black',
                                text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=1, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=200, height=30, text='Плотность (кг/м^3)', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=2, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=300, height=30, text='Удельная теплоемкость (Дж/(кг*°С))', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=3, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=250, height=30, text='Температура плавления (°С)', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=4, padx=1, pady=1)  # position the entry within the frame

        print(table)
        # code for creating table
        for i in range(len(table)):
            for j in range(columns + 1):
                if j == 1:
                    self.label1 = c.CTkLabel(self.root, width=200, height=30, text=f'{table[i].material}', fg_color='grey',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.label1.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                    material_label_list.append(self.label1)
                elif j == 2:
                    self.label2 = c.CTkLabel(self.root, width=200, height=30, text=f'{table[i].density}', fg_color='grey',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.label2.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                    density_label_list.append(self.label2)
                elif j == 3:
                    self.label3 = c.CTkLabel(self.root, width=300, height=30, text=f'{table[i].heat_capacity}', fg_color='grey',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.label3.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                    heat_capacity_label_list.append(self.label3)
                elif j == 4:
                    print(f'melting temperature: {table[i].melting_temperature}')
                    self.label4 = c.CTkLabel(self.root, width=250, height=30, text=f'{table[i].melting_temperature}', fg_color='grey',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.label4.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                    melting_temperature_label_list.append(self.label4)
                else:
                    self.label5 = c.CTkLabel(self.root, width=100, height=30, text=f'{i + 1}', fg_color='black',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.label5.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                    id_label_list.append(self.label5)

        for i in range(len(material_label_list)):
            self.materials_dict[i] = {
                'material': material_label_list[i].cget('text'),
                'density': density_label_list[i].cget('text'),
                'heat_capacity': heat_capacity_label_list[i].cget('text'),
                'melting_temperature': melting_temperature_label_list[i].cget('text'),
                'id': id_label_list[i].cget('text'),
            }
        print(self.materials_dict)

        for label in material_label_list:
            label.bind('<Button-1>', lambda e, label=label: self.on_label_click(label))

    def on_label_click(self, label: c.CTkLabel):
        material = label.cget('text')
        density = ' '
        heat_capacity = ' '
        melting_temperature = ' '
        id = ''
        print(material)
        for key in self.materials_dict:
            value = self.materials_dict[key]
            if value['material'] == material:
                density = value['density']
                heat_capacity = value['heat_capacity']
                melting_temperature = value['melting_temperature']
                id = value['id']

        self.root.winfo_toplevel().material_id.configure(text=id, text_color='black')
        # material
        entry: c.c.CTkEntry = self.root.winfo_toplevel().material_name
        entry.delete(0, c.END)
        entry.insert(0, material)

        # density
        density_entry: c.c.CTkEntry = self.root.winfo_toplevel().material_density
        density_entry.delete(0, c.END)
        density_entry.insert(0, density)

        # Heat capacity
        heat_capacity_entry: c.c.CTkEntry = self.root.winfo_toplevel().material_heat_capacity
        heat_capacity_entry.delete(0, c.END)
        heat_capacity_entry.insert(0, heat_capacity)

        # Melting temperature
        melting_temp_entry: c.c.CTkEntry = self.root.winfo_toplevel().material_melting_temp
        melting_temp_entry.delete(0, c.END)
        melting_temp_entry.insert(0, melting_temperature)

class MathModel_Table:
    def __init__(self, root, table, columns: int):

        self.root = root
        self.math_model_dict = {}
        consistency_coefficient_label_list: list[c.CTkLabel] = []
        temp_viscosity_coefficient_label_list: list[c.CTkLabel] = []
        casting_temperature_label_list: list[c.CTkLabel] = []
        melting_temperature_label_list: list[c.CTkLabel] = []
        flow_index_label_list: list[c.CTkLabel] = []
        cover_heat_transfer_coefficient_label_list: list[c.CTkLabel] = []
        material_id_label_list: list[c.CTkLabel] = []
        id_label_list: list[c.CTkLabel] = []


        # Header row
        self.label = c.CTkLabel(self.root, width=60, height=30, text='id', fg_color='black',
                              text_color='white', font=('Arial', 13, 'bold'))
        self.label.grid(row=0, column=0, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=200, height=30, text='Коэфф. консистенции (Па*с^n)...', fg_color='black',
                              text_color='white', font=('Arial', 13, 'bold'))
        self.label.grid(row=0, column=1, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=250, height=30, text='Темп. коэфф. вязкости (1/°С) ...', fg_color='black',
                              text_color='white', font=('Arial', 13, 'bold'))
        self.label.grid(row=0, column=2, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=200, height=30, text='Темп. приведения (°С)', fg_color='black',
                                text_color='white', font=('Arial', 13, 'bold'))
        self.label.grid(row=0, column=3, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=90, height=30, text='Индекс течения', fg_color='black',
                              text_color='white', font=('Arial', 13, 'bold'))
        self.label.grid(row=0, column=4, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=250, height=30, text='Коэфф. теплоотдачи (Вт/(м2*°С))...', fg_color='black',
                              text_color='white', font=('Arial', 13, 'bold'))
        self.label.grid(row=0, column=5, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=100, height=30, text='ID материала',
                                fg_color='black',
                                text_color='white', font=('Arial', 13, 'bold'))
        self.label.grid(row=0, column=6, padx=1, pady=1)  # position the entry within the frame

        # code for creating table
        for i in range(len(table)):
            for j in range(columns + 2):
                if j == 1:
                    self.label1 = c.CTkLabel(self.root, width=200, height=30, text=f'{table[i].consistency_coefficient}', fg_color='grey',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.label1.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                    consistency_coefficient_label_list.append(self.label1)
                elif j == 2:
                    self.label2 = c.CTkLabel(self.root, width=250, height=30, text=f'{table[i].temp_viscosity_coefficient}', fg_color='grey',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.label2.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                    temp_viscosity_coefficient_label_list.append(self.label2)
                elif j == 3:
                    self.label2 = c.CTkLabel(self.root, width=200, height=30, text=f'{table[i].casting_temperature}', fg_color='grey',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.label2.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                    casting_temperature_label_list.append(self.label2)
                elif j == 4:
                    self.label2 = c.CTkLabel(self.root, width=90, height=30, text=f'{table[i].flow_index}', fg_color='grey',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.label2.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                    flow_index_label_list.append(self.label2)
                elif j == 5:
                    self.label2 = c.CTkLabel(self.root, width=250, height=30, text=f'{table[i].cover_heat_transfer_coefficient}', fg_color='grey',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.label2.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                    cover_heat_transfer_coefficient_label_list.append(self.label2)
                elif j == 6:
                    self.label2 = c.CTkLabel(self.root, width=100, height=30, text=f'{table[i].material_id}', fg_color='grey',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.label2.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                    material_id_label_list.append(self.label2)

                else:
                    self.label3 = c.CTkLabel(self.root, width=60, height=30, text=f'{i + 1}', fg_color='black',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.label3.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                    id_label_list.append(self.label3)

        for i in range(len(consistency_coefficient_label_list)):
            self.math_model_dict[i] = {
                'consistency_coefficient': consistency_coefficient_label_list[i].cget('text'),
                'cover_heat_transfer_coefficient': cover_heat_transfer_coefficient_label_list[i].cget('text'),
                'temp_viscosity_coefficient': temp_viscosity_coefficient_label_list[i].cget('text'),
                'casting_temperature': casting_temperature_label_list[i].cget('text'),
                'flow_index': flow_index_label_list[i].cget('text'),
                'id': id_label_list[i].cget('text'),
                'material_id': material_id_label_list[i].cget('text'),
            }
        print(self.math_model_dict)

        for label in consistency_coefficient_label_list:
            label.bind('<Button-1>', lambda e, label=label: self.on_label_click(label))

    def on_label_click(self, label: c.CTkLabel):
        consistency_coefficient = label.cget('text')
        temp_viscosity_coefficient = ' '
        casting_temperature = ' '
        flow_index = ' '
        id = ' '
        material_id = ' '
        print(consistency_coefficient)
        for key in self.math_model_dict:
            value = self.math_model_dict[key]
            if value['consistency_coefficient'] == consistency_coefficient:
                temp_viscosity_coefficient = value['temp_viscosity_coefficient']
                casting_temperature = value['casting_temperature']
                flow_index = value['flow_index']
                cover_heat_transfer_coefficient = value['cover_heat_transfer_coefficient']
                id = value['id']
                material_id = value['material_id']


        self.root.winfo_toplevel().math_model_params_id.configure(text=id, text_color='black')

        # Consistency coefficient
        entry: c.c.CTkEntry = self.root.winfo_toplevel().math_model_params_consistency_coeff
        entry.delete(0, c.END)
        entry.insert(0, consistency_coefficient)

        # Temperature coefficient...
        temp_coeff_entry: c.c.CTkEntry = self.root.winfo_toplevel().math_model_params_temp_coeff
        temp_coeff_entry.delete(0, c.END)
        temp_coeff_entry.insert(0, temp_viscosity_coefficient)

        # Casting temperature
        casting_temp_entry: c.c.CTkEntry = self.root.winfo_toplevel().math_model_params_casting_temp
        casting_temp_entry.delete(0, c.END)
        casting_temp_entry.insert(0, casting_temperature)

        # Flow index
        flow_index_entry: c.c.CTkEntry = self.root.winfo_toplevel().math_model_params_flow_index
        flow_index_entry.delete(0, c.END)
        flow_index_entry.insert(0, flow_index)

        # Cover heat transfer coeff
        cover_heat_trans_entry: c.c.CTkEntry = self.root.winfo_toplevel().math_model_params_cover_heat_trans
        cover_heat_trans_entry.delete(0, c.END)
        cover_heat_trans_entry.insert(0, cover_heat_transfer_coefficient)

        # Material id
        material_id_entry: c.c.CTkEntry = self.root.winfo_toplevel().math_model_material_id
        material_id_entry.delete(0, c.END)
        material_id_entry.insert(0, material_id)

class ProcessParams_Table:
    def __init__(self, root, table, columns: int):

        self.root = root
        self.process_dict = {}
        cover_speed_label_list: list[c.CTkLabel] = []
        cover_temperature_label_list: list[c.CTkLabel] = []
        id_label_list: list[c.CTkLabel] = []

        # Header row
        self.label = c.CTkLabel(self.root, width=100, height=30, text='id', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=0, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=300, height=30, text='Скорость крышки (м/с)', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=1, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=300, height=30, text='Температура крышки (°С)', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=2, padx=1, pady=1)  # position the entry within the frame

        # code for creating table
        for i in range(len(table)):
            for j in range(columns + 1):
                if j == 1:
                    self.label1 = c.CTkLabel(self.root, width=300, height=30, text=f'{table[i].cover_speed}', fg_color='grey',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.label1.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                    cover_speed_label_list.append(self.label1)
                elif j == 2:
                    self.label2 = c.CTkLabel(self.root, width=300, height=30, text=f'{table[i].cover_temperature}', fg_color='grey',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.label2.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                    cover_temperature_label_list.append(self.label2)
                else:
                    self.label3 = c.CTkLabel(self.root, width=100, height=30, text=f'{i + 1}', fg_color='black',
                                             text_color='white', font=('Arial', 16, 'bold'))
                    self.label3.grid(row=i + 1, column=j, padx=1, pady=1)  # position the entry within the frame
                    id_label_list.append(self.label3)

        for i in range(len(cover_speed_label_list)):
            self.process_dict[i] = {
                'cover_speed': cover_speed_label_list[i].cget('text'),
                'cover_temperature': cover_temperature_label_list[i].cget('text'),
                'id': id_label_list[i].cget('text'),
            }
        print(self.process_dict)

        for label in cover_speed_label_list:
            label.bind('<Button-1>', lambda e, label=label: self.on_label_click(label))

    def on_label_click(self, label: c.CTkLabel):
        cover_speed = label.cget('text')
        cover_temperature = ' '
        id = ' '
        print(cover_speed)
        for key in self.process_dict:
            value = self.process_dict[key]
            if value['cover_speed'] == cover_speed:
                cover_temperature = value['cover_temperature']
                id = value['id']

        self.root.winfo_toplevel().process_params_id.configure(text=id, text_color='black')
        # Cover speed
        entry: c.c.CTkEntry = self.root.winfo_toplevel().cover_speed
        entry.delete(0, c.END)
        entry.insert(0, cover_speed)

        # Cover temperature
        cover_temp_entry: c.c.CTkEntry = self.root.winfo_toplevel().cover_temperature
        cover_temp_entry.delete(0, c.END)
        cover_temp_entry.insert(0, cover_temperature)
