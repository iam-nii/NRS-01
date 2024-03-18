import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

vertices = np.array([
        [-3, 0, 0],
        [3, 0, 0],
        [0, -3, 0],
        [0, 3, 0],
        [0, 0, -3],
        [0, 0, 3]
    ])

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
axis = []

fig = ''
ax = ''
def add_xy_elements():
    xy_frame.grid(row=3,column=1,pady=5)
    # Position the x label in the first column in the second row
    x_label.grid(column=0, row=1)
    # Position the x_textbox from the second column to the third column in the second row
    xo.grid(column=1, row=1, columnspan=2, padx=10)
    # Position the y label in the 4th colum
    y_label.grid(column=3, row=1)
    # Position the y_textbox from the 5th column to the 6th column in the second row
    yo.grid(column=4, row=1, columnspan=2, padx=10)

def generate_cube(faces=faces):
    global axis,fig,ax
    fig = plt.figure(figsize=(20, 15))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect([2, 2, 3])


    # Определение вершин и граней октаэдра


    ax.add_collection3d(Poly3DCollection(faces,antialiased=True, facecolors='darkgrey',
                                         linewidths=0.2, edgecolors='k', alpha=0.6))
    ax.set_aspect('equal')

    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # get the axis vectors
    ax.view_init(elev=90, azim=0)
    x_axis = ax.xaxis.get_transform().transform((1, 0, 0))
    y_axis = ax.yaxis.get_transform().transform((0, 1, 0))
    z_axis = ax.zaxis.get_transform().transform((0, 0, 1))
    x_axis = x_axis / np.linalg.norm(x_axis)
    y_axis = y_axis / np.linalg.norm(y_axis)
    z_axis = z_axis / np.linalg.norm(z_axis)

    # print the axis vectors
    print("X axis:", x_axis)
    print("Y axis:", y_axis)
    print("Z axis:", z_axis)

    axis = [x_axis[0], y_axis[1], z_axis[2]]

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    # canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=0)
    canvas.get_tk_widget().grid(row=2,column=1,columnspan=2, padx=100)

def optionmenu_callback(choice):
    global choice_
    choice_ = choice

    if choice == "Rotate":
        try:
            for element in entries:
                if element.winfo_exists():
                    element.grid_forget()
                else:
                    continue
        except UnboundLocalError:
            angle.grid(row=3,column=1,pady=5)
        else:
            angle.grid(row=3,column=1,pady=5)

    elif choice == "Scale":
        try:
            for element in entries:
                if element.winfo_exists():
                    element.pack_forget()
        except:
            scale.grid(row=3,column=1,pady=5)
        else:
            scale.grid(row=3,column=1,pady=5)

    elif choice == "Move":
        # Removing other elements if they exist
        try:
            for element in entries:
                if element.winfo_exists():
                    element.pack_forget()
                else:
                    continue

        except UnboundLocalError:
            # Adding the new elements
            xy_frame.grid(row=3,column=1,pady=5)
            # Position the x label in the first column in the second row
            x_label.grid(column=0, row=1)
            # Position the x_textbox from the second column to the third column in the second row
            xo.grid(column=1, row=1, columnspan=2, padx=10)
            # Position the y label in the 4th colum
            y_label.grid(column=3, row=1)
            # Position the y_textbox from the 5th column to the 6th column in the second row
            yo.grid(column=4, row=1, columnspan=2, padx=10)
            # Position the z label in the 5th colum
            z_label.grid(column=6, row=1)
            # Position the z_textbox from the 5th column to the 6th column in the second row
            zo.grid(column=7, row=1, columnspan=2, padx=10)
        else:
            # Adding the new elements
            xy_frame.grid(row=3,column=1,pady=5)
            # Position the x label in the first column in the second row
            x_label.grid(column=0, row=1, padx=0)
            # Position the x_textbox from the second column to the third column in the second row
            xo.grid(column=1, row=1, columnspan=2, padx=0)
            # Position the y label in the 4th colum
            y_label.grid(column=3, row=1, padx=0)
            # Position the y_textbox from the 5th column to the 6th column in the second row
            yo.grid(column=4, row=1, columnspan=2, padx=0)
            # Position the z label in the 5th colum
            z_label.grid(column=6, row=1)
            # Position the z_textbox from the 5th column to the 6th column in the second row
            zo.grid(column=7, row=1, columnspan=2, padx=10)


def go_callback(choice):
    print(choice)
    if choice == 'menu':
        warning.grid(row=1,pady=5)
    elif choice == 'move':

        ax.clear()

        new_x = float(options['move']['xo'].get())
        new_y = float(options['move']['yo'].get())
        # Creating the new shape


        fig.canvas.draw()

    else:
        print(options[choice].get())
        option_value = float(options[choice].get())
        ax.clear()
        if choice == 'rotate':
            # Rotate the figure
            rotated_vertices = rotate(angle=option_value)
            print(rotated_vertices)
            # update faces to reflect the new vertex positions
            rotated_faces = [[rotated_vertices[i] for i in face] for face in [
                [0, 2, 4],
                [0, 3, 4],
                [1, 2, 4],
                [1, 3, 4],
                [0, 2, 5],
                [0, 3, 5],
                [1, 2, 5],
                [1, 3, 5]
            ]]
            generate_cube(faces=rotated_faces)
            pass

        elif choice == 'scale':

            # Scale the figure

            # Creating the affine transformation based on the given scale
            try:
                if option_value < 0:
                    t2 = mpl.transforms.Affine2D().scale(1/option_value) + ax.transData
                elif option_value > 0:
                    t2 = mpl.transforms.Affine2D().scale(option_value) + ax.transData

                # Setting the transformation to the new rhombus
                new_rhombus.set_transform(t2)
            except:
                pass
            finally:
                # Adding the new rhombus to the axes
                ax.add_patch(new_rhombus)

        fig.canvas.draw()

def rotate(angle):
    global axis, vertices
    """
    Rotate a set of 3D points around a given axis by a given angle.

    Args:
    - vertices: The points to rotate (list of lists of 3 floats).
    - axis: The rotation axis (list of 3 floats with length 1).
    - angle: The rotation angle in radians (float).

    Returns:
    - The rotated points (list of lists of 3 floats).
    """
    # Create a rotation matrix from the axis and angle
    a, b, c = axis
    ca = np.cos(angle)
    sa = np.sin(angle)
    cpa = 1 - ca
    xx = a * a * cpa
    yy = b * b * cpa
    zz = c * c * cpa
    xy = a * b * cpa
    xz = a * c * cpa
    yz = b * c * cpa

    # Apply the rotation matrix to each point
    rotated_vertices = []
    for point in vertices:
        rotated_point = [
            xx * point[0] + xy * point[1] + xz * point[2],
            xy * point[0] + yy * point[1] + yz * point[2],
            xz * point[0] + yz * point[1] + zz * point[2]
        ]
        rotated_vertices.append(rotated_point)

    return rotated_vertices


def move():
    # Перемещение
    translation_matrix = np.array([1, 1, 1])
    translated_vertices = vertices + translation_matrix
    ax.scatter(translated_vertices[:, 0], translated_vertices[:, 1], translated_vertices[:, 2], color='b')
def scale():
    # Масштабирование
    scale_matrix = np.array([[0.5, 0, 0],
                             [0, 0.5, 0],
                             [0, 0, 0.5]])
    scaled_vertices = np.dot(vertices, scale_matrix)
    ax.scatter(scaled_vertices[:, 0], scaled_vertices[:, 1], scaled_vertices[:, 2], color='r')



window = ctk.CTk()
window.geometry("900x750")
window.title("2 Лаба - Вариант 2")
window.grid_rowconfigure(4, weight=1,pad=100)
window.grid_columnconfigure(4, weight=1)

choice_= 'Menu'

# Variable elements
xy_frame = ctk.CTkFrame(window)
x_label = ctk.CTkLabel(master=xy_frame,text="X: ")
y_label = ctk.CTkLabel(master=xy_frame,text="Y: ")
z_label = ctk.CTkLabel(master=xy_frame,text="Z: ")
xo = ctk.CTkEntry(master=xy_frame, placeholder_text='New Center (x)')
yo = ctk.CTkEntry(master=xy_frame, placeholder_text='New Center (y)')
zo = ctk.CTkEntry(master=xy_frame, placeholder_text='New Center (z)')
angle = ctk.CTkEntry(window, placeholder_text='Угол поворота')
scale = ctk.CTkEntry(window, placeholder_text='Маштаб')
warning = ctk.CTkLabel(window, text='Select an operation',text_color='red',font=('Arial',22,'italic'))

entries = [xo, yo,zo,x_label,y_label, angle, scale, warning,xy_frame]
options = {
    'move': {
        'xo':entries[0],
        'yo':entries[1],
        'zo':entries[2],
    },
    'rotate': entries[5],
    'scale': entries[6],
}

optionmenu_var = ctk.StringVar(value="Menu")
optionmenu = ctk.CTkOptionMenu(window,values=["Rotate", "Scale", "Move"], width=200, variable=optionmenu_var,
                                         command=optionmenu_callback, fg_color='#6B6A65')
optionmenu.grid(row=0,column=1,pady=15, padx=20)
generate_cube()

go = ctk.CTkButton(window,command=lambda: go_callback(choice_.lower()),text='Go',anchor='w')
go.grid(row=3,column=2, pady=20)


window.mainloop()