from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Entities.base import BaseEntity
    from Core.vector2 import Vector2

class Map:

    def __init__(self, map_size : Vector2) -> None:
        self.entity_index = 0

        self.map_size = map_size
        self.entities = {}
        
        pass

    def addEntity(self, entity : BaseEntity):
        self.entity_index += 1
        self.entities[self.entity_index] = entity
        entity.setMap(self)
        return self.entity_index

    def removeEntity(self, index : int):
        self.entities[index].removeMap()
        self.entities[index] = None

    def moveEntity(self, entity : BaseEntity, position : Vector2):
        entity.sumPosition(position)


    # def moveEntity(self, index : int, position : Vector2):
    #     if not self.entities[index]:
    #         return

    #     self.entities[index].sumPosition(position)