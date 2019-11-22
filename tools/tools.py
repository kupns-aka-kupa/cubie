import math


class Tools:

    def __init__(self):
        self.math = math

    def rotate(self, pos, rad):
        x, y = pos
        cos, sin = math.cos(rad), math.sin(rad)
        return x * cos - y * sin, y * cos + x * sin
