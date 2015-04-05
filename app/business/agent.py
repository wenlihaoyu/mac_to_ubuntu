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
        self.strategy=None
        self.order=None
        self.strategy_data=None
        self.MarketOrderRepository=None
        self.AccountRepository=None
    def strategy(self):
        self.SolonStrategyAgent=SolonStrategyAgent(self.uid,self.database)
        self.getAction(state)

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
        
    
        
        

    
