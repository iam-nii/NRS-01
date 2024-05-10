import sys
from PyQt6 import QtWidgets as qw, uic
from optimization_methods.windows.rootentry import RootEntry

class UserWindow(RootEntry):
    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.init_ui()

    def init_ui(self):
        self.window = uic.loadUi("./windows/userWindow_ui.ui")

# app = qw.QApplication(sys.argv)
# window = UserWindow(app)
# window.window.show()
# app.exec()
