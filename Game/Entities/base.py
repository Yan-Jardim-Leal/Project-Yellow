from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Core.vector2 import Vector2
    from World.map import Map
    from Enum.actions import Actions
    from Types.entities import EntityType

class BaseEntity:
    _creation_id = 0

    def __init__(self, data : EntityType):
        
        self.data = data
        self.actions = {}

        self._id_entity = BaseEntity._creation_id
        BaseEntity._creation_id += 1

        pass

    def doAction(self, action : Actions, param):
        if not self.actions[action]:
            raise Exception("[Base] Action not registered")

        self.actions[action].doAction(param)

    def setMap(self, map : Map) -> bool:
        self.data["map"] = map
        return True

    def sumPosition(self, position : Vector2):
        self.data["position"] = self.data['position'] + position
            
    def getPosition(self):
        return self.data["position"]