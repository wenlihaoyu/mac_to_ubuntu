from helper.util import raiseNotDefined
from model.BasicAsset import *
from model.order import *
from dataLogic.repository import *
from random import choice
class StrategyAgent(object):
    """
    An agent must define a getAction method
    """
    def __init__(self):
        pass
    def getAction(self, state):
        """
        The Agent will receive a market state and must return an action.
        """
        raiseNotDefined()

    def predict(self):
        raiseNotDefined()

class SolonStrategyAgent(StrategyAgent):
    ### according to the current stock price making sure whether buy /sell/open
    ###close
    def __init__(self,uid,database):
        self.uid=uid
        self.database=database
        self.BasicAsset=BasicAsset(uid,self.database)
       
        self.Symbols=self.BasicAsset.getSymbol()
        self.BasicAsset.save()
    def getAction(self, date,flag="database",state):
        self.order=[]
        self.price={}
        if flag=="database":
            for symbol in self.Symbols:
                self.Repository=Repository(symbol,DATABASE=self.database)
                self.price[symbol]=list(self.Repository.read(date,period='day'))
                self.Repository.save()
                self.Repository=None
        else:
                        #state=='url'
         ###get the stock price from url
            for symbol in self.Symbols:
                self.stock=stock(symbol=symbol,begin=date,to=date,period='day')
                self.price[symbol]=[symbol]
                self.price[symbol].extend(self.get_from_url())
                self.stock=None
                    ##if state=='buy':
        for symbol in self.Symbols:
                orders=MarketOrder(uid=self.uid,timestamp=date,strategy=state)
                orders.addOrderItem(symbol=symbol,price=float(self.price[symbol][7]),num=choice(range(1,100)*100))
        return orders

    def predict(self):
        raiseNotDefined()
    def save():
       self.BasicAsset.save()

class Action(object):
    OPON = "Open"
    CLOSE = "Close"
    NOTHING = "Nothing"
    

    

    
