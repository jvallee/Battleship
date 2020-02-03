from package1 import *
from package1.Order import *
from Models.Fleet import *

class Player(object):
    """description of class"""
    
    f:Fleet

    def __init__(self, name, URI = None):
        self.name = name 
        self.URI = URI


    def getNextMove(self):
        order = Order()
        order.coordinates.X = 0
        order.coordinates.Y = 1
        return order

    def getFleet(self):
        self.f = Fleet("")
        self.f.name = self.name
        return self.f


