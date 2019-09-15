class Camera():

    def __init__(self, pygame, data, pos = (0, 0, 10), rot = (0, 0), zoom = 200):
        self.pg = pygame
        self.data = data
        self.pos = list(pos)
        self.rot = list(rot)
        self.orto_view = False
        self.zoom = zoom
        self.U_rot = 0
        self.D_rot = 0
        self.R_rot = 0
        self.L_rot = 0
        self.B_rot = 0
        self.F_rot = 0

    def events(self, event):
        math = self.data.math
        key_map = self.data.key_map
        if event.type == self.pg.KEYDOWN:
#            print(event.key)
            if event.key == key_map.key['o']:
                self.orto_view = not self.orto_view
            if event.key == key_map.key['q']:
                self.U_rot -= math.pi / 2
                if self.U_rot < -2 * math.pi:
                     self.U_rot = 0
            if event.key == key_map.key['e']:
                self.U_rot += math.pi / 2
                if self.U_rot > 2 * math.pi:
                     self.U_rot = 0

        if event.type == self.pg.MOUSEMOTION:
            x, y = event.rel
            y /= 400
            x /= 400
            self.rot[0] += y
            self.rot[1] += x
            if self.rot[0] >= math.pi:
                self.rot[0] = -math.pi
            elif self.rot[0] <= -math.pi:
                self.rot[0] = math.pi

            elif self.rot[1] >= math.pi:
                self.rot[1] = -math.pi
            elif self.rot[1] <= -math.pi:
                self.rot[1] = math.pi


        if event.type == self.pg.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.zoom += 50
            if event.button == 5:
                self.zoom -= 50
