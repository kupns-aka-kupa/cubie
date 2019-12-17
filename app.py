import pygame

from objects.camera.camera import Camera
from viewport.view import Viewport
from events.events import Events
from conf import Config


class App:

    __run = False
    global_settings = None

    def __init__(self):
        self.__run = True
        self.pg = pygame
        self.pg.init()
        self.global_conf = Config()
        self.clock = self.pg.time.Clock()
        self.global_settings = self.global_conf.GLOBAL_SETTINGS
        self.camera = Camera(self)
        self.viewport = Viewport(self)
        self.events = Events(self)

    def init(self):

        self.pg.display.set_mode(
            (
                self.global_settings['VIEWPORT']['DEVICE']['SCREEN_WIDTH'],
                self.global_settings['VIEWPORT']['DEVICE']['SCREEN_HEIGHT']
            ),
            # self.global_settings['PREFERENCES']['FLAGS']
        )
        self.pg.display.set_caption(self.global_settings['VIEWPORT']['DEVICE']['APP_NAME'])

    def update(self):

        while self.__run:
            self.events.update()
            self.viewport.update()

            self.pg.display.flip()

            self.clock.tick(self.global_settings['VIEWPORT']['DEVICE']['FPS'])

    def suicide(self):
        self.__run = False
