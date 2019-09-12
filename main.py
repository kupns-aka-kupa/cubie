import sys, math
import pygame as pg
from data import data

def rotate(pos, rad):
    x, y = pos
    cos ,sin = math.cos(rad), math.sin(rad)
    return x * cos - y * sin, y * cos + x * sin

class Viewport():

    def __init__(self):
        self.grid = Grid()
#       UP_CORNERS
#       start_coord(y,x,z)
        self.corner_YOB = Cube(vertex, edges, (2, -2, -2))
        self.corner_YBR = Cube(vertex, edges, (2, -2, 2))
        self.corner_YRG = Cube(vertex, edges, (-2, -2, 2))
        self.corner_YGO = Cube(vertex, edges, (-2, -2, -2))
#       DOWN_CORNERS
        self.corner_WBO = Cube(vertex, edges, (2, 2, -2))
        self.corner_WRB = Cube(vertex, edges, (2, 2, 2))
        self.corner_WGR = Cube(vertex, edges, (-2, 2, 2))
        self.corner_WOG = Cube(vertex, edges, (-2, 2, -2))
#       UP_EDGES
        self.edge_YB = Cube(vertex, edges, (2, -2, 0))
        self.edge_YR = Cube(vertex, edges, (0, -2, 2))
        self.edge_YG = Cube(vertex, edges, (-2, -2, 0))
        self.edge_YO = Cube(vertex, edges, (0, -2, -2))
#       MIDDLE_EDGES
        self.edge_OB = Cube(vertex, edges, (2, 0, -2))
        self.edge_BR = Cube(vertex, edges, (2, 0, 2))
        self.edge_RG = Cube(vertex, edges, (-2, 0, 2))
        self.edge_GO = Cube(vertex, edges, (-2, 0, -2))
#       DOWN_EDGES
        self.edge_WB = Cube(vertex, edges, (2, 2, 0))
        self.edge_WR = Cube(vertex, edges, (0, 2, 2))
        self.edge_WG = Cube(vertex, edges, (-2, 2, 0))
        self.edge_WO = Cube(vertex, edges, (0, 2, -2))
#       СENTERS
        self.center_Y = Cube(vertex, edges, (0, -2, 0))
        self.center_W = Cube(vertex, edges, (0, 2, 0))
        self.center_B = Cube(vertex, edges, (2, 0, 0))
        self.center_G = Cube(vertex, edges, (-2, 0, 0))
        self.center_O = Cube(vertex, edges, (0, 0, -2))
        self.center_R = Cube(vertex, edges, (0, 0, 2))

    def update(self):
#       render
        self.grid.render()
#       UP_CORNERS
        self.corner_YOB.render([colors.orange, colors.blue, colors.yellow, colors.black])
        self.corner_YBR.render([colors.black, colors.blue, colors.yellow, colors.red, colors.black])
        self.corner_YRG.render([colors.black, colors.black, colors.yellow, colors.red, colors.green, colors.black])
        self.corner_YGO.render([colors.orange, colors.black, colors.yellow, colors.black, colors.green, colors.black])
#       DOWN_CORNERS
        self.corner_WBO.render([colors.orange, colors.blue, colors.black, colors.black, colors.black, colors.white])
        self.corner_WRB.render([colors.black, colors.blue, colors.black, colors.red, colors.black, colors.white])
        self.corner_WGR.render([colors.black, colors.black, colors.black, colors.red, colors.green, colors.white])
        self.corner_WOG.render([colors.orange, colors.black, colors.black, colors.black, colors.green, colors.white])
#       UP_EDGES
        self.edge_YB.render([colors.black, colors.blue, colors.yellow, colors.black])
        self.edge_YR.render([colors.black, colors.black, colors.yellow, colors.red, colors.black])
        self.edge_YG.render([colors.black, colors.black, colors.yellow, colors.black, colors.green, colors.black])
        self.edge_YO.render([colors.orange, colors.black, colors.yellow, colors.black])
#       MIDDLE_EDGES
        self.edge_OB.render([colors.orange, colors.blue, colors.black])
        self.edge_BR.render([colors.black, colors.blue, colors.black, colors.red, colors.black])
        self.edge_RG.render([colors.black, colors.black, colors.black, colors.red, colors.green, colors.black])
        self.edge_GO.render([colors.orange, colors.black, colors.black, colors.black, colors.green, colors.black])
#       DOWN_EDGES
        self.edge_WB.render([colors.black, colors.blue, colors.black, colors.black, colors.black, colors.white])
        self.edge_WR.render([colors.black, colors.black, colors.black, colors.red, colors.black, colors.white])
        self.edge_WG.render([colors.black, colors.black, colors.black, colors.black, colors.green, colors.white])
        self.edge_WO.render([colors.orange, colors.black, colors.black, colors.black, colors.black, colors.white])
#       СENTERS
        self.center_O.render([ colors.orange, colors.black])
        self.center_B.render([ colors.black, colors.blue, colors.black])
        self.center_Y.render([ colors.black, colors.black, colors.yellow, colors.black])
        self.center_R.render([ colors.black, colors.black, colors.black, colors.red, colors.black])
        self.center_W.render([ colors.black, colors.black, colors.black, colors.black, colors.black, colors.white])
        self.center_G.render([ colors.black, colors.black, colors.black, colors.black, colors.green, colors.black])

class Cube(Viewport):

    def __init__(self, vertex , edges, pos, rot = (0, 0)):
        self.x0, self.y0, self.z0 = pos
        self.rot = rot
        self.vertex = vertex
        self.edges = edges
        self.width = 2

    def render(self, color):

        verts_list = []; screen_coords = []
        for x, y, z in vertex:
            x += camera.pos[0] + self.x0 + self.rot[0]
            y += camera.pos[1] + self.y0 + self.rot[1]
            z += self.z0
            x, z = rotate((x, z), camera.rot[1])
            y, z = rotate((y, z), camera.rot[0])
            if camera.orto_view:
                z = camera.pos[2]
            elif not camera.orto_view:
                z += camera.pos[2]
            verts_list += [(x, y, z)]

            f = camera.zoom / z
            x, y = x * f, y * f
            screen_coords += [(cx + int(x), cy + int(y))]

        face_list = []; depth = []

        for f in range(len(faces)):
            face = faces[f]
            on_screen = False
            for i in face:
                x, y = screen_coords[i]
                if verts_list[i][2] > 0 and x > 0 and x < w and y > 0 and y < h:
                    on_screen = True
                    break
            if  on_screen:
                coords = [screen_coords[i] for i in face]
                face_list += [coords]
                depth += [sum(sum(verts_list[j][i] for j in face) ** 2 for i in range(3))]
        order = sorted(range(len(face_list)), key = lambda i : depth[i], reverse = 1)
        for i in order:
            try: pg.draw.polygon(screen, color[i], face_list[i])
            except : pg.draw.polygon(screen, color[-1], face_list[i])

#        for edge in edges:
#            points = []
#            for x, y, z in (vertex[edge[0]], vertex[edge[1]]):
#                x += self.x0 + self.rot[0]
#                y += self.y0 + self.rot[1]
#                z += self.z0
#                x, z = rotate((x, z), camera.rot[1])
#                y, z = rotate((y, z), camera.rot[0])
#                if camera.orto_view:
#                    z = camera.pos[2]
#                elif not camera.orto_view:
#                    z += camera.pos[2]
#                f = camera.zoom / z
#                x, y = x * f, y * f
#                points += [(cx + int(x), cy + int(y))]
#            pg.draw.line(screen, colors.black, points[0], points[1], self.width)

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
            pg.draw.line(screen, data.colors.black, [cx + 3 * x , cy + 3 *y], (cx + self.size * x, cy + self.size * y), 1)

class Camera():

    def __init__(self, pos = (0, 0, 10), rot = (0, 0), zoom = 200):
        self.pos = list(pos)
        self.rot = list(rot)
        self.orto_view = False
        self.zoom = zoom

    def events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == 111:
                self.orto_view = not self.orto_view

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
viewport = Viewport()

pg.init()
w, h = 800, 800; cx, cy = w // 2, h // 2
screen = pg.display.set_mode((w, h))
clock = pg.time.Clock()

pg.event.get()
pg.mouse.get_rel()
pg.mouse.set_visible(0)
pg.event.set_grab(1)
pg.display.set_caption('RubiCubie')

font = pg.font.SysFont('Comic Sans MS', 15)

while 1:
    for event in pg.event.get():
        if event.type == pg.quit: sys.exit()
        camera.events(event)

    screen.fill(colors.white)
    viewport.update()
    pg.display.flip()
