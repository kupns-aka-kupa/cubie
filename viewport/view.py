from objects.camera import camera
from objects.puzzles.rubiks_cube import rubiks_cube
from objects.grid import grid
from objects.GUI import gui
import data


class Viewport:

    def __init__(self, pygame):
        self.pg = pygame
        self.clock = self.pg.time.Clock()
        self.data = data.Data()
        self.gui = gui.GUI(self.pg, (self.data.gui, self.data.device))
        self.camera = camera.Camera(self.pg, self.data)
        self.rubiks_cube = rubiks_cube.RubiksCube(self.camera, self.pg, (self.data.cube, self.data.device))
        self.grid = grid.Grid(self.camera, self.pg, (self.data.grid, self.data.device))
        self.init_pygame()
        self.gui.init_gui()

    def init_pygame(self):
        w, h = self.data.device.width, self.data.device.height
        self.pg.display.set_mode((w, h))
        self.pg.display.set_caption('RubiCubie')

    def update(self):
        self.pg.display.get_surface().fill(self.data.colors.white)
        # self.grid.render()
        self.rubiks_cube.render()
        # self.gui.render_gui()
        self.pg.display.flip()
        self.clock.tick(self.data.device.fps)
