
class Cube():

    def __init__(self, camera, pygame, data, tools, pos, rot = (0, 0)):
        self.camera = camera
        self.pg = pygame
        self.data = data
        self.tools = tools
        self.x0, self.y0, self.z0 = pos
        self.rot = rot
        self.width = 2

    def render(self, color):
        math = self.data.math
        tools = self.tools
        screen = self.pg.display.get_surface()
        camera = self.camera
        colors = self.data.colors
        cx, cy = self.data.device.center_x, self.data.device.center_y
        w, h = self.data.device.width, self.data.device.height
        vertex = self.data.cube.vertex
        faces = self.data.cube.faces
        edges = self.data.cube.edges

        verts_list = []; screen_coords = []

        for x, y, z in vertex:
            x += camera.pos[0] + self.x0
            y += camera.pos[1] + self.y0
            z += self.z0
            x, z = tools.rotate((x, z), self.rot[0])
            y, z = tools.rotate((y, z), self.rot[1])
            x, z = tools.rotate((x, z), camera.rot[1])
            y, z = tools.rotate((y, z), camera.rot[0])

            if camera.orto_view:
                z += camera.pos[2]
                verts_list.append((x, y, z))
                z = camera.pos[2]
            elif not camera.orto_view:
                z += camera.pos[2]
                verts_list.append((x, y, z))

            f = camera.zoom / z
            x, y = x * f, y * f
            screen_coords.append((cx + int(x), cy + int(y)))

        face_list = []; point_list = []; depth = []

        face_order = self.display_order(faces, face_list, verts_list, screen_coords)
        for i in face_order:
            try: self.pg.draw.polygon(screen, color[i], face_list[i])
            except : self.pg.draw.polygon(screen, color[-1], face_list[i])

        edge_order = self.display_order(edges, point_list, verts_list, screen_coords)
        for i in edge_order:
            self.pg.draw.line(screen, colors.black, point_list[i][0], point_list[i][1], self.width)

    def display_order(self, elements, elements_list, verts_list, screen_coords):
        w, h = self.data.device.width, self.data.device.height
        depth = []
        for i in range(len(elements)):
            element = elements[i]
            on_screen = False
            for j in element:
                x, y = screen_coords[j]
                if verts_list[j][2] > 0 and x > 0 and x < w and y > 0 and y < h:
                    on_screen = True
                    break
            if  on_screen:
                elements_list.append([screen_coords[i] for i in element])
                depth.append(sum(sum(verts_list[j][k] for j in element) ** 2 for k in range(len(element) - 1)))

        return sorted(range(len(elements_list)), key = lambda i : depth[i], reverse = 1)
