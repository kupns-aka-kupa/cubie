import pygame as pg
import data
from viewport import view
from tools import file_manager as fm
from events import events

pg.init()
clock = pg.time.Clock()

data = data.Data()
device = data.device
w, h = device.width,  device.height

viewport = view.Viewport(pg, data)
events = events.Events(viewport)

screen = pg.display.set_mode((w, h))
pg.display.set_caption('RubiCubie')

while True:
    events.update()
    viewport.update()
    clock.tick(device.fps)
