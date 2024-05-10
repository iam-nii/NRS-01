import sys
from PyQt6 import QtWidgets as qw, uic
from optimization_methods.windows.root import Root
import optimization_methods.windows.utils as owu
import optimization_methods.windows.loginWindow_ui as Login

class SignupWindow(Root):
    def __init__(self,app):
        super().__init__(app)
        self.app = app
        self.init_ui()

    def init_ui(self):
        # Import the ui file
        self.window:qw.QMainWindow = uic.loadUi("./windows/signup.ui")
        # self.window.setStyleSheet("background-color:#ECECEC")

        # Username Entry
        self.username: qw.QLineEdit = self.window.username_entry
        # Password Entry
        self.password: qw.QLineEdit = self.window.password_entry
        # Role combobox
        self.role: qw.QComboBox = self.window.role_cbx
        # Login link
        self.login: qw.QLabel = self.window.login_link
        self.login.setStyleSheet("color: blue;")
        # SignUp signal - connect
        self.login.mousePressEvent = self.login_clicked  # Install event filter

        # Signup button
        self.signup_button: qw.QPushButton = self.window.signup_btn
        # SignUp signal - connect
        self.signup_button.clicked.connect(self.signup_clicked)

        # User not found
        self.user_not_found:qw.QLabel = self.window.user_not_found
        self.user_not_found.setStyleSheet("color: red")
        self.user_not_found.setHidden(True)


        # self.window.show()
        # self.app.exec()
    def signup_clicked(self):
        print("signing up...")
        username = self.username.text()
        password = self.password.text()
        role = self.role.currentText()

        print(f"{username}: {password}: {role}")
        if username == "admin" and password == "password":
            print("true")

            self.login_window = Login.LoginWindow()
            self.login_window.window.show()
            self.window.close()

        # user = owu.User(username, password, ROLE)
        # database = owu.Database()
        # try:
        #     database.session.add(user)
        #     database.session.commit()
        #     print('User successfully added...')
        #     login = Login.Loginwindow()
        #     self.close()
        # except Exception:
        #     print(Exception)

    def login_clicked(self,event):
        print("Loggin in...")
        self.login_window = Login.LoginWindow(self.app)
        self.login_window.window.show()
        self.window.close()

# signup = SignupWindow()