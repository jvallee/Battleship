from package1 import *
from package1.Order import *
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
        #X = random.randint(1,19)
        #Y = random.randint(1,19)
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

    def getNextMove(self):
        # add try catch
        order = Order.Order()
       
        #x = int(input("please enter the X coordinate of where you would like to attack: \n"))
        #y = int(input("please enter the Y coordinate of where you would like to attack: \n"))
        x = random.randint(0,19)
        y = random.randint(0,19)
        if x < 0 or y < 0:
            print("Shooting outside the game board, sorry that's your turn")
        order.coordinates = (x,y)
        order.attacking = "Player1"
        return order

    
