from package1 import *



class Fleet(object):
    """description of class"""
    def __init__(self, name):
        self.aircraftcarrier = Ships.AircraftCarrier() 
        self.battleship = Ships.Battleship()
        self.destroyer = Ships.Destroyer()
        self.ptboat = Ships.PTBoat()
        self.submarine = Ships.Submarine()
        self.name = name

    def GetShips(self):
        ships = []
        ship.append(aircraftcarrier)
        ships.append(battleship)
        ships.append(destroyer)
        ships.append(ptboat)
        ships.append(submarine)

    def isSunk(self):
        ships = self.GetShips()
        for ship in ships:
            if not ship.isSunk:
                return False

        return True

