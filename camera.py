import math

class Camera():

    def __init__(self, pygame, pos = (0, 0, 10), rot = (0, 0), zoom = 200):
        self.pg = pygame
        self.pos = list(pos)
        self.rot = list(rot)
        self.orto_view = False
        self.zoom = zoom

    def events(self, event):
        if event.type == self.pg.KEYDOWN:
            if event.key == 111:
                self.orto_view = not self.orto_view

        if event.type == self.pg.MOUSEMOTION:
            x, y = event.rel
            y /= 400
            x /= 400
            self.rot[0] += y
            self.rot[1] += x
            if self.rot[0] > 2 * math.pi or self.rot[0] < -2 * math.pi:
                self.rot[0] = 0
            elif self.rot[1] > 2 * math.pi or self.rot[1] < -2 * math.pi:
                self.rot[1] = 0


        if event.type == self.pg.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.zoom += 50
            if event.button == 5:
                self.zoom -= 50
