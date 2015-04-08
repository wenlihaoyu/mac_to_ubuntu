from dataLogic.repository import *
from model.order import *
import sqlite3
from business.strategy import *
from business.agent import *
class BaseMarket(object):
    pass

class VirtualMarket(BaseMarket):
    ticks=0
    def __init__(self, database="db/finance.db",n=100):
        # account register
        # load asset data
        self.database = database
        self.n=n
    def get_ticks(self):
         sql="select distinct date from stock_day;"
         date=None
         try:
             conn=sqlite3.connect(self.database)
             cursor=conn.cursor()
             date=cursor.execute(sql).fetchall()
             date=[i[0] for i in date]
             conn.close()
         except:
             return 0
         self.date=date
    def run_by_step(self,period='day'):
        for t in self.date[range(self.n)]:
            x=simulation('db/finance.db')
            x.set_bassagent('account',"accountitem",'2013-03-15')

class simulation:
    def __init__(self,database):
        self.database=database
        self.agent={}
        #self.account={}
        #pass
    #def create_account(self,uid,passwd):
        #self.account[uid]=passwd
        #self.account=Account(uid,passwd)
        #self.DemoAgent=DemoAgent(self.account,self.database)
        #   self.AccountRepository=AccountRepository(self.database)
        #self.AccountRepository.create(uid,passwd)
       #self.AccountRepository.save()
    def set_bassagent(self,TABLE,detailTABLE,date):
        ##TABLE is accout,detailTable is accountdeatail
        def get_uid(database,TABLE):
            u_id=None
            conn=None
            try:
                conn=sqlite3.connect(database)
                cursor=conn.cursor()
                sql="select uid ,passwd from %s;"%TABLE
                u_id=cursor.execute(sql).fetchall()
                conn.close()
            except:
                conn.close()
            return u_id
        uids=get_uid(self.database,TABLE)
        for uid in uids:
            ##simulation the angent load the account
            self.agent[uid[0][0]]=DemoAgent(uid[0][0],uid[1][0],self.database)
            ### load the
            #self.agent[uid].account.__str__()
            ### openPosition
            ### according to the stock price implementation strategy
            self.agent[uid[0][0]].strategy(date=date)
            #self.agent[uid].orders=self.agent[uid].strategy(date,state).orders
            ### make order into class order and orderitem
            ##self.agent[uid].openPosition()
            
            self.agent[uid[0][0]].MarketOrderRepository=MarketOrderRepository(self.database)
            self.agent[uid[0][0]].MarketOrderRepository.create(self.agent[uid[0][0]].orders)
                #self.agent[uid].MarketOrderRepository.update(order)
            self.agent[uid[0][0]].MarketOrderRepository.save()
            self.agent[uid[0][0]].AccountRepository=AccountRepository(self.database)
            # self.agent[uid].AccountRepository.updateitems(self.uid)
            self.agent[uid[0][0]].AccountRepository.updateavgcost(uid[0][0])
            self.agent[uid[0][0]].AccountRepository.save()

#from business.simulator import *
#x=simulation('db/finance.db')
#x.set_bassagent('account',"accountitem",'2013-03-15')











