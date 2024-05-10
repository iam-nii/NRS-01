import sys
from PyQt6 import QtWidgets as qw, uic
from optimization_methods.windows.root import Root
import optimization_methods.windows.userWindow_ui as userWindow
import optimization_methods.windows.signupWindow_ui as signUpWindow

class LoginWindow(Root):
    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.init_ui()

    def init_ui(self):
        # Import the ui file
        self.window:qw.QMainWindow = uic.loadUi("./windows/login.ui")

        # Initialize UI elements
        self.username = self.window.username_entry
        self.password = self.window.password_entry
        self.role = self.window.role_cbx
        self.signup = self.window.signup_link
        self.signup.setStyleSheet("color: blue;")
        self.signup.mousePressEvent = self.signup_clicked

        self.login_button = self.window.login_btn
        self.login_button.clicked.connect(self.login_clicked)

        self.user_not_found = self.window.user_not_found
        self.user_not_found.setStyleSheet("color: red")
        self.user_not_found.setHidden(True)

    def login_clicked(self):
        username = self.username.text()
        print(username)

        print("Logging in...")
        # Create an instance of MainWindow
        self.user_window = userWindow.UserWindow(self.app)
        self.user_window.window.show()  # Show the main window
        self.window.close()
        # self.app.exec()


        # app = qw.QApplication(sys.argv)
        # login_window = LoginWindow(app)
        # login_window.window.show()
        # app.exec()

    def signup_clicked(self, event):
        print("Signing up...")
        self.signup_window = signUpWindow.SignupWindow(self.app)
        self.signup_window.window.show()
        self.window.close()