from ..utils.proection2d import project_2d_coord


class Polyhedron:
    __verts_list = []
    __screen_coords = []

    def __init__(self, root, data, geometry_data=None):
        self.root = root
        self.camera = self.root.root.camera
        self.pg = self.root.root.pg
        [self.x0, self.y0, self.z0], self.own_colors = data
        self.aradx = 0
        self.arady = 0
        self.aradz = 0
        self.depth = 0
        if geometry_data is None:
            self.geometry_data = self.geometry_data_gen()
        else:
            self.geometry_data = geometry_data
        self.vertex = self.geometry_data['vertex'].copy()

    def geometry_data_gen(self):
        pass

    def get_surface(self):
        screen = self.pg.display.get_surface()
        w, h = self.root.root.global_settings['VIEWPORT']['DEVICE']['SCREEN_WIDTH'], \
               self.root.root.global_settings['VIEWPORT']['DEVICE']['SCREEN_HEIGHT']
        cx, cy = w // 2, h // 2
        return screen, cx, cy, w, h

    def rotation(self, angles):
        self.aradx, self.arady, self.aradz = angles
        self.x0, self.z0 = project_2d_coord((self.x0, self.z0), self.aradx)
        self.y0, self.z0 = project_2d_coord((self.y0, self.z0), self.arady)
        self.x0, self.y0 = project_2d_coord((self.x0, self.y0), self.aradz)

        self.x0, self.y0, self.z0 = round(self.x0), round(self.y0), round(self.z0)

        for i in range(len(self.vertex)):
            x, y, z = self.vertex[i]
            x, z = project_2d_coord((x, z), self.aradx)
            y, z = project_2d_coord((y, z), self.arady)
            x, y = project_2d_coord((x, y), self.aradz)

            self.vertex[i] = [x, y, z]

    def calculate_coords(self):
        screen, cx, cy, w, h = self.get_surface()
        vertex_list = []
        screen_coords = []

        for i in range(len(self.vertex)):
            x, y, z = self.vertex[i]

            x += self.camera.pos[0] + self.x0
            y += self.camera.pos[1] + self.y0
            z += self.z0
            x, z = project_2d_coord((x, z), self.camera.rot[1])
            y, z = project_2d_coord((y, z), self.camera.rot[0])

            if self.camera.orto_view:
                z += self.camera.pos[2]
                vertex_list.append((x, y, z))
                z = self.camera.pos[2]
            elif not self.camera.orto_view:
                z += self.camera.pos[2]
                vertex_list.append((x, y, z))

            f = self.camera.fov / z
            x, y = x * f, y * f
            screen_coords.append((cx + int(x), cy + int(y)))
        return vertex_list, screen_coords

    def render(self):
        screen, cx, cy, w, h = self.get_surface()
        self.__verts_list, self.__screen_coords = self.calculate_coords()

        face_list, face_order, self.depth = self.render_order(self.geometry_data['faces'], self.__verts_list,
                                                              self.__screen_coords)

        for i in face_order:
            try:
                self.pg.draw.polygon(screen, self.own_colors[i], face_list[i])
                self.pg.draw.line(screen,
                                  self.root.current_palette['BLACK'],
                                  face_list[i][0],
                                  face_list[i][1],
                                  self.geometry_data['line_width'])
                self.pg.draw.line(screen,
                                  self.root.current_palette['BLACK'],
                                  face_list[i][2],
                                  face_list[i][3],
                                  self.geometry_data['line_width'])
                self.pg.draw.line(screen,
                                  self.root.current_palette['BLACK'],
                                  face_list[i][0], face_list[i][3],
                                  self.geometry_data['line_width'])
                self.pg.draw.line(screen,
                                  self.root.current_palette['BLACK'],
                                  face_list[i][1], face_list[i][2],
                                  self.geometry_data['line_width'])
            except:
                self.pg.draw.polygon(screen, self.own_colors[-1], face_list[i])

    def render_order(self, elements, verts_list, screen_coords):
        elements_list = []
        w, h = self.root.root.global_settings['VIEWPORT']['DEVICE']['SCREEN_WIDTH'], \
               self.root.root.global_settings['VIEWPORT']['DEVICE']['SCREEN_HEIGHT']
        depth = []
        for i in range(len(elements)):
            element = elements[i]
            on_screen = False
            for j in element:
                x, y = screen_coords[j]
                if verts_list[j][2] > 0 and 0 < x < w and 0 < y < h:
                    on_screen = True
                    break
            if on_screen:
                elements_list.append([screen_coords[i] for i in element])
                depth.append(sum(sum(verts_list[j][k] for j in element) ** 2 for k in range(len(element) - 1)))
        return elements_list, sorted(range(len(elements_list)), key=lambda i: depth[i], reverse=1), sum(
            i for i in depth) / len(depth)
