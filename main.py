import sys, math
import pygame as pg
from data import data

def rotate(pos, rad):
    x, y = pos
    cos ,sin = math.cos(rad), math.sin(rad)
    return x * cos - y * sin, y * cos + x * sin

class Viewport():

    def __init__(self):
        grid = Grid()
        grid.render()
#       start_coord(y,x,z)
#       UP
        corner_YOB = Cube(vertex, edges, (2, -2, -2))
#        corner_YBR = Cube(vertex, edges, (2, -2, 2))
#        corner_YRG = Cube(vertex, edges, (-2, -2, 2))
#        corner_YGO = Cube(vertex, edges, (-2, -2, -2))
#        center_Y = Cube(vertex, edges, (0, -2, 0))

#       DOWN
#        corner_WBO = Cube(vertex, edges, (2, +2, -2))
#        corner_WRB = Cube(vertex, edges, (2, +2, 2))
#        corner_WGR = Cube(vertex, edges, (-2, +2, 2))
#        corner_WOG = Cube(vertex, edges, (-2, +2, -2))
#        center_W = Cube(vertex, edges, (0, 2, 0))

#       UP
        corner_YOB.render()
#        corner_YBR.render()
#        corner_YRG.render()
#        corner_YGO.render()
#        center_W.render()

#       DOWN
#        corner_WBO.render()
#        corner_WRB.render()
#        corner_WGR.render()
#        corner_WOG.render()
#        center_Y.render()

class Cube(Viewport):

    def __init__(self, vertex , edges, pos, rot = (0, 0)):
        self.x0, self.y0, self.z0 = pos
        self.rot = rot
        self.vertex = vertex
        self.edges = edges
        self.width = 10

    def render(self):

#        verts_list = []; screen_coords = []
#        for x, y, z in vertex:
#            x += camera.pos[0] + self.x0 + self.rot[0]
#            y += camera.pos[1] + self.y0 + self.rot[1]
#            z += self.z0
#            x, z = rotate((x, z), camera.rot[1])
#            y, z = rotate((y, z), camera.rot[0])
#            z = camera.pos[2]
#            verts_list += [(x, y, z)]
#
#            f = camera.zoom / z
#            x, y = x * f, y * f
#            screen_coords += [(cx + int(x), cy + int(y))]
#
#        face_list = []; face_color = []
#
#        for face in faces:
#            on_screen = False
#            for i in face:
#                if verts_list[i][2] > 0:
#                    on_screen = True
#                    break
#            if  on_screen:
#                coords = [screen_coords[i] for i in face]
#                face_list += coords
#        for i in range(len(face_list)):
#            pg.draw.polygon(screen, colors.black, face_list[i], self.width)

        for edge in edges:
            points = []
            for x, y, z in (vertex[edge[0]], vertex[edge[1]]):
                x += self.x0 + self.rot[0]
                y += self.y0 + self.rot[1]
                z += self.z0
                x, z = rotate((x, z), camera.rot[1])
                y, z = rotate((y, z), camera.rot[0])
                if camera.orto_view:
                    z = camera.pos[2]
                elif not camera.orto_view:
                    z += camera.pos[2]
                f = camera.zoom / z
                x, y = x * f, y * f
                points += [(cx + int(x), cy + int(y))]
            pg.draw.line(screen, colors.black, points[0], points[1], 1)

class Grid(Viewport):

    def __init__(self, pos = (0, 0, 0)):
        self.pos = list(pos)
        self.size = 10
        self.axis = data.grid.vertex
        self.labels = data.grid.labels

    def render(self):

#       indexs
        for axle in self.axis:
            for i in range(1, self.size):
                x, y, z = axle
                x *= i; y *= i; z *= i
                index = x + y + z
                x, z = rotate((x, z), camera.rot[1])
                y, z = rotate((y, z), camera.rot[0])
                if camera.orto_view:
                    z = camera.pos[2]
                elif not camera.orto_view:
                    z += camera.pos[2]
                f = camera.zoom / z
                x, y = x * f, y * f
                screen.blit(font.render(str(index), False, colors.black), (cx + x, cy + y))
                pg.draw.circle(screen, data.colors.black, (cx + int(x), cy + int(y)), 2)
#       labels
        for i in range(len(self.axis)):
            x = self.axis[i][0] + self.pos[0]
            y = self.axis[i][1] + self.pos[1]
            z = self.axis[i][2] + self.pos[2]
            x, z = rotate((x, z), camera.rot[1])
            y, z = rotate((y, z), camera.rot[0])
            if camera.orto_view:
                z = camera.pos[2]
            elif not camera.orto_view:
                z += camera.pos[2]
            f = camera.zoom / z
            x, y = x * f, y * f
            screen.blit(font.render(self.labels[i], False, colors.black), (cx + self.size * x, cy + self.size * y))
            pg.draw.line(screen, data.colors.black, [cx + x , cy + y], (cx + self.size * x, cy + self.size * y), 1)

class Camera():

    def __init__(self, pos = (0, 0, 10), rot = (0, 0), zoom = 200):
        self.pos = list(pos)
        self.rot = list(rot)
        self.orto_view = False
        self.zoom = zoom

    def update(self, key):
        if key[pg.K_o]:
            self.orto_view = not self.orto_view

    def events(self, event):
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

vertex = data.cube.vertex
edges = data.cube.edges
faces = data.cube.faces
colors = data.colors

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

while 1:
    for event in pg.event.get():
        if event.type == pg.quit: sys.exit()
        camera.events(event)

    screen.fill(colors.white)
    Viewport()
    key = pg.key.get_pressed()
    camera.update(key)
    pg.display.flip()
