import cube
from itertools import product as pd

class RubiksCube():

    def __init__(self, camera, pygame, data):
        self.camera = camera
        self.pg = pygame
        self.data, self.device = data
        self.depth = 0
        self.queue = []
        self.dimension = 5
        self.wireframe = False
        self.cube_generator()


    def cube_generator(self):
        self.cube_init()
        self.queue_init()

    def cube_init(self):
        colors = self.data.colors
#       start_coord(y,x,z)
        self.corners = [
            [None, colors['YGO_corner']],
            [None, colors['YRG_corner']],
            [None, colors['WGO_corner']],
            [None, colors['WRG_corner']],
            [None, colors['YOB_corner']],
            [None, colors['YBR_corner']],
            [None, colors['WOB_corner']],
            [None, colors['WBR_corner']]
        ]

        self.edges = [
            [[], colors['YB_edges']],
            [[], colors['WB_edges']],
            [[], colors['YG_edges']],
            [[], colors['WG_edges']],
            [[], colors['GO_edges']],
            [[], colors['OB_edges']],
            [[], colors['RG_edges']],
            [[], colors['BR_edges']],
            [[], colors['WO_edges']],
            [[], colors['WR_edges']],
            [[], colors['YR_edges']],
            [[], colors['YO_edges']],
        ]

        self.centers = [
            [[], colors['B_center']],
            [[], colors['G_center']],
            [[], colors['W_center']],
            [[], colors['Y_center']],
            [[], colors['R_center']],
            [[], colors['O_center']],
        ]

        self.coords_gen(self.dimension)

    def coords_gen(self, n):
        n = n - 1
        even = bool(n % 2)

        corners_coords = [(-n, n), (-n, n), (-n, n)]
        cp_cor = tuple(pd(*corners_coords))
        for i in range(len(self.corners)):
            self.corners[i][0] = cp_cor[i]

        if even:
            pass
        else:

            for i in range(n, 0 , -2):

                YB_edges = [(n, n, n), (-n, -n, -n), (n - i, -n + i, -n + i)]
                self.edges[0][0] += list(set(pd(*list(YB_edges))))

                WB_edges = [(n, n, n), (n, n, n), (n - i, -n + i, -n + i)]
                self.edges[1][0] += list(set(pd(*list(WB_edges))))

                YG_edges = [(-n, -n, -n), (-n, -n, -n), (n - i, -n + i, -n + i)]
                self.edges[2][0] += list(set(pd(*list(YG_edges))))

                WG_edges = [(-n, -n, -n), (n, n, n), (n - i, -n + i, -n + i)]
                self.edges[3][0] += list(set(pd(*list(WG_edges))))

                GO_edges = [(-n, -n, -n), (n - i, -n + i, -n + i), (-n, -n, -n)]
                self.edges[4][0] += list(set(pd(*list(GO_edges))))

                OB_edges = [(n, n, n), (n - i, -n + i, -n + i), (-n, -n, -n)]
                self.edges[5][0] += list(set(pd(*list(OB_edges))))

                BR_edges = [(-n, -n, -n), (n - i, -n + i, -n + i), (n, n, n)]
                self.edges[6][0] += list(set(pd(*list(BR_edges))))

                RG_edges = [(n, n, n), (n - i, -n + i, -n + i), (n, n, n)]
                self.edges[7][0] += list(set(pd(*list(RG_edges))))

                WO_edges = [(n - i, -n + i, -n + i), (n, n, n), (-n, -n, -n)]
                self.edges[8][0] += list(set(pd(*list(WO_edges))))

                WR_edges = [(n - i, -n + i, -n + i), (n, n, n), (n, n, n)]
                self.edges[9][0] += list(set(pd(*list(WR_edges))))

                YR_edges = [(n - i, -n + i, -n + i), (-n, -n, -n), (n, n, n)]
                self.edges[10][0] += list(set(pd(*list(YR_edges))))

                YO_edges = [(n - i, -n + i, -n + i), (-n, -n, -n), (-n, -n, -n)]
                self.edges[11][0] += list(set(pd(*list(YO_edges))))

                for j in range(n, 0 , -2):

                    B_center = (n, n, n), (n - j, -n + j, n - j), (n - i, -n + i, n - i)
                    G_center = (-n, -n, -n), (n - j, -n + j, n - j), (n - i, -n + i, n - i)
                    self.centers[0][0] += list(set(pd(*list(B_center))))
                    self.centers[1][0] += list(set(pd(*list(G_center))))

                    W_center = (n - j, -n + j, n - j), (n, n, n), (n - i, -n + i, n - i)
                    Y_center = (n - j, -n + j, n - j), (-n, -n, -n), (n - i, -n + i, n - i)
                    self.centers[2][0] += list(set(pd(*list(W_center))))
                    self.centers[3][0] += list(set(pd(*list(Y_center))))

                    R_center = (n - j, -n + j, n - j), (n - i, -n + i, n - i), (n, n, n)
                    O_center = (n - j, -n + j, n - j), (n - i, -n + i, n - i), (-n, -n, -n)
                    self.centers[4][0] += list(set(pd(*list(R_center))))
                    self.centers[5][0] += list(set(pd(*list(O_center))))

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
            self.queue.append(cube.Cube(self.camera, self.pg, (self.data, self.device), corner[1], corner[0]))

            for edge in self.edges:
                for i in range(len(edge[0])):
                    self.queue.append(cube.Cube(self.camera, self.pg, (self.data, self.device), edge[1], edge[0][i]))

            for center in self.centers:
                for i in range(len(center[0])):
                    self.queue.append(cube.Cube(self.camera, self.pg, (self.data, self.device), center[1], center[0][i]))

    def display_order(self):
        depth = []
        for el in self.queue:
            depth.append(el.depth)
        return sorted(range(len(self.queue)), key = lambda i : depth[i], reverse = 1)

    def render(self):
        display = self.display_order()
        for i in display:
            self.queue[i].render()
