from package1 import *
from package1.Order import *
from package1.Ship import *
from Models.Fleet import *
import random

class Player(object):
    """description of class"""
    
    f:Fleet
    players:set
    isSunk: bool
    lastcoor = (-1, 0)

    def __init__(self, name, URI = None):
        self.name = name 
        self.URI = URI
        self.isSunk = False


    def getNextMove(self):
        order = Order.Order()
        
        currX = self.lastcoor[0]+1
        currY = self.lastcoor[1]
        if currX >= 20:
            currX = 0 
            currY +=1
        self.lastcoor = (currX, currY)
        order.coordinates = self.lastcoor
        order.attacking = self.players[0]
        return order

    def postPlayers(self, players : set):
        p :Player
        newplayers = []
        for p in players:
            if  not p.name == self.name:
                newplayers.append(p.name)
                
        self.players = newplayers

    def getFleet(self):
        self.f = Fleet("")
        self.f.name = self.name
        return self.f


class userPlayer(Player):
    def __init__(self, name, URI = None):
        self.name = input("What is your name?\n")
        self.isSunk = False
    
    def getShipPlacemnet(self, ship):
        
        while True:
            try:
                print("\n     Placing ", ship.name)
                x = int(input("         enter X Coordinate:\n       "))
                y = int(input("         enter Y Coordinate:\n       "))
                orientation = input("         enter orientation (h or v):\n       ")
                if orientation not in ['v','h']:
                    raise Exception("       orientation has to be 'v' for vertical or 'h' for horizantal")

                break

            except Exception as inst:
                print("Issue here with try again")
                print(inst)

            
        ship.position = (x, y)
        if orientation == 'v':
            ship.shipOrientation =  Orientation.Vertical
        elif orientation == 'h':
            ship.shipOrientation =  Orientation.Horizantal


    def getFleet(self):
        self.f = Fleet("")
        self.f.name = self.name
        print("Getting ready to place your Fleet")
        for ship in self.f.GetShips():
            self.getShipPlacemnet(ship)

        return self.f

    def getNextMove(self):
        # add try catch
        order = Order.Order()
        while True:
            try:
                x = int(input("please enter the X coordinate of where you would like to attack: \n"))
                y = int(input("please enter the Y coordinate of where you would like to attack: \n"))
                #x = random.randint(0,19)
                #y = random.randint(0,19)
                break
            except:
                print("try again")
                

        if x < 0 or y < 0:
            print("Shooting outside the game board, sorry that's your turn")
        order.coordinates = (x,y)
        order.attacking = "Player1"
        return order


    
