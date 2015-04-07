from dataLogic.repository import *
from model.order import *
import sqlite3
class BaseMarket(object):
    pass

class VirtualMarket(BaseMarket):
    ticks=0
    def __init__(self, agent, database="db/finance.db"):
        # account register
        # load asset data
        self.database = database
        self.agent = agent
    
               
# def __load_assets(self):
    #pass
    
    

    def run_by_step(self,period='day'):
        LOCAL_TABLE_NAME={'5min':'stock_5min','15min':'stock_15min','30min':'stock_30min','60min':'stock_60min','day':'stock_day' ,'week':'stock_week','month':'stock_month','year':'stock_year'}
        try:
            stock_period=LOCAL_TABLE_NAME[period]

            conn=sqlite3.connect(self.database)
            cursor=conn.cursor()
            sql="select * from %s where Date='%';"%(stock_period,t)
            data=cursor.execute(sql).fetchall()
        except:
            self.conn.close()
                        ### get the current all stocks record
        self.conn.close()
#pass


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
            users=[]
            try:
                conn=sqlite3.connect(self.database)
                cursor=conn.cursor()
                sql="select uid ,passwd from %s;"%ABLE
                u_id=cursor.execute(sql).fetchall()
                conn.close()
            except:
                conn.close()
            return(u_id)
        uids=get_uid(self.database,TABLE)
        for uid in uids:
            ##simulation the angent load the account
            self.agent[uid]=DemoAgent(uid,passwd,self.database)
            ### load the
            self.agent[uid].account.__str__()
            ### openPosition
            ### according to the stock price implementation strategy
            self.agent[uid].strategy(date=date,state=state)
            #self.agent[uid].orders=self.agent[uid].strategy(date,state).orders
            ### make order into class order and orderitem
            ##self.agent[uid].openPosition()
            
            self.agent[uid].MarketOrderRepository=MarketOrderRepository(self.database)
            self.agent[uid].MarketOrderRepository.create(order)
                #self.agent[uid].MarketOrderRepository.update(order)
            self.agent[uid].MarketOrderRepository.save()
            self.agent[uid].AccountRepository=AccountRepository(self.database)
            # self.agent[uid].AccountRepository.updateitems(self.uid)
            self.agent[uid].AccountRepository.updateavgcost(self.uid)
            self.agent[uid].AccountRepository.save()












