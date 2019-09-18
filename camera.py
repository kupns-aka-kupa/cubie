class Camera():

    def __init__(self, pygame, data, pos = (0, 0, 10), rot = (0, 0), zoom = 200):
        self.pg = pygame
        self.data = data
        self.pos = list(pos)
        self.rot = list(rot)
        self.orto_view = False
        #keys func
        self.zoom = zoom
