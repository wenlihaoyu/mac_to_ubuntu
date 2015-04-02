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
        try:
               self.conn=sqlite3.connect(self.database)
               self.cursor=self.conn.cursor()
        except:
               self.conn.close()
               
    def __load_assets(self):
    
    

    def run_by_step(self，period='day'):
        pass

    
class simulation:
    def __init__(self,database):
        self.database=database
        self.agent={}
        #self.account={}
          pass
    def create_account(self,uid,passwd):
        #self.account[uid]=passwd
        #self.account=Account(uid,passwd)
        #self.DemoAgent=DemoAgent(self.account,self.database)
        self.AccountRepository=AccountRepository(self.database)
        self.AccountRepository.create(uid,passwd)
        self.AccountRepository.save()
    def set_bassagent(self,TABLE,detailTABLE):
        def get_uid(database,TABLE):
            users=[]
            try:
                conn=sqlite3.connect(self.database)
                cursor=conn.cursor()
                sql="select uid ,passwd from %s;"#TABLE
                users=cursor.commit(sql).fetchall()
                conn.close()
            except:
                conn.close()
            return(users)
        users=get_uid(self.database,TABLE)
        for user in users:
            ##simulation the angent load the account
            self.agent[user.uid]=DemoAgent(uid,passwd)
            ### load the
            self.agent[user.uid].account.__str__()
            account=Account(user.uid,user.passwd)









