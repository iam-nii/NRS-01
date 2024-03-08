import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from customtkinter import *
import matplotlib as mpl
import random


# Initial dimensions
D1 = 100
D2 = 150
initial_point = [[0, D1], [D2, 0], [0, -D1], [-D2, 0]]
SHAPES = []
COLORS = ['blue']

def add_xy_elements():
    xy_frame.pack()
    # Position the x label in the first column in the second row
    x_label.grid(column=0, row=1)
    # Position the x_textbox from the second column to the third column in the second row
    xo.grid(column=1, row=1, columnspan=2, padx=10)
    # Position the y label in the 4th colum
    y_label.grid(column=3, row=1)
    # Position the y_textbox from the 5th column to the 6th column in the second row
    yo.grid(column=4, row=1, columnspan=2, padx=10)
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
            angle.pack(pady=5)
        else:
            angle.pack(pady=5)

    elif choice == "Scale":
        try:
            for element in entries:
                if element.winfo_exists():
                    element.pack_forget()
        except:
            scale.pack(pady=5)
        else:
            scale.pack(pady=5)

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
            add_xy_elements()
        else:
            # Adding the new elements
            add_xy_elements()


def reset():
    # Removing the shapes so that a new one can be drawn
    for shape in SHAPES[:]:
        popped = SHAPES.pop(SHAPES.index(shape))
        try:
            popped.remove()
        except ValueError:
            continue
    print(SHAPES)
def go_callback(choice):
    if choice == 'menu':
        warning.pack(pady=5)
    elif choice == 'move':

        reset()

        new_x = float(options['move']['xo'].get())
        new_y = float(options['move']['yo'].get())


        # Creating the new rhombus with the same dimensions
        new_coordinates = [[point[0] + new_x,point[1] + new_y] for point in initial_point]

        # Drawing the new rhombus with the new coordinates
        new_poly = Polygon(new_coordinates, closed=True,color=COLORS[random.randint(0, len(COLORS)-1)])
        SHAPES.append(new_poly)
        ax.add_patch(new_poly)

        fig.canvas.draw()

    else:
        option_value = float(options[choice].get())
        if choice == 'rotate':

            reset()

            # Creating the new rhombus with the same dimensions
            new_rhombus = Polygon(initial_point, closed=True,color=COLORS[random.randint(0,len(COLORS)-1)])
            SHAPES.append(new_rhombus)

            # Creating the affine transformation based on the given angle

            # Setting the transformation to the new rhombus
            new_rhombus.set_transform(t2)

            # Adding the new rhombus to the axes
            ax.add_patch(new_rhombus)

        elif choice == 'scale':
            reset()
            # Creating the new rhombus with the same dimensions
            new_rhombus = Polygon(initial_point, closed=True, color=COLORS[random.randint(0,len(COLORS)-1)])
            SHAPES.append(new_rhombus)

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





# Create a Tkinter application
app = CTk()
app.geometry("800x800")

choice_ = 'Menu'

# Variable elements
xy_frame = CTkFrame(app)
x_label = CTkLabel(master=xy_frame,text="X: ")
y_label = CTkLabel(master=xy_frame,text="Y: ")
xo = CTkEntry(master=xy_frame, placeholder_text='New Center (x)')
yo = CTkEntry(master=xy_frame, placeholder_text='New Center (y)')
angle = CTkEntry(app, placeholder_text='Угол поворота')
scale = CTkEntry(app, placeholder_text='Маштаб')
warning = CTkLabel(app, text='Select an operation',text_color='red',font=('Arial',22,'italic'))

entries = [xo, yo,x_label,y_label, angle, scale, warning,xy_frame]
options = {
    'move': {
        'xo':entries[0],
        'yo':entries[1]
    },
    'rotate': entries[4],
    'scale': entries[5],
}

# Add options to the menu
optionmenu_var = StringVar(value="Menu")
optionmenu = CTkOptionMenu(app,values=["Rotate", "Scale", "Move"],
                                         command=optionmenu_callback,
                                         variable=optionmenu_var)
optionmenu.pack()

fig = plt.figure()
ax = fig.add_subplot(111)
fig, ax = plt.subplots(figsize=(20, 15))
polygon = Polygon(initial_point, closed=True,color=COLORS[random.randint(0, len(COLORS)-1)])
# Test
# polygon = Polygon([[90.0, 190.0], [240.0, 90.0], [90.0, -10.0], [-60.0, 90.0]], closed=True,color=COLORS[random.randint(0, len(COLORS)-1)])
SHAPES.append(polygon)
# r1 = patches.Rectangle((0,0), 20, 40, color="blue", alpha=0.50)
# r2 = patches.Rectangle((0,0), 20, 40, color="red",  alpha=0.50)



# ax.add_patch(r1)
# ax.add_patch(r2)
ax.add_patch(polygon)

ax.set_aspect('equal')
canvas = FigureCanvasTkAgg(fig, master=app)
canvas.get_tk_widget().pack(pady=10)

go = CTkButton(app,command=lambda: go_callback(choice_.lower()),text='Go')
go.pack(side=RIGHT, padx=50)

plt.xlim(-500, 500)
plt.ylim(-500, 500)

plt.grid(True)

# plt.show()
app.mainloop()