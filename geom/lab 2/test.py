import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def generate_cube():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Определение вершин и граней октаэдра
    vertices = np.array([
        [-1, 0, 0],
        [1, 0, 0],
        [0, -1, 0],
        [0, 1, 0],
        [0, 0, -1],
        [0, 0, 1]
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

    ax.add_collection3d(Poly3DCollection(faces, facecolors='darkgrey', linewidths=0.3, edgecolors='k', alpha=0.6))
    ax.set_aspect('equal')

    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    # canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=0)
    canvas.get_tk_widget().grid(row=1,column=1)


def optionmenu_callback(choice):
    print(choice)


window = ctk.CTk()
window.geometry("800x600")
window.title("2 Лаба - Вариант 2")
window.grid_rowconfigure(4, weight=1)
window.grid_columnconfigure(3, weight=1)

optionmenu_var = ctk.StringVar(value="Menu")
optionmenu = ctk.CTkOptionMenu(window,values=["Rotate", "Scale", "Move"],
                                         command=optionmenu_callback, fg_color='#6B6A65')
optionmenu.grid(row=0,column=1,pady=5, padx=20)


window.mainloop()