from ..puzzle import Puzzle
from objects.primitives.cube.cube import Cube
from itertools import product as pd
from .presets import cube_dimension_presets

CUBE_COLOR_MAP = ['objects/puzzle/rubiks_cube/cube_color_map.json']


class RubiksCube(Puzzle):
    __corners = None
    __edges = None
    __centers = None

    def __init__(self, root):
        super().__init__(root)
        self.color_map = self.root.root.file_manager.load(CUBE_COLOR_MAP)['CUBE_COLOR_MAP']
        self.depth = 0
        self.dimension = 3
        self.puzzle_gen()

    def puzzle_gen(self):
        super().puzzle_gen()
        self.render_queue_init(Cube)

    def puzzle_struct_init(self):
        #        start_coord - y,x,z
        self.__corners = [
            [[], self.color_map['YGO_corner']],
            [[], self.color_map['YRG_corner']],
            [[], self.color_map['WGO_corner']],
            [[], self.color_map['WRG_corner']],
            [[], self.color_map['YOB_corner']],
            [[], self.color_map['YBR_corner']],
            [[], self.color_map['WOB_corner']],
            [[], self.color_map['WBR_corner']]
        ]
        self.__edges = [
            [[], self.color_map['YB_edges']],
            [[], self.color_map['WB_edges']],
            [[], self.color_map['YG_edges']],
            [[], self.color_map['WG_edges']],
            [[], self.color_map['GO_edges']],
            [[], self.color_map['OB_edges']],
            [[], self.color_map['RG_edges']],
            [[], self.color_map['BR_edges']],
            [[], self.color_map['WO_edges']],
            [[], self.color_map['WR_edges']],
            [[], self.color_map['YR_edges']],
            [[], self.color_map['YO_edges']]
        ]
        self.__centers = [
            [[], self.color_map['B_center']],
            [[], self.color_map['G_center']],
            [[], self.color_map['W_center']],
            [[], self.color_map['Y_center']],
            [[], self.color_map['R_center']],
            [[], self.color_map['O_center']]
        ]
        self._struct = [self.__corners, self.__edges, self.__centers]

    def __corners_coordinates_gen(self):
        n = self.dimension - 1
        coords = (-n, n), (-n, n), (-n, n)
        return [tuple(pd(*coords))[i] for i in range(len(self.__corners))]

    def __edges_coordinates_gen(self, mult, i):
        n = self.dimension - 1
        coords = [
            # YB_edges
            ((n, n, n), (-n, -n, -n), (n - i * mult, -n + i * mult, -n + i * mult)),
            # WB_edges
            ((n, n, n), (n, n, n), (n - i * mult, -n + i * mult, -n + i * mult)),
            # YG_edges
            ((-n, -n, -n), (-n, -n, -n), (n - i * mult, -n + i * mult, -n + i * mult)),
            # WG_edges
            ((-n, -n, -n), (n, n, n), (n - i * mult, -n + i * mult, -n + i * mult)),
            # GO_edges
            ((-n, -n, -n), (n - i * mult, -n + i * mult, -n + i * mult), (-n, -n, -n)),
            # OB_edges
            ((n, n, n), (n - i * mult, -n + i * mult, -n + i * mult), (-n, -n, -n)),
            # BR_edges
            ((-n, -n, -n), (n - i * mult, -n + i * mult, -n + i * mult), (n, n, n)),
            # RG_edges
            ((n, n, n), (n - i * mult, -n + i * mult, -n + i * mult), (n, n, n)),
            # WO_edges
            ((n - i * mult, -n + i * mult, -n + i * mult), (n, n, n), (-n, -n, -n)),
            # WR_edges
            ((n - i * mult, -n + i * mult, -n + i * mult), (n, n, n), (n, n, n)),
            # YR_edges
            ((n - i * mult, -n + i * mult, -n + i * mult), (-n, -n, -n), (n, n, n)),
            # YO_edges
            ((n - i * mult, -n + i * mult, -n + i * mult), (-n, -n, -n), (-n, -n, -n))
        ]
        return [tuple(set(pd(*coords[j]))) for j in range(len(self.__edges))]

    def __centers_coordinates_gen(self, mult, i, j):
        n = self.dimension - 1
        coords = [
            # B_center
            ((n, n, n), (n - j * mult, -n + j * mult, n - j * mult), (n - i * mult, -n + i * mult, n - i * mult)),
            # G_center
            ((-n, -n, -n), (n - j * mult, -n + j * mult, n - j * mult), (n - i * mult, -n + i * mult, n - i * mult)),
            # W_center
            ((n - j * mult, -n + j * mult, n - j * mult), (n, n, n), (n - i * mult, -n + i * mult, n - i * mult)),
            # Y_center
            ((n - j * mult, -n + j * mult, n - j * mult), (-n, -n, -n), (n - i * mult, -n + i * mult, n - i * mult)),
            # R_center
            ((n - j * mult, -n + j * mult, n - j * mult), (n - i * mult, -n + i * mult, n - i * mult), (n, n, n)),
            # O_center
            ((n - j * mult, -n + j * mult, n - j * mult), (n - i * mult, -n + i * mult, n - i * mult), (-n, -n, -n))
        ]
        return [tuple(set(pd(*coords[k]))) for k in range(len(self.__centers))]

    def puzzle_part_coordinates_gen(self, tresh, mult):
        # просто не суйся сюда ,окэй?
        # все работает корректно ,а точнее лишних экземпляров не создает
        corners = []
        edges = [[] for _ in range(len(self.__edges))]
        centers = [[] for _ in range(len(self.__centers))]
        coords = [corners, edges, centers]

        n = self.dimension - 1
        corners_coords = self.__corners_coordinates_gen()
        for j in range(len(self.__corners)):
            corners.append([corners_coords[j]])
        for i in range(n - tresh, 0, -2):
            edges_coords = self.__edges_coordinates_gen(mult, i)
            for j in range(len(self.__edges)):
                edges[j] += edges_coords[j]
            for j in range(n - tresh, 0, -2):
                centers_coords = self.__centers_coordinates_gen(mult, i, j)
                for k in range(len(self.__centers)):
                    centers[k] += centers_coords[k]
        return coords

    def puzzle_parts_gen(self):
        n = self.dimension - 1
        even = bool(n % 2)

        if len(cube_dimension_presets) >= n:
            return self.puzzle_default_preset_load(cube_dimension_presets, n - 1)
        else:
            if even:
                return self.puzzle_part_coordinates_gen(2, 2)
            else:
                return self.puzzle_part_coordinates_gen(0, 1)

    def puzzle_logic(self, angles):
        for cube in self._render_queue:
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
