from .parallelepiped import Parallelepiped


class Cube(Parallelepiped):
    def __init__(self, root, data):
        super().__init__(root, data, root.root.global_settings['PUZZLE']['PRIMITIVES']['REGULAR']['CUBE'])
