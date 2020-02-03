from .Coordinate import *
from enum import Enum

class Ship(object):
    def __init__(self):
        self.positionAbsolute = Coordinate(0,0)
        self.shipOrientation = Orientation.Vertical

    def initializeDamage(self):
        self.damage = [False]*self.length

        def isSunk():
            damage = self.damage
            for cell in damage:
                if cell == False:
                    return False

            return True


        





class Orientation(Enum):
    Vertical = 1
    Horizantal = 2