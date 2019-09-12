class Data():
    def __init__(self):
        self.colors = colors()
        self.cube = cube()
        self.grid = grid()

class colors(Data):
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 200, 64)
        self.yellow = (225, 225, 0)
        self.blue = (0, 0, 255)
        self.orange = (255, 165, 0)
        self.red = (255, 0, 0)

class cube(Data):
    def __init__(self):
            self.vertex = (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
            self.edges = (0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4) ,(0, 4), (1, 5), (2, 6), (3, 7)
            self.faces = (0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (2, 3, 7, 6), (0, 3, 7, 4), (1, 2, 6, 5)

class grid(Data):
    def __init__(self):
        self.vertex = [[1, 0, 0], [0, -1, 0], [0, 0, 1], [-1, 0, 0], [0, 1, 0], [0, 0, -1]]
        self.labels = ['+y', '-x', '+z', '-y', '+x', '-z' ]

data = Data()
