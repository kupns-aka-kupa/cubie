from os import sys
import math

INPUT_FILES_SETTINGS = ['settings/key_bindings/key_map.json']


class Events:
    def __init__(self, root):
        self.root = root
        self.__viewport = self.root.viewport
        self.__camera = self.root.camera
        self.__pg = self.root.pg
        self.key_map = self.root.file_manager.load(INPUT_FILES_SETTINGS)['KEY_MAP']
        self.shift = False
        self.ctrl = False
        self.middle_mouse = False

    def update(self):
        for event in self.__pg.event.get():
            if event.type == self.__pg.QUIT:
                self.__pg.quit()
                sys.exit()
            keys = self.__pg.key.get_pressed()
            mouse_btns = self.__pg.mouse.get_pressed()
            self.shift = keys[self.__pg.K_LSHIFT]
            self.ctrl = keys[self.__pg.K_LCTRL]
            self.middle_mouse = mouse_btns[1]

            if event.type == self.__pg.KEYDOWN:
                self.keyboard_keydown(event)
            if event.type == self.__pg.MOUSEMOTION:
                self.mouse_move(event)
            if event.type == self.__pg.MOUSEBUTTONDOWN:
                self.mouse_keydown(event)

    def keyboard_keydown(self, event):

        U_angle = 0
        D_angle = 0
        R_angle = 0
        L_angle = 0
        B_angle = 0
        F_angle = 0

        if event.key == self.key_map.get('o'):
            self.__camera.orto_view = not self.__camera.orto_view

        if event.key == self.key_map.get('-'):
            self.__camera.pos[2] += 1

        if event.key == self.key_map.get('+'):
            self.__camera.pos[2] -= 1

        if event.key == self.key_map.get('U'):
            if self.shift:
                U_angle -= math.pi / 2
            else:
                U_angle += math.pi / 2

        if event.key == self.key_map.get('D'):
            if self.shift:
                D_angle -= math.pi / 2
            else:
                D_angle += math.pi / 2

        if event.key == self.key_map.get('R'):
            if self.shift:
                R_angle -= math.pi / 2
            else:
                R_angle += math.pi / 2

        if event.key == self.key_map.get('L'):
            if self.shift:
                L_angle -= math.pi / 2
            else:
                L_angle += math.pi / 2

        if event.key == self.key_map.get('F'):
            if self.shift:
                F_angle -= math.pi / 2
            else:
                F_angle += math.pi / 2

        if event.key == self.key_map.get('B'):
            if self.shift:
                B_angle -= math.pi / 2
            else:
                B_angle += math.pi / 2

        angles = (U_angle, D_angle, R_angle, L_angle, F_angle, B_angle)
        self.__viewport.puzzle.puzzle_logic(angles)

    def mouse_move(self, event):
        # self.__viewport.gui.mouse_x, self.__viewport.gui.mouse_x = event.pos
        if self.middle_mouse:
            x, y = event.rel
            self.__camera.rot[0] += y / self.root._settings['PREFERENCES']['MOUSE_SENSITIVITY']
            self.__camera.rot[1] += x / self.root._settings['PREFERENCES']['MOUSE_SENSITIVITY']

            if self.__camera.rot[0] >= math.pi:
                self.__camera.rot[0] = -math.pi
            elif self.__camera.rot[0] <= -math.pi:
                self.__camera.rot[0] = math.pi

            elif self.__camera.rot[1] >= math.pi:
                self.__camera.rot[1] = -math.pi
            elif self.__camera.rot[1] <= -math.pi:
                self.__camera.rot[1] = math.pi

    def mouse_keydown(self, event):
        if event.button == 4:
            self.__camera.fov += 50
        if event.button == 5:
            self.__camera.fov -= 50
