import sys, math
import pygame as pg

def rotate2d(pos, rad):
    x, y = pos
    cos ,sin = math.cos(rad), math.sin(rad)
    return x * cos - y * sin, y * cos + x * sin

class Grid():
    def __init__(self, pos = (0, 0, 0)):
        self.pos = list(pos)
        self.size = 10
        self.axis = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]
        self.labels = ['y', 'x', 'z', '-y', '-x', '-z' ]

    def render(self):
        for i in range(len(self.axis)):
            x, y, z = self.axis[i]
            x, z = rotate2d((x, z), camera.rot[1])
            y, z = rotate2d((y, z), camera.rot[0])
            z += 5
            f = 200 / z
            x, y = x * f, y * f
            screen.blit(font.render(self.labels[i], False, black), (cx + self.size * x, cy + self.size * y))
            pg.draw.line(screen, black, [cx, cy], (cx + self.size * x, cy + self.size * y), 1)

class Camera():

    def __init__(self, pos = (0, 0, 0), rot = (0, 0)):
        self.pos = list(pos)
        self.rot = list(rot)

    def events(self, event):
#        pressed = pg.mouse.get_pressed()
        if event.type == pg.MOUSEMOTION:
#            if pressed[1] and event.type == pg.MOUSEBUTTONDOWN and event.button == 2:
                x, y = event.rel
                y /= 200
                x /= 200
                self.rot[0] += y
                self.rot[1] += x

grid = Grid((0, 0, 0))
camera = Camera((0, 0, 5))

pg.init()
w, h = 1000, 1000; cx, cy = w // 2, h // 2
screen = pg.display.set_mode((w, h))
clock = pg.time.Clock()

pg.event.get()
pg.mouse.get_rel()
pg.mouse.set_visible(0)
pg.event.set_grab(1)

font = pg.font.SysFont('Comic Sans MS', 15)
black = (0, 0, 0)
white = (255, 255, 255)
vertex = (1, 1, 1), (-1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, -1, -1), (-1, -1, 1), (1, -1, -1), (-1, 1, -1)
edges = (0, 1), (0, 2), (0, 3), (4, 5), (4, 6), (4, 7), (2, 6), (2, 7) ,(1, 7), (3, 5), (1, 5), (3, 6)

while 1:
    dt = clock.tick() / 1000
    for event in pg.event.get():
        if event.type == pg.quit: sys.exit()
        camera.events(event)

    screen.fill(white)
#    for edge in edges:
#        points = []
#        for x, y, z in (vertex[edge[0]], vertex[edge[1]]):
#            x -= camera.pos[0]
#            y -= camera.pos[1]
#            z -= camera.pos[2]
#            x, z = rotate2d((x, z), camera.rot[1])
#            y, z = rotate2d((y, z), cam.rot[0])
#            f = 200 / z
#            x, y = x * f, y * f
#            points += [(cx + int(x), cy + int(y))]
#        pg.draw.line(screen, black, points[0], points[1], 1)
    grid.render()

    pg.display.flip()
