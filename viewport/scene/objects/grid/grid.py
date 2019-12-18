from ..utils.proection2d import project_2d_coord


class Grid:

    def __init__(self, root, pos=(0, 0, 0)):
        self.root = root
        self.camera = self.root.root.camera
        self.pg = self.root.root.pg
        self.data = root.root.global_settings['PUZZLE']['PRIMITIVES']['REGULAR']['GRID']
        self.position = list(pos)
        self.font = self.pg.font.SysFont('Lucida Console', 15)

    def render(self):
        screen = self.pg.display.get_surface()
        cx = self.root.root.global_settings['VIEWPORT']['DEVICE']['SCREEN_WIDTH'] // 2
        cy = self.root.root.global_settings['VIEWPORT']['DEVICE']['SCREEN_HEIGHT'] // 2

        for i in range(len(self.data['vertex'])):
            for j in range(1, self.data['size']):
                x = self.data['vertex'][i][0] + self.position[0]
                y = self.data['vertex'][i][1] + self.position[1]
                z = self.data['vertex'][i][2] + self.position[2]
                x *= j
                y *= j
                z *= j
                index = x + y + z
                x, z = project_2d_coord((x, z), self.camera.rot[1])
                y, z = project_2d_coord((y, z), self.camera.rot[0])

                if self.camera.orto_view:
                    z = self.camera.pos[2]
                elif not self.camera.orto_view:
                    z += self.camera.pos[2]
                f = self.camera.fov / z
                x, y = x * f, y * f
                # chars grid and dots
                screen.blit(self.font.render(str(index), False, self.root.settings['PALETTE']['BLACK']), (cx + x, cy + y))
                self.pg.draw.circle(screen, self.root.settings['PALETTE']['BLACK'], (cx + int(x), cy + int(y)), 2)
            # labels and axels
            screen.blit(self.font.render(self.data['labels'][i], False, self.root.settings['PALETTE']['BLACK']),
                        (cx + 1.1 * x, cy + 1.1 * y))
            self.pg.draw.line(screen, self.root.settings['PALETTE']['BLACK'], [cx, cy], (cx + x, cy + y), 1)
