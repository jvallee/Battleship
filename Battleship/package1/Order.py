from .Coordinate import *
from enum import Enum




class Order(object):
    class OrderType(Enum):
        Attack = 1
        Recon = 2
        Broadcast = 3
    coordinates = Coordinate(-1,-1)
    orderfrom = ""
    ordertype = OrderType.Attack
    attacking = ""


