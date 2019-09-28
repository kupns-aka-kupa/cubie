from os import sys
import math


class Events:
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

            if event.type == self.pg.KEYDOWN:
                self.keyboard_keydown(event)
            if event.type == self.pg.MOUSEMOTION:
                self.mouse_move(event)
            if event.type == self.pg.MOUSEBUTTONDOWN:
                self.mouse_keydown(event)

    def keyboard_keydown(self, event):
        key_map = self.data.key_map

        U_angle = 0
        D_angle = 0
        R_angle = 0
        L_angle = 0
        B_angle = 0
        F_angle = 0

        if event.key == key_map.key['o']:
            self.camera.orto_view = not self.camera.orto_view

        if event.key == key_map.key['-']:
            self.camera.pos[2] += 1

        if event.key == key_map.key['+']:
            self.camera.pos[2] -= 1

        if event.key == key_map.key['U']:
            if self.shift:
                U_angle -= math.pi / 2
            else:
                U_angle += math.pi / 2

        if event.key == key_map.key['D']:
            if self.shift:
                D_angle -= math.pi / 2
            else:
                D_angle += math.pi / 2

        if event.key == key_map.key['R']:
            if self.shift:
                R_angle -= math.pi / 2
            else:
                R_angle += math.pi / 2

        if event.key == key_map.key['L']:
            if self.shift:
                L_angle -= math.pi / 2
            else:
                L_angle += math.pi / 2

        if event.key == key_map.key['F']:
            if self.shift:
                F_angle -= math.pi / 2
            else:
                F_angle += math.pi / 2

        if event.key == key_map.key['B']:
            if self.shift:
                B_angle -= math.pi / 2
            else:
                B_angle += math.pi / 2

        angles = (U_angle, D_angle, R_angle, L_angle, F_angle, B_angle)
        self.viewport.rubiks_cube.logic(angles)

    def mouse_move(self, event):
        sensivity = self.data.device.sensivity
        self.viewport.gui.mouse_x, self.viewport.gui.mouse_x = event.pos
        if self.middle_mouse:
            x, y = event.rel
            self.camera.rot[0] += y / sensivity
            self.camera.rot[1] += x / sensivity

            if self.camera.rot[0] >= math.pi:
                self.camera.rot[0] = -math.pi
            elif self.camera.rot[0] <= -math.pi:
                self.camera.rot[0] = math.pi

            elif self.camera.rot[1] >= math.pi:
                self.camera.rot[1] = -math.pi
            elif self.camera.rot[1] <= -math.pi:
                self.camera.rot[1] = math.pi

    def mouse_keydown(self, event):
        if event.button == 4:
            self.camera.fov += 50
        if event.button == 5:
            self.camera.fov -= 50
