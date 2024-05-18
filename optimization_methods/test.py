from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(300, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Login label
        login_label = QLabel("Login")
        login_label.setFont(QFont("Arial", 20))
        layout.addWidget(login_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Username and password fields
        username_label = QLabel("Username:")
        self.username_field = QLineEdit()
        password_label = QLabel("Password:")
        self.password_field = QLineEdit(echoMode=QLineEdit.EchoMode.Password)

        username_layout = QHBoxLayout()
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_field)

        password_layout = QHBoxLayout()
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_field)

        layout.addLayout(username_layout)
        layout.addLayout(password_layout)

        # Login button
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_field.text()
        password = self.password_field.text()

        # Replace with your actual credential check
        if username == "admin" and password == "secret":
            # Create an instance of MainWindow
            self.main_window = MainWindow()
            self.close()
            self.main_window.show()  # Show the main window
        else:
            # Show error message
            print("Invalid credentials")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setFixedSize(500, 300)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Welcome label
        welcome_label = QLabel("Welcome, Admin!")
        welcome_label.setFont(QFont("Arial", 18))
        layout.addWidget(welcome_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Change user button
        change_user_button = QPushButton("Change User")
        change_user_button.clicked.connect(self.open_login_window)
        layout.addWidget(change_user_button, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_login_window(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon("your_icon.png"))  # Set your app icon (optional)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
