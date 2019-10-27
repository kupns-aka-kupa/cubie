from app.tools import tools
from app.viewport.view import device_data, palette, fm

data = fm.open_file('app/objects/grid/grid.json')


class Grid:

    def __init__(self, camera, pygame, pos=(0, 0, 0)):

        self.camera = camera
        self.pg = pygame
        self.tools = tools.Tools()
        self.pos = list(pos)
        self.font = self.pg.font.SysFont('Lucida Console', 15)

    def render(self):
        screen = self.pg.display.get_surface()
        cx, cy = device_data['width'] // 2, device_data['height'] // 2

        for i in range(len(data['vertex'])):
            for j in range(1, data['size']):
                x = data['vertex'][i][0] + self.pos[0]
                y = data['vertex'][i][1] + self.pos[1]
                z = data['vertex'][i][2] + self.pos[2]
                x *= j; y *= j; z *= j
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
                screen.blit(self.font.render(str(index), False, palette['black']), (cx + x, cy + y))
                self.pg.draw.circle(screen, palette['black'], (cx + int(x), cy + int(y)), 2)
            #           labels and axels
            screen.blit(self.font.render(data['labels'][i], False, palette['black']), (cx + 1.1 * x, cy + 1.1 * y))
            self.pg.draw.line(screen, palette['black'], [cx, cy], (cx + x, cy + y), 1)
