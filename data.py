from tools import file_manager

fm = file_manager.FileManager()


class Data:
    def __init__(self):
        self.colors = Palette()
        self.device = Device()
        self.cube = Cube(self.colors)
        self.grid = Grid(self.colors)
        self.gui = GUI()
        self.key_map = Keys()


class Keys(Data):
    def __init__(self):
        self.key = fm.open_file('settings/key_bindings/key_map.json')


class Device(Data):
    def __init__(self):
        data = fm.open_file('settings/device/preferences.json')
        self.width = data['width']
        self.height = data['height']
        self.center_x = self.width // 2
        self.center_y = self.height // 2
        self.mode = data['mode']
        self.fps = data['fps']
        self.sensivity = data['sensivity']


class Cube(Data):
    def __init__(self, palette):
        data = fm.open_file('objects/primitives/cube/cube.json')
        self.palette = palette
        self.line_width = data['line_width']
        self.vertex = data['vertex']
        self.edges = data['edges']
        self.faces = data['faces']
        self.colors = {
            'YOB_corner': [self.palette.orange, self.palette.blue, self.palette.yellow, self.palette.black],
            'YBR_corner': [self.palette.black, self.palette.blue, self.palette.yellow, self.palette.red,
                           self.palette.black],
            'YRG_corner': [self.palette.black, self.palette.black, self.palette.yellow, self.palette.red,
                           self.palette.green, self.palette.black],
            'YGO_corner': [self.palette.orange, self.palette.black, self.palette.yellow, self.palette.black,
                           self.palette.green, self.palette.black],

            'WOB_corner': [self.palette.orange, self.palette.blue, self.palette.black, self.palette.black,
                           self.palette.black, self.palette.white],
            'WBR_corner': [self.palette.black, self.palette.blue, self.palette.black, self.palette.red,
                           self.palette.black, self.palette.white],
            'WRG_corner': [self.palette.black, self.palette.black, self.palette.black, self.palette.red,
                           self.palette.green, self.palette.white],
            'WGO_corner': [self.palette.orange, self.palette.black, self.palette.black, self.palette.black,
                           self.palette.green, self.palette.white],

            'YB_edges': [self.palette.black, self.palette.blue, self.palette.yellow, self.palette.black],
            'YR_edges': [self.palette.black, self.palette.black, self.palette.yellow, self.palette.red,
                         self.palette.black],
            'YG_edges': [self.palette.black, self.palette.black, self.palette.yellow, self.palette.black,
                         self.palette.green, self.palette.black],
            'YO_edges': [self.palette.orange, self.palette.black, self.palette.yellow, self.palette.black],

            'WB_edges': [self.palette.black, self.palette.blue, self.palette.black, self.palette.black,
                         self.palette.black, self.palette.white],
            'WR_edges': [self.palette.black, self.palette.black, self.palette.black, self.palette.red,
                         self.palette.black, self.palette.white],
            'WG_edges': [self.palette.black, self.palette.black, self.palette.black, self.palette.black,
                         self.palette.green, self.palette.white],
            'WO_edges': [self.palette.orange, self.palette.black, self.palette.black, self.palette.black,
                         self.palette.black, self.palette.white],

            'OB_edges': [self.palette.orange, self.palette.blue, self.palette.black],
            'BR_edges': [self.palette.black, self.palette.blue, self.palette.black, self.palette.red,
                         self.palette.black],
            'RG_edges': [self.palette.black, self.palette.black, self.palette.black, self.palette.red,
                         self.palette.green, self.palette.black],
            'GO_edges': [self.palette.orange, self.palette.black, self.palette.black, self.palette.black,
                         self.palette.green, self.palette.black],

            'B_center': [self.palette.black, self.palette.blue, self.palette.black],
            'W_center': [self.palette.black, self.palette.black, self.palette.black, self.palette.black,
                         self.palette.black, self.palette.white],
            'R_center': [self.palette.black, self.palette.black, self.palette.black, self.palette.red,
                         self.palette.black],
            'G_center': [self.palette.black, self.palette.black, self.palette.black, self.palette.black,
                         self.palette.green, self.palette.black],
            'Y_center': [self.palette.black, self.palette.black, self.palette.yellow, self.palette.black],
            'O_center': [self.palette.orange, self.palette.black]
        }


class Palette(Data):
    def __init__(self):
        data = fm.open_file('settings/device/palette.json')
        self.black = data['black']
        self.white = data['white']
        self.green = data['green']
        self.yellow = data['yellow']
        self.blue = data['blue']
        self.orange = data['orange']
        self.red = data['red']


class GUI(Data):
    def __init__(self):
        self.buttons = {
            'Play': {
                'action': (),
                'New': {
                    'action': ()
                },
                'Load': {
                    'action': ()
                }
            },
            'Profile': {
                'action': ()
            },
            'Settings': {
                'action': ()
            },
            'About': {
                'action': ()
            },
            'Exit': {
                'action': (),
                'Yes': {
                    'action': ()
                },
                'No': {
                    'action': ()
                }
            }
        }


class Grid(Data):
    def __init__(self, palette):
        data = fm.open_file('objects/grid/grid.json')
        self.colors = palette
        self.vertex = data['vertex']
        self.size = data['size']
        self.labels = data['labels']
