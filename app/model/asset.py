_5_MIN='5Min'
_15_MIN='15Min'
_30_MIN='30Min'
_ONE_HOUR='1H'
_ONE_DAY='1D'
_ONE_WEEK='1W'
_ONE_MONTH='1Mon'
_ONE_YEAR='1Y'


class Asset(object):
    pass

class BasicAsset(asset):
    def __init__(self,uid,database):
       self.LOCAL_TABLE_NAME={'5min':'stock_5min','15min':'stock_15min','30min':'stock_30min','60min':'stock_60min','day':'stock_day' ,'week':'stock_week','month':'stock_month','year':'stock_year'}
       self.database=database
       self.uid=uid
       try:
          self.conn=sqlite3.connect(self.database)
          self.cursor=self.conn.cursor()
       except:
          self.conn.close()

    def getSymbol(self,table='account',detailtable='accountitem'):
        symbols=[]
        sql=" select distinct symbol from %s where uid='%s';"%(detailtable,self.uid)
        try:
            symbols=self.cursor.execute(sql).fetchall()
            symbols=list(symbols)
        except:
            self.conn.close()
        return symbols


    def getDataSource(self):
        

    def getPeriod(self):
        pass
    
    def getClose(self, from=None, to=None, freq=None):
        pass

    def getOpen(self, from=None, to=None, freq=None):
        pass

    def getHigh(self, from=None, to=None, freq=None):
        pass

    def getLow(self, from=None, to=None, freq=None):
        pass

    def get5Min(self, from=None, to=None, source=None):
        pass

    def get15Min(self, from=None, to=None, source=None):
        pass

    def get30Min(self, from=None, to=None, source=None):
        pass

    def get1Hour(self, from=None, to=None, source=None):
        pass

    def get1Day(self, from=None, to=None, source=None):
        pass

    def get1Week(self, from=None, to=None, source=None):
        pass

    def get1Month(self, from=None, to=None, source=None):
        pass

    def get1Year(self, from=None, to=None, source=None):
        pass

    def validate(self):
        pass

class Stock(BasicAsset):
    pass


class Future(BasicAsset):
    pass


class Option(BasicAsset):
    pass

