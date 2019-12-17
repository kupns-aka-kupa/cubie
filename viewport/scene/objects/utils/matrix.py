""" 2d Matrix rotate"""


def rotckw(mat, n, k):
    # Clockwise rotate
    return [[mat[k][j][n - (i + 1)] for j in range(len(mat[k]))] for i in range(len(mat[k]))]


def rotackw(mat, n, k):
    # Anticlockwise rotate
    return [[mat[k][n - (i + 1)][j] for i in range(len(mat[k]))] for j in range(len(mat[k]))]
