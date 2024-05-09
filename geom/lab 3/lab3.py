import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class OctahedronVisualizer:
    def __init__(self):
        self.vertices = np.array([
            [-3, 0, 0],
            [3, 0, 0],
            [0, -3, 0],
            [0, 3, 0],
            [0, 0, -3],
            [0, 0, 3]
        ])
        self.faces = [
            [0, 2, 4],
            [0, 3, 4],
            [1, 2, 4],
            [1, 3, 4],
            [0, 2, 5],
            [0, 3, 5],
            [1, 2, 5],
            [1, 3, 5]
        ]
        self.light_source = np.array([3, 3, 3])

    def calculate_lighting(self):
        normals = []
        face_colors = []
        for face in self.faces:
            v0 = self.vertices[face[1]] - self.vertices[face[0]]
            v1 = self.vertices[face[2]] - self.vertices[face[0]]
            normal = np.cross(v0, v1)
            normal_unit = normal / np.linalg.norm(normal)
            light_direction = self.light_source - self.vertices[face[0]]
            light_direction_unit = light_direction / np.linalg.norm(light_direction)
            cos_angle = np.dot(normal_unit, light_direction_unit)
            light_intensity = 0.5 + 0.5 * max(cos_angle, 0)
            face_color = (light_intensity, light_intensity, light_intensity)
            face_colors.append(face_color)
        return face_colors

    def project_shadows(self):
        shadows = []
        for vertex in self.vertices:
            lx, ly, lz = self.light_source
            x, y, z = vertex
            shadow_x = x  # Предварительная инициализация
            shadow_y = y  # Предварительная инициализация
            if z!= lz:  # Уточненное условие для предотвращения деления на ноль
                scale = (0 - z) / (lz - z)
                shadow_x = x + scale * (lx - x)
                shadow_y = y + scale * (ly - y)
            shadows.append([shadow_x, shadow_y, 0])  # Тень на плоскости XY
        return shadows

    # def draw(self):
    #     fig = plt.figure()
    #     ax = fig.add_subplot(111, projection='3d')
    #     face_colors = self.calculate_lighting()
    #     shadows = self.project_shadows()
    #
    #     # Отрисовка теней
    #     for face in self.faces:
    #         shadow_polygon = [shadows[idx] for idx in face]
    #         ax.add_collection3d(Poly3DCollection([shadow_polygon], facecolors='gray', alpha=0.5))
    #
    #     # Отрисовка октаэдра
    #     for i, face in enumerate(self.faces):
    #         ax.add_collection3d(Poly3DCollection([self.vertices[face]], facecolors=face_colors[i], edgecolors='k'))
    #
    #     # Визуализация источника света
    #     self.light_source_plot = ax.scatter(*self.light_source, color='yellow', s=100, label='Источник света')
    #
    #     ax.set_xlim([-2, 2])
    #     ax.set_ylim([-2, 2])
    #     ax.set_zlim([-2, 2])
    #     ax.set_xlabel('X')
    #     ax.set_ylabel('Y')
    #     ax.set_zlabel('Z')
    #     ax.legend(loc='upper right')
    #     ax.view_init(elev=20, azim=30)
    #
    #     plt.show()

    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        face_colors = self.calculate_lighting()
        shadows = self.project_shadows()

        # Отрисовка октаэдра
        for i, face in enumerate(self.faces):
            ax.add_collection3d(Poly3DCollection([self.vertices[face]], facecolors=face_colors[i], edgecolors='k'))

        # Отрисовка теней
        for face in self.faces:
            shadow_polygon = [shadows[idx] for idx in face]
            ax.add_collection3d(Poly3DCollection([shadow_polygon], facecolors='gray', alpha=0.5))

        # Визуализация источника света
        self.light_source_plot = ax.scatter(*self.light_source, color='yellow', s=100, label='Источник света')

        ax.set_xlim([-15, 15])
        ax.set_ylim([-15, 15])
        ax.set_zlim([-15, 15])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend(loc='upper right')
        ax.view_init(elev=20, azim=30)

        plt.show()

    def set_light_source(self, x, y, z):
        self.light_source = np.array([x, y, z])

class OctahedronApp:
    def __init__(self, master):
        self.master = master
        master.title("Octahedron Visualizer")

        tk.Label(master, text="Enter light source coordinates:").pack()

        self.light_source_entry = {}
        for i, coord in enumerate(["X", "Y", "Z"]):
            tk.Label(master, text=f"{coord} coordinate: ").pack()
            entry = tk.Entry(master, width=10)
            entry.pack()
            self.light_source_entry[coord] = entry

        tk.Button(master, text="Render", command=self.render_plot).pack()

    def render_plot(self):
        x = float(self.light_source_entry["X"].get())
        y = float(self.light_source_entry["Y"].get())
        z = float(self.light_source_entry["Z"].get())

        visualizer = OctahedronVisualizer()
        visualizer.set_light_source(x, y, z)
        visualizer.draw()

root = tk.Tk()
app = OctahedronApp(root)
root.mainloop()