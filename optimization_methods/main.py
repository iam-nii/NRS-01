# import optimization_methods.windows.Login as Login
#
# app = Login.Login()
#
# app.mainloop()

import sys
from PyQt6 import QtWidgets as qw
from optimization_methods.windows.mainWindows.loginWindow_ui import LoginWindow

def main():
    app = qw.QApplication(sys.argv)
    login_window = LoginWindow(app)
    login_window.window.show()
    app.exec()

if __name__ == "__main__":
    main()