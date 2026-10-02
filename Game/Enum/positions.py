from enum import Enum
from Core.vector2 import Vector2 

class Positions(Enum):

    LEFT = Vector2(-1, 0)
    RIGHT = Vector2(1, 0)
    UP = Vector2(0, 1)
    DOWN = Vector2(0, -1)

