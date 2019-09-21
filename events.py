from os import sys
import math

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
            if event.type == self.pg.QUIT: self.pg.quit(); sys.exit()
            keys = self.pg.key.get_pressed()
            mouse_btns = self.pg.mouse.get_pressed()
            self.shift = keys[self.pg.K_LSHIFT]
            self.ctrl = keys[self.pg.K_LCTRL]
            self.middle_mouse = mouse_btns[1]
            self.mouse_events(event)
            self.keyboard_events(event)

    def keyboard_events(self, event):
        key_map = self.data.key_map

        U_angle = 0
        D_angle = 0
        R_angle = 0
        L_angle = 0
        B_angle = 0
        F_angle = 0

        if event.type == self.pg.KEYDOWN:
            if event.key == key_map.key['o']:
                self.camera.orto_view = not self.camera.orto_view

            if event.key == key_map.key['-']:
                self.camera.pos[2] += 1

            if event.key == key_map.key['+']:
                self.camera.pos[2] -= 1

            if event.key == key_map.key['up']:
                if self.shift:
                    U_angle -= math.pi / 2
                else:
                    U_angle += math.pi / 2

            if event.key == key_map.key['down']:
                if self.shift:
                    D_angle -= math.pi / 2
                else:
                    D_angle += math.pi / 2

            if event.key == key_map.key['right']:
                if self.shift:
                    R_angle -= math.pi / 2
                else:
                    R_angle += math.pi / 2

            if event.key == key_map.key['left']:
                if self.shift:
                    L_angle -= math.pi / 2
                else:
                    L_angle += math.pi / 2

            if event.key == key_map.key['front']:
                if self.shift:
                    F_angle -= math.pi / 2
                else:
                    F_angle += math.pi / 2

            if event.key == key_map.key['back']:
                if self.shift:
                    B_angle -= math.pi / 2
                else:
                    B_angle += math.pi / 2

            angles = (U_angle, D_angle, R_angle, L_angle, F_angle, B_angle)
            self.viewport.rubiks_cube.logic(angles)


    def mouse_events(self, event):
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
                self.camera.fov += 50
            if event.button == 5:
                self.camera.fov -= 50
