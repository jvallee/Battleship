from package1 import *
from package1.Ship import *


class Fleet(object):
    """description of class"""
    def __init__(self, name):
        self.aircraftcarrier = Ships.AircraftCarrier(15, 0) 
        self.aircraftcarrier.shipOrientation = Orientation.Horizantal
        
        self.battleship = Ships.Battleship(0, 10)
        self.battleship.shipOrientation = Orientation.Horizantal
        
        self.destroyer = Ships.Destroyer(3,4)
        self.destroyer.shipOrientation = Orientation.Horizantal

        self.ptboat = Ships.PTBoat(17,16)
        self.submarine = Ships.Submarine(16,15)
        self.name = name

    def GetShips(self):
        ships = []
        ships.append(self.aircraftcarrier)
        ships.append(self.battleship)
        ships.append(self.destroyer)
        ships.append(self.ptboat)
        ships.append(self.submarine)
        return ships

    def isSunk(self):
        ships = self.GetShips()
        for ship in ships:
            if not ship.isSunk():
                return False

        return True

