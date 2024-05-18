import sys
import numpy as np
from PyQt6 import QtWidgets as qw, uic
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex, QRunnable,QThreadPool, pyqtSlot
import pyqtgraph as pg
from optimization_methods.windows.rootentry import RootEntry
import optimization_methods.windows.mainWindows.loginWindow_ui as Login
# from optimization_methods.windows.ui_test import GraphWindow
import matplotlib
matplotlib.use('QtAgg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from PyQt6.QtCore import QMetaObject, Qt
from PyQt6.QtWidgets import QVBoxLayout

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

DATA = [["A1", "A2","C" ,"Целевая Функция"]]

class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)
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

class UserWindow(qw.QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.init_ui()
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    def init_ui(self):
        try:
            # self.window = uic.loadUi("./windows/mainWindows/userWindow_ui.ui")
            self.window = uic.loadUi("./windows/mainWindows/userWindow1_ui.ui")
            # Input frame
            self.input_frame:qw.QWidget = self.window.input_frame

            # Table frame
            self.table_frame:qw.QWidget = self.window.table_frame
            self.TABLE = self.table_frame.findChild(qw.QTableView,"results_table")

            # 2d Graph frame
            # self.graph = MplCanvas(self, width=5, height=4, dpi=100)
            # self.twod_frame = QWidget(self)
            # layout = QVBoxLayout()
            # layout.addWidget(self.graph)
            # self.twod_frame.setLayout(layout)
            # self.plot_2d_graph(DATA)  # Call your plotting function
            self.graph = MplCanvas(self,width=10,height=7,dpi=100)
            self.twod_frame = self.window.twod_graph_frame
            layout = QVBoxLayout()
            layout.addWidget(self.graph)
            self.twod_frame.setLayout(layout)

            # 3d Graph frame
            self.threed_frame:qw.QWidget = self.window.threed_frame

            # Menu options
            self.change_user_menu: qw.QWidge-tAction = self.window.changeUser_menu.triggered.connect(
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


    def thread_calculate_btn(self):
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

        # Ensure all required variables are initialized
        C = []
        A1_list = []
        A2_list = []
        total_production = []
        # DATA = []  # Ensure DATA is defined

        # Convert text inputs to float and handle potential conversion errors
        try:
            min_a1 = float(self.min_a1.text())  # 1
            max_a1 = float(self.max_a1.text())  # 10
            min_a2 = float(self.min_a2.text())  # 1
            max_a2 = float(self.max_a2.text())  # 10
        except ValueError:
            print("Error: Ensure that the text inputs are valid numeric values.")
            raise

        step = 0.1  # Step size for incrementing A1 and A2
        print("Calculating...")

        A1 = min_a1
        while A1 <= max_a1:
            A2 = max_a2  # Reset A2 to its initial value at the start of each A1 loop
            while A2 >= min_a2:
                if A1 + A2 < 8:
                    # Calculate the production of C in kg/h
                    output = alpha * (A1 ** 2 + beta * A2 - mu * V1) ** N + alpha1 * (
                            beta1 * A1 + A2 ** 2 - mu1 * V2) ** N

                    A1_list.append(A1)
                    A2_list.append(A2)

                    # Calculate the total production in 8 hours (workday)
                    function = output * 8
                    DATA.append([round(A1, 1), round(A2, 1), round(output, 2), round(function, 2)])
                A2 -= step
            A1 += step

        print("Calculation completed.")
        print("Building table...")
        data_model = TableModel(DATA)
        self.TABLE.setModel(data_model)
        self.TABLE.setColumnWidth(0, 120)  # Set the width of the first column to 100 pixels
        self.TABLE.setColumnWidth(1, 120)
        self.TABLE.setColumnWidth(2, 120)
        self.TABLE.setColumnWidth(3, 150)
        print("Table build done.")

        self.thread_plot_2d_graph(DATA)

    def calculate_btn_clicked(self):
        worker = Worker(self.thread_calculate_btn)
        self.threadpool.start(worker)

    def thread_plot_2d_graph(self,data):
        worker = Worker(lambda :self.plot_2d_graph(data))
        self.threadpool.start(worker)
    def plot_2d_graph(self, data) -> None:
        print("Plotting 2d graph...")
        try:
            x = [float(d[0]) for d in data[1:]]
            y = [float(d[1]) for d in data[1:]]
            z = [float(d[3]) for d in data[1:]]  # Assuming the third element in data is the value to contour
            print((x,y,z))

            print("Creating the x and y grid...")
            # Create a grid of x and y values
            xi = np.linspace(min(x), max(x), 100)
            yi = np.linspace(min(y), max(y), 100)
            xi, yi = np.meshgrid(xi, yi)

            # Interpolate z values on the grid
            print("Interpolating z values on the grid...")
            zi = griddata((x, y), z, (xi, yi), method='cubic')

            # Clear any existing plots
            print("clearing existing plots...")
            self.graph.axes.clear()

            # # Create a contour plot
            print("Creating contout plot...")
            contour = self.graph.axes.contourf(xi, yi, zi, levels=100, cmap="RdYlBu")

            # Add a color bar

            cbar = self.graph.figure.colorbar(contour, ax=self.graph.axes)
            cbar.set_label('Целевая функция')
            # # Create the contour plot with filled contours
            # contour_filled = self.graph.axes.contourf(xi, yi, zi, levels=100, cmap="RdYlBu")
            #
            #
            # # Add a color bar
            # print("Adding color to bar")
            # cbar = plt.colorbar(contour_filled)
            # cbar.set_label('Целевая функция')

            # Set labels and title
            print("Setting titles and labels...")
            self.graph.axes.set_xlabel('A1')
            self.graph.axes.set_ylabel('A2')
            self.graph.axes.set_title('Визуализация 2д-графика')

            # Refresh the plot
            print("Refreshing the plot...")
            self.graph.draw()

            # Update the layout
            print("Updating the layout...")
            try:
                layout = QVBoxLayout()
                layout.addWidget(self.graph)
                self.twod_frame.setLayout(layout)
            except Exception as e:
                print(f"Error in updating layout: {e}")
            print("Contour graph plotted!")
        except Exception as e:
            print(f"Error in plot_2d_graph: {e}")


    def change_user(self):
        print("Changing user...")
        self.login_window = Login.LoginWindow(self.app)
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



