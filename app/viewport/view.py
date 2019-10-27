
from app.tools.file_manager import FileManager

fm = FileManager()
palette = fm.open_file('app/settings/device/palette.json')
device_data = fm.open_file('app/settings/device/preferences.json')

from camera.camera import Camera
from puzzles.rubiks_cube.rubiks_cube import RubiksCube
from grid.grid import Grid
from app.viewport.gui.gui import GUI


class Viewport:

    def __init__(self, pygame):
        self.pg = pygame
        self.clock = pygame.time.Clock()
        self.gui = GUI(pygame)
        self.camera = Camera(pygame)
        self.rubiks_cube = RubiksCube(self.camera, pygame)
        self.grid = Grid(self.camera, pygame)
        self.init_pygame()
        self.gui.init_gui()

    def init_pygame(self):
        w, h = device_data['width'], device_data['height']
        self.pg.display.set_mode((w, h))
        self.pg.display.set_caption('RubiCubie')

    def update(self):
        self.pg.display.get_surface().fill(palette['white'])
        # self.grid.render()
        self.rubiks_cube.render()
        # self.gui.render_gui()
        self.pg.display.flip()
        self.clock.tick(device_data['fps'])
