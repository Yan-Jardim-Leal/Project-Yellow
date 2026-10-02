from Entities.base import BaseEntity
from Actions.Movement.move import MoveAction
from Types.entities import EntityType
from Enum.actions import Actions

class Player(BaseEntity):

    def __init__(self, data: EntityType):
        super().__init__(data)
        self.actions = {
            Actions.MOVE : MoveAction(self)
        }
