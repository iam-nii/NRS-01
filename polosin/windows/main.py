import customtkinter as c
import tkinter as tk

from auth import Login

# Main window
class Main(c.CTk):
    def __init__(self):
        super().__init__()
        # Geometry and window config
        self.main_width = 1028
        self.main_height = 800
        self.geometry(f"{self.main_width}x{self.main_height}")
        self.configure(title='Main window', fg_color='#232E33', padx=0)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(2, weight=1)

        # Create the menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Create the file menu
        filemenu = tk.Menu(menubar, tearoff=0)

        # Add menu items to the file menu
        filemenu.add_command(label="Change User", command=lambda :change_user_click, font=('Arial', 20, 'normal'))
        filemenu.add_command(label="Open", command=donothing, font=('Arial', 20, 'normal'))
        filemenu.add_command(label="Help", command=donothing, font=('Arial', 20, 'normal'))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit, font=('Arial', 20, 'normal'))

        # Add the file menu to the menu bar
        menubar.add_cascade(label="Tools", menu=filemenu, font=('Arial', 20, 'normal'))

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
        # for each element and functio in the tables dictionary, pass they key strin as a paramenter to the function
        for table,func in tables_dict.items():
            tables_menu.add_command(label=f"{table}",command=lambda t = table:func(t,self.table_frame)  ,font=('Arial', 20, 'normal'))

        menubar.add_cascade(label="Select table", menu=tables_menu,font=('Arial', 20, 'normal'))



        # # Left
        # self.left_frame = c.CTkFrame(master=self, bg_color='white', fg_color='transparent', height=500)
        # self.left_frame.grid(row=1, column=0, pady=20, padx=30)
        #
        # # Table selection
        #
        # self.selection_combobox = c.CTkComboBox(self.left_frame, values=self.database.get_tables(),width=200,
        #                                      command=combobox_callback)
        # self.selection_combobox.pack()
        #
        # self.main_frame = c.CTkFrame(self, fg_color='#14282F',height=700, width=700)
        # self.main_frame.grid(row=1, column=1, pady=20, padx=30)  # specify row and column for the frame

        # Table frame


        # # Base frame
        # self.base_frame = c.CTkFrame(self,fg_color='#14282F', height=200)
        # self.base_frame.pack()





    def file_click(self):
        print("file")

    def change_user_click(self):
        self.destroy()
        login = Login()
        login.mainloop()

    def help_click(self):
        print("Help")






