# from optimization_methods.windows.ui_test import GraphWindow
import traceback
import matplotlib
import numpy as np
import optimization_methods.windows.mainWindows.loginWindow_ui as Login
from PyQt6 import QtWidgets as qw, uic
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, QRunnable, QThreadPool, pyqtSlot
matplotlib.use('QtAgg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from scipy.interpolate import LinearNDInterpolator
from scipy.interpolate import griddata
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout
from optimization_methods.windows.utils import Database,User, Tasks,SolutionMethods



class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MplCanvas_3d(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111, projection='3d')  # Add a 3D subplot
        super().__init__(fig)


DATA = [["A1", "A2", "C", "Целевая Функция"]]


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
        self._data = data[1:]  # Remove the first row from the data list
        self._headers = data[0]  # Store the first row as the headers

    def rowCount(self, parent=QModelIndex()):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        # The length of the longest list
        return len(max(self._data, key=len))

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
        self.cbar_2d = None
        self.cbar_3d = None
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    def init_ui(self):
        try:
            self.database = Database()

            # self.window = uic.loadUi("./windows/mainWindows/userWindow_ui.ui")
            self.window = uic.loadUi("./windows/mainWindows/userWindow1_ui.ui")
            # Input frame
            self.input_frame: qw.QWidget = self.window.input_frame

            # Table frame
            self.table_frame: qw.QWidget = self.window.table_frame
            self.TABLE = self.table_frame.findChild(qw.QTableView, "results_table")

            # 2d Graph frame
            self.graph = MplCanvas(self, width=10, height=7, dpi=100)
            self.twod_frame = self.window.twod_graph_frame
            self.twod_layout = QVBoxLayout()
            self.twod_layout.addWidget(self.graph)
            self.twod_frame.setLayout(self.twod_layout)

            # 3d Graph frame
            self.graph_3d = MplCanvas_3d(self, width=9, height=7, dpi=100)
            self.three_d_frame: qw.QWidget = self.window.threed_frame
            self.three_d_layout = QVBoxLayout()
            self.three_d_layout.addWidget(self.graph_3d)
            self.three_d_frame.setLayout(self.three_d_layout)

            # Results frame
            self.results = self.window.results_frame
            self.obj_max_a1: qw.QLineEdit = self.results.findChild(qw.QLineEdit, "obj_max_a1")
            self.obj_max_a2: qw.QLineEdit = self.results.findChild(qw.QLineEdit, "obj_max_a2")
            self.obj_min_a1: qw.QLineEdit = self.results.findChild(qw.QLineEdit, "obj_min_a1")
            self.obj_min_a2: qw.QLineEdit = self.results.findChild(qw.QLineEdit, "obj_min_a2")
            self.result_output_text: qw.QLineEdit = self.results.findChild(qw.QLineEdit, "result_output_text")
            self.obj_func_max_txt: qw.QLineEdit = self.results.findChild(qw.QLineEdit, "obj_func_max_txt")
            self.obj_func_min_txt: qw.QLineEdit = self.results.findChild(qw.QLineEdit, "obj_func_min_txt")
            self.results_elements = [self.obj_max_a1, self.obj_max_a2, self.obj_min_a1, self.obj_min_a2,
                                     self.result_output_text, self.obj_func_max_txt, self.obj_func_min_txt]

            # Menu options
            self.change_user_menu: qw.QWidge - tAction = self.window.changeUser_menu.triggered.connect(
                self.change_user)
            self.help_menu: qw.QWidgetAction = self.window.help_menu.triggered.connect(self.help_menu_click)
            self.exit: qw.QWidgetAction = self.window.exit_menu.triggered.connect(self.exit_menu_click)

            self.v1: qw.QLineEdit = self.input_frame.findChild(qw.QLineEdit, "v1_txt")
            # print(self.v1)
            self.v2: qw.QLineEdit = self.input_frame.findChild(qw.QLineEdit, "v2_txt")
            self.min_a2: qw.QLineEdit = self.input_frame.findChild(qw.QLineEdit, "min_a2_txt")
            self.min_a1: qw.QLineEdit = self.input_frame.findChild(qw.QLineEdit, "min_a1_txt")
            self.max_a1: qw.QLineEdit = self.input_frame.findChild(qw.QLineEdit, "max_a1_txt")
            self.max_a2: qw.QLineEdit = self.input_frame.findChild(qw.QLineEdit, "max_a2_txt")

            self.mu = self.mu1 = self.alpha = self.alpha1 = self.beta = self.beta1 = 1

            self.accuracy_txt: qw.QLineEdit = self.input_frame.findChild(qw.QLineEdit, "accuracy_txt")
            self.solution_method: qw.QComboBox = self.input_frame.findChild(qw.QComboBox, "method_cbx")

            # Calculate button
            self.calculate_btn = self.input_frame.findChild(qw.QPushButton, "calculate_btn")
            # print(self.calculate_btn)
            self.calculate_btn.clicked.connect(self.calculate_btn_clicked)
            
            # Warning
            self.warning_text:qw.QLabel = self.input_frame.findChild(qw.QLabel, "warning_txt")
            self.warning_text.setHidden(True)
            
            # Combobox
            self.tasks_cbx: qw.QComboBox = self.input_frame.findChild(qw.QComboBox,'method_cbx')
            print(self.tasks_cbx)
            if self.tasks_cbx:
                methods = self.database.get_solution_methods()
                for i in range(len(methods)):
                    self.tasks_cbx.addItem(str(methods[i].method))


                # def disableItemWithValue(value):
                #     for index in range(self.tasks_cbx.count()):
                #         if self.tasks_cbx.itemText(index) != value:
                #             self.tasks_cbx.setItemData(index, 0, Qt.ItemIsEnabled)
                #             break  # Optional: exit loop after the first match
                #             # Disable item with a specific value
                #
                # disableItemWithValue("Метод Бокса")
        except Exception as e:
            print(traceback.print_exc())

    def thread_calculate_btn(self):
        try:
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
            # step = 0.1
            if V1 == 0 or V2 == 0:
                self.warning_text.setHidden(False)
                raise Exception(f"{self.warning_text.text()}")

            self.warning_text.setHidden(True)
        except Exception as e:
            print(f"Exception: {e}. Details: {traceback.print_exc()}")
            self.warning_text.setHidden(False)
            return

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
        try:
            step = round(float(self.accuracy_txt.text()), 3)  # Step size for incrementing A1 and A2
            print("Calculating...")

            A1 = min_a1
            while A1 <= max_a1:
                A2 = max_a2  # Reset A2 to its initial value at the start of each A1 loop
                while A2 >= min_a2:
                    # Calculate the production of C in kg/h
                    output = alpha * (A1 ** 2 + beta * A2 - mu * V1) ** N + alpha1 * (
                            beta1 * A1 + A2 ** 2 - mu1 * V2) ** N
                    # Calculate the total production in 8 hours (workday)
                    function = output * 8
                    if A1 + A2 < 8:
                        A1_list.append(round(A1, 1))
                        A2_list.append(round(A2, 1))
                        total_production.append(round(function, 2))
                    DATA.append([round(A1, 1), round(A2, 1), round(output, 2), round(function, 2)])
                    A2 -= step
                A1 += step
        except Exception as e:
            print(f"Exception: {e}. Details:{traceback.print_exc()}")
        print("Calculation completed.")
        print("Building table...")
        # data_model = TableModel([value for value in DATA if DATA[0]+DATA[1]<8])
        data_model = TableModel(DATA)
        self.TABLE.setModel(data_model)
        self.TABLE.setColumnWidth(0, 120)  # Set the width of the first column to 100 pixels
        self.TABLE.setColumnWidth(1, 120)
        self.TABLE.setColumnWidth(2, 120)
        self.TABLE.setColumnWidth(3, 150)
        print("Table build done.")
        try:
            print("Calculating extreme...")
            try:
                method = self.tasks_cbx.currentText()
                results = [[0,0,0],[0,0,0]]
                if method == "Метод Бокса":
                    print("Calculating using the Box method...")
                    results = self.box_method(A1_list, A2_list, total_production)
                if method == "Метод сканирования":
                    print("Calculating using the Scannig method...")
                    results = self.scanning_method(A1_list, A2_list, total_production)
                    print(results)


                print("Placing texts in text fields")
                self.obj_max_a1.setText(str(results[1][0]))
                self.obj_max_a2.setText(str(results[1][1]))
                self.obj_min_a1.setText(str(results[0][0]))
                self.obj_min_a2.setText(str(results[0][1]))

                self.obj_func_max_txt.setText(str(results[1][2]))
                self.obj_func_min_txt.setText(str(results[0][2]))
                result = f"Максимальный выход целевого компонента в кг за рабочую смену ( 8 часов) составляет {str(results[1][2])}"
                print("Printing Optimal values...")
                self.result_output_text.setText(result)
                for element in self.results_elements:
                    element.setReadOnly(True)

                print("Done")

                print(results)
            except Exception as e:
                print(traceback.print_exc())
            # [[x_min_extreme, y_min_extreme, z_min_extreme], [x_max_extreme, y_max_extreme, z_max_extreme]]

        except Exception as e:
            print(f"Error calculating extreme: {e}. Details: {traceback.print_exc()}")

        self.thread_plot_2d_graph(DATA, results[1])
        try:
            self.thread_plot_3d_graph([DATA[row] for row in range(1, len(DATA)) if DATA[row][0] + DATA[row][1] < 8])
        except Exception as e:
            print(f"Exception: {e}. Details: {traceback.print_exc()}")

    def calculate_btn_clicked(self):
        worker = Worker(self.thread_calculate_btn)
        self.threadpool.start(worker)

    def box_method(self, x_values, y_values, z_values):
        try:
            print("Calculating extreme values...")

            # Initial guess for the extreme points
            x_min, x_max = min(x_values), max(x_values)
            y_min, y_max = min(y_values), max(y_values)

            # Initialize the extreme points
            print("Initializing extreme points...")
            x_min_extreme, y_min_extreme, z_min_extreme = x_values[0], y_values[0], z_values[0]
            x_max_extreme, y_max_extreme, z_max_extreme = x_values[0], y_values[0], z_values[0]

            # Iterate through all values to find the extreme points
            print("Iterating through values to find the extreme points")
            for x, y, z in zip(x_values, y_values, z_values):
                if z > z_max_extreme:
                    # Update the maximum extreme point if a higher value is found
                    x_max_extreme, y_max_extreme, z_max_extreme = x, y, z
                    print(f"New max found: {x_max_extreme}, {y_max_extreme}, {z_max_extreme}")
                if z < z_min_extreme:
                    # Update the minimum extreme point if a lower value is found
                    x_min_extreme, y_min_extreme, z_min_extreme = x, y, z
                    print(f"New min found: {x_min_extreme}, {y_min_extreme}, {z_min_extreme}")

        except Exception as e:
            print(f"Error finding extreme point: {e}")

        # Output the extreme points
        print("Returning extreme points...")
        return [[x_min_extreme, y_min_extreme, z_min_extreme], [x_max_extreme, y_max_extreme, z_max_extreme]]

    def box_method2(self,A1, A2, F, max_iter=100, tolerance=1e-6, jitter=1e-5, alpha=1.3):
        # Initialize the complex of points
        points = np.array(list(zip(A1, A2, F)))

        def centroid(points, exclude_index):
            # Calculate the centroid of the points complex, excluding one
            filtered_points = np.delete(points, exclude_index, axis=0)
            return np.mean(filtered_points[:, :2], axis=0)

        def reflect(best_point, centroid):
            # Reflect the worst point relative to the centroid
            return centroid + alpha * (best_point[:2] - centroid)

        # Precompute the interpolation function
        interpolator = LinearNDInterpolator(points[:, :2], points[:, 2])

        for iteration in range(max_iter):
            # Add random noise to avoid calculation errors
            points[:, :2] += np.random.uniform(-jitter, jitter, size=points[:, :2].shape)

            # Sort points by function values
            points = points[points[:, 2].argsort()]

            # Define the best and worst points
            best = points[0]
            worst = points[-1]

            # Compute the centroid of all points except the best one
            c = centroid(points, 0)

            # Reflect the best point
            reflected_point = reflect(best, c)

            # Interpolate the function value at the reflected point
            reflected_value = interpolator(reflected_point)

            # Handle cases where the reflected value goes beyond known data boundaries
            if np.isnan(reflected_value):
                reflected_value = worst[2]

            # Compare the reflected value with the worst point
            if reflected_value > worst[2]:
                # Replace the worst point with the reflected point
                points[-1] = np.append(reflected_point, reflected_value)
            else:
                # If reflection does not improve the result, compress towards the best point
                points[1:, :2] = best[:2] + 0.5 * (points[1:, :2] - best[:2])

            # Check for convergence
            if np.std(points[:, 2]) < tolerance:
                break

        # Sort points after convergence, where the best point should be the minimum and the worst point the maximum
        points = points[points[:, 2].argsort()]
        min_point = points[0]
        max_point = points[-1]

        return [[round(min_point[0], 3), round(min_point[1], 3), round(min_point[2], 3)],
                [round(max_point[0], 3), round(max_point[1], 3), round(max_point[2], 3)]]
    def scanning_method(self,A1, A2, F):
        # Начальные значения для минимальных и максимальных экстремумов
        min_extreme = [A1[0], A2[0], F[0]]
        max_extreme = [A1[0], A2[0], F[0]]

        # Проход по всем значениям и нахождение минимальных и максимальных
        for a1, a2, f in zip(A1, A2, F):
            if f < min_extreme[2]:
                min_extreme = [a1, a2, f]
            if f > max_extreme[2]:
                max_extreme = [a1, a2, f]

        return [min_extreme, max_extreme]

    def thread_plot_2d_graph(self, data,max_values):
        worker = Worker(lambda: self.plot_2d_graph(data,max_values))
        self.threadpool.start(worker)

    def plot_2d_graph(self, data,max_values) -> None:
        print("Plotting 2d graph...")
        try:
            x = [float(d[0]) for d in data[1:]]
            y = [float(d[1]) for d in data[1:]]
            z = [float(d[3]) for d in data[1:]]  # Assuming the third element in data is the value to contour

            print("Creating the x and y grid...")
            # Create a grid of x and y values
            xi = np.linspace(min(x), max(x), 100)
            yi = np.linspace(min(y), max(y), 100)
            xi, yi = np.meshgrid(xi, yi)

            # Interpolate z values on the grid
            print("Interpolating z values on the grid...")
            zi = griddata((x, y), z, (xi, yi), method='cubic')

            # Clear any existing plots
            print("Clearing existing plots...")
            self.graph.axes.clear()

            # Create a contour plot
            print("Creating contour plot...")
            contour = self.graph.axes.contourf(xi, yi, zi, levels=100, cmap="RdYlBu")

            # Add a color bar
            # Add a color bar if it doesn't exist
            print("Handling color bar...")
            try:
                if self.cbar_2d is None:
                    self.cbar_2d = self.graph.figure.colorbar(contour, ax=self.graph.axes)
                    self.cbar_2d.set_label('Целевая функция')
                else:
                    self.cbar_2d.update_normal(contour)
            except Exception as e:
                print(f"Exception: {e}. Details: {traceback.print_exc()}")


            # Plot the line x + y = 8
            print("Plotting x + y = 8 line...")
            x_line = np.linspace(min(xi.flatten()), max(xi.flatten()), 100)
            y_line = 9   - x_line
            self.graph.axes.plot(x_line, y_line, 'k--', label='x + y ≤ 8')

            try:
                # Plot the maximum point of the onjective function (x_max,y_max)
                max_x = max_values[0]
                max_y = max_values[1]
                print(f"Plotting ({max_x},{max_y})")
                self.graph.axes.plot(max_x,max_y,'ko', label=f'({max_x},{max_y})')
            except Exception as e:
                print(f"Exception: {e}. Details:{traceback.print_exc()}")

            # Set the x and y axis limits to start from 0
            self.graph.axes.set_xlim(1, max(xi.flatten()))
            self.graph.axes.set_ylim(1, max(yi.flatten()))

            # Set labels and title
            print("Setting titles and labels...")
            self.graph.axes.set_xlabel('A1')
            self.graph.axes.set_ylabel('A2')
            self.graph.axes.set_title('Визуализация 2д-графика')
            self.graph.axes.legend()

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

    def thread_plot_3d_graph(self, data):
        worker = Worker(lambda: self.plot_3d_graph(data))
        self.threadpool.start(worker)

    def plot_3d_graph(self, data):
        print("Inititating 3d plot...")
        try:
            x = [float(d[0]) for d in data[1:]]
            y = [float(d[1]) for d in data[1:]]
            z = [float(d[3]) for d in data[1:]]

            print("Creating the x, y and z grid...")

            xi = np.linspace(min(x), max(x), 100)
            yi = np.linspace(min(y), max(y), 100)
            xi, yi = np.meshgrid(xi, yi)

            zi = griddata((x, y), z, (xi, yi), method='cubic')

            self.graph_3d.axes.clear()  # Clear the existing plot on the canvas

            print("Plotting the 3d graph...")
            surf = self.graph_3d.axes.plot_surface(xi, yi, zi, cmap="RdYlBu")  # Plot directly onto self.graph_3d

            print("Handling color bar...")
            try:
                if self.cbar_3d is None:
                    self.cbar_3d = self.graph_3d.figure.colorbar(surf, ax=self.graph_3d.axes)
                    self.cbar_3d.set_label('Целевая функция')
                else:
                    self.cbar_3d.update_normal(surf)
            except Exception as e:
                print(f"Exception: {e}. Details: {traceback.print_exc()}")


            print("Setting the axes labels...")
            self.graph_3d.axes.set_xlabel('A1')
            self.graph_3d.axes.set_ylabel('A2')
            self.graph_3d.axes.set_zlabel('Целевая функция')
            self.graph_3d.axes.set_title('Визуализация 3д-графика')

            self.graph_3d.draw()  # Update the canvas
            print("3d plot done!")

        except Exception as e:
            print(f"Error in plot_3d_graph: {e}")

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

# # Example usage:
# x_values = [1, 2, 3, 4, 5]
# y_values = [2, 3, 4, 5, 6]
# z_values = [10, 12, 15, 14, 11]
#
# min_extreme, max_extreme = box_method(x_values, y_values, z_values)
# print(f"Minimum Extreme Point: {min_extreme}")
# print(f"Maximum Extreme Point: {max_extreme}")
