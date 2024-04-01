import customtkinter as c
import tkinter as tk
import optimization_methods.windows.utils as owu
import optimization_methods.windows.Login as Login

database = owu.Database()
def tables_select(choice,frame:c.CTkFrame):
    match choice:
        case 'users':
            try:
                for widget in frame.winfo_children():
                    widget.destroy()
            except Exception as e:
                print(e)
            else:
                result = database.get_users()
                table = result[0]
                columns = result[1]

                table = owu.User_Table(frame, table, columns)
                frame.grid(row=0,column=1,pady=30,padx=50,rowspan=2,columnspan=3)
        case 'chanel':
            try:
                for widget in frame.winfo_children():
                    widget.destroy()
            except Exception as e:
                print(e)
            else:
                result = database.get_chanel_params()
                table = result[0]
                columns = result[1]

                table = Chanel_Table(frame, table, columns)
                frame.grid(row=0,column=1,pady=30,padx=50,rowspan=2,columnspan=3)
        case 'material':
            try:
                for widget in frame.winfo_children():
                    widget.destroy()
            except Exception as e:
                print(e)
            else:
                result = database.get_materials()
                table = result[0]
                columns = result[1]

                table = Material_Table(frame, table, columns)
                frame.grid(row=0,column=1,pady=30,padx=50,rowspan=2,columnspan=3)
        case 'math_model':
            try:
                for widget in frame.winfo_children():
                    widget.destroy()
            except Exception as e:
                print(e)
            else:
                result = database.get_math_module()
                table = result[0]
                columns = result[1]

                table = MathModel_Table(frame, table, columns)
                frame.grid(row=0,column=1,pady=30,padx=50,rowspan=2,columnspan=3)
        case 'process_params':
            try:
                for widget in frame.winfo_children():
                    widget.destroy()
            except Exception as e:
                print(e)
            else:
                result = database.get_process_params()
                table = result[0]
                columns = result[1]

                table = ProcessParams_Table(frame, table, columns)
                frame.grid(row=0,column=1,pady=30,padx=50,rowspan=2,columnspan=3)

def donothing():
    pass
class Main(c.CTk):
    def __init__(self):
        super().__init__()
        # Geometry and window config
        self.main_width = 1028
        self.main_height = 800
        self.geometry(f"{self.main_width}x{self.main_height}")
        self.configure(title='Main window', fg_color='#232E33', padx=0)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

        # --------------------- Menu bar ----------------------------------------------- #

        # Create the menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Create the file menu
        filemenu = tk.Menu(menubar, tearoff=0)

        # Add menu items to the file menu
        filemenu.add_command(label="Change User", command=self.change_user_click, font=('Arial', 20, 'normal'))
        filemenu.add_command(label="Open", command=donothing, font=('Arial', 20, 'normal'))
        filemenu.add_command(label="Help", command=donothing, font=('Arial', 20, 'normal'))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit, font=('Arial', 20, 'normal'))

        # Add the file menu to the menu bar
        menubar.add_cascade(label="Tools", menu=filemenu, font=('Arial', 20, 'normal'))

        # ----------------------------- End of Menu ----------------------------------- #

        # Create the table selection menu
        tables_menu = tk.Menu(menubar,tearoff=0)

        # Add the tables to the file menu
        tables_list = database.get_tables()

        tables_dict = {
            table:tables_select for table in tables_list
        }
        print(tables_dict)
        self.table_frame = c.CTkFrame(self)
        # self.table_frame.pack(pady=30)
        # for each element and function in the tables dictionary, pass they key string as a paramenter to the function
        for table,func in tables_dict.items():
            tables_menu.add_command(label=f"{table}",command=lambda t = table:func(t,self.table_frame)  ,font=('Arial', 20, 'normal'))

        menubar.add_cascade(label="Select table", menu=tables_menu,font=('Arial', 20, 'normal'))

        self.left_frame = c.CTkFrame(self, fg_color='#1C414D', width=100)
        self.left_frame.grid(row=0,column=0,pady=30,padx=20, rowspan=3)

        self.table_id = c.CTkLabel(self.left_frame,fg_color='#D9D9D9',
                                   text='sample text', width=150, text_color='black')
        self.table_id.pack(pady=10, padx=30)

        self.table_username = c.CTkEntry(self.left_frame, fg_color='#D9D9D9', corner_radius=0,
                                     border_width=0,border_color='black', placeholder_text='Username', width=150, text_color='black')
        self.table_username.pack(pady=10, padx=30)

        self.table_role = c.CTkEntry(self.left_frame, fg_color='#D9D9D9',placeholder_text='Role', corner_radius=0,
                                     border_width=0,border_color='black', width=150, text_color='black')
        self.table_role.pack(pady=10, padx=30)

        self.edit_button = c.CTkButton(self.left_frame, width=150, text='EDIT',fg_color='#238FB1')
        self.delete_button = c.CTkButton(self.left_frame, width=150, text='DELETE',fg_color='#FB5757')
        self.edit_button.pack(pady=10,padx=30)
        self.delete_button.pack(pady=10,padx=30)

    def file_click(self):
        print("file")

    def change_user_click(self):
        self.destroy()
        login = Login.Login()
        login.mainloop()

    def help_click(self):
        print("Help")

    def user_control(self,username):
        self.table_username.config(text=username)