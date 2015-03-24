import sqlite3
import sys
import traceback
from model.order import *

class Repository(object):

    def create(self):
        pass

    def read(self):
        pass
    
    def update(self):
        pass

    def delete(self):
        pass
    
    def save(self):
        pass

    
class MarketOrderRepository(Repository):
    TABLE = 'market_order'
    
    def __init__(self, database="db/finance.db", uid=None, passwd=None):
        self.database = database
        try:
            self.conn = sqlite3.connect(self.database)
            self.cursor = self.conn.cursor()
        except:
            self.conn.close()
            traceback.print_exc()
            sys.exit(1)

    def create(self, order):
        try:
            sql = """insert into %s values('%s', '%s', '%s', %s, %s);""" %(MarketOrderRepository.TABLE, order.getOid(), order.getTimestamp(), order.getSymbol(), order.getPrice(), order.getNum())
            self.cursor.execute(sql)
        except:
            self.conn.close()
            traceback.print_exc()
            sys.exit(1)

    def read(self):
        pass
            
    def update(self, order):
        pass

    def delete(self, order):
        pass

    def save(self):
        try:
            self.conn.commit()
            self.conn.close()
        except:
            traceback.print_exc()
            sys.exit(1)


    
