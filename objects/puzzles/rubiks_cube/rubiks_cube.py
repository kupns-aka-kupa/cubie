from objects.primitives.cube import cube
from itertools import product as pd
from itertools import compress as cp

class RubiksCube:

    def __init__(self, camera, pygame, data):
        self.camera = camera
        self.pg = pygame
        self.data, self.device = data
        self.depth = 0
        self.queue = []
        self.dimension = 3
        self.wireframe = False
        self.cube_generator()


    def cube_generator(self):
        self.cube_init()
        self.queue_init()

    def cube_init(self):
        colors = self.data.colors
#       start_coord - y,x,z
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
            [[], colors['YO_edges']]
        ]

        self.centers = [
            [[], colors['B_center']],
            [[], colors['G_center']],
            [[], colors['W_center']],
            [[], colors['Y_center']],
            [[], colors['R_center']],
            [[], colors['O_center']]
        ]

        self.coords_gen()

    def coords_pieces_gen(self, tresh, mult):
        n = self.dimension - 1

        corners_coords = (-n, n), (-n, n), (-n, n)
        for i in range(len(self.corners)):
            self.corners[i][0] = tuple(pd(*corners_coords))[i]

        for i in range(n - tresh, 0 , -2):

            YB_edges = (n, n, n), (-n, -n, -n), (n - i * mult, -n + i * mult, -n + i * mult)
            self.edges[0][0] += tuple(set(pd(*YB_edges)))

            WB_edges = (n, n, n), (n, n, n), (n - i * mult, -n + i * mult, -n + i * mult)
            self.edges[1][0] += tuple(set(pd(*WB_edges)))

            YG_edges = (-n, -n, -n), (-n, -n, -n), (n - i * mult, -n + i * mult, -n + i * mult)
            self.edges[2][0] += tuple(set(pd(*YG_edges)))

            WG_edges = (-n, -n, -n), (n, n, n), (n - i * mult, -n + i * mult, -n + i * mult)
            self.edges[3][0] += tuple(set(pd(*WG_edges)))

            GO_edges = (-n, -n, -n), (n - i * mult, -n + i * mult, -n + i * mult), (-n, -n, -n)
            self.edges[4][0] += tuple(set(pd(*GO_edges)))

            OB_edges = (n, n, n), (n - i * mult, -n + i * mult, -n + i * mult), (-n, -n, -n)
            self.edges[5][0] += tuple(set(pd(*OB_edges)))

            BR_edges = (-n, -n, -n), (n - i * mult, -n + i * mult, -n + i * mult), (n, n, n)
            self.edges[6][0] += tuple(set(pd(*BR_edges)))

            RG_edges = (n, n, n), (n - i * mult, -n + i * mult, -n + i * mult), (n, n, n)
            self.edges[7][0] += tuple(set(pd(*RG_edges)))

            WO_edges = (n - i * mult, -n + i * mult, -n + i * mult), (n, n, n), (-n, -n, -n)
            self.edges[8][0] += tuple(set(pd(*WO_edges)))

            WR_edges = (n - i * mult, -n + i * mult, -n + i * mult), (n, n, n), (n, n, n)
            self.edges[9][0] += tuple(set(pd(*WR_edges)))

            YR_edges = (n - i * mult, -n + i * mult, -n + i * mult), (-n, -n, -n), (n, n, n)
            self.edges[10][0] += tuple(set(pd(*YR_edges)))

            YO_edges = (n - i * mult, -n + i * mult, -n + i * mult), (-n, -n, -n), (-n, -n, -n)
            self.edges[11][0] += tuple(set(pd(*YO_edges)))

            for j in range(n - tresh, 0 , -2):

                B_center = (n, n, n), (n - j * mult, -n + j * mult, n - j * mult), (n - i * mult, -n + i * mult, n - i * mult)
                G_center = (-n, -n, -n), (n - j * mult, -n + j * mult, n - j * mult), (n - i * mult, -n + i * mult, n - i * mult)
                self.centers[0][0] += tuple(set(pd(*B_center)))
                self.centers[1][0] += tuple(set(pd(*G_center)))

                W_center = (n - j * mult, -n + j * mult, n - j * mult), (n, n, n), (n - i * mult, -n + i * mult, n - i * mult)
                Y_center = (n - j * mult, -n + j * mult, n - j * mult), (-n, -n, -n), (n - i * mult, -n + i * mult, n - i * mult)
                self.centers[2][0] += tuple(set(pd(*W_center)))
                self.centers[3][0] += tuple(set(pd(*Y_center)))

                R_center = (n - j * mult, -n + j * mult, n - j * mult), (n - i * mult, -n + i * mult, n - i * mult), (n, n, n)
                O_center = (n - j * mult, -n + j * mult, n - j * mult), (n - i * mult, -n + i * mult, n - i * mult), (-n, -n, -n)
                self.centers[4][0] += tuple(set(pd(*R_center)))
                self.centers[5][0] += tuple(set(pd(*O_center)))

    def coords_gen(self):
        n = self.dimension - 1
        even = bool(n % 2)

        if even:
            self.coords_pieces_gen(2, 2)
        else:
            self.coords_pieces_gen(0, 1)

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
#
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
