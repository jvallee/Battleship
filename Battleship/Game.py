from Models.Player import *
from Models.Fleet import *
from package1.Order import *

class Game(object):
    players = []
    fleets = {}
    gameover = False
    

    def makePlayers(self):
        self.players.append(Player("Player1"))
        self.players.append(Player("Player2"))

    def makeFleets(self):
        p: Player
        for p in players:
            p.getFleet()
            fleets[p.name] = p.f #need to be able to handle name collisions
        return fleet
    
    def startGame(self):
        while not gameover:
            p: Player
            for p in self.players:
                o = p.getNextMove()
                self.ExecuteOrder(o)

    def ExecuteOrder(o:Order):
        print("Executing Order")


