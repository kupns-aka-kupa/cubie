from objects.primitives.cube.cube import Cube
from itertools import product as pd
from .data import color_map


class Puzzle:
    __corners = None
    __edges = None
    __centers = None
    wireframe = False

    def __init__(self, root):
        self.root = root
        self.camera = self.root.camera
        self.pg = self.root.pg
        self.render_queue = []
        self.dimension = 3
        self.cube_generator()

    def cube_generator(self):
        self.cube_init()
        self.render_queue_init()

    def cube_init(self):
        #       start_coord - y,x,z
        self.__corners = [
            [None, color_map['YGO_corner']],
            [None, color_map['YRG_corner']],
            [None, color_map['WGO_corner']],
            [None, color_map['WRG_corner']],
            [None, color_map['YOB_corner']],
            [None, color_map['YBR_corner']],
            [None, color_map['WOB_corner']],
            [None, color_map['WBR_corner']]
        ]
        self.__edges = [
            [[], color_map['YB_edges']],
            [[], color_map['WB_edges']],
            [[], color_map['YG_edges']],
            [[], color_map['WG_edges']],
            [[], color_map['GO_edges']],
            [[], color_map['OB_edges']],
            [[], color_map['RG_edges']],
            [[], color_map['BR_edges']],
            [[], color_map['WO_edges']],
            [[], color_map['WR_edges']],
            [[], color_map['YR_edges']],
            [[], color_map['YO_edges']]
        ]
        self.__centers = [
            [[], color_map['B_center']],
            [[], color_map['G_center']],
            [[], color_map['W_center']],
            [[], color_map['Y_center']],
            [[], color_map['R_center']],
            [[], color_map['O_center']]
        ]
        self.coords_gen()

    def coords_pieces_gen(self, tresh, mult):
        n = self.dimension - 1
        # corners
        coords = (-n, n), (-n, n), (-n, n)
        for i in range(len(self.__corners)):
            self.__corners[i][0] = tuple(pd(*coords))[i]

        for i in range(n - tresh, 0, -2):
            # YB_edges
            coords = (n, n, n), (-n, -n, -n), (n - i * mult, -n + i * mult, -n + i * mult)
            self.__edges[0][0] += tuple(set(pd(*coords)))
            # WB_edges
            coords = (n, n, n), (n, n, n), (n - i * mult, -n + i * mult, -n + i * mult)
            self.__edges[1][0] += tuple(set(pd(*coords)))
            # YG_edges
            coords = (-n, -n, -n), (-n, -n, -n), (n - i * mult, -n + i * mult, -n + i * mult)
            self.__edges[2][0] += tuple(set(pd(*coords)))
            # WG_edges
            coords = (-n, -n, -n), (n, n, n), (n - i * mult, -n + i * mult, -n + i * mult)
            self.__edges[3][0] += tuple(set(pd(*coords)))
            # GO_edges
            coords = (-n, -n, -n), (n - i * mult, -n + i * mult, -n + i * mult), (-n, -n, -n)
            self.__edges[4][0] += tuple(set(pd(*coords)))
            # OB_edges
            coords = (n, n, n), (n - i * mult, -n + i * mult, -n + i * mult), (-n, -n, -n)
            self.__edges[5][0] += tuple(set(pd(*coords)))
            # BR_edges
            coords = (-n, -n, -n), (n - i * mult, -n + i * mult, -n + i * mult), (n, n, n)
            self.__edges[6][0] += tuple(set(pd(*coords)))
            # RG_edges
            coords = (n, n, n), (n - i * mult, -n + i * mult, -n + i * mult), (n, n, n)
            self.__edges[7][0] += tuple(set(pd(*coords)))
            # WO_edges
            coords = (n - i * mult, -n + i * mult, -n + i * mult), (n, n, n), (-n, -n, -n)
            self.__edges[8][0] += tuple(set(pd(*coords)))
            # WR_edges
            coords = (n - i * mult, -n + i * mult, -n + i * mult), (n, n, n), (n, n, n)
            self.__edges[9][0] += tuple(set(pd(*coords)))
            # YR_edges
            coords = (n - i * mult, -n + i * mult, -n + i * mult), (-n, -n, -n), (n, n, n)
            self.__edges[10][0] += tuple(set(pd(*coords)))
            # YO_edges
            coords = (n - i * mult, -n + i * mult, -n + i * mult), (-n, -n, -n), (-n, -n, -n)
            self.__edges[11][0] += tuple(set(pd(*coords)))

            for j in range(n - tresh, 0, -2):
                # B_center
                coords = (n, n, n), \
                         (n - j * mult, -n + j * mult, n - j * mult), \
                         (n - i * mult, -n + i * mult, n - i * mult)
                self.__centers[0][0] += tuple(set(pd(*coords)))
                # G_center
                coords = (-n, -n, -n), \
                         (n - j * mult, -n + j * mult, n - j * mult), \
                         (n - i * mult, -n + i * mult, n - i * mult)
                self.__centers[1][0] += tuple(set(pd(*coords)))
                # W_center
                coords = (n - j * mult, -n + j * mult, n - j * mult), \
                         (n, n, n), \
                         (n - i * mult, -n + i * mult, n - i * mult)
                self.__centers[2][0] += tuple(set(pd(*coords)))
                # Y_center
                coords = (n - j * mult, -n + j * mult, n - j * mult), \
                         (-n, -n, -n), \
                         (n - i * mult, -n + i * mult, n - i * mult)
                self.__centers[3][0] += tuple(set(pd(*coords)))
                # R_center
                coords = (n - j * mult, -n + j * mult, n - j * mult), \
                         (n - i * mult, -n + i * mult, n - i * mult), \
                         (n, n, n)
                self.__centers[4][0] += tuple(set(pd(*coords)))
                # O_center
                coords = (n - j * mult, -n + j * mult, n - j * mult), \
                         (n - i * mult, -n + i * mult, n - i * mult), \
                         (-n, -n, -n)
                self.__centers[5][0] += tuple(set(pd(*coords)))

    def coords_gen(self):
        n = self.dimension - 1
        even = bool(n % 2)

        if even:
            self.coords_pieces_gen(2, 2)
        else:
            self.coords_pieces_gen(0, 1)

    def logic(self, angles):
        for cube in self.render_queue:
            if cube.y0 == -2:  # UP
                cube.rotation((-angles[0], 0, 0))

            if cube.y0 == 2:  # DOWN
                cube.rotation((angles[1], 0, 0))

            if cube.x0 == 2:  # RIGHT
                cube.rotation((0, -angles[2], 0))

            if cube.x0 == -2:  # LEFT
                cube.rotation((0, angles[3], 0))

            if cube.z0 == -2:  # FRONT
                cube.rotation((0, 0, angles[4]))

            if cube.z0 == 2:  # BACK
                cube.rotation((0, 0, -angles[5]))

    def queue_init(self):
        for corner in self.__corners:
            self.render_queue.append(
                Cube(self.root, corner)
            )

        for edge in self.__edges:
            for i in range(len(edge[0])):
                self.render_queue.append(
                    Cube(self.root, [edge[1], edge[0][i]])
                )

        for center in self.__centers:
            for i in range(len(center[0])):
                self.render_queue.append(
                    Cube(self.root, [center[1], center[0][i]])
                )

    def render_order(self):
        depth = []
        for el in self.render_queue:
            depth.append(el.depth)
        return sorted(range(len(self.render_queue)), key=lambda i: depth[i], reverse=1)

    def render(self):
        display = self.render_order()
        for i in display:
            self.render_queue[i].render()
