from enum import Enum
from collections import namedtuple

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


BACKGROUND_COLOR = (125, 125, 125)
PLAYER_COLOR = (0, 0, 0)
APPLE_COLOR = (255, 0, 0)
WINDOW_SIZE = (800, 600)
SQUARE_SIZE = 20
FPS = 20

class Moves(Enum):
    RIGHT = 1
    UP = 2
    DOWN = 3
    LEFT = 4
