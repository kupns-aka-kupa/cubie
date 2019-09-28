import pygame as pg
from viewport import view
from events import events

pg.init()

viewport = view.Viewport(pg)
events = events.Events(viewport)

while True:
    events.update()
    viewport.update()
