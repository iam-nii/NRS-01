import sys
from PyQt6 import QtWidgets as qw, uic
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex
from optimization_methods.windows.rootentry import RootEntry
import optimization_methods.windows.mainWindows.loginWindow_ui as Login

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data[1:] # Remove the first row from the data list
        self._headers = data[0] # Store the first row as the headers
    def rowCount(self, parent=QModelIndex()):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        # The length of the longest list
        return len(max(self._data,key=len))

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        # Display data
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            try:
                return self._data[index.row()][index.column()]
            except IndexError:
                return ''

    def setData(self, index, value, role=Qt.ItemDataRole.DisplayRole):
        if role != Qt.ItemDataRole.DisplayRole:
            return False
        row = index.row()
        column = index.column()
        self._data[row][column] = value
        self.dataChanged.emit(index, index)
        return True

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._headers[section]

class UserWindow(RootEntry):
    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.init_ui()

    def init_ui(self):
        try:
            # self.window = uic.loadUi("./windows/mainWindows/userWindow_ui.ui")
            self.window = uic.loadUi("./windows/mainWindows/userWindow1_ui.ui")
            # Input frame
            self.input_frame:qw.QTabWidget = self.window.input_frame

            # Table frame
            self.table_frame:qw.QTabWidget = self.window.table_frame
            self.TABLE = self.table_frame.findChild(qw.QTableView,"results_table")

            # 2d Graph frame
            self.twod_frame:qw.QTabWidget = self.window.twod_graph_frame

            # 3d Graph frame
            self.threed_frame:qw.QTabWidget = self.window.threed_frame

            # Menu options
            self.change_user_menu: qw.QWidgetAction = self.window.changeUser_menu.triggered.connect(
                self.change_user)
            self.help_menu: qw.QWidgetAction = self.window.help_menu.triggered.connect(self.help_menu_click)
            self.exit: qw.QWidgetAction = self.window.exit_menu.triggered.connect(self.exit_menu_click)

            self.v1: qw.QLineEdit = self.input_frame.findChild(qw.QLineEdit,"v1_txt")
            # print(self.v1)
            self.v2: qw.QLineEdit = self.input_frame.findChild(qw.QLineEdit,"v2_txt")
            self.min_a2: qw.QLineEdit = self.input_frame.findChild(qw.QLineEdit,"min_a2_txt")
            self.min_a1: qw.QLineEdit = self.input_frame.findChild(qw.QLineEdit,"min_a1_txt")
            self.max_a1: qw.QLineEdit = self.input_frame.findChild(qw.QLineEdit,"max_a1_txt")
            self.max_a2: qw.QLineEdit = self.input_frame.findChild(qw.QLineEdit,"max_a2_txt")

            self.mu = self.mu1 = self.alpha = self.alpha1 = self.beta = self.beta1 = 1

            self.accuracy: qw.QLineEdit = self.input_frame.findChild(qw.QLineEdit,"accuracy_txt")
            self.solution_method: qw.QComboBox = self.input_frame.findChild(qw.QComboBox,"method_cbx")

            # Calculate button
            self.calculate_btn = self.input_frame.findChild(qw.QPushButton, "calculate_btn")
            # print(self.calculate_btn)
            self.calculate_btn.clicked.connect(self.calculate_btn_clicked)
        except Exception as e:
            print(e)


    def calculate_btn_clicked(self):
        # Define the constants
        N = 2  # Number of reactors
        V1 = float(self.v1.text())  # Working volume of reactor 1 (m^3)
        V2 = float(self.v2.text())  # Working volume of reactor 2 (m^3)
        alpha = float(self.alpha)
        alpha1 = float(self.alpha1)
        beta = float(self.beta1)
        beta1 = float(self.beta1)
        mu = float(self.mu)
        mu1 = float(self.mu1)
        step = 0.1

        # print("Calculating...")

        C = []
        A1_list = []
        A2_list = []
        total_production = []
        A1 = float(self.min_a1.text())
        A2 = float(self.min_a2.text())
        step = 0.01  # set the step size for incrementing A1 and A2
        while A1 <= float(self.max_a1.text()):
            A2 = float(self.min_a2.text())  # reset A2 to its initial value
            while A2 <= float(self.max_a2.text()):
                # print("Calculating...")
                # Calculate the production of C in kg/h
                output = alpha * (A1 ** 2 + beta * A2 - mu * V1) ** N + alpha1 * (beta1 * A1 + A2 ** 2 - mu1 * V2) ** N
                C.append(round(output, 2))
                A1_list.append(A1)
                A2_list.append(A2)

                # Calculate the total production in 8 hours (workday)
                total_production.append(output * 8)
                A2 += step
            A1 += step
        print(A1_list)
        print(A2_list)
        print(len(C))
        print(len(total_production))


    def change_user(self):
        print("Changing user...")
        self.login_window = Login.LoginWindow()
        self.login_window.window.show()
        self.window.close()

    def help_menu_click(self):
        print("Helping...")

    def exit_menu_click(self):
        print("Exiting...")
        self.window.close()

# self.user_window = userWindow.UserWindow(self.app)
# self.user_window.window.show()  # Show the main window

# app = qw.QApplication(sys.argv)
# window = UserWindow(app)
# window.window.show()
# app.exec()
