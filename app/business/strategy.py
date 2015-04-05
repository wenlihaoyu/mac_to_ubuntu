from helper.util import raiseNotDefined
from model.BasicAsset import *


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
    
    def getAction(self, state):
        raiseNotDefined()

    def predict(self):
        raiseNotDefined()
    def save():
       self.BasicAsset.save()

class Action(object):
    OPON = "Open"
    CLOSE = "Close"
    NOTHING = "Nothing"
    

    

    
