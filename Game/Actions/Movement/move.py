from Enum.positions import Positions
from Actions.base import BaseAction

class MoveAction(BaseAction):

    def doAction(self, param : Positions):
        self.entity.data["map"].moveEntity(self.entity, param.value)



