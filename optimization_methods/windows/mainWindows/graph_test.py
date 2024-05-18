from PyQt6 import QtWidgets
import pyqtgraph as pg
import numpy as np


class YourMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the main window
        self.setWindowTitle("T1 vs T2 Graph")

        # Create a central widget for the main window
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QtWidgets.QVBoxLayout(central_widget)

        # Create a PlotWidget object
        plot_widget = pg.PlotWidget()

        # Generate data for T1 and T2
        T1 = np.linspace(1, 10, 1)
        T2 = np.linspace(1, 10, 1) #+ np.random.normal(size=100)  # Adding some noise for demonstration

        # Plot T1 against T2
        plot_widget.plot(T1, T2, pen='b')

        # Add the PlotWidget to the layout
        layout.addWidget(plot_widget)

        # Set the layout for the central widget
        central_widget.setLayout(layout)


# Create an instance of the main window and run the application
app = QtWidgets.QApplication([])
window = YourMainWindow()
window.show()
app.exec()
