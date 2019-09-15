import math
import pygame as pg
import data
import view
import camera
import emoji

pg.init()
clock = pg.time.Clock()

data = data.Data()
colors = data.colors
device = data.device
w, h = device.width,  device.height; cx, cy = device.center_x, device.center_y
screen = pg.display.set_mode((w, h))

camera = camera.Camera(pg, data)
viewport = view.Viewport(camera, pg, data)

pg.event.get()
pg.mouse.get_rel()
pg.mouse.set_visible(0)
pg.event.set_grab(1)
pg.display.set_caption('RubiCubie')

viewport.cube_init()
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        camera.events(event)
    screen.fill(colors.white)
    viewport.update()
    pg.display.flip()
