from dataLogic.repository import *
import sqlite3
## hasattr(conn,'open')
class load:
    def __init__(self,database):
         self.name=name().name
         self.database=database
    def load(self,begin,to,period="day"):
        for i in range(begin,to):
            repositorys=Repository(self.name[i],database=database)
            repositorys.create(begin,to,period)
            repositorys.save()
        return(True)
class delete:
    def __init__(self,database):
        self.database=database
        try:
            self.conn=sqlite3.connect(self.database)
            self.cursor=self.conn.cursor()
        except:
            if hasattr(self.conn,'close'):
                self.conn.close()
            return False
    def get_TableName(self):
        sql="select tbl_name from sqlite_master where type='table';"
        try:
          data=self.cursor.execute(sql).fetchall()
          self.table=[tabl[0] for tabl in data]
        except:
            if hasattr(self.conn,'close'):
               self.conn.close()
            return False
    def delete_TableData(self,tblname):
        sql="delete from %s;"%tblname
        try:        
           self.cursor.execute(sql);
           self.conn.commit()
        except:
            if hasattr(self.conn,'close'):
               self.conn.close()
            return False  
    def delete_allTableData(self):
        if hasattr(self,'table'):
            for tabl in self.table:
                self.delete_TableData(tabl)
        else:
            print("The database tables are not exist")
    def save(self):
        if hasattr(self.conn,'close'):
           self.conn.close()