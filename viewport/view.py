from .scene.objects.puzzle.rubiks_cube.rubiks_cube import RubiksCube
from .scene.objects.puzzle.mirror_cube.mirror_cube import MirrorCube
from .scene.objects.grid.grid import Grid
# from .scene.objects.gui.gui import GUI


class Viewport:

    def __init__(self, root):
        self.root = root
        self.settings = root.global_settings['VIEWPORT']
        self.current_palette = self.settings['PALETTES']['KDE']

        # self.puzzle = RubiksCube(self, 3)
        self.puzzle = MirrorCube(self)
        self.grid = Grid(self)
        # self.gui = GUI(self)
        # self.gui.init_gui()

    def update(self):
        self.root.pg.display.get_surface().fill(self.current_palette['WHITE'])
        self.puzzle.render()
        # self.grid.render()
        # self.gui.render_gui()

