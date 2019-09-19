import cube

class RubiksCube():

    def __init__(self, camera, pygame, data, tools):
        self.camera = camera
        self.pg = pygame
        self.data, self.device = data
        self.tools = tools
        self.depth = 0
        self.queue = []
        self.cube_generator()


    def cube_generator(self):
        self.cube_init()
        self.queue_init()

    def cube_init(self):
        colors = self.data.colors

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

    def logic(self, angles):
        for cube in self.queue:
            if cube.y0 == -2:#UP
                cube.rotation((-angles[0], 0, 0))

            if cube.y0 == 2:#DOWN
                cube.rotation((angles[1], 0, 0))

            if cube.x0 == 2:#RIGHT
                cube.rotation((0, -angles[2], 0))

            if cube.x0 == -2:#LEFT
                cube.rotation((0, angles[3], 0))

            if cube.z0 == -2:#FRONT
                cube.rotation((0, 0, angles[4]))

            if cube.z0 == 2:#BACK
                cube.rotation((0, 0, -angles[5]))

    def queue_init(self):
        for corner in self.corners:
            self.queue.append(cube.Cube(self.camera, self.pg, (self.data, self.device), corner[1], self.tools, corner[0]))

        for edge in self.edges:
            for i in range(len(edge[0])):
                self.queue.append(cube.Cube(self.camera, self.pg, (self.data, self.device), edge[1], self.tools, edge[0][i]))

        for center in self.centers:
            for i in range(len(center[0])):
                self.queue.append(cube.Cube(self.camera, self.pg, (self.data, self.device), center[1], self.tools, center[0][i]))

    def display_order(self):
        depth = []
        for el in self.queue:
            depth.append(el.depth)
        return sorted(range(len(self.queue)), key = lambda i : depth[i], reverse = 1)

    def render(self):
        display = self.display_order()
        for i in display:
            self.queue[i].render()
