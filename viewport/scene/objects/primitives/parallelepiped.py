from .polyhedron import Polyhedron

""" The relationship of the parties:

    1) Z.O.X plane projection:

        |5 / 13|   1     |    15 / 13     |
        |      |         |                |
    ___\|/____\|/_______\|/______________\|/
       /|      |         |                |
5 / 9   |      |         |                |
    ___\|______|_________|________________|
       /|      |         |                |
        |      |         |                |
    1   |      |         |                |
        |      |         |                |
    ___\|______|_________|________________|
       /|      |         |                |
        |      |         |                |
        |      |         |                |
10 / 9  |      |         |                |
        |      |         |                |
        |      |         |                |
    ___\|______|_________|________________|

    2) Y.O.X plane projection:

        | 1 / 3 |   1     |    4 / 3       |
        |       |         |                |
    ___\|/_____\|/_______\|/______________\|/
       /|       |         |                |
5 / 9   |       |         |                |
    ___\|_______|_________|________________|
       /|       |         |                |
        |       |         |                |
    1   |       |         |                |
        |       |         |                |
    ___\|_______|_________|________________|
       /|       |         |                |
        |       |         |                |
        |       |         |                |
10 / 9  |       |         |                |
        |       |         |                |
        |       |         |                |
    ___\|_______|_________|________________|

     1) axis
    / 2) coefficient
    |/ 3) less/greater
    ||/
    YCL

"""

YCL, XCL, ZCL = 5 / 9, 5 / 13, 1 / 3
YCG, XCG, ZCG = 10 / 9, 15 / 13, 4 / 3


class Parallelepiped(Polyhedron):

    def __init__(self, root, data, geometry_data=None):
        super().__init__(root, data, geometry_data)

    def geometry_data_gen(self):
        data = self.root.root.global_settings['PUZZLE']['PRIMITIVES']['REGULAR']['CUBE'].copy()

        if self.y0 != 0:
            if self.y0 < 0:
                data['vertex'] = [[point[0], point[1] * YCL + 1 - YCL, point[2]] for point in data['vertex']]
            else:
                data['vertex'] = [[point[0], point[1] * YCG + YCG - 1, point[2]] for point in data['vertex']]
        if self.x0 != 0:
            if self.x0 < 0:
                data['vertex'] = [[point[0] * XCL + 1 - XCL, point[1], point[2]] for point in data['vertex']]
            else:
                data['vertex'] = [[point[0] * XCG + XCG - 1, point[1], point[2]] for point in data['vertex']]
        if self.z0 != 0:
            if self.z0 < 0:
                data['vertex'] = [[point[0], point[1], point[2] * ZCL + 1 - ZCL] for point in data['vertex']]
            else:
                data['vertex'] = [[point[0], point[1], point[2] * ZCG + ZCG - 1] for point in data['vertex']]

        return data
