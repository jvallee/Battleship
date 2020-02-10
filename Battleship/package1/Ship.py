from enum import Enum

class Orientation(Enum):
    Vertical = 1
    Horizantal = 2


class Ship(object):
    def __init__(self, x = 0, y = 0, fleetName = ""):
        self.position = (x,y)
        self.shipOrientation = Orientation.Vertical
        self.fleetName = fleetName

    def initializeDamage(self):
        self.damage = [False]*self.length

    def isSunk(self):
        damage = self.damage
        for cell in damage:
            if cell == False:
                return False

        return True


        





