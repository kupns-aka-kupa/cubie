from app.tools import tools
from app.viewport.view import device_data, fm, palette

data = fm.open_file('app/objects/primitives/cube/cube.json')


class Cube:
    def __init__(self, camera, pygame, own_colors, pos):
        self.camera = camera
        self.pg = pygame
        self.own_colors = own_colors
        self.tools = tools.Tools()
        self.x0, self.y0, self.z0 = pos
        self.vertex = data['vertex'].copy()
        self.rotx = 0; self.roty = 0; self.rotz = 0
        self.depth = 0

    def redesignation(self):
        screen = self.pg.display.get_surface()
        camera = self.camera
        w, h = device_data['width'], device_data['height']
        cx, cy = w // 2, h // 2
        faces = data['faces']
        edges = data['edges']
        return screen, camera, cx, cy, w, h, faces, edges

    def rotation(self, angles):
        self.rotx, self.roty, self.rotz = angles
        self.x0, self.z0 = self.tools.rotate((self.x0, self.z0), self.rotx)
        self.y0, self.z0 = self.tools.rotate((self.y0, self.z0), self.roty)
        self.x0, self.y0 = self.tools.rotate((self.x0, self.y0), self.rotz)

        self.x0, self.y0, self.z0 = round(self.x0), round(self.y0), round(self.z0)

        for i in range(len(self.vertex)):
            x, y, z = self.vertex[i]
            x, z = self.tools.rotate((x, z), self.rotx)
            y, z = self.tools.rotate((y, z), self.roty)
            x, y = self.tools.rotate((x, y), self.rotz)

            self.vertex[i] = [x, y, z]

        self.rotx = 0; self.roty = 0; self.rotz = 0

    def calculate_coords(self):
        screen, camera, cx, cy, w, h, faces, edges = self.redesignation()
        verts_list = []; screen_coords = []

        for i in range(len(self.vertex)):
            x, y, z = self.vertex[i]

            x += camera.pos[0] + self.x0
            y += camera.pos[1] + self.y0
            z += self.z0
            x, z = self.tools.rotate((x, z), camera.rot[1])
            y, z = self.tools.rotate((y, z), camera.rot[0])

            if camera.orto_view:
                z += camera.pos[2]
                verts_list.append((x, y, z))
                z = camera.pos[2]
            elif not camera.orto_view:
                z += camera.pos[2]
                verts_list.append((x, y, z))

            f = camera.fov / z
            x, y = x * f, y * f
            screen_coords.append((cx + int(x), cy + int(y)))
        return  verts_list, screen_coords

    def render(self):
        screen, camera, cx, cy, w, h, faces, edges = self.redesignation()
        verts_list, screen_coords = self.calculate_coords()
        face_list = []; point_list = []; depth = []

        edge_order, self.depth = self.render_order(edges, point_list, verts_list, screen_coords)
        face_order, self.depth = self.render_order(faces, face_list, verts_list, screen_coords)

        for i in face_order:
            try:
                self.pg.draw.polygon(screen, self.own_colors[i], face_list[i])
                self.pg.draw.line(screen, palette['black'], face_list[i][0],  face_list[i][1], data['line_width'])
                self.pg.draw.line(screen, palette['black'],  face_list[i][2],  face_list[i][3], data['line_width'])
                self.pg.draw.line(screen, palette['black'],  face_list[i][0],  face_list[i][3], data['line_width'])
                self.pg.draw.line(screen, palette['black'],  face_list[i][1],  face_list[i][2], data['line_width'])
            except:
                self.pg.draw.polygon(screen, self.own_colors[-1], face_list[i])

        # for i in edge_order:
        #     self.pg.draw.line(screen, palette['black'], point_list[edge_order[i]][0], point_list[
        #     edge_order[i]][1], data['line_width'])

    def render_order(self, elements, elements_list, verts_list, screen_coords):
        w, h = device_data['width'], device_data['height']
        depth = []
        for i in range(len(elements)):
            element = elements[i]
            on_screen = False
            for j in element:
                x, y = screen_coords[j]
                if verts_list[j][2] > 0 and 0 < x < w and 0 < y < h:
                    on_screen = True
                    break
            if  on_screen:
                elements_list.append([screen_coords[i] for i in element])
                depth.append(sum(sum(verts_list[j][k] for j in element) ** 2 for k in range(len(element) - 1)))
        return sorted(range(len(elements_list)), key=lambda i : depth[i], reverse = 1), sum(i for i in depth) / len(depth)
