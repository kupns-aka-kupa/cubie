from tools.tools import Tools

GRID_DATA = ['objects/grid/grid.json']


class Grid:

    def __init__(self, root, pos=(0, 0, 0)):
        self.root = root
        self.camera = self.root.root.camera
        self.pg = self.root.root.pg
        self.data = self.root.root.file_manager.load(GRID_DATA)['GRID']
        self.tools = Tools()
        self.position = list(pos)
        self.font = self.pg.font.SysFont('Lucida Console', 15)

    def render(self):
        screen = self.pg.display.get_surface()
        cx = self.root.root._settings['PREFERENCES']['SCREEN_WIDTH'] // 2
        cy = self.root.root._settings['PREFERENCES']['SCREEN_HEIGHT'] // 2

        for i in range(len(self.data['vertex'])):
            for j in range(1, self.data['size']):
                x = self.data['vertex'][i][0] + self.position[0]
                y = self.data['vertex'][i][1] + self.position[1]
                z = self.data['vertex'][i][2] + self.position[2]
                x *= j;
                y *= j;
                z *= j
                index = x + y + z
                x, z = self.tools.rotate((x, z), self.camera.rot[1])
                y, z = self.tools.rotate((y, z), self.camera.rot[0])
                if self.camera.orto_view:
                    z = self.camera.pos[2]
                elif not self.camera.orto_view:
                    z += self.camera.pos[2]
                f = self.camera.fov / z
                x, y = x * f, y * f
                #               char grid and dots
                screen.blit(
                    self.font.render(str(index),
                                     False,
                                     self.root.settings['PALETTE']['BLACK']), (cx + x, cy + y))

                self.pg.draw.circle(screen,
                                    self.root.settings['PALETTE']['BLACK'],
                                    (cx + int(x), cy + int(y)),
                                    2)
            #           labels and axels
            screen.blit(self.font.render(self.data['labels'][i], False, self.root.settings['PALETTE']['BLACK']),
                        (cx + 1.1 * x, cy + 1.1 * y))
            self.pg.draw.line(screen, self.root.settings['PALETTE']['BLACK'], [cx, cy], (cx + x, cy + y), 1)
