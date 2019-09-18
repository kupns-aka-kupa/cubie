class Data():
    def __init__(self):
        self.colors = palette()
        self.cube = cube()
        self.grid = grid()
        self.device = device()
        self.key_map = keys()

class keys(Data):
    def __init__(self):
        self.key = {
        'up' : 119,#w
        'down' : 115,#s
        'left' : 97,#a
        'right' : 100,#d
        'front' : 101,#e
        'back' : 113,#q
        'o' : 111,#o
        'z' : 122,#z
        'x' : 120,#x
        'c' : 99,#c
        'layer_1' : 49,#1
        'layer_2' : 50,#2
        'layer_3' : 51,#3
        'layer_4' : 52,#4
        }

class device(Data):
    def __init__(self):
        self.width = 800
        self.height = 800
        self.center_x = self.width // 2
        self.center_y = self.height // 2
        self.fps = 60

class cube(Data):
    def __init__(self):
        self.palette = palette()
        self.line_width = 2
        self.vertex = (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
        self.edges = (0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4) ,(0, 4), (1, 5), (2, 6), (3, 7)
        self.faces = (0, 1, 2, 3), (1, 2, 6, 5), (0, 1, 5, 4), (4, 5, 6, 7), (0, 3, 7, 4), (2, 3, 7, 6)
        self.colors = {
            'YOB_corner': [self.palette.orange, self.palette.blue, self.palette.yellow, self.palette.black],
            'YBR_corner': [self.palette.black, self.palette.blue, self.palette.yellow, self.palette.red, self.palette.black],
            'YRG_corner': [self.palette.black, self.palette.black, self.palette.yellow, self.palette.red, self.palette.green, self.palette.black],
            'YGO_corner': [self.palette.orange, self.palette.black, self.palette.yellow, self.palette.black, self.palette.green, self.palette.black],

            'WOB_corner': [self.palette.orange, self.palette.blue, self.palette.black, self.palette.black, self.palette.black, self.palette.white],
            'WBR_corner': [self.palette.black, self.palette.blue, self.palette.black, self.palette.red, self.palette.black, self.palette.white],
            'WRG_corner': [self.palette.black, self.palette.black, self.palette.black, self.palette.red, self.palette.green, self.palette.white],
            'WGO_corner': [self.palette.orange, self.palette.black, self.palette.black, self.palette.black, self.palette.green, self.palette.white],

            'YB_edges' : [self.palette.black, self.palette.blue, self.palette.yellow, self.palette.black],
            'YR_edges' : [self.palette.black, self.palette.black, self.palette.yellow, self.palette.red, self.palette.black],
            'YG_edges' : [self.palette.black, self.palette.black, self.palette.yellow, self.palette.black, self.palette.green, self.palette.black],
            'YO_edges' : [self.palette.orange, self.palette.black, self.palette.yellow, self.palette.black],

            'WB_edges' : [self.palette.black, self.palette.blue, self.palette.black, self.palette.black, self.palette.black, self.palette.white],
            'WR_edges' : [self.palette.black, self.palette.black, self.palette.black, self.palette.red, self.palette.black, self.palette.white],
            'WG_edges' : [self.palette.black, self.palette.black, self.palette.black, self.palette.black, self.palette.green, self.palette.white],
            'WO_edges' : [self.palette.orange, self.palette.black, self.palette.black, self.palette.black, self.palette.black, self.palette.white],

            'OB_edges' : [self.palette.orange, self.palette.blue, self.palette.black],
            'BR_edges' : [self.palette.black, self.palette.blue, self.palette.black, self.palette.red, self.palette.black],
            'RG_edges' : [self.palette.black, self.palette.black, self.palette.black, self.palette.red, self.palette.green, self.palette.black],
            'GO_edges' : [self.palette.orange, self.palette.black, self.palette.black, self.palette.black, self.palette.green, self.palette.black],

            'B_center' : [self.palette.black, self.palette.blue, self.palette.black],
            'W_center' : [self.palette.black, self.palette.black, self.palette.black, self.palette.black, self.palette.black, self.palette.white],
            'R_center' : [self.palette.black, self.palette.black, self.palette.black, self.palette.red, self.palette.black],
            'G_center' : [self.palette.black, self.palette.black, self.palette.black, self.palette.black, self.palette.green, self.palette.black],
            'Y_center' : [self.palette.black, self.palette.black, self.palette.yellow, self.palette.black],
            'O_center' : [self.palette.orange, self.palette.black]
            }

class palette(Data):
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 200, 64)
        self.yellow = (225, 225, 0)
        self.blue = (0, 0, 255)
        self.orange = (255, 165, 0)
        self.red = (255, 0, 0)

class grid(Data):
    def __init__(self):
        self.colors = palette()
        self.vertex = [[1, 0, 0], [0, -1, 0], [0, 0, 1], [-1, 0, 0], [0, 1, 0], [0, 0, -1]]
        self.size = 10
        self.labels = ['+y', '-x', '+z', '-y', '+x', '-z' ]
