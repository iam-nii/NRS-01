import customtkinter as c


class User_Table:
    def __init__(self, root,table,columns:int):

        self.root = root
        self.users_dict = {}

        # Header row
        self.label = c.CTkLabel(self.root, width=100, height=30, text='id', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=0, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=300, height=30, text='Username', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=1, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=300, height=30, text='Role', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=2, padx=1, pady=1)  # position the entry within the frame

        username_label_list: list[c.CTkLabel] = []
        role_label_list: list[c.CTkLabel] = []
        id_label_list: list[c.CTkLabel] = []

        # code for creating table
        for i in range(len(table)):
            for j in range(columns + 1):
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
                else:
                    self.label3 = c.CTkLabel(root, width=100, height=30, text=f'{i+1}', fg_color='black',
                                          text_color='white', font=('Arial', 16, 'bold'))
                    self.label3.grid(row=i+1, column=j, padx=1, pady=1)  # position the entry within the frame
                    id_label_list.append(self.label3)

        for i in range(len(username_label_list)):
            self.users_dict[i] = {
                'username': username_label_list[i].cget('text'),
                'role': role_label_list[i].cget('text'),
                'id':id_label_list[i].cget('text'),
            }
        print(self.users_dict)

        for label in username_label_list:
            label.bind('<Button-1>',lambda e,label = label: self.on_label_click(label))

    def on_label_click(self,label:c.CTkLabel):
        username = label.cget('text')
        role = ' '
        id = ' '
        print(username)
        for key in self.users_dict:
            value = self.users_dict[key]
            if value['username'] == username:
                id = value['id']
                role = value['role']


        self.root.winfo_toplevel().table_id.configure(text=id, text_color='black')
        # Username
        entry:c.c.CTkEntry = self.root.winfo_toplevel().table_username
        entry.delete(0,c.END)
        entry.insert(0,username)

        # role
        role_entry:c.c.CTkEntry = self.root.winfo_toplevel().table_role
        role_entry.delete(0,c.END)
        role_entry.insert(0,role)
        # self.root.winfo_toplevel().table_username.configure(text=username, text_color='black',width=100)
        # self.root.winfo_toplevel().table_role.configure(text=role, text_color='black',width=100)


class Chanel_Table:
    def __init__(self, root,table,columns:int):

        # Header row
        self.label = c.CTkLabel(root, width=100, height=30, text='id', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=0, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(root, width=300, height=30, text='width', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=1, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(root, width=300, height=30, text='depth', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=2, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(root, width=300, height=30, text='length', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=3, padx=1, pady=1)  # position the entry within the frame

class Material_Table:
    def __init__(self, root, table, columns: int):

        # Header row
        self.label = c.CTkLabel(root, width=100, height=30, text='id', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=0, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(root, width=100, height=30, text='material', fg_color='black',
                                text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=1, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(root, width=300, height=30, text='Density', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=2, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(root, width=300, height=30, text='Heat Capacity', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=3, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(root, width=300, height=30, text='Melting Temperature', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=4, padx=1, pady=1)  # position the entry within the frame

class MathModel_Table:
    def __init__(self, root, table, columns: int):

        # Header row
        self.label = c.CTkLabel(root, width=100, height=30, text='id', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=0, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(root, width=300, height=30, text='Consistency coefficient', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=1, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(root, width=300, height=30, text='Temp Viscosity coefficient', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=2, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(root, width=300, height=30, text='Flow index', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=3, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(root, width=300, height=30, text='Cover heat transfer coefficient', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=43, padx=1, pady=1)  # position the entry within the frame

class ProcessParams_Table:
    def __init__(self, root, table, columns: int):

        # Header row
        self.label = c.CTkLabel(root, width=100, height=30, text='id', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=0, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(root, width=300, height=30, text='Cover speed', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=1, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(root, width=300, height=30, text='Heat Capacity', fg_color='black',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=2, padx=1, pady=1)  # position the entry within the frame
