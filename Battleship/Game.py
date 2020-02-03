from Models.Player import *
from Models.Fleet import *
from package1.Order import *

class Game(object):
    players = []
    fleets = {}
    gameover = False
    
    def initGame(self):
        self.makePlayers()
        self.makeFleets()
        p:Player
        playerset = set(self.players)
        for p in self.players:
            p.postPlayers(playerset)


    def makePlayers(self):
        self.players.append(Player("Player1"))
        self.players.append(Player("Player2"))

    

    def makeFleets(self):
        p: Player
        for p in self.players:
            p.getFleet()
            self.fleets[p.name] = p.f #need to be able to handle name collisions
        return 
   
    

    def startGame(self):
        while not gameover:
            p: Player
            for p in self.players:
                o = p.getNextMove()
                self.ExecuteOrder(o)
                self.isGameOver()


    def ExecuteOrder(self, o:Order):
        print("Executing Order")



    def isGameOver(self):
        p: Player
        nonSunkPlayers = 0

        for p in self.players:
            if not p.isSunk:
                if p.f.isSunk():
                    p.isSunk == True
                else:
                    nonSunkPlayers += 1

        if nonSunkPlayers == 1:
            self.gameover = True
        elif nonSunkPlayers < 1:
            raise Exception("Should not be here")



