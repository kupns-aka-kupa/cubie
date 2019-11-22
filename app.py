import pygame

from objects.camera.camera import Camera
from viewport.view import Viewport
from events.events import Events
from tools.file_manager import FileManager


class App:

    __run = False
    _settings = None

    def __init__(self, config):
        self.__run = True
        self.config = config
        self.pg = pygame
        self.pg.init()
        self.clock = self.pg.time.Clock()
        self.file_manager = FileManager(self)
        self._settings = self.file_manager.load(config.GLOBAL_SETTINGS)
        self.camera = Camera(self)
        self.viewport = Viewport(self)
        self.events = Events(self)

    def init(self):

        self.pg.display.set_mode(
            (
                self._settings['PREFERENCES']['SCREEN_WIDTH'],
                self._settings['PREFERENCES']['SCREEN_HEIGHT']
            ),
            # self._settings['PREFERENCES']['FLAGS']
        )
        self.pg.display.set_caption(self._settings['PREFERENCES']['APP_NAME'])

    def update(self):

        while self.__run:
            self.events.update()
            self.viewport.update()

            self.pg.display.flip()

            self.clock.tick(self._settings["PREFERENCES"]['FPS'])

    def suicide(self):
        self.__run = False
