import pygame as pg
from app.viewport.view import Viewport
from app.events.events import Events

pg.init()

viewport = Viewport(pg)
events = Events(viewport)

while True:
    events.update()
    viewport.update()
