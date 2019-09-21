class Camera():

    def __init__(self, pygame, data, pos = (0, 0, 15), rot = (0, 0), fov = 200):
        self.pg = pygame
        self.data = data
        self.pos = list(pos)
        self.rot = list(rot)
        self.orto_view = False
        #keys func
        self.fov = fov

    def set_height(self, dim):
        self.pos[2] = dim
