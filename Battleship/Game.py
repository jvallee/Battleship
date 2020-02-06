from Models.Player import *
from Models.Fleet import *
from package1.Order import *
from package1.Ship import *

class Game(object):
    players = []
    fleets = {}
    gameover = False
    fleetsandcoordinates  = {}
    
    def initGame(self):
        self.makePlayers()
        self.makeFleets()
        p:Player
        playerset = set(self.players)
        for p in self.players:
            p.postPlayers(playerset)

        self.placePlayersFleets()
        


    def makePlayers(self):
        self.players.append(Player("Player1"))
        self.players.append(userPlayer("Player2"))

    

    def makeFleets(self):
        p: Player

        for p in self.players:
            p.getFleet()
            self.fleets[p.name] = p.f #need to be able to handle name collisions
        return 
   


    def validateFleets(self):
        print("validating Ships")




    def placePlayersFleets(self):
        print("Placing fleets")

        for fname in self.fleets:
            self.fleetsandcoordinates[fname] = {}  
            self.placefleet(self.fleets[fname])


            
    def placefleet(self, fleet :Fleet):
        s: Ship
        for s in fleet.GetShips():
            self.placeship(s, fleet.name)
            s.initializeDamage()

        x = self.fleetsandcoordinates
        print("Ships placed \n\n\n\n\n\n\n")


    def placeship(self, ship:Ship, name:str):
        s = ship
        x = ship.position[0]
        y = ship.position[1]
        playerships = self.fleetsandcoordinates[name]

        for i in range(0, ship.length):
            if ship.shipOrientation == Orientation.Horizantal:
                c = (x+i, y)

            elif ship.shipOrientation == Orientation.Vertical:
                c = (x, y+i)

            if c in playerships:
                raise Exception("Ship already here")
            
            else:
                playerships[c] = ship
                print(type(ship), " placed at coordinate ", c[0], c[1]) 

        x = playerships
        y = self.fleetsandcoordinates


    def startGame(self):
        while not self.gameover:
            p: Player
            for p in self.players:
                if p.isSunk == True:
                    continue
                print("\n\n")
                o = p.getNextMove()
                o.orderfrom = p.name
                #o.coordinates = (15,0)
                self.ExecuteOrder(o)
                if o.coordinates == (17,17):
                    print("here")
                if o.orderresult == OrderResult.Shiphit:
                    print("hit here")
                self.isGameOver()
                if self.gameover:
                    break
                
        for p in self.players:
            if not p.isSunk == True:
                x = p.f.isSunk()
                print(p.name, " has won")


    def ExecuteOrder(self, o):
        if o.ordertype == OrderType.Attack:
            self.ExecuteAttack(o)
        elif o.ordertype == OrderType.Broadcast:
            #ExecuteBroadcast()
            print("Data is ", o.message)
        elif o.ordertype == OrderType.Recon:
            ExecuteRecon(o)
        else:
            raise Excepetion("Should not be here, ordertype")

        print("Executing Order")

    def ExecuteAttack(self, o: Order):
        print("attack")

        if o.coordinates == (0,10):
            print("here")
            pass


        if o.coordinates in self.fleetsandcoordinates[o.attacking]:
            ship :Ship
            ship = self.fleetsandcoordinates[o.attacking][o.coordinates]
            if o.coordinates[0] == ship.position[0]:
                offset = o.coordinates[1] - ship.position[1]

            else:
                offset = o.coordinates[0] - ship.position[0]
            ship.damage[offset] = True
            o.orderresult = OrderResult.Shiphit
            print(o.orderfrom, " hit ", o.attacking, " at ", o.coordinates)

        else:
            print(o.orderfrom, " missed ", o.attacking, " at ", o.coordinates)




    def ExecuteRecon(Self, o):
        print("Execiting Recon")



    def isGameOver(self):
        p: Player
        nonSunkPlayers = 0

        for p in self.players:
            if not p.isSunk:
                if p.f.isSunk():
                    p.isSunk =True
                else:
                    nonSunkPlayers += 1

        if nonSunkPlayers == 1:
            self.gameover = True

        elif nonSunkPlayers < 1:
            raise Exception("Should not be here")



