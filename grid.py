class Grid():

    def __init__(self, camera, pygame, data, tools, pos = (0, 0, 0)):

        self.camera = camera
        self.pg = pygame
        self.data = data
        self.tools = tools
        self.data_device = self.data.device
        self.pos = list(pos)
        self.size = 10
        self.axis = data.grid.vertex
        self.labels = data.grid.labels
        self.font = self.pg.font.SysFont('Comic Sans MS', 15)
        self.screen = self.pg.display.get_surface()

    def render(self):

        colors = self.data.colors
        camera = self.camera
        tools = self.tools
        cx, cy = self.data.device.center_x, self.data.device.center_y

        for i in range(len(self.axis)):
            for j in range(1, self.size):
                x = self.axis[i][0] + self.pos[0]
                y = self.axis[i][1] + self.pos[1]
                z = self.axis[i][2] + self.pos[2]
                x *= j; y *= j; z *= j
                index = x + y + z
                x, z = tools.rotate((x, z), camera.rot[1])
                y, z = tools.rotate((y, z), camera.rot[0])
                if camera.orto_view:
                    z = camera.pos[2]
                elif not camera.orto_view:
                    z += camera.pos[2]
                f = camera.zoom / z
                x, y = x * f, y * f
#               char grid and dots
                self.screen.blit(self.font.render(str(index), False, colors.black), (cx + x, cy + y))
                self.pg.draw.circle(self.screen, colors.black, (cx + int(x), cy + int(y)), 2)
#       labels and axels
            self.screen.blit(self.font.render(self.labels[i], False, colors.black), (cx + x, cy + y))
            self.pg.draw.line(self.screen, colors.black, [cx , cy ], (cx + x, cy + y), 1)
