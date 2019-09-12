import sys, math
import pygame as pg
import view
import camera


pg.init()

device = view.data.device

w, h = device.width,  device.height; cx, cy = device.center_x, device.center_y
screen = pg.display.set_mode((w, h))

camera = camera.Camera(pg)
viewport = view.Viewport(camera, pg)

colors = view.data.colors


clock = pg.time.Clock()

pg.event.get()
pg.mouse.get_rel()
pg.mouse.set_visible(0)
pg.event.set_grab(1)
pg.display.set_caption('RubiCubie')

while 1:
    for event in pg.event.get():
        if event.type == pg.quit: sys.exit()
        camera.events(event)

    screen.fill(colors.white)
    viewport.update()
    pg.display.flip()
