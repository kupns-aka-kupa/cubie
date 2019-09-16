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
        self.corners = [
            [(2, -2, -2), colors['YOB_corner']],
            [(2, -2, 2), colors['YBR_corner']],
            [(-2, -2, 2), colors['YRG_corner']],
            [(-2, -2, -2), colors['YGO_corner']],
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
            [[(0, 2, 2)], colors['WR_edges']],
            [[(-2, 2, 0)], colors['WG_edges']],
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
        for cube in self.queue:
            if cube.y0 == -2:#UP
                cube.rot = [self.camera.U_rot, 0, 0]

        for cube in self.queue:
            if cube.y0 == 2:#DOWN
                cube.rot = [self.camera.D_rot, 0, 0]

        for cube in self.queue:
            if cube.z0 == 2:#FRONT
                cube.rot = [0, 0, -self.camera.F_rot]

        for cube in self.queue:
            if cube.z0 == -2:#BACK
                cube.rot = [0, 0, self.camera.B_rot]

        for cube in self.queue:
            if cube.x0 == -2:#LEFT
                cube.rot = [0, 0, self.camera.L_rot]

        for cube in self.queue:
            if cube.x0 == 2:#RIGHT
                cube.rot = [0, -self.camera.R_rot, 0]



    def queue_init(self):
        for corners in self.corners:
            self.queue.append(self.cube.Cube(self.camera, self.pg, self.data, corners[1], tools, corners[0]))

        for edge in self.edges:
            for i in range(len(edge[0])):
                self.queue.append(self.cube.Cube(self.camera, self.pg, self.data, edge[1], tools, edge[0][i]))

        for center in self.centers:
            for i in range(len(center[0])):
                self.queue.append(self.cube.Cube(self.camera, self.pg, self.data, center[1], tools, center[0][i]))

    def display_order(self):
        depth = []
        for cube in self.queue:
            depth.append(cube.depth)
        return sorted(range(len(self.queue)), key = lambda i : depth[i], reverse = 1)

    def update(self):
        self.grid.render()
        display = self.display_order()
        for i in display:
            self.queue[i].render()
