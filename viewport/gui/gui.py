from viewport.gui.button import button
from viewport.view import device_data
# from gui.check_box import check_box
# from gui.scroll_bar import scroll_bar


class GUI:
    def __init__(self, pygame):
        self.pg = pygame
        self.mouse_x = 0
        self.mouse_y = 0
        x, y = device_data['width'], device_data['height']
        self.offset_x = 0
        self.offset_y = y / 32
        self.x0 = x / 16
        self.y0 = y / 10
        self.width, self.height = x / 4, y / 8
        self.buttons = []

    def init_gui(self):
        self.start_x = self.setup(self.x0, self.offset_x, 5)
        self.unpack(button)

    def render_gui(self):
        for item in self.buttons:
            item.render()

    def unpack(self, obj):
        if isinstance(obj, dict):
            start_y = self.setup(self.y0, self.offset_y, len(obj))
            for key, value in obj.items():
                if isinstance(value, tuple):
                    continue
                else:
                    self.buttons.append(
                        button.Button(self.pg, (next(self.start_x), next(start_y)), (self.width, self.height), key))
                    self.unpack(value)
                    self.start_x = self.setup(self.x0, self.offset_x, 5)

    @staticmethod
    def setup(zero, offset, _len):
        for i in range(1, _len + 1):
            yield i * (zero + offset)
