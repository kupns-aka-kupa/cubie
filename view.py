import tools, camera, rubiks_cube, grid

class Viewport():

    def __init__(self, pygame, data):
        self.tools = tools.Tools()
        self.pg = pygame
        self.data = data
        self.camera = camera.Camera(self.pg, self.data)
        self.rubiks_cube = rubiks_cube.RubiksCube(self.camera, self.pg, (self.data.cube, self.data.device), self.tools)
        self.grid = grid.Grid(self.camera, self.pg, (self.data.grid, self.data.device), self.tools)

    def update(self):
        self.pg.display.get_surface().fill(self.data.colors.white)
        self.grid.render()
        self.rubiks_cube.render()
        self.pg.display.flip()
