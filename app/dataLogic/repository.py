import sqlite3
import traceback
import urllib.request,urllib.parse,urllib.error
from model.order import *
from model.account import *
#from helper.util import *
from uuid import uuid1
DATABASE="db/finance.db"
class init_table:
    ### create the tables of we need with the function create_table
    def __init__(self,database="db/finance.db"):
        self.database=database
        try:
            self.conn=sqlite3.connect(self.database)
            self.cursor=self.conn.cursor()
        except:
            self.conn.close()

    def create_table(self):
        LOCAL_TABLE_NAME={'5min':'stock_5min','15min':'stock_15min','30min':'stock_30min','60min':'stock_60min','day':'stock_day' ,'week':'stock_week','month':'stock_month','year':'stock_year'}
        
        try:
           sql="select tbl_name from sqlite_master where type='table' and tbl_name='%s';"%"stock"
           if len(self.cursor.execute(sql).fetchall())==0:
               self.cursor.execute("create table %s(symbol text primary key,name text,market text,source text,comment text);"%"stock")
               self.conn.commit()
           sql="select tbl_name from sqlite_master where type='table' and tbl_name='%s';"%"marketorder"
           if len(self.cursor.execute(sql).fetchall())==0:
               self.cursor.execute("create table marketorder(oid varchar primary key, uid varchar, timestamp varchar, strategy varchar);")
               self.conn.commit()
           sql="select tbl_name from sqlite_master where type='table' and tbl_name='%s';"%"marketorderitem"
           if len(self.cursor.execute(sql).fetchall())==0:
               self.cursor.execute("create table marketorderitem(id varchar primary key, oid varchar, symbol varchar, price real, num int);")
               self.conn.commit()
           sql="select tbl_name from sqlite_master where type='table' and tbl_name='%s';"%"account"
           if len(self.cursor.execute(sql).fetchall())==0:
               self.cursor.execute("create table account(uid varchar primary key, passwd varchar);")
               self.conn.commit()
           sql="select tbl_name from sqlite_master where type='table' and tbl_name='%s';"%"accountitem"
           if len(self.cursor.execute(sql).fetchall())==0:
               self.cursor.execute("create table accountitem(uid varchar, symbol varchar, avgcost real, num int);")
               self.conn.commit()
        except:
           self.conn.close()
    
        for key in LOCAL_TABLE_NAME:
            sql="select tbl_name from sqlite_master where type='table' and tbl_name='%s';"%LOCAL_TABLE_NAME[key]
            try:
                if len(self.cursor.execute(sql).fetchall())==0:
                    sql="create table %s(symbol text ,Date text, Open real,High real ,Low real,Close real,Volume integer, Adj_close real);"%LOCAL_TABLE_NAME[key]
                    self.cursor.execute(sql)
                    self.conn.commit()
            except:
                self.conn.close()
    def save(self):
        self.conn.close()
class  stock:
    def __init__(self,symbol='600000.ss',begin='2011-01-01',to='2012-01-01',period='day'):
        self.symbol=symbol
        self.begin=begin
        self.to=to
        self.period=period
        
    def search_from_url(self):
        def get_time(t):
            if t==None or t=="":
                t_year=""
                t_month=""
                t_day=""
            else:
                t_year=str(int(t[0:4]))
                t_month=str(int(t[5:7])-1)
                t_day=str(int(t[8:10]))
            return list([t_year,t_month,t_day])
        begin_time=get_time(self.begin)
        to_time=get_time(self.to) 
        url_name=['sina','sohu','googel','yahoo']
        if self.period=='day':
           period='d'
        url='http://ichart.yahoo.com/table.csv?s=%s&a=%s&b=%s&c=%s&d=%s&e=%s&f=%s&g=%s&ignore=.csv'%(self.symbol,begin_time[1],begin_time[2],begin_time[0],to_time[1],to_time[2],to_time[0],period)
        response=urllib.request.urlopen(url)
        response=response.read()
        data=response.replace(b'[[',b'[')
        data=data.replace(b']]',b']')
        data=data.replace(b'[',b'')
        data=data.replace(b'],',b'\n')
        data=data.replace(b']',b'\n')
        data=data.replace(b'"',b'')
        data=data.split(b'\n')
        data=[str(i,"utf-8").split(',') for i in data[0:len(data)-1]]
        self.data=data[1:len(data)-1]
        
class name:
    def __init__(self):
        self.name="600000.ss,600004.ss,600005.ss,600006.ss,600007.ss,600008.ss,600009.ss,600010.ss,600011.ss,600012.ss,600015.ss,600016.ss,600017.ss,600018.ss,600019.ss,600020.ss,600021.ss,600022.ss,600026.ss,600027.ss,600028.ss,600029.ss,600030.ss,600031.ss,600033.ss,600035.ss,600036.ss,600037.ss,600038.ss,600039.ss,600048.ss,600050.ss,600051.ss,600052.ss,600053.ss,600054.ss,600055.ss,600056.ss,600057.ss,600058.ss,600059.ss,600061.ss,600062.ss,600063.ss,600064.ss,600066.ss,600067.ss,600068.ss,600069.ss,600070.ss,600071.ss,600072.ss,600073.ss,600074.ss,600075.ss,600076.ss,600077.ss,600078.ss,600079.ss,600080.ss,600081.ss,600082.ss,600083.ss,600084.ss,600085.ss,600086.ss,600087.ss,600088.ss,600089.ss,600090.ss,600091.ss,600093.ss,600094.ss,600095.ss,600096.ss,600097.ss,600098.ss,600099.ss,600100.ss,600101.ss,600103.ss,600104.ss,600105.ss,600106.ss,600107.ss,600108.ss,600109.ss,600110.ss,600111.ss,600112.ss,600113.ss,600114.ss,600115.ss,600116.ss,600117.ss,600118.ss,600119.ss,600120.ss,600121.ss,600122.ss,600123.ss,600125.ss,600126.ss,600127.ss,600128.ss,600129.ss,600130.ss,600131.ss,600132.ss,600133.ss,600135.ss,600136.ss,600137.ss,600138.ss,600139.ss,600141.ss,600143.ss,600145.ss,600146.ss,600148.ss,600149.ss,600150.ss,600151.ss,600152.ss,600153.ss,600155.ss,600156.ss,600157.ss,600158.ss,600159.ss,600160.ss,600161.ss,600162.ss,600163.ss,600165.ss,600166.ss,600167.ss,600168.ss,600169.ss,600170.ss,600171.ss,600172.ss,600173.ss,600175.ss,600176.ss,600177.ss,600178.ss,600179.ss,600180.ss,600182.ss,600183.ss,600184.ss,600185.ss,600186.ss,600187.ss,600188.ss,600189.ss,600190.ss,600191.ss,600192.ss,600193.ss,600195.ss,600196.ss,600197.ss,600198.ss,600199.ss,600200.ss,600201.ss,600202.ss,600203.ss,600206.ss,600207.ss,600208.ss,600209.ss,600210.ss,600211.ss,600212.ss,600213.ss,600215.ss,600216.ss,600217.ss,600218.ss,600219.ss,600220.ss,600221.ss,600222.ss,600223.ss,600225.ss,600226.ss,600227.ss,600228.ss,600229.ss,600230.ss,600231.ss,600232.ss,600233.ss,600234.ss,600235.ss,600236.ss,600237.ss,600238.ss,600239.ss,600240.ss,600241.ss,600242.ss,600243.ss,600246.ss,600247.ss,600248.ss,600249.ss,600250.ss,600251.ss,600252.ss,600253.ss,600255.ss,600256.ss,600257.ss,600258.ss,600259.ss,600260.ss,600261.ss,600262.ss,600265.ss,600266.ss,600267.ss,600268.ss,600269.ss,600270.ss,600271.ss,600272.ss,600273.ss,600275.ss,600276.ss,600277.ss,600278.ss,600279.ss,600280.ss,600281.ss,600282.ss,600283.ss,600284.ss,600285.ss,600287.ss,600288.ss,600289.ss,600290.ss,600291.ss,600292.ss,600293.ss,600295.ss,600297.ss,600298.ss,600299.ss,600300.ss,600301.ss,600302.ss,600303.ss,600305.ss,600306.ss,600307.ss,600308.ss,600309.ss,600310.ss,600311.ss,600312.ss,600313.ss,600315.ss,600316.ss,600317.ss,600319.ss,600320.ss,600321.ss,600322.ss,600323.ss,600325.ss,600326.ss,600327.ss,600328.ss,600329.ss,600330.ss,600331.ss,600332.ss,600333.ss,600335.ss,600336.ss,600337.ss,600338.ss,600339.ss,600340.ss,600343.ss,600345.ss,600346.ss,600348.ss,600350.ss,600351.ss,600352.ss,600353.ss,600354.ss,600355.ss,600356.ss,600358.ss,600359.ss,600360.ss,600361.ss,600362.ss,600363.ss,600365.ss,600366.ss,600367.ss,600368.ss,600369.ss,600370.ss,600371.ss,600372.ss,600373.ss,600375.ss,600376.ss,600377.ss,600378.ss,600379.ss,600380.ss,600381.ss,600382.ss,600383.ss,600385.ss,600386.ss,600387.ss,600388.ss,600389.ss,600390.ss,600391.ss,600392.ss,600393.ss,600395.ss,600396.ss,600397.ss,600398.ss,600399.ss,600400.ss,600401.ss,600403.ss,600405.ss,600406.ss,600408.ss,600409.ss,600410.ss,600415.ss,600416.ss,600418.ss,600419.ss,600420.ss,600421.ss,600422.ss,600423.ss,600425.ss,600426.ss,600428.ss,600429.ss,600432.ss,600433.ss,600435.ss,600436.ss,600438.ss,600439.ss,600444.ss,600446.ss,600448.ss,600449.ss,600452.ss,600455.ss,600456.ss,600458.ss,600459.ss,600460.ss,600461.ss,600462.ss,600463.ss,600466.ss,600467.ss,600468.ss,600469.ss,600470.ss,600475.ss,600476.ss,600477.ss,600478.ss,600479.ss,600480.ss,600481.ss,600482.ss,600483.ss,600485.ss,600486.ss,600487.ss,600488.ss,600489.ss,600490.ss,600491.ss,600493.ss,600495.ss,600496.ss,600497.ss,600498.ss,600499.ss,600500.ss,600501.ss,600502.ss,600503.ss,600505.ss,600506.ss,600507.ss,600508.ss,600509.ss,600510.ss,600511.ss,600512.ss,600513.ss,600515.ss,600516.ss,600517.ss,600518.ss,600519.ss,600520.ss,600521.ss,600522.ss,600523.ss,600525.ss,600526.ss,600527.ss,600528.ss,600529.ss,600530.ss,600531.ss,600532.ss,600533.ss,600535.ss,600536.ss,600537.ss,600538.ss,600539.ss,600540.ss,600543.ss,600545.ss,600546.ss,600547.ss,600548.ss,600549.ss,600550.ss,600551.ss,600552.ss,600555.ss,600556.ss,600557.ss,600558.ss,600559.ss,600560.ss,600561.ss,600562.ss,600563.ss,600565.ss,600566.ss,600567.ss,600568.ss,600569.ss,600570.ss,600571.ss,600572.ss,600573.ss,600575.ss,600576.ss,600577.ss,600578.ss,600579.ss,600580.ss,600581.ss,600582.ss,600583.ss,600584.ss,600585.ss,600586.ss,600587.ss,600588.ss,600589.ss,600590.ss,600592.ss,600593.ss,600594.ss,600595.ss,600596.ss,600597.ss,600598.ss,600599.ss,600600.ss,600601.ss,600602.ss,600603.ss,600604.ss,600605.ss,600606.ss,600608.ss,600609.ss,600610.ss,600611.ss,600612.ss,600613.ss,600614.ss,600615.ss,600616.ss,600617.ss,600618.ss,600619.ss,600620.ss,600621.ss,600622.ss,600623.ss,600624.ss,600626.ss,600628.ss,600629.ss,600630.ss,600633.ss,600634.ss,600635.ss,600636.ss,600637.ss,600638.ss,600639.ss,600640.ss,600641.ss,600642.ss,600643.ss,600644.ss,600645.ss,600647.ss,600648.ss,600649.ss,600650.ss,600651.ss,600652.ss,600653.ss,600654.ss,600655.ss,600656.ss,600657.ss,600658.ss,600660.ss,600661.ss,600662.ss,600663.ss,600664.ss,600665.ss,600666.ss,600667.ss,600668.ss,600671.ss,600673.ss,600674.ss,600675.ss,600676.ss,600677.ss,600678.ss,600679.ss,600680.ss,600681.ss,600682.ss,600683.ss,600684.ss,600685.ss,600686.ss,600687.ss,600688.ss,600689.ss,600690.ss,600691.ss,600692.ss,600693.ss,600694.ss,600695.ss,600696.ss,600697.ss,600698.ss,600699.ss,600701.ss,600702.ss,600703.ss,600704.ss,600705.ss,600706.ss,600707.ss,600708.ss,600710.ss,600711.ss,600712.ss,600713.ss,600714.ss,600715.ss,600716.ss,600717.ss,600718.ss,600719.ss,600720.ss,600721.ss,600722.ss,600723.ss,600724.ss,600725.ss,600726.ss,600727.ss,600728.ss,600729.ss,600730.ss,600731.ss,600732.ss,600733.ss,600734.ss,600735.ss,600736.ss,600737.ss,600738.ss,600739.ss,600740.ss,600741.ss,600742.ss,600743.ss,600744.ss,600745.ss,600746.ss,600747.ss,600748.ss,600749.ss,600750.ss,600751.ss,600753.ss,600754.ss,600755.ss,600756.ss,600757.ss,600758.ss,600759.ss,600760.ss,600761.ss,600763.ss,600764.ss,600765.ss,600766.ss,600767.ss,600768.ss,600769.ss,600770.ss,600771.ss,600773.ss,600774.ss,600775.ss,600776.ss,600777.ss,600778.ss,600779.ss,600780.ss,600781.ss,600782.ss,600783.ss,600784.ss,600785.ss,600787.ss,600789.ss,600790.ss,600791.ss,600792.ss,600793.ss,600794.ss,600795.ss,600796.ss,600797.ss,600798.ss,600800.ss,600801.ss,600802.ss,600803.ss,600804.ss,600805.ss,600806.ss,600807.ss,600808.ss,600809.ss,600810.ss,600811.ss,600812.ss,600814.ss,600815.ss,600816.ss,600817.ss,600818.ss,600819.ss,600820.ss,600821.ss,600822.ss,600823.ss,600824.ss,600825.ss,600826.ss,600827.ss,600828.ss,600829.ss,600830.ss,600831.ss,600832.ss,600833.ss,600834.ss,600835.ss,600836.ss,600837.ss,600838.ss,600839.ss,600841.ss,600843.ss,600844.ss,600845.ss,600846.ss,600847.ss,600848.ss,600850.ss,600851.ss,600853.ss,600854.ss,600855.ss,600856.ss,600857.ss,600858.ss,600859.ss,600860.ss,600861.ss,600862.ss,600863.ss,600864.ss,600865.ss,600866.ss,600867.ss,600868.ss,600869.ss,600870.ss,600871.ss,600872.ss,600873.ss,600874.ss,600875.ss,600876.ss,600877.ss,600879.ss,600880.ss,600881.ss,600882.ss,600883.ss,600884.ss,600885.ss,600886.ss,600887.ss,600888.ss,600889.ss,600890.ss,600891.ss,600892.ss,600893.ss,600894.ss,600895.ss,600896.ss,600897.ss,600898.ss,600900.ss,600960.ss,600961.ss,600962.ss,600963.ss,600965.ss,600966.ss,600967.ss,600969.ss,600970.ss,600971.ss,600973.ss,600975.ss,600976.ss,600978.ss,600979.ss,600980.ss,600981.ss,600982.ss,600983.ss,600984.ss,600985.ss,600986.ss,600987.ss,600988.ss,600990.ss,600992.ss,600993.ss,600995.ss,600997.ss,600998.ss,600999.ss,601000.ss,601001.ss,601002.ss,601003.ss,601005.ss,601006.ss,601007.ss,601008.ss,601009.ss,601010.ss,601011.ss,601012.ss,601018.ss,601028.ss,601038.ss,601058.ss,601088.ss,601098.ss,601099.ss,601100.ss,601101.ss,601106.ss,601107.ss,601111.ss,601113.ss,601116.ss,601117.ss,601118.ss,601126.ss,601137.ss,601139.ss,601158.ss,601166.ss,601168.ss,601169.ss,601177.ss,601179.ss,601186.ss,601188.ss,601199.ss,601208.ss,601216.ss,601218.ss,601222.ss,601231.ss,601233.ss,601238.ss,601258.ss,601268.ss,601288.ss,601299.ss,601311.ss,601313.ss,601328.ss,601333.ss,601336.ss,601339.ss,601369.ss,601377.ss,601388.ss,601390.ss,601398.ss,601515.ss,601518.ss,601519.ss,601555.ss,601558.ss,601566.ss,601567.ss,601588.ss,601599.ss,601600.ss,601601.ss,601607.ss,601608.ss,601616.ss,601618.ss,601628.ss,601633.ss,601636.ss,601666.ss,601668.ss,601669.ss,601677.ss,601678.ss,601688.ss,601699.ss,601700.ss,601717.ss,601718.ss,601727.ss,601766.ss,601777.ss,601788.ss,601789.ss,601798.ss,601799.ss,601800.ss,601801.ss,601808.ss,601818.ss,601857.ss,601866.ss,601872.ss,601877.ss,601880.ss,601886.ss,601888.ss,601890.ss,601898.ss,601899.ss,601901.ss,601908.ss,601918.ss,601919.ss,601928.ss,601929.ss,601933.ss,601939.ss,601958.ss,601965.ss,601988.ss,601989.ss,601991.ss,601992.ss,601996.ss,601998.ss,601999.ss,603000.ss,603001.ss,603002.ss,603003.ss,603008.ss,603077.ss,603123.ss,603128.ss,603167.ss,603333.ss,603366.ss,603399.ss,603766.ss,603993.ss"
        self.name=self.name.split(',')        
        
class Repository(object):

    def __init__(self,symbol,name="",market="",source="Yahoo",comment="",database='db/finance.db' ):
        self.symbol=symbol
        self.name=name
        self.market=market
        self.source=source
        self.comment=comment
        self.LOCAL_TABLE_NAME={'5min':'stock_5min','15min':'stock_15min','30min':'stock_30min','60min':'stock_60min','day':'stock_day' ,'week':'stock_week','month':'stock_month','year':'stock_year'}
        try:
            self.conn = sqlite3.connect(database)
            self.cursor = self.conn.cursor()

        except:
            self.conn.close()
            traceback.print_exc()
    
    def create(self,begin,to,period):
        table_name=self.LOCAL_TABLE_NAME[period]
        self.stock=stock(symbol=self.symbol,begin=begin,to=to,period='day')
        self.stock.search_from_url()
        if len(self.stock.data)==0:
           return('F')
        for da in self.stock.data:
            sql="insert into %s values('%s','%s',%s,%s,%s,%s,%s,%s);"%(table_name,self.symbol,da[0],da[1],da[2],da[3],da[4],str(int(da[5])),da[6])
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except:
                self.conn.close()
                break
        try:
            self.cursor.execute("insert into stock values('%s','%s','%s','%s','%s');"%(self.symbol,self.name,self.market,self.source,self.comment))
            
            self.conn.commit()
        except:
            self.conn.close()
    def save(self):
        self.conn.close()

    def read(self,date,period):
        data=None
        if period in self.LOCAL_TABLE_NAME:
           table_name=self.LOCAL_TABLE_NAME[period]
        else:
           return 0
        sql="select symbol,date,open,high,low,close,volume,adj_close from %s where symbol='%s' and date='%s'"%(table_name,self.symbol,date)
        try:
            data=self.cursor.execute(sql).fetchall()
        except:
            self.conn.close()
        return data
#symbol text ,Date text, Open real,High real ,Low real,Close real,Volume integer, #Adj_close real
   # def update(self):
        

    #def delete(self):
        
    
    #def save(self):


    
class MarketOrderRepository(Repository):
    """
    MarketOrderRepository
    It is used to manipulate market order

    Attr:
       database: 
    """
    ACCOUNT = "account"
    ACCOUNTITEM = "accountitem"
    MARKETORDER="marketorder"
    MARKETORDERITEM="marketorderitem"
    def __init__(self,database):
        self.database=database
        try:
            self.conn=sqlite3.connect(self.database)
            self.cursor=self.conn.cursor()
            
        except:
            self.conn.close()
    def create(self, order):
        """
        Create a market order

        Parameters:
           order: market order
        
        Example:
        >>> from dataLogic.repository import *
        >>> mr = MarketOrderRepository()
        >>> order = MarketOrder('xxb', '20:08:00', 'arbitrage')
        >>> order.addOrderItem('AAPL', 20.0, 300)
        >>> order.addOrderItem('QY', 10.0, -400)
        >>> mr.create(order)
        >>> mr.save()
        """
        try:
            insertOrder = "insert into %s values('%s','%s','%s','%s');" %(self.MARKETORDER, str(order.oid), str(order.uid), str(order.timestamp),  str(order.strategy))
            for item in order.items:
                insertItems = "insert into %s values('%s', '%s', '%s', %f,%d);" %(self.MARKETORDERITEM, item.id, item.oid, item.symbol, item.price, item.num)
                self.cursor.execute(insertItems)
                self.conn.commit()
            self.cursor.execute(insertOrder)
            self.conn.commit()
        except:
            #self.conn.close()
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
            getorder = """select * from %s where oid = '%s';""" %(self.MARKETORDER, oid)
            getitems = """select * from %s where oid = '%s';""" %(self.MARKETORDERITEM, oid)

            orderRecord = self.cursor.execute(getorder).fetchone()
            itemsRecord = self.cursor.execute(getitems).fetchall()
            orderItems = []
            for item in itemsRecord:
                orderitem = MarketOrderItem(item[0], item[1], item[2], item[3], item[4])
                orderItems.append(orderitem)
            order = MarketOrder(orderRecord[0], orderRecord[1], orderRecord[2], orderRecord[3], orderItems)
            #self.conn.close()
            return order
        except:
            #self.conn.close()
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
    ACCOUNT = "account"
    ACCOUNTITEM = "accountitem"
    MARKETORDER="marketorder"
    MARKETORDERITEM="marketorderitem"
    def __init__(self,database):
        try:
            self.conn=sqlite3.connect(database)
            self.cursor=self.conn.cursor()
        except:
            self.conn.close()
    def flag(self,uid):
        sql="select * from %s where uid='%s';"%(self.TABLE,uid)
        try:
            if len(self.cursor.execute(sql).fetchall())==0:
                return True
            else:
                return False
        except:
            return
    def create(self,account):
        """
        Create a Account
       Account（uid, passwd, items）
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
        #self.account=account
        if self.flag(account.uid):
            sql="insert into %s values('%s','%s');"%(self.ACCOUNT,account.uid,account.passwd)
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except:
                return

    def update(self, account):
        self.passwd = account.passwd
        

    def delete(self, account):
        if not self.flag(account.uid):
            try:
                ###delete table marketorderitem
                sql="delete from %s where oid in (select oid from %s where uid='%s');"%(self.MARKETORDERITEM,self.MARKETORDER,account.uid)
                self.cursor.execute(sql)
                self.conn.commit()
                ###delete table marketorder
                sql="delete from %s where uid='%s';"%s(self.MARKETORDER,account.uid)
                self.cursor.execute(sql)
                self.conn.commit()
                ##delete the accountitem
                sql="delete from %s where uid='%s';"%s(self.ACCOUNTITEM,account.uid)
                self.cursor.execute(sql)
                self.conn.commit()
                ##delete the account
                sql="delete from %s where uid='%s';"%s(self.ACCOUNT,account.uid)
                self.cursor.execute(sql)
                self.conn.commit()
            except:
                return
                
        

    def read(self, uid):
        pass

    def save(self):
        if hasattr(self.conn,'close'):
           self.conn.close()
        

    def updateaccount(self,uid):
        if not self.flag(uid):
               sql="select distinct symbol from %s t1 join %s t2 on t1.oid=t2.oid where uid='%s' ;"%(self.MARKETORDER,self.MARKETORDERITEM,uid)
               try:
                   symbols=self.cursor.execute(sql).fetchall()
                   if len(symbols)>0:
                ##convert the tumple to list
                       symbols=[symbol[0] for symbol in symbols]
                   else:
                        print("Update the symbol cost error,the marketorder is empty\n")
                        return
                   for symbol in symbols:
                        sql="select t1.timestamp,t2.price,t2.num,t1.strategy from %s t1 join %s t2 on t1.oid=t2.oid where t1.uid='%s' and symbol='%s'"%(self.MARKETORDER,self.MARKETORDERITEM,uid,symbol)
                        data=self.cursor.execute(sql).fetchall()
                        if len(data)>0:
                           data=[list(da) for da in data]
                           avgcost=cumpute(data)
                           num=0
                           for i in range(len(data)):
                                num+=int(data[i][2])
                           accountitem=AccountItem(uid, symbol, avgcost, num) 
                       #self.accountitem=AccountItem(uid, symbol, avgcost, num)
                       ###update the data in database
                           sql="select symbol from %s where symbol='%' and uid='%s';"%(self.ACCOUNTITEM,accountitem.symbol,accountitem.uid)
                           if len(self.cursor.execute(sql))>0:
                              sql="update %s  set avgcost=%f and num=%d where symbol='%s' and uid ='%s';"%(self.ACCOUNTITEM,accountitem.avgcost,accountitem.num,accountitem.symbol,accountitem.uid)
                              self.cursor.execute(sql)
                              self.conn.commit()
                           else:
                               ##uid varchar, symbol varchar, avgcost real, num int
                              sql="insert into %s values('%s','%s',%f,%d);"%(self.ACCOUNTITEM,accountitem.uid,accountitem.symbol,accountitem.avgcost,accountitem.num)
                              self.cursor.execute(sql)
                              self.conn.commit()
               except:
                   return
        

    
    
