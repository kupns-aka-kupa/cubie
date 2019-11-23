from objects.puzzle.rubiks_cube.rubiks_cube import RubiksCube
from objects.grid.grid import Grid
# from viewport.gui.gui import GUI

from objects.puzzle.data import color_map

VIEWPORT_FILES_SETTINGS = ['settings/palette.json']
PUZZLES_COLOR_MAP = 'objects/puzzle/rubiks_cube/cube_color_map.json'


class Viewport:

    def __init__(self, root):
        self.root = root
        self.settings = self.root.file_manager.load(VIEWPORT_FILES_SETTINGS)

        json_color_map = {key: [self.settings['PALETTE'][color] for color in data] for key, data in color_map.items()}
        self.root.file_manager.write_file(json_color_map, PUZZLES_COLOR_MAP)

        self.puzzle = RubiksCube(self)
        self.grid = Grid(self)
        # self.gui = GUI(self.root.pg)
        # self.gui.init_gui()

    def update(self):
        self.root.pg.display.get_surface().fill(self.settings['PALETTE']['WHITE'])
        self.puzzle.render()
        # self.grid.render()
        # self.gui.render_gui()

