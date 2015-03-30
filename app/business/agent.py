from helper.util import *
from model.order import *
from dataLogic.repository import *

class BaseAgent(object):
    def __init__(self, account, database):
        self.database = database
        self.account = account

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
    def __init__(self, account, database):
        super(DemoAgent, self).__init__(account, database)
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
        
    
        
        

    
