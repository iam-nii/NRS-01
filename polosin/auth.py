import customtkinter as c
import tkinter
from utilities import User,Database,EncDecPass
from sqlalchemy import select

width = 500
height = 500

class App(c.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(6, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)


ROLE = ''

class Login(App):
    def __init__(self):
        super().__init__()

        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)

        self.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.title("Login")
        self.configure(fg_color='#232E33', pady=80, padx=0)

        # Login label
        self.login = c.CTkLabel(self, text="Login", font=('Bell MT', 60))
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
        self.username = c.CTkEntry(self.username_frame, placeholder_text='Username',text_color='#000000',
                                   placeholder_text_color='#000000', fg_color='#D9D9D9', border_width=0,
                                   width=200, height=40, corner_radius=30)
        self.username.grid(row=1)

        # Password
        # Frame
        self.password_frame = c.CTkFrame(self, fg_color='#232E33')
        self.password_frame.grid_rowconfigure(2, weight=0)
        self.password_frame.grid(row=2, pady=15)

        # Entry
        self.password = c.CTkEntry(self.password_frame, placeholder_text='Password', show='*', text_color='#000000',
                                   placeholder_text_color='#000000', fg_color='#D9D9D9', border_width=0,
                                   width=200, height=40, corner_radius=30)
        self.password.grid(row=1)

        # Admin / user frame
        self.frame = c.CTkFrame(self, fg_color='#232E33')
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid(row=3)

        radio_var = tkinter.IntVar(value=0)
        # Admin radio
        self.combobox_var = c.StringVar(value="role")
        self.combobox = c.CTkComboBox(self.frame, values=["admin", "user"], corner_radius=30,fg_color='#D9D9D9',
                                             command=self.user_select_event, variable=self.combobox_var, width=200,
                                                  text_color='#000000',state='readonly',height=40,dropdown_font=('',20))
        self.combobox.grid(column=0, row=0, pady=10)


        # Login button
        self.login_button = c.CTkButton(self, text='LOGIN', command=self.login_button, width=200, fg_color='#17203D',
                                        corner_radius=15)
        self.login_button.grid(row=4, pady=5)

        # No account
        self.no_account_frame = c.CTkFrame(self, fg_color='#232E33', width=200, height=30)
        self.no_account_frame.grid_columnconfigure(2, weight=0)
        self.no_account_frame.grid(row=5)

        # No account label
        self.no_account_label = c.CTkLabel(self.no_account_frame, text='Dont have an account?')
        self.no_account_label.grid(column=0, row=0, padx=5)

        self.signup = c.CTkLabel(self.no_account_frame, text='Sign Up', text_color='#3DB3FF', cursor='mouse')
        self.signup.bind("<Button-1>", self.signup_command)
        self.signup.grid(column=1, row=0)

    def user_select_event(self):
        print("admin interface")


    def login_button(self):
        database = Database()

        user = select(User).where(User.username == self.username.get())
        # print(user)
        database.select_user(user)


    def signup_command(self, event):
        self.destroy()
        signup = SignUp()
        signup.mainloop()


class SignUp(App):
    def __init__(self):
        super().__init__()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)

        self.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.title("Login")
        self.configure(fg_color='#232E33', pady=80, padx=0)

        # Login label
        self.login = c.CTkLabel(self, text="Sign up", font=('Bell MT', 60))
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
        self.username = c.CTkEntry(self.username_frame, placeholder_text='Username', text_color='#000000',
                                   placeholder_text_color='#000000', fg_color='#D9D9D9', border_width=0,
                                   width=200, height=40, corner_radius=30)
        self.username.grid(row=1)

        # Password
        # Frame
        self.password_frame = c.CTkFrame(self, fg_color='#232E33')
        self.password_frame.grid_rowconfigure(2, weight=0)
        self.password_frame.grid(row=2, pady=15)

        # Entry
        self.password = c.CTkEntry(self.password_frame, placeholder_text='Password', show='*', text_color='#000000',
                                   placeholder_text_color='#000000', fg_color='#D9D9D9', border_width=0,
                                   width=200, height=40, corner_radius=30)
        self.password.grid(row=1)

        # Admin / user frame
        self.frame = c.CTkFrame(self, fg_color='#232E33')
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid(row=3)

        radio_var = tkinter.IntVar(value=0)
        # Admin radio
        self.combobox_var = c.StringVar(value="role")
        self.combobox = c.CTkComboBox(self.frame, values=["admin", "user"], corner_radius=30, fg_color='#D9D9D9',
                                      command=self.user_select_event, variable=self.combobox_var, width=200,
                                      text_color='#000000', state='readonly', height=40, dropdown_font=('', 20))
        self.combobox.grid(column=0, row=0, pady=10)

        # Login button
        self.login_button = c.CTkButton(self, text='LOGIN', command=self.signup_button_click, width=200, fg_color='#17203D',
                                        corner_radius=15)
        self.login_button.grid(row=4, pady=5)

        # No account
        self.no_account_frame = c.CTkFrame(self, fg_color='#232E33', width=200, height=30)
        self.no_account_frame.grid_columnconfigure(2, weight=0)
        self.no_account_frame.grid(row=5)

        # No account label
        self.no_account_label = c.CTkLabel(self.no_account_frame, text='Already have an account?')
        self.no_account_label.grid(column=0, row=0, padx=5)

        self.signup = c.CTkLabel(self.no_account_frame, text='Login', text_color='#3DB3FF', cursor='mouse')
        self.signup.bind("<Button-1>", self.login_command)
        self.signup.grid(column=1, row=0)

    def user_select_event(self):
        print("admin interface")

    def signup_button_click(self):
        global ROLE
        print('Sign up according to the user class')
        username = self.username.get()
        password = self.password.get()
        role = ROLE
        print((username,password,role))
        user = User(username,password,role)
        database = Database()
        try:
            database.session.add(user)
            database.session.commit()
            print('User successfully added...')
            signup_command(True)
        except Exception:
            print(Exception)




    def login_command(self, event):
        self.destroy()
        login = Login()
        login.mainloop()
