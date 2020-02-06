from enum import Enum




class OrderType(Enum):
    Attack = 1
    Recon = 2
    Broadcast = 3

class OrderResult(Enum):
    notexecuted = 0
    Shiphit = 1
    Shipmiss = 2
    Shipfound = 3
    shipnotfound = 4


class Order(object):
    
    coordinates = (-1,-1)
    orderfrom = ""
    ordertype = OrderType.Attack
    attacking = ""
    orderfrom = ""
    message = ""
    orderresult = OrderResult.notexecuted



