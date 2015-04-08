import sqlite3
from  random import sample
from dataLogic.repository import *
from model.order import *
class init:
    def __init__(self,agentnum=10,database='db/finance.db'):
        self.agentnum=agentnum
        self.database=database
        self.symbol={}
    def init_agent_num(self):
        uid={}

        for i in range(self.agentnum):
            uid[i]=str(i)
        self.uid=uid
    def init_agent_stocks(self):
        try:
           conn=sqlite3.connect(self.database)
           cursor=conn.cursor()
           symbols=cursor.execute("select distinct symbol from stock").fetchall()
           symbols=[i[0] for i in symbols]
           for key in self.uid:
                    self.symbol[self.uid[key]]=sample(symbols,10)
        except:
            conn.close()
            return 0
        conn.close()
    def init_agent_table(self):
        for key in self.uid:
            orders=MarketOrder(self.uid[key],"1990-01-01",strategy=sample(["sell","buy"],1)[0])
            for symbol in self.symbol[self.uid[key]]:
                    orders.addOrderItem(symbol,0,0)
            self.MarketOrderRepository=MarketOrderRepository(self.database)
            self.MarketOrderRepository.create(orders)
            self.MarketOrderRepository.save()
        for key in self.uid:
            self.AccountRepository=AccountRepository(self.database)
            self.AccountRepository.create(self.uid[key],self.uid[key])
            self.AccountRepository.insert(self.uid[key])
            self.AccountRepository.updateavgcost(self.uid[key])
            self.AccountRepository.save()
def initial():
    x=init()
    x.init_agent_num()
    x.init_agent_stocks()
    x.init_agent_table()




