import customtkinter as c
import optimization_methods.windows.utils as owu
import optimization_methods.windows.Signup as Signup
import optimization_methods.windows.MainWin as MainWin
import optimization_methods.windows.ui_test as UserWindow
import customtkinter as c
from PyQt6 import QtWidgets, uic
import sys


app = UserWindow.APP

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

class Login(App):
    def __init__(self):
        super().__init__()

        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)

        self.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.title("Логин")
        self.configure(fg_color='#232E33', pady=80, padx=0)

        # Login label
        self.login = c.CTkLabel(self, text="Авторизация", font=('Bell MT', 30))
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

        # radio_var = tkinter.IntVar(value=0)
        # Combobox
        self.combobox_var = c.StringVar(value="Роль")
        self.combobox = c.CTkComboBox(self.frame, values=["Администратор", "Исследователь"], corner_radius=30,
                                      fg_color='#D9D9D9',
                                      command=self.user_select_event, variable=self.combobox_var, width=200,
                                      text_color='#000000', state='readonly', height=40, dropdown_font=('', 20))
        self.combobox.grid(column=0, row=0, pady=10)

        # Login button
        self.login_button = c.CTkButton(self, text='Войти', command=self.login_button, width=200, fg_color='#17203D',
                                        corner_radius=15)
        self.login_button.grid(row=4, pady=5)

        # Invalid user
        self.label = c.CTkLabel(self, text='Пользователь не найден!', text_color='red')

        # No account
        self.no_account_frame = c.CTkFrame(self, fg_color='#232E33', width=200, height=30)
        self.no_account_frame.grid_columnconfigure(2, weight=0)
        self.no_account_frame.grid(row=6)

        # No account label
        self.no_account_label = c.CTkLabel(self.no_account_frame, text='Нет в системе?')
        self.no_account_label.grid(column=0, row=0, padx=5)

        self.signup = c.CTkLabel(self.no_account_frame, text='Регистрация', text_color='#3DB3FF', cursor='mouse')
        self.signup.bind("<Button-1>", self.signup_command)
        self.signup.grid(column=1, row=0)

    def user_select_event(self, selection):
        print(selection)

    def login_button(self):
        database = owu.Database()

        # user = select(User).where(User.username == self.username.get())
        # print(user)
        # result = database.select_user(user)

        username = self.username.get()
        password = self.password.get()
        role = self.combobox.get()
        user = owu.User(username, password, role)

        result = database.select_user(user, self.username.get())
        print(result)
        if result is not None:
            print(f'User password: {result.password}')
            decryptor = owu.EncDecPass()
            user_password = decryptor.decrypt_password(encoded_password=result.password).decode()
            print(f'Decrypted password: {user_password}')

            if password == user_password:
                print('Login success')
                self.destroy()
                user_window = UserWindow.MainWindow()
                user_window.show()
                app.exec()
                # main = MainWin.Main()
                # main.mainloop()

        else:
            self.label.grid(row=5)

    def signup_command(self, event):
        try:
            self.destroy()
        except Exception:
            print(Exception)
        finally:
            signup = SignUp()
            signup.mainloop()

    def signup_command(self, event):
        self.destroy()
        signup = Signup.SignUp()
        signup.mainloop()
