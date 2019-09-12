class Cube():

    def __init__(self, camera, pygame, data, tools, vertex , edges, pos, rot = (0, 0)):
        self.tools = tools
        self.camera = camera
        self.pg = pygame
        self.data = data
        self.x0, self.y0, self.z0 = pos
        self.rot = rot
        self.vertex = vertex
        self.edges = edges
        self.width = 2
        self.screen = self.pg.display.get_surface()

    def render(self, color):

        tools = self.tools
        colors = self.data.colors
        cx, cy = self.data.device.center_x, self.data.device.center_y
        w, h = self.data.device.width, self.data.device.height
        camera = self.camera
        faces = self.data.cube.faces

        verts_list = []; screen_coords = []
        for x, y, z in self.vertex:
            x += camera.pos[0] + self.x0 + self.rot[0]
            y += camera.pos[1] + self.y0 + self.rot[1]
            z += self.z0
            x, z = tools.rotate((x, z), camera.rot[1])
            y, z = tools.rotate((y, z), camera.rot[0])
            if camera.orto_view:
                z = camera.pos[2]
            elif not camera.orto_view:
                z += camera.pos[2]
            verts_list += [(x, y, z)]
            f = camera.zoom / z
            x, y = x * f, y * f
            screen_coords += [(cx + int(x), cy + int(y))]

        for edge in self.edges:
            points = []
            for x, y, z in (self.vertex[edge[0]], self.vertex[edge[1]]):
                x += self.x0 + self.rot[0]
                y += self.y0 + self.rot[1]
                z += self.z0
                x, z = tools.rotate((x, z), camera.rot[1])
                y, z = tools.rotate((y, z), camera.rot[0])
                if camera.orto_view:
                    z = camera.pos[2]
                elif not camera.orto_view:
                    z += camera.pos[2]
                f = camera.zoom / z
                x, y = x * f, y * f
                points += [(cx + int(x), cy + int(y))]
            self.pg.draw.line(self.screen, colors.black, points[0], points[1], self.width)


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
            try: self.pg.draw.polygon(self.screen, color[i], face_list[i])
            except : self.pg.draw.polygon(self.screen, color[-1], face_list[i])
