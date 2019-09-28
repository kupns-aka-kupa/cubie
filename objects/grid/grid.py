from tools import tools


class Grid:

    def __init__(self, camera, pygame, data, pos=(0, 0, 0)):

        self.camera = camera
        self.pg = pygame
        self.data, self.device = data
        self.tools = tools.Tools()
        self.pos = list(pos)
        self.size = self.data.size
        self.axis = self.data.vertex
        self.labels = self.data.labels
        self.font = self.pg.font.SysFont('Lucida Console', 15)

    def render(self):
        screen = self.pg.display.get_surface()
        colors = self.data.colors
        camera = self.camera
        cx, cy = self.device.center_x, self.device.center_y

        for i in range(len(self.axis)):
            for j in range(1, self.size):
                x = self.axis[i][0] + self.pos[0]
                y = self.axis[i][1] + self.pos[1]
                z = self.axis[i][2] + self.pos[2]
                x *= j; y *= j; z *= j
                index = x + y + z
                x, z = self.tools.rotate((x, z), camera.rot[1])
                y, z = self.tools.rotate((y, z), camera.rot[0])
                if camera.orto_view:
                    z = camera.pos[2]
                elif not camera.orto_view:
                    z += camera.pos[2]
                f = camera.fov / z
                x, y = x * f, y * f
                #               char grid and dots
                screen.blit(self.font.render(str(index), False, colors.black), (cx + x, cy + y))
                self.pg.draw.circle(screen, colors.black, (cx + int(x), cy + int(y)), 2)
            #           labels and axels
            screen.blit(self.font.render(self.labels[i], False, colors.black), (cx + 1.1 * x, cy + 1.1 * y))
            self.pg.draw.line(screen, colors.black, [cx, cy], (cx + x, cy + y), 1)
