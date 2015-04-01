from dataLogic.repository import *
import sqlite3
class BaseMarket(object):
    pass

class VirtualMarket(Market):
    def __init__(self, agent, database="db/finance.db"):
        # account register
        # load asset data
        self.database = database
        self.agent = agent
        self.conn=sqlite3.connect(self.database)

    def __load_assets(self):
    
    

    def run_by_step(self，period='day'):
        pass

    


