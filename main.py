import sys, math
import pygame as pg
import data

def rotate(pos, rad):
    x, y = pos
    cos ,sin = math.cos(rad), math.sin(rad)
    return x * cos - y * sin, y * cos + x * sin

class Rubie_cube():

    def __init__(self):
        corner_YOB = Cube(vertex, edges, (0, 0, 0))
        corner_YOB.render()

class Cube(Rubie_cube):

    def __init__(self, vertex , edges, pos, rot = (0, 0)):
        self.x0, self.y0, self.z0 = pos
        self.rot = rot
        self.vertex = vertex
        self.edges = edges

    def render(self):
        for edge in edges:
            points = []
            for x, y, z in (vertex[edge[0]], vertex[edge[1]]):
#                self.rot = rotate((x, y), 4)
                x += camera.pos[0] + self.x0 + self.rot[0]
                y += camera.pos[1] + self.y0 + self.rot[1]
                z += self.z0
                x, z = rotate((x, z), camera.rot[1])
                y, z = rotate((y, z), camera.rot[0])
                z = camera.pos[2]
                f = camera.zoom / z
                x, y = x * f, y * f
                points += [(cx + int(x), cy + int(y))]
            pg.draw.line(screen, colors['black'], points[0], points[1], 1)

class Grid():

    def __init__(self, pos = (0, 0, 0)):
        self.pos = list(pos)
        self.size = 10
        self.axis = [[1, 0, 0], [0, -1, 0], [0, 0, 1], [-1, 0, 0], [0, 1, 0], [0, 0, -1]]
        self.labels = ['+y', '-x', '+z', '-y', '+x', '-z' ]

    def render(self):

        for axle in self.axis:
            for i in range(1, self.size):
                x, y, z = axle
                x *= i; y *= i; z *= i
                index = x + y + z
                x, z = rotate((x, z), camera.rot[1])
                y, z = rotate((y, z), camera.rot[0])
                z = camera.pos[2]
                f = camera.zoom / z
                x, y = x * f, y * f
                screen.blit(font.render(str(index), False, colors['black']), (cx + x, cy + y))
                pg.draw.circle(screen, colors['black'], (cx + int(x), cy + int(y)), 2)
#
        for i in range(len(self.axis)):
            x = self.axis[i][0] + self.pos[0]
            y = self.axis[i][1] + self.pos[1]
            z = self.axis[i][2] + self.pos[2]
            x, z = rotate((x, z), camera.rot[1])
            y, z = rotate((y, z), camera.rot[0])
            z = camera.pos[2]
            f = camera.zoom / z
            x, y = x * f, y * f
            screen.blit(font.render(self.labels[i], False, colors['black']), (cx + self.size * x, cy + self.size * y))
            pg.draw.line(screen, colors['black'], [cx + x , cy + y], (cx + self.size * x, cy + self.size * y), 1)

class Camera():

    def __init__(self, pos = (0, 0, 5), rot = (0, 0), zoom = 200):
        self.pos = list(pos)
        self.rot = list(rot)
        self.zoom = zoom

    def events(self, event):
#        pressed = pg.mouse.get_pressed()
        if event.type == pg.MOUSEMOTION:
                x, y = event.rel
                y /= 200
                x /= 200
                self.rot[0] += y
                self.rot[1] += x

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 4:
                camera.zoom += 50
            if event.button == 5:
                camera.zoom -= 50

vertex = (1, 1, 1), (-1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, -1, -1), (-1, -1, 1), (1, -1, -1), (-1, 1, -1)
edges = (0, 1), (0, 2), (0, 3), (4, 5), (4, 6), (4, 7), (2, 6), (2, 7) ,(1, 7), (3, 5), (1, 5), (3, 6)

grid = Grid()
camera = Camera()

pg.init()
w, h = 800, 800; cx, cy = w // 2, h // 2
screen = pg.display.set_mode((w, h))
clock = pg.time.Clock()

pg.event.get()
pg.mouse.get_rel()
pg.mouse.set_visible(0)
pg.event.set_grab(0)

font = pg.font.SysFont('Comic Sans MS', 15)
colors = {
    'black' : (0, 0, 0),
    'white' : (255, 255, 255)
}

while 1:
    for event in pg.event.get():
        if event.type == pg.quit: sys.exit()
        camera.events(event)

    screen.fill(colors['white'])
    Rubie_cube()
    grid.render()

    pg.display.flip()
