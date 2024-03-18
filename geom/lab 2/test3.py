import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# vertices = np.array([
#         [-3, 0, 0],
#         [3, 0, 0],
#         [0, -3, 0],
#         [0, 3, 0],
#         [0, 0, -3],
#         [0, 0, 3]
#     ])
# faces = [[vertices[i] for i in face] for face in [
#     [0, 2, 4],
#     [0, 3, 4],
#     [1, 2, 4],
#     [1, 3, 4],
#     [0, 2, 5],
#     [0, 3, 5],
#     [1, 2, 5],
#     [1, 3, 5]
# ]]

# Define the vertices of the octahedron
vertices = np.array([
    [-3, 0, 0],
    [3, 0, 0],
    [0, -3, 0],
    [0, 3, 0],
    [0, 0, -3],
    [0, 0, 3]
])

# # Define the faces of the octahedron as pairs of vertices
# faces = [
#     [vertices[0], vertices[2], vertices[4]],
#     [vertices[0], vertices[3], vertices[4]],
#     [vertices[1], vertices[2], vertices[4]],
#     [vertices[1], vertices[3], vertices[4]],
#     [vertices[0], vertices[2], vertices[5]],
#     [vertices[0], vertices[3], vertices[5]],
#     [vertices[1], vertices[2], vertices[5]],
#     [vertices[1], vertices[3], vertices[5]]
# ]
faces = [[vertices[i] for i in face] for face in [
    [0, 2, 4],
    [0, 3, 4],
    [1, 2, 4],
    [1, 3, 4],
    [0, 2, 5],
    [0, 3, 5],
    [1, 2, 5],
    [1, 3, 5]
]]

def create_plot():
    global vertices

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])

    # Set the initial viewpoint
    ax.view_init(elev=0, azim=0)


    # Plot the octahedron
    # ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='r', alpha=0.5)
    ax.add_collection3d(Poly3DCollection(faces, antialiased=True, facecolors='darkgrey',
                                         linewidths=0.2, edgecolors='k', alpha=0.6))
    return fig, ax
def update_plot(scale, x_shift, y_shift, z_shift, ax, rotation_angle):
    global vertices
    # Scale the vertices
    vertices_scaled = np.array([
        [scale*v[0], scale*v[1], scale*v[2]] for v in vertices
    ])

    # Shift the vertices
    vertices_shifted = np.array([
        [v[0] + x_shift, v[1] + y_shift, v[2] + z_shift] for v in vertices_scaled
    ])

    # Rotate the vertices around the z-axis
    rotation_matrix = np.array([
        [np.cos(rotation_angle), -np.sin(rotation_angle), 0],
        [np.sin(rotation_angle), np.cos(rotation_angle), 0],
        [0, 0, 1]
    ])
    vertices_rotated = np.dot(vertices_shifted, rotation_matrix)

    # Clear the previous plot
    ax.clear()
    # Update the plot limits
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])

    # Create a new faces list using the updated vertices
    faces = [[vertices_rotated[i] for i in face] for face in [
        [0, 2, 4],
        [0, 3, 4],
        [1, 2, 4],
        [1, 3, 4],
        [0, 2, 5],
        [0, 3, 5],
        [1, 2, 5],
        [1, 3, 5]
    ]]

    # # Rotate the plot
    # ax.view_init(elev=90, azim=rotation_angle)

    # Set the initial viewpoint
    ax.view_init(elev=0, azim=0)

    # Plot the updated octahedron
    ax.add_collection3d(Poly3DCollection(faces, antialiased=True, facecolors='darkgrey',
                                         linewidths=0.2, edgecolors='k', alpha=0.6))

    canvas.draw()

root = tk.Tk()

# Create a frame for the input fields
input_frame = ttk.LabelFrame(root, text='Input Parameters')
input_frame.grid(column=0, row=0, padx=10, pady=10, sticky='w')

# Create input fields for scaling, shifting, and rotation
scale_label = ttk.Label(input_frame, text='Scale:')
scale_label.grid(column=0, row=0, padx=5, pady=5, sticky='w')
scale_entry = ttk.Entry(input_frame, width=10)
scale_entry.grid(column=1, row=0, padx=5, pady=5, sticky='w')

x_shift_label = ttk.Label(input_frame, text='X Shift:')
x_shift_label.grid(column=0, row=1, padx=5, pady=5, sticky='w')
x_shift_entry = ttk.Entry(input_frame, width=10)
x_shift_entry.grid(column=1, row=1, padx=5, pady=5, sticky='w')

y_shift_label = ttk.Label(input_frame, text='Y Shift:')
y_shift_label.grid(column=0, row=2, padx=5, pady=5, sticky='w')
y_shift_entry = ttk.Entry(input_frame, width=10)
y_shift_entry.grid(column=1, row=2, padx=5, pady=5, sticky='w')

z_shift_label = ttk.Label(input_frame, text='Z Shift:')
z_shift_label.grid(column=0, row=3, padx=5, pady=5, sticky='w')
z_shift_entry = ttk.Entry(input_frame, width=10)
z_shift_entry.grid(column=1, row=3, padx=5, pady=5, sticky='w')

angle_label = ttk.Label(input_frame, text='Angle:')
angle_label.grid(column=0, row=4, padx=5, pady=5, sticky='w')
angle_entry = ttk.Entry(input_frame, width=10)
angle_entry.grid(column=1, row=4, padx=5, pady=5, sticky='w')

# Create a frame for the plot
plot_frame = ttk.LabelFrame(root, text='Octahedron Plot')
plot_frame.grid(column=0, row=1, padx=10, pady=10, sticky='w')

# Create the 3D plot
fig, ax = create_plot()

# Disable mouse events
ax.mouse_rotate = False
ax.mouse_zoom = False

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Create the canvas for the plot
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.draw()
canvas.get_tk_widget().grid(column=0, row=0, padx=10, pady=10, sticky='w')

# Define a function to update the plot when the user clicks the button
def update_plot_button():
    global ax
    scale = float(scale_entry.get())
    x_shift = float(x_shift_entry.get())
    y_shift = float(y_shift_entry.get())
    z_shift = float(z_shift_entry.get())
    angle = float(angle_entry.get())

    update_plot(scale, x_shift, y_shift, z_shift, ax,angle)


# Create a button to update the plot
update_button = ttk.Button(root, text='Update Plot', command=update_plot_button)
update_button.grid(column=0, row=2, padx=10, pady=10, sticky='w')

root.mainloop()