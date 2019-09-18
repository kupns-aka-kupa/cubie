class Events():
    def __init__(self, viewport):
        self.viewport = viewport
        self.camera = self.viewport.camera
        self.pg = self.viewport.pg
        self.data = self.viewport.data
        self.shift = False
        self.ctrl = False
        self.middle_mouse = False

    def update(self):
        for event in self.pg.event.get():
            if event.type == self.pg.QUIT: self.pg.quit()
            keys = self.pg.key.get_pressed()
            mouse_btns = self.pg.mouse.get_pressed()
            self.shift = keys[self.pg.K_LSHIFT]
            self.ctrl = keys[self.pg.K_LCTRL]
            self.middle_mouse = mouse_btns[1]
            self.mouse_events(event)
            self.keyboard_events(event)

#    def rot_angle(self, event, key):
#        math = self.data.math
#        angle = 0
#        if event.key == key:
#            if self.shift:
#                angle -= math.pi / 2
#            else:
#                angle += math.pi / 2
#
#        return angle

    def keyboard_events(self, event):
        math = self.viewport.tools.math
        key_map = self.data.key_map

        if event.type == self.pg.KEYDOWN:
            if event.key == key_map.key['o']:
                self.camera.orto_view = not self.camera.orto_view
#
#            U_angle = self.rot_angle(event, key_map.key['up'])
#            D_angle = self.rot_angle(event, key_map.key['down'])
#            F_angle = self.rot_angle(event, key_map.key['front'])
#            B_angle = self.rot_angle(event, key_map.key['back'])
#            L_angle = self.rot_angle(event, key_map.key['left'])
#            R_angle = self.rot_angle(event, key_map.key['right'])
#
#        return (U_angle, D_angle, F_angle , B_angle, L_angle, R_angle)

    def mouse_events(self, event):
        math = self.viewport.tools.math
        key_map = self.data.key_map
        if event.type == self.pg.MOUSEMOTION and self.middle_mouse:
            x, y = event.rel
            y /= 200
            x /= 200
            self.camera.rot[0] += y
            self.camera.rot[1] += x

            if self.camera.rot[0] >= math.pi:
                self.camera.rot[0] = -math.pi
            elif self.camera.rot[0] <= -math.pi:
                self.camera.rot[0] = math.pi

            elif self.camera.rot[1] >= math.pi:
                self.camera.rot[1] = -math.pi
            elif self.camera.rot[1] <= -math.pi:
                self.camera.rot[1] = math.pi


        if event.type == self.pg.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.camera.zoom += 50
            if event.button == 5:
                self.camera.zoom -= 50
