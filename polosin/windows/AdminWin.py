import customtkinter as c
import tkinter as tk
import polosin.windows.Login as Login
from polosin.public.Database_root import Database
from polosin.public.Tables import *
import polosin.public.PasswordGen as PasswordGen
from polosin.public.databases import User
from polosin.public.Tables import *


def donothing():
    pass

database = Database()



# Main window
class Admin(c.CTk):
    def __init__(self):
        super().__init__()
        # Geometry and window config
        self.main_width = 1028
        self.main_height = 800
        self.geometry(f"{self.main_width}x{self.main_height}")
        self.configure(title='Admin window', fg_color='#232E33', padx=0)
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

        # Create the table selection menu
        tables_menu = tk.Menu(menubar,tearoff=0)

        # Add the tables to the file menu
        tables_list = database.get_tables()

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

        menubar.add_cascade(label="Select table", menu=tables_menu,font=('Arial', 20, 'normal'))

        # User Edit frame
        self.user_edit_frame = c.CTkFrame(self, fg_color='#1C414D', width=100)

        self.table_id = c.CTkLabel(self.user_edit_frame, fg_color='#D9D9D9', text=' '
                                   , width=150, text_color='black')
        self.table_id.pack(pady=10, padx=30)

        self.table_username = c.CTkEntry(self.user_edit_frame, fg_color='#D9D9D9', corner_radius=0,
                                         border_width=0, border_color='black', placeholder_text='Username', width=150,
                                         text_color='black')
        self.table_username.pack(pady=10, padx=30)

        self.table_role = c.CTkEntry(self.user_edit_frame, fg_color='#D9D9D9', placeholder_text='Role', corner_radius=0,
                                     border_width=0, border_color='black', width=150, text_color='black')
        self.table_role.pack(pady=10, padx=30)

        # Buttons
        self.user_edit_button = c.CTkButton(self.user_edit_frame, width=150, text='ОБНОВЛЯТЬ', fg_color='#238FB1')
        self.user_delete_button = c.CTkButton(self.user_edit_frame, width=150, text='УДАЛИТЬ', fg_color='#FB5757')
        self.user_add_button = c.CTkButton(self.user_edit_frame, width=150, text='ДОБАВИТЬ', fg_color='#6CD63C',
                                           command=self.user_edit_on_add_click)
        self.user_edit_button.pack(pady=10, padx=30)
        self.user_delete_button.pack(pady=10, padx=30)
        self.user_add_button.pack(pady=10, padx=30)

        # Chanel Edit frame
        self.chanel_edit_frame = c.CTkFrame(self, fg_color='#1C414D', width=100)

        self.chanel_id = c.CTkLabel(self.chanel_edit_frame, fg_color='#D9D9D9', text=' '
                                   , width=150, text_color='black')
        self.chanel_id.pack(pady=10, padx=30)

        self.chanel_width = c.CTkEntry(self.chanel_edit_frame, fg_color='#D9D9D9', corner_radius=0,
                                         border_width=0, border_color='black', placeholder_text='Ширина', width=150,
                                         text_color='black')
        self.chanel_width.pack(pady=10, padx=30)

        self.chanel_depth = c.CTkEntry(self.chanel_edit_frame, fg_color='#D9D9D9', placeholder_text='Глубина', corner_radius=0,
                                     border_width=0, border_color='black', width=150, text_color='black')
        self.chanel_depth.pack(pady=10, padx=30)

        self.chanel_length = c.CTkEntry(self.chanel_edit_frame, fg_color='#D9D9D9', placeholder_text='Длина',
                                     corner_radius=0,
                                     border_width=0, border_color='black', width=150, text_color='black')
        self.chanel_length.pack(pady=10, padx=30)

        # Buttons
        self.chanel_edit_button = c.CTkButton(self.chanel_edit_frame, width=150, text='ОБНОВЛЯТЬ', fg_color='#238FB1')
        self.chanel_delete_button = c.CTkButton(self.chanel_edit_frame, width=150, text='УДАЛИТЬ', fg_color='#FB5757')
        self.chanel_add_button = c.CTkButton(self.chanel_edit_frame, width=150, text='ДОБАВИТЬ', fg_color='#6CD63C',
                                             command=self.user_edit_on_add_click)
        self.chanel_edit_button.pack(pady=10, padx=30)
        self.chanel_delete_button.pack(pady=10, padx=30)
        self.chanel_add_button.pack(pady=10, padx=30)

    def tables_select(self,choice, frame: c.CTkFrame):
        match choice:
            case 'users':
                try:
                    for widget in frame.winfo_children():
                        widget.destroy()
                    self.chanel_edit_frame.grid_forget()
                except Exception as e:
                    print(e)
                else:
                    result = database.get_users()
                    table = result[0]
                    columns = result[1]

                    table = User_Table(frame, table, columns)
                    frame.grid(row=0, column=1, pady=30, columnspan=3)
                    # self.user_edit_frame = c.CTkFrame(self, fg_color='#1C414D', width=100)
                    self.user_edit_frame.grid(row=0, column=0, pady=10, padx=20)
                    # self.left_frame.grid(row=0, column=0, pady=30, padx=20, rowspan=3)
            case 'chanel':
                try:
                    for widget in frame.winfo_children():
                        widget.destroy()
                    self.user_edit_frame.grid_forget()
                except Exception as e:
                    print(e)
                else:
                    result = database.get_chanel_params()
                    table = result[0]
                    columns = result[1]
                    print(table)

                    table = Chanel_Table(frame, table, columns)
                    frame.grid(row=0, column=1, pady=30, columnspan=3)

                    self.chanel_edit_frame.grid(row=0, column=0, pady=10, padx=20)
            case 'material':
                try:
                    for widget in frame.winfo_children():
                        widget.destroy()
                    self.chanel_edit_frame.grid_forget()
                except Exception as e:
                    print(e)
                else:
                    result = database.get_materials()
                    print("Material results")
                    print(result)
                    table = result[0]
                    columns = result[1]

                    table = Material_Table(frame, table, columns)
                    frame.grid(row=0, column=1, pady=30, columnspan=3)
            case 'math_model':
                try:
                    for widget in frame.winfo_children():
                        widget.destroy()
                    self.chanel_edit_frame.grid_forget()
                except Exception as e:
                    print(e)
                else:
                    result = database.get_math_module()
                    table = result[0]
                    columns = result[1]

                    table = MathModel_Table(frame, table, columns)
                    frame.grid(row=0, column=1, pady=30, columnspan=3)
            case 'process_params':
                try:
                    for widget in frame.winfo_children():
                        widget.destroy()
                    self.chanel_edit_frame.grid_forget()
                except Exception as e:
                    print(e)
                else:
                    result = database.get_process_params()
                    table = result[0]
                    columns = result[1]

                    table = ProcessParams_Table(frame, table, columns)
                    frame.grid(row=0, column=1, pady=30, columnspan=3)

    def user_edit_on_add_click(self):
        # Top level window
        self.add_user_window = c.CTkToplevel(self,fg_color="#232E33")
        self.add_user_window.geometry('400x250')
        self.add_user_window.title('Add new user')
        self.add_user_window.resizable(False,False)
        self.add_user_window.attributes('-topmost', 'true')

        # Username
        self.new_username = c.CTkEntry(master=self.add_user_window,placeholder_text='Username',width=200)
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
        self.new_add_button = c.CTkButton(master=self.add_user_window,text='ADD',fg_color='#6CD63C',command=self.on_new_add_click)

        # Warning
        self.warning = c.CTkLabel(master=self.add_user_window,text='Error adding new user',text_color='red')

        # Success
        self.success = c.CTkLabel(master=self.add_user_window,text='User successfully added',text_color='green')
        self.success.pack(pady=10)
        self.success.hide()

        # Pack elements
        self.new_username.pack(pady=10)
        self.new_role.pack(pady=10)
        self.new_password.pack(pady=10)
        self.new_add_button.pack(pady=10)


    def on_new_add_click(self):
        username = self.new_username.get()
        password = self.new_password.get()
        role = self.new_role.get()
        print((username, password, role))
        user = User(username, password, role)
        try:

            database.session.add(user)
            database.session.commit()
            print('User successfully added...')
            self.success.show()
            self.add_user_window.after(200,self.success.destroy())

        except Exception:
            print(Exception)
            self.add_user_window.after(200, self.warning.pack())
            self.add_user_window.after(1000, self.warning.destroy())

    def pack_and_destroy_success(self):
        self.add_user_window.after(1000,self.success.pack(pady=10))


    def file_click(self):
        print("file")

    def change_user_click(self):
        print('change user')
        self.destroy()
        login = Login.Login()
        login.mainloop()

    def help_click(self):
        print('help')
