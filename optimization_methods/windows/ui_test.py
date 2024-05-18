from PyQt6 import QtWidgets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas


class GraphWindow(QtWidgets.QMainWindow):
    def __init__(self, data):
        super().__init__()
        print("Starting the plot")

        # Extract columns A1 and A2 from the data
        x = np.array([row[0] for row in data[1:]])  # Skip header
        y = np.array([row[1] for row in data[1:]])  # Skip header

        print((len(x),len(y)))

        # Create a QWidget and set it as the central widget
        print("Creating a widget and setting it as the central widget")
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the central widget
        layout = QtWidgets.QVBoxLayout(central_widget)

        # Create a Matplotlib figure and axis
        try:
            print("Creating figure and axis...")
            self.figure, self.ax = plt.subplots()

            # Create a canvas to display the figure
            print("Creating canvas...")
            self.canvas = FigureCanvas(self.figure)

            # Add the canvas to the layout
            print("Adding the canvas to the layout...")
            layout.addWidget(self.canvas)

            # Plot the data
            print("Plotting the data...")
            self.ax.plot(x, y, 'r-')  # 'r-' stands for red line

            # Draw the canvas
            self.canvas.draw()
        except Exception as e:
            print(e)
