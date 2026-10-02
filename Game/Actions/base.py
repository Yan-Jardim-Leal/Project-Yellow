from Entities.base import BaseEntity

class BaseAction():

    def __init__(self, entity : BaseEntity):
        self.entity = entity

    def doAction(self, param):
        pass
