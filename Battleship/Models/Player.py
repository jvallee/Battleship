from package1 import *
from package1.Order import *
from Models.Fleet import *

class Player(object):
    """description of class"""
    
    f:Fleet
    players:set
    isSunk: bool

    def __init__(self, name, URI = None):
        self.name = name 
        self.URI = URI
        self.isSunk = False


    def getNextMove(self):
        order = Order()
        order.coordinates.X = 0
        order.coordinates.Y = 1
        order.attacking = self.players[0]
        return order

    def postPlayers(self, players : set):
        p :Player
        for p in players:
            if p.name == self.name:
                players.remove(p)
                break
        self.players = players

    def getFleet(self):
        self.f = Fleet("")
        self.f.name = self.name
        return self.f


