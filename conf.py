
class Config:
    def __init__(self):

        DEVICE_PREFERENSES = 'settings/device/preferences.json'
        self.GLOBAL_SETTINGS = [DEVICE_PREFERENSES]

        CUBE_COLOR_MAP = 'objects/puzzle/rubiks_cube/cube_color_map.json'
        PYRAMIDE_COLOR_MAP = 'objects/puzzle/pyramide/pyramide_color_map.json'
        PUZZLES_COLOR_MAP = [CUBE_COLOR_MAP, PYRAMIDE_COLOR_MAP]

        PALLETE = 'settings/palette.json'
        self.VIEWPORT_SETTINGS = [PALLETE, PUZZLES_COLOR_MAP]
