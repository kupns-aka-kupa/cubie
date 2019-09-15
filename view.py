import tools, cube, grid
tools = tools.Tools()

class Viewport():

    def __init__(self, camera, pygame, data):
        self.camera = camera
        self.pg = pygame
        self.data = data
        self.cube = cube
        self.grid = grid.Grid(self.camera, self.pg, self.data, tools)
        self.queue = []

    def cube_generator(self, n):
        pass

    def cube_init(self):
        colors = self.data.cube.colors

#       start_coord(y,x,z)
        self.Y_corners = [
            [(2, -2, -2), colors['YOB_corner']],
            [(2, -2, 2), colors['YBR_corner']],
            [(-2, -2, 2), colors['YRG_corner']],
            [(-2, -2, -2), colors['YGO_corner']]
        ]
        self.W_corners = [
            [(2, 2, -2), colors['WOB_corner']],
            [(2, 2, 2), colors['WBR_corner']],
            [(-2, 2, 2), colors['WRG_corner']],
            [(-2, 2, -2), colors['WGO_corner']]
        ]
        self.edges = [
            [[(2, -2, 0)], colors['YB_edges']],
            [[(0, -2, 2)], colors['YR_edges']],
            [[(-2, -2, 0)], colors['YG_edges']],
            [[(0, -2, -2)], colors['YO_edges']],
            [[(2, 2, 0)], colors['WB_edges']],
            [[(0, 2, 2)], colors['WG_edges']],
            [[(-2, 2, 0)], colors['WR_edges']],
            [[(0, 2, -2)], colors['WO_edges']],
            [[(2, 0, -2)], colors['OB_edges']],
            [[(2, 0, 2)], colors['BR_edges']],
            [[(-2, 0, 2)], colors['RG_edges']],
            [[(-2, 0, -2)], colors['GO_edges']]
        ]
        self.centers = [
            [[(2, 0, 0)], colors['B_center']],
            [[(0, 2, 0)], colors['W_center']],
            [[(0, 0, 2)], colors['R_center']],
            [[(-2, 0, 0)], colors['G_center']],
            [[(0, -2, 0)], colors['Y_center']],
            [[(0, 0, -2)], colors['O_center']],
        ]

    def logic(self):
        R = self.centers[0]
        D = self.centers[1]
        B = self.centers[2]
        L = self.centers[3]
        U = self.centers[4]
        F = self.centers[5]

    def queue_init(self):
        for edge in self.edges:
            for i in range(len(edge[0])):
                self.queue.append(self.cube.Cube(self.camera, self.pg, self.data, edge[1], tools, edge[0][i]))

    def display_order(self):
        order = []
        for i in self.queue:
            asix_x = i.x0 + i.y0 + i.z0
            rot = asix_x - self.camera.rot[1]
            order.append(rot)
        return sorted(range(len(order)), key = lambda i : order[i], reverse = 1)

    def update(self):
        self.grid.render()
        self.logic()
        display = self.display_order()
        for el in self.queue:
            el.render()
