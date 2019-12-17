class Camera:

    def __init__(self, root, pos=(0, 0, 15), rot=(0, 0), fov=200):
        self.root = root
        self.pg = self.root.pg
        self.pos = list(pos)
        self.rot = list(rot)
        self.orto_view = False
        #keys func
        self.fov = fov

    def set_height(self, dim):
        self.pos[2] = dim
