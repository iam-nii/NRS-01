from PyQt6 import QtWidgets as qw, uic
import optimization_methods.windows.utils as owu
from optimization_methods.windows.rootentry import RootEntry
import optimization_methods.windows.mainWindows.userWindow_ui as userWindow
import optimization_methods.windows.mainWindows.adminWindow_ui as adminWindow
import optimization_methods.windows.mainWindows.signupWindow_ui as signUpWindow

class LoginWindow(RootEntry):
    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.init_ui()

    def init_ui(self):
        # Import the ui file
        self.window:qw.QMainWindow = uic.loadUi("./windows/mainWindows/login.ui")

        # Initialize UI elements
        self.username = self.window.username_entry
        self.password:qw.QLineEdit = self.window.password_entry
        self.password.setEchoMode(qw.QLineEdit.EchoMode.Password)
        self.role:qw.QComboBox = self.window.role_cbx
        self.signup = self.window.signup_link
        self.signup.setStyleSheet("color: blue;")
        self.signup.mousePressEvent = self.signup_clicked

        self.login_button = self.window.login_btn
        self.login_button.clicked.connect(self.login_clicked)

        self.user_not_found = self.window.user_not_found
        self.user_not_found.setStyleSheet("color: red")
        self.user_not_found.setHidden(True)

    def login_clicked(self):
        database = owu.Database()

        username = self.username.text()
        password = self.password.text()
        role:str = self.role.currentText()
        user = owu.User(username,password,role)


        # if role == "Админ":
        #     role = "Администратор"
        print((username,password,role))

        # self.database = owu.Database()

        result = database.select_user(user, username)
        print(result)
        if result is not None:
            print(f'User password: {result.password}')
            self.decryptor = owu.EncDecPass()
            user_password = self.decryptor.decrypt_password(encoded_password=result.password).decode()
            print(f'Decrypted password: {user_password}')

            if password == user_password and role == result.role:
                print("Logging in...")
                if role.lower() == "пользователь":
                    # Create an instance of MainWindow
                    self.user_window = userWindow.UserWindow(self.app)
                    self.user_window.window.show()  # Show the main window
                    self.window.close()
                if role.lower() == "админ":
                    self.admin_window = adminWindow.AdminWindow(self.app)
                    self.admin_window.window.show()
                    self.window.close()
            else:
                self.user_not_found.setHidden(False)
        else:
            self.user_not_found.setHidden(False)




    def signup_clicked(self, event):
        print("Signing up...")
        self.signup_window = signUpWindow.SignupWindow(self.app)
        self.signup_window.window.show()
        self.window.close()