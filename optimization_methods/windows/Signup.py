import optimization_methods.windows.Login as Login
import optimization_methods.windows.utils as owu
import customtkinter as c
import tkinter

width = 500
height = 500
ROLE = ''

class App(c.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(6, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

def donothing():
    pass

class SignUp(App):
    def __init__(self):
        super().__init__()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)

        self.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.title("Регистрация")
        self.configure(fg_color='#232E33', pady=80, padx=0)

        # Login label
        self.login = c.CTkLabel(self, text="Регистрация", font=('Bell MT', 30))
        self.login.grid(row=0, pady=10)

        # Username
        # Frame
        self.username_frame = c.CTkFrame(self, fg_color='#232E33')
        self.username_frame.grid_rowconfigure(2, weight=0)
        self.username_frame.grid(row=1, pady=10)

        # Label
        # self.username_label = c.CTkLabel(self.username_frame, text='Username', anchor="w", justify="left",
        #                                  width=200, height=30)
        # self.username_label.grid(row=0)

        # Entry
        self.username = c.CTkEntry(self.username_frame, placeholder_text='Логин', text_color='#000000',
                                   placeholder_text_color='#000000', fg_color='#D9D9D9', border_width=0,
                                   width=200, height=40, corner_radius=30)
        self.username.grid(row=1)

        # Password
        # Frame
        self.password_frame = c.CTkFrame(self, fg_color='#232E33')
        self.password_frame.grid_rowconfigure(2, weight=0)
        self.password_frame.grid(row=2, pady=15)

        # Entry
        self.password = c.CTkEntry(self.password_frame, placeholder_text='Пароль', show='*', text_color='#000000',
                                   placeholder_text_color='#000000', fg_color='#D9D9D9', border_width=0,
                                   width=200, height=40, corner_radius=30)
        self.password.grid(row=1)

        # Admin / user frame
        self.frame = c.CTkFrame(self, fg_color='#232E33')
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid(row=3)

        radio_var = tkinter.IntVar(value=0)

        # combobox - User role
        self.combobox_var = c.StringVar(value="Роль")
        self.combobox = c.CTkComboBox(self.frame, values=["Администратор", "Исследователь"], corner_radius=30,
                                      fg_color='#D9D9D9',
                                      command=self.user_select_event, variable=self.combobox_var, width=200,
                                      text_color='#000000', state='readonly', height=40, dropdown_font=('', 20))
        self.combobox.grid(column=0, row=0, pady=10)

        # Login button
        self.login_button = c.CTkButton(self, text='Зарегистрироваться', command=self.signup_button_click, width=200,
                                        fg_color='#17203D',
                                        corner_radius=15)
        self.login_button.grid(row=4, pady=5)

        # No account
        self.no_account_frame = c.CTkFrame(self, fg_color='#232E33', width=200, height=30)
        self.no_account_frame.grid_columnconfigure(2, weight=0)
        self.no_account_frame.grid(row=5)

        # No account label
        self.no_account_label = c.CTkLabel(self.no_account_frame, text='Уже в системе?')
        self.no_account_label.grid(column=0, row=0, padx=5)

        self.signup = c.CTkLabel(self.no_account_frame, text='Войти', text_color='#3DB3FF', cursor='mouse')
        self.signup.bind("<Button-1>", self.login_command)
        self.signup.grid(column=1, row=0)

    def user_select_event(self, role):
        print(role)
        global ROLE
        ROLE = role

    def signup_button_click(self):
        global ROLE
        print('Sign up according to the user class')
        username = self.username.get()
        password = self.password.get()
        # role = ROLE
        print((username, password, ROLE))
        user = owu.User(username, password, ROLE)
        database = owu.Database()
        try:
            database.session.add(user)
            database.session.commit()
            print('User successfully added...')
            self.signup_command(True)
        except Exception:
            print(Exception)

    def login_command(self, event):
        self.destroy()
        login = Login.Login()
        login.mainloop()

    def signup_command(self, event: bool):
        pass

