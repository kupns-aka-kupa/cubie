class Button:

    def __init__(self, pygame, position, size, text=''):
        self.pg = pygame
        self.x, self.y = position
        self.width, self.height = size
        self.text = text
        self.font = self.pg.font.SysFont('Ubuntu', 40)
        self.border = 2
        self.border_color = (24, 24, 24)

    def render(self):
        color = (234, 234, 234)
        screen = self.pg.display.get_surface()
        self.pg.draw.rect(screen, color, (self.x, self.y, self.width, self.height), 0)
        if self.border:
            self.pg.draw.rect(screen, self.border_color, (self.x, self.y, self.width, self.height), self.border)


        if self.text != '':
            text = self.font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def hover(self):
        pass

    def active(self):
        pass

    def overlap(self, pos):
        x, y = self.events.mouse_events()
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            return True
        return False
