from optimization_methods.windows.root import App
import customtkinter as c
import tkinter

class Login(App):
    def __init__(self):
        super().__init__()
        width = 500
        height = 400
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)

        self.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.title("Login")
        self.configure(fg_color='#466AE2',pady=80,padx=0)


        # Login label
        self.login = c.CTkLabel(self,text="Login",font=('Cooper Black',30))
        self.login.grid(row=0,pady=10)

        # Username
        # Frame
        self.username_frame = c.CTkFrame(self,fg_color='#466AE2')
        self.username_frame.grid_rowconfigure(2,weight=0)
        self.username_frame.grid(row=1, pady=10)

        # Label
        self.username_label = c.CTkLabel(self.username_frame,text='Username',anchor="w", justify="left",
                                         width=200, height=30)
        self.username_label.grid(row=0)

        # Entry
        self.username = c.CTkEntry(self.username_frame,placeholder_text='Type you username',
                                   placeholder_text_color='#4A70EF', fg_color='#2047C9', border_width=0,
                                   width=200, height=30)
        self.username.grid(row=1)

        # Password
        # Frame
        self.password_frame = c.CTkFrame(self,fg_color='#466AE2')
        self.password_frame.grid_rowconfigure(2,weight=0)
        self.password_frame.grid(row=2, pady=10)

        # Label
        self.password_label = c.CTkLabel(self.password_frame,text='Password', anchor="w", justify="left",
                                         width=200, height=30)
        self.password_label.grid(row=0)

        # Entry
        self.password = c.CTkEntry(self.password_frame,placeholder_text='Type your password',show='*',
                                   placeholder_text_color='#4A70EF',fg_color='#2047C9', border_width=0,
                                   width=200, height=30)
        self.password.grid(row=1)

        # Admin / user frame
        self.frame = c.CTkFrame(self,fg_color='#466AE2')
        self.frame.grid_columnconfigure(2,weight=1)
        self.frame.grid(row=3, pady=10)

        radio_var = tkinter.IntVar(value=0)
        # Admin radio
        self.admin_radio = c.CTkRadioButton(self.frame,text="Admin", command=self.admin_event, variable=radio_var,value=1)
        self.admin_radio.grid(column=0,row=0)

        # user radio
        self.user_radio = c.CTkRadioButton(self.frame,text='User', command=self.user_event, variable=radio_var,value=2)
        self.user_radio.grid(column=1,row=0)

        # Login button
        self.login_button = c.CTkButton(self, text='LOGIN', command=self.login_button, width=200,fg_color='#17203D',
                                        corner_radius=15)
        self.login_button.grid(row=4, pady=5)
        print(self.login_button.cget('corner_radius'))

        # No account
        self.no_account_frame = c.CTkFrame(self,fg_color='#466AE2',width=200, height=30)
        self.no_account_frame.grid_columnconfigure(2,weight=0)
        self.no_account_frame.grid(row=5)

        # No account label
        self.no_account_label = c.CTkLabel(self.no_account_frame,text='Dont have an account?')
        self.no_account_label.grid(column=0, row=0, padx=5)

        self.signup = c.CTkLabel(self.no_account_frame,text='Sign Up',text_color='#3DB3FF',cursor='mouse')
        self.signup.bind("<Button-1>", self.signup_command)
        self.signup.grid(column=1,row=0)



    def admin_event(self):
        print("admin interface")

    def user_event(self):
        print("user interface")

    def login_button(self):
        print('Login according to the user class')

    def signup_command(self,event):
        signup = SignUp()

        signup.mainloop()

        self.destroy()
