import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera

class GraphicsEngine:
    def __init__(self,win_size=(800,600)):
        # init pygame modules
        pg.init()
        self.WIN_SIZE = win_size

        # set opengl attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        # create opengl context
        pg.display.set_mode(self.WIN_SIZE,flags=pg.OPENGL | pg.DOUBLEBUF)

        # detect and use existing opengl context
        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST)

        # create an object to help track time
        self.clock = pg.time.Clock()
        self.time = 0

        # camera
        self.camera = Camera(self)

        # scene
        self.scene = Octahedron(self)

    # Method for checking events
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        # clear framebuffer
        self.ctx.clear(color=(0.08,0.16,0.18))
        # render scene
        self.scene.render()
        # swap buffers
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001
    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.render()
            self.clock.tick()

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()


