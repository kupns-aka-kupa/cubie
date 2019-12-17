from viewport.scene.objects.utils.proection2d import project_2d_coord


class Cube:
    __verts_list = []
    __screen_coords = []

    def __init__(self, root, data):
        self.root = root
        self.camera = self.root.root.camera
        self.pg = self.root.root.pg
        self.data = root.root.global_settings['PUZZLE']['PRIMITIVES']['CUBE']
        [self.x0, self.y0, self.z0], self.own_colors = data
        self.vertex = self.data['vertex'].copy()
        self.rotx = 0
        self.roty = 0
        self.rotz = 0
        self.depth = 0

    def set_surface(self):
        screen = self.pg.display.get_surface()
        w, h = self.root.root.global_settings['VIEWPORT']['DEVICE']['SCREEN_WIDTH'], \
               self.root.root.global_settings['VIEWPORT']['DEVICE']['SCREEN_HEIGHT']
        cx, cy = w // 2, h // 2

        return screen, cx, cy, w, h

    def rotation(self, angles):
        self.rotx, self.roty, self.rotz = angles
        self.x0, self.z0 = project_2d_coord((self.x0, self.z0), self.rotx)
        self.y0, self.z0 = project_2d_coord((self.y0, self.z0), self.roty)
        self.x0, self.y0 = project_2d_coord((self.x0, self.y0), self.rotz)

        self.x0, self.y0, self.z0 = round(self.x0), round(self.y0), round(self.z0)

        for i in range(len(self.vertex)):
            x, y, z = self.vertex[i]
            x, z = project_2d_coord((x, z), self.rotx)
            y, z = project_2d_coord((y, z), self.roty)
            x, y = project_2d_coord((x, y), self.rotz)

            self.vertex[i] = [x, y, z]

    def calculate_coords(self):
        screen, cx, cy, w, h = self.set_surface()
        verts_list = []
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
                verts_list.append((x, y, z))
                z = self.camera.pos[2]
            elif not self.camera.orto_view:
                z += self.camera.pos[2]
                verts_list.append((x, y, z))

            f = self.camera.fov / z
            x, y = x * f, y * f
            screen_coords.append((cx + int(x), cy + int(y)))
        return verts_list, screen_coords

    def render(self):
        screen, cx, cy, w, h = self.set_surface()
        self.__verts_list, self.__screen_coords = self.calculate_coords()

        # edge_order, self.depth = self.render_order(self.data['edges'], point_list, self.__verts_list,
        #                                            self.__screen_coords)
        face_list, face_order, self.depth = self.render_order(self.data['faces'], self.__verts_list,
                                                              self.__screen_coords)

        for i in face_order:
            try:
                self.pg.draw.polygon(screen, self.own_colors[i], face_list[i])
                self.pg.draw.line(screen,
                                  self.root.current_palette['BLACK'],
                                  face_list[i][0],
                                  face_list[i][1],
                                  self.data['line_width'])
                self.pg.draw.line(screen,
                                  self.root.current_palette['BLACK'],
                                  face_list[i][2],
                                  face_list[i][3],
                                  self.data['line_width'])
                self.pg.draw.line(screen,
                                  self.root.current_palette['BLACK'],
                                  face_list[i][0], face_list[i][3],
                                  self.data['line_width'])
                self.pg.draw.line(screen,
                                  self.root.current_palette['BLACK'],
                                  face_list[i][1], face_list[i][2],
                                  self.data['line_width'])
            except:
                self.pg.draw.polygon(screen, self.own_colors[-1], face_list[i])

        # for i in edge_order:
        #     self.pg.draw.line(screen, self.root.current_palette['BLACK'], point_list[edge_order[i]][0], point_list[
        #     edge_order[i]][1],  self.data['line_width'])

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
