#from helper.util import *
from model.order import *
from dataLogic.repository import *
from random import choice
from business.strategy import *
class BaseAgent(object):
    def __init__(self, user, database):
        self.database = database

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
    def __init__(self, user, database):
       # super(DemoAgent, self).__init__(user.uid, database)
        self.repository = MarketOrderRepository(database)
        self.database=database
        self.order=None
        self.uid=user.uid
        self.passwd=user.passwd
        self.database=database
        self.strategy_data=None
        self.MarketOrderRepository=None
        self.AccountRepository=None
    def strategy(self,date):
        self.SolonStrategyAgent=SolonStrategyAgent(self.uid,self.database)
        self.orders=self.SolonStrategyAgent.getAction(date=date,flag="database",state=choice(["buy","sell"]))

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
        
    
        
        

    
