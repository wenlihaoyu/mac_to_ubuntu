from helper.util import *
from model.order import *
from dataLogic.repository import *

class BaseAgent(object):
    def __init__(self, uid,passwd, database):
        self.database = database
        self.account = Account(uid,passwd)

    def openPosition(self):
        raiseNotDefined()

    def closePosition(self):
        raiseNotDefined()

    def updatePosition(self):
        raiseNotDefined()
        
    def long(self):
        raiseNotDefined()

    def short(self):
        raiseNotDefined()

    def close(self):
        raiseNotDefined()
        
    def __fireOrders(self):
        raiseNotDefined()

class DemoAgent(BaseAgent):
    def __init__(self, uid,passwd, database):
        super(DemoAgent, self).__init__(uid,passwd, database)
        self.repository = MarketOrderRepository(database)

    def openPosition(self):
        raiseNotDefined()

    def closePosition(self):
        raiseNotDefined()

    def updatePosition(self):
        raiseNotDefined()
        
    def long(self, order):
        raiseNotDefined()

    def short(self):
        raiseNotDefined()

    def close(self):
        raiseNotDefined()
        
    def __fireOrders(self, orders):
        for order in orders:
            self.repository.create(order)
        self.repository.save()
        
    
        
        

    
