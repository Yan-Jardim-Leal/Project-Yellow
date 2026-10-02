from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Core.vector2 import Vector2
    from World.map import Map

from typing import TypedDict, NotRequired

class EntityType(TypedDict):
    name : NotRequired[str]

    life : NotRequired[int]
    max_life : NotRequired[int]
    mana : NotRequired[int]

    position : Vector2
    map : Map
