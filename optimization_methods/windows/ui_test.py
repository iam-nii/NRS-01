
# import optimization_methods.windows.UserWindow as Ui_Win
# from optimization_methods.windows.UserWindow import Ui_MainWindow
import optimization_methods.windows.UserWin as user_win
import sys
from PyQt6 import QtWidgets, uic



class MainWindow(QtWidgets.QMainWindow, user_win.Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

APP = QtWidgets.QApplication(sys.argv)
window = MainWindow()
# window.show()
# APP.exec()