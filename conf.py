from file import load
import os

CONFIG_DIR = os.path.dirname(os.path.abspath(__file__)) + '/config'


class Config:

    # Global app conf
    __DEVICE_PREFERENSES = CONFIG_DIR + '/device_preferences.json'
    __KEYBOARD_MAP = CONFIG_DIR + '/events/keyboard_map.json'
    __STANDART_PALETTE = CONFIG_DIR + '/palettes/standart_palette.json'
    __KDE_PALETTE = CONFIG_DIR + '/palettes/kde_palette.json'

    # Geometry data
    __GRID_DATA = CONFIG_DIR + '/geometry/grid.json'
    __CUBE_DATA = CONFIG_DIR + '/geometry/cube.json'
    __PYRAMIDE_DATA = CONFIG_DIR + '/geometry/pyramide.json'

    # Color data
    __RUBIKS_CUBE_COLOR_MAP = CONFIG_DIR + '/maps/rubiks_cube_color_map.json'
    __MIRROR_CUBE_COLOR_MAP = CONFIG_DIR + '/maps/mirror_cube_color_map.json'
    
    __PUZZLE_COLOR_MAPS = {
        'RUBIKS_CUBE': __RUBIKS_CUBE_COLOR_MAP,
        'MIRROR_CUBE': __MIRROR_CUBE_COLOR_MAP
    }

    __PRIMITIVE_DATA = {
        'CUBE': load(__CUBE_DATA),
        'GRID': load(__GRID_DATA),
        'PYRAMIDE': load(__PYRAMIDE_DATA)
    }

    __VIEWPORT_SETTINGS = {
        'DEVICE': load(__DEVICE_PREFERENSES),
        'PALETTES': {
            'STD': load(__STANDART_PALETTE),
            'KDE': load(__KDE_PALETTE)
        }

    }

    __EVENTS_SETTINGS = {
        'KEYBOARD': load(__KEYBOARD_MAP)
    }

    __PUZZLE_SETTINGS = {
        'PRIMITIVES': __PRIMITIVE_DATA,
        'COLOR_MAPS': __PUZZLE_COLOR_MAPS
    }

    GLOBAL_SETTINGS = {
        'VIEWPORT': __VIEWPORT_SETTINGS,
        'PUZZLE': __PUZZLE_SETTINGS,
        'EVENTS': __EVENTS_SETTINGS
    }

