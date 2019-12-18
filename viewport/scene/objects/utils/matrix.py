""" Matrix utils"""
from itertools import product as pd


def _rotckw(mat, n, k):
    # Clockwise 2d matrix rotate
    return [[mat[k][j][n - (i + 1)] for j in range(len(mat[k]))] for i in range(len(mat[k]))]


def _rotackw(mat, n, k):
    # Anticlockwise 2d matrix rotate
    return [[mat[k][n - (i + 1)][j] for i in range(len(mat[k]))] for j in range(len(mat[k]))]


def _corners_coordinates_gen(self):
    n = self.dimension - 1
    coords = (-n, n), (-n, n), (-n, n)
    return [tuple(pd(*coords))[i] for i in range(len(self.__corners))]


def _edges_coordinates_gen(self, mult, i):
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


def _centers_coordinates_gen(self, mult, i, j):
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
