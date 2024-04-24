import numpy as np
import glm
import pygame as pg

class Octahedron:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program('default')
        self.vao = self.get_vao()
        self.m_module = self.get_model_marix()
        self.on_init()

    def get_texture(self,path):
        texture = pg.image.load(path).convert()
        texture = self.ctx.texture(size=texture.get_size(),components=3,
                                   data=pg.image.tostring(texture, 'RGB'))

    def update(self):
        m_model = glm.rotate(self.m_module, self.app.time, glm.vec3(0,1,0))
        self.shader_program['m_model'].write(m_model)

    def get_model_marix(self):

        m_model = glm.mat4()
        return m_model
    def on_init(self):
        self.shader_program['m_proj'].write(self.app.camera.m_proj)
        self.shader_program['m_view'].write(self.app.camera.m_view)
        self.shader_program['m_model'].write(self.m_module)

    def render(self):
        self.update()
        self.vao.render()

    def destroy(self):
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()

    def get_vao(self):
        vao = self.ctx.vertex_array(self.shader_program, [(self.vbo, '2f 3f','in_textcoord_0','in_position')])
        return vao

    def get_vertex_points(self):
        # octahedron vertices : An octahedron has 6 vertices and 12 faces, each of which is an equilateral triangle.
        vertex_points = [
            (1, 0, 0),  # Top vertex
            (-1, 0, 0),  # Front right vertex
            (0, -1, 0),  # Front left vertex
            (0, 1, 0),  # Back left vertex
            (0, 0, -1),  # Back right vertex
            (0, 0, 1)  # Bottom vertex
        ]
        indices = [
            (0, 2, 4), (0, 3, 4),
            (1, 2, 4), (1, 3, 4),
            (0, 2, 5), (0, 3, 5),
            (1, 2, 5), (1, 3, 5)
        ]
        vertex_points = self.get_data(vertices=vertex_points, indices=indices)

        # Define the texture coordinates for an octahedron
        texture_coord = [
            (0, 0),  # Top vertex
            (1, 0),  # Front right vertex
            (0.5, 1),  # Front left vertex
            (0.5, 1),  # Back left vertex
            (0, 0.5),  # Back right vertex
            (1, 0.5)  # Bottom vertex
        ]

        texture_coord_indices = [
            (0, 2, 3),  # Top triangle
            (0, 1, 2),  # Front right triangle
            (0, 2, 3),  # Front left triangle
            (0, 1, 2),  # Back left triangle
            (0, 2, 5),  # Back right triangle
            (0, 3, 5),  # Bottom triangle
            (1, 2, 5),  # Left triangle
            (1, 3, 5)  # Right triangle
        ]

        texture_coord_data = self.get_data(texture_coord, texture_coord_indices)
        vertex_points = np.hstack([texture_coord_data, vertex_points])
        return vertex_points


    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data,dtype='f4')

    def get_vbo(self):
        # Vertext buffer object
        vertext_data = self.get_vertex_points()
        vbo = self.ctx.buffer(vertext_data)
        return vbo

    def get_shader_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program
