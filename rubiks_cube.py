import cube

class RubiksCube():

    def __init__(self, camera, pygame, data, tools):
        self.camera = camera
        self.pg = pygame
        self.data, self.device = data
        self.tools = tools
        self.depth = 0
        self.queue = []
        self.U_rot = 0
        self.D_rot = 0
        self.R_rot = 0
        self.L_rot = 0
        self.B_rot = 0
        self.F_rot = 0
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

#    def logic(self, rot):
#        U_angle, D_angle, F_angle ,B_angle, L_angle, R_angle = list(angles)
#        self.U_rot += U_angle
#        self.D_rot += D_angle
#        self.R_rot += F_angle
#        self.L_rot += B_angle
#        self.B_rot += L_angle
#        self.F_rot += R_angle
#        for cube in self.queue:
#            if cube.y0 == -2:#UP
#                cube.rot = [self.U_rot, 0, 0]
#                cube.x0, cube.z0 = tools.rotate((cube.x0, cube.z0), U_angle)
#            if cube.y0 == 2:#DOWN
#                cube.rot = [self.D_rot, 0, 0]
#                cube.x0, cube.z0 = tools.rotate((cube.x0, cube.z0), D_angle)
#
#            if cube.z0 == 2:#FRONT
#                cube.rot = [0, 0, -F_rot]
#
#            if cube.z0 == -2:#BACK
#                cube.rot = [0, 0, B_rot]
#
#            if cube.x0 == -2:#LEFT
#                cube.rot = [0, L_rot, 0]
#
#            if cube.x0 == 2:#RIGHT
#                cube.rot = [0, -R_rot, 0]


    def queue_init(self):
        for corners in self.corners:
            self.queue.append(cube.Cube(self.camera, self.pg, (self.data, self.device), corners[1], self.tools, corners[0]))

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
