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

    def logic(self, rot):
        if rot[0] != 0:
            for cube in self.queue:
                if cube.y0 == -2:#UP
                    cube.rotx -= rot[0]
                    cube.x0, cube.z0 = self.tools.rotate((cube.x0, cube.z0), -rot[0])
                    cube.x0 = round(cube.x0)
                    cube.z0 = round(cube.z0)


        if rot[1] != 0:
            for cube in self.queue:
                if cube.y0 == 2 :#DOWN
                    cube.rotx += rot[1]
                    cube.x0, cube.z0 = self.tools.rotate((cube.x0, cube.z0), rot[1])
                    cube.x0 = round(cube.x0)
                    cube.z0 = round(cube.z0)
#
        if rot[2] != 0:
            for cube in self.queue:
                if cube.x0 == 2:#RIGHT
                    cube.roty -= rot[2]
                    cube.y0, cube.z0 = self.tools.rotate((cube.y0, cube.z0), -rot[2])
                    cube.y0 = round(cube.y0)
                    cube.z0 = round(cube.z0)
#
        if rot[3] != 0:
            for cube in self.queue:
                if cube.x0 == -2:#LEFT
                    cube.roty += rot[3]
                    cube.y0, cube.z0 = self.tools.rotate((cube.y0, cube.z0), rot[3])
                    cube.y0 = round(cube.y0)
                    cube.z0 = round(cube.z0)
#
        if rot[4] != 0:
            for cube in self.queue:
                if cube.z0 == -2:#FRONT
                    cube.rotz += rot[4]
                    cube.x0, cube.y0 = self.tools.rotate((cube.x0, cube.y0), rot[4])
                    cube.x0 = round(cube.x0)
                    cube.y0 = round(cube.y0)

        if rot[5] != 0:
            for cube in self.queue:
                if cube.z0 == 2 :#BACK
                    cube.rotz -= rot[5]
                    cube.x0, cube.y0 = self.tools.rotate((cube.x0, cube.y0), -rot[5])
                    cube.x0 = round(cube.x0)
                    cube.y0 = round(cube.y0)



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
