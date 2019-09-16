class Camera():

    def __init__(self, pygame, data, pos = (0, 0, 10), rot = (0, 0), zoom = 200):
        self.pg = pygame
        self.data = data
        self.pos = list(pos)
        self.rot = list(rot)
        #keys func
        self.orto_view = False
        self.shift = False
        self.ctrl = False
        self.zoom = zoom
        self.U_rot = 0
        self.D_rot = 0
        self.R_rot = 0
        self.L_rot = 0
        self.B_rot = 0
        self.F_rot = 0

    def events(self, event):
        keys = self.pg.key.get_pressed()
        math = self.data.math
        key_map = self.data.key_map
        if event.type == self.pg.KEYDOWN:
            if event.key == key_map.key['o']:
                self.orto_view = not self.orto_view

            if event.key == key_map.key['up']:
                if self.shift:
                    self.U_rot -= math.pi / 2
                else:
                    self.U_rot += math.pi / 2

                if self.U_rot <= -2 * math.pi:
                    self.U_rot = 0
                elif self.U_rot >= 2 * math.pi:
                    self.U_rot = 0
                return True

            if event.key == key_map.key['down']:
                if self.shift:
                    self.D_rot -= math.pi / 2
                else:
                    self.D_rot += math.pi / 2

                if self.D_rot <= -2 * math.pi:
                    self.D_rot = 0
                elif self.D_rot >= 2 * math.pi:
                    self.D_rot = 0
                return True

            if event.key == key_map.key['lelf']:
                if self.shift:
                    self.L_rot -= math.pi / 2
                else:
                    self.L_rot += math.pi / 2

                if self.L_rot <= -2 * math.pi:
                    self.L_rot = 0
                elif self.L_rot >= 2 * math.pi:
                    self.L_rot = 0
                return True

            if event.key == key_map.key['right']:
                if self.shift:
                    self.R_rot -= math.pi / 2
                else:
                    self.R_rot += math.pi / 2

                if self.R_rot <= -2 * math.pi:
                    self.R_rot = 0
                elif self.R_rot >= 2 * math.pi:
                    self.R_rot = 0
                return True

            if event.key == key_map.key['front']:
                if self.shift:
                    self.F_rot -= math.pi / 2
                else:
                    self.F_rot += math.pi / 2

                if self.F_rot <= -2 * math.pi:
                    self.F_rot = 0
                elif self.F_rot >= 2 * math.pi:
                    self.F_rot = 0
                return True

            if event.key == key_map.key['back']:
                if self.shift:
                    self.B_rot -= math.pi / 2
                else:
                    self.B_rot += math.pi / 2

                if self.B_rot <= -2 * math.pi:
                    self.B_rot = 0
                elif self.B_rot >= 2 * math.pi:
                    self.B_rot = 0
                return True

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
