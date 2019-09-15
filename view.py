import tools, cube, grid
tools = tools.Tools()

class Viewport():

    def __init__(self, camera, pygame, data):
        self.camera = camera
        self.pg = pygame
        self.data = data
        self.cube = cube
        self.grid = grid.Grid(self.camera, self.pg, self.data, tools)
        self.rubicube = []
        self.rubicube_colors = []

    def cube_init(self):
        colors = self.data.colors

#       start_coord(y,x,z)
        self.Y_corners = [
            [(2, -2, -2), [colors.orange, colors.blue, colors.yellow, colors.black]],
            [(2, -2, 2), [colors.black, colors.blue, colors.yellow, colors.red, colors.black]],
            [(-2, -2, 2), [colors.black, colors.black, colors.yellow, colors.red, colors.green, colors.black]],
            [(-2, -2, -2), [colors.orange, colors.black, colors.yellow, colors.black, colors.green, colors.black]]
        ]
        self.W_corners = [
            [(2, 2, -2), [colors.orange, colors.blue, colors.black, colors.black, colors.black, colors.white]],
            [(2, 2, 2), [colors.black, colors.blue, colors.black, colors.red, colors.black, colors.white]],
            [(-2, 2, 2), [colors.black, colors.black, colors.black, colors.red, colors.green, colors.white]],
            [(-2, 2, -2), [colors.orange, colors.black, colors.black, colors.black, colors.green, colors.white]]
        ]
        self.edges = [
            [[(2, -2, 0)], [colors.black, colors.blue, colors.yellow, colors.black]],#YB_edges
            [[(0, -2, 2)], [colors.black, colors.black, colors.yellow, colors.red, colors.black]],#YR_edges
            [[(-2, -2, 0)], [colors.black, colors.black, colors.yellow, colors.black, colors.green, colors.black]],#YG_edges
            [[(0, -2, -2)], [colors.orange, colors.black, colors.yellow, colors.black]],#YO_edges
#            [[(2, 2, 0)], [colors.black, colors.blue, colors.black, colors.black, colors.black, colors.white]],#WB_edges
#            [[(0, 2, 2)], [colors.black, colors.black, colors.black, colors.red, colors.black, colors.white]],#WG_edges
#            [[(-2, 2, 0)], [colors.black, colors.black, colors.black, colors.black, colors.green, colors.white]],#WR_edges
#            [[(0, 2, -2)], [colors.orange, colors.black, colors.black, colors.black, colors.black, colors.white]],#WO_edges
#            [[(2, 0, -2)], [colors.orange, colors.blue, colors.black]],#OB_edges
#            [[(2, 0, 2)], [colors.black, colors.blue, colors.black, colors.red, colors.black]],#BR_edges
#            [[(-2, 0, 2)], [colors.black, colors.black, colors.black, colors.red, colors.green, colors.black]],#RG_edges
#            [[(-2, 0, -2)], [colors.orange, colors.black, colors.black, colors.black, colors.green, colors.black]]#GO_edges
        ]
        self.centers = [
            [[(0, 0, -2)], [colors.orange, colors.black]],
            [[(2, 0, 0)], [colors.black, colors.blue, colors.black]],
            [[(0, -2, 0)], [colors.black, colors.black, colors.yellow, colors.black]],
            [[(0, 0, 2)], [colors.black, colors.black, colors.black, colors.red, colors.black]],
            [[(-2, 0, 0)], [colors.black, colors.black, colors.black, colors.black, colors.green, colors.black]],
            [[(0, 2, 0)], [colors.black, colors.black, colors.black, colors.black, colors.black, colors.white]]
        ]
#        for i in self.centers:
#            self.rubicube.append(self.cube.Cube(self.camera, self.pg, data, tools, i[0]))
#
#        for i in  self.W_corners:
#            self.rubicube.append(self.cube.Cube(self.camera, self.pg, data, tools, i[0]))
#
#        for i in  self.Y_corners:
#            self.rubicube.append(self.cube.Cube(self.camera, self.pg, data, tools, i[0]))

        for edge in self.edges :
            for i in  range(len(edge[0])):
                self.rubicube.append(self.cube.Cube(self.camera, self.pg, self.data, tools, edge[0][i]))
                self.rubicube_colors.append(edge[1])

    def display_order(self):
        order = []
        for i in self.rubicube:
            asix_x = i.x0 + i.y0 + i.z0
            rot = asix_x - self.camera.rot[1]
            order.append(rot)
        return sorted(range(len(order)), key = lambda i : order[i], reverse = 1)

    def update(self):
        self.grid.render()
        display = self.display_order()
        for i in range(len(self.rubicube)):
            self.rubicube[display[i]].render( self.rubicube_colors[display[i]])
