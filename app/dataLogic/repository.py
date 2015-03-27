import sqlite3
import sys
import traceback
from model.order import *
from helper.util import *

class Repository(object):


    def __init__(self, database="db/finance.db"):
        self.database = database
        try:
            self.conn = sqlite3.connect(self.database)
            self.cursor = self.conn.cursor()
        except:
            self.conn.close()
            traceback.print_exc()
    
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
    """
    MarketOrderRepository
    It is used to manipulate market order

    Attr:
       database: 
    """
    TABLE = 'marketorder'
    DETAILTABLE = 'marketorderitem'

    def create(self, order):
        """
        Create a market order

        Parameters:
           order: market order
        
        Example:
        >>> from dataLogic.repository import *
        >>> mr = MarketOrderRepository()
        >>> orderitems = [MarketOrderItem('111', '123', 'AAPL', 20.0, 300)]
        >>> order = MarketOrder('123', 'xxb', '20:08:00', 'arbitrage', orderitems)
        >>> mr.create(order)
        >>> mr.save()
        """
        try:
            insertOrder = """insert into %s values('%s','%s', '%s', '%s');""" %(MarketOrderRepository.TABLE, order.oid, order.uid, order.timestamp,  order.strategy)
            for item in order.items:
                insertItems = """insert into %s values('%s', '%s', '%s', %s, %s); """ %(MarketOrderRepository.DETAILTABLE, item.id, item.oid, item.symbol, item.price, item.num)
                self.cursor.execute(insertItems)
            self.cursor.execute(insertOrder)
        except:
            self.conn.close()
            traceback.print_exc()


    def read(self, oid):
        """
        Read data from database

        Parameters:
           oid: order id

        Example:
        >>> from dataLogic.repository import *
        >>> mr = MarketOrderRepository()
        >>> order = mr.read('123')
        >>> print order
        """
        try:
            getorder = """select * from %s where oid = '%s';""" %(MarketOrderRepository.TABLE, oid)
            getitems = """select * from %s where oid = '%s';""" %(MarketOrderRepository.DETAILTABLE, oid)

            orderRecord = self.cursor.execute(getorder).fetchone()
            itemsRecord = self.cursor.execute(getitems).fetchall()
            orderItems = []
            for item in itemsRecord:
                orderitem = MarketOrderItem(item[0], item[1], item[2], item[3], item[4])
                orderItems.append(orderitem)
            order = MarketOrder(orderRecord[0], orderRecord[1], orderRecord[2], orderRecord[3], orderItems)
            self.conn.close()
            return order
        except:
            self.conn.close()
            traceback.print_exc()
            
                     
    def update(self, order):
        raiseNotDefined()

    def delete(self, order):
        raiseNotDefined()

    def save(self):
        try:
            self.conn.commit()
            self.conn.close()
        except:
            traceback.print_exc()
            

class AccountRepository(Repository):
    """
    AccountRepository
    It is used to manipulate user data

    Attr:
    """
    TABLE = "account"
    DETAILTABLE = "accountitem"

    def create(self, uid, passwd):
        """
        Create a Account

        Parameters:
           order: user id
           passwd: account password

        Example:
        >>> from dataLogic.repository import *
        >>> ar = AccountRepository()
        >>> account = account('0000','passwd')
        >>> ar.create(account)
        >>> ar.save()
        """
        pass

    def update(self, passwd):
        self.passwd = passwd

    def delete(self, uid):
        pass

    def read(self, uid):
        pass

    def save(self):
        pass

    def updateitems(self):
        pass

    
    
