from dataLogic.repository import *
class load:
    def __init__(self):
         self.name=name().name
    def create(self):
         x=init_table()
         x.create_table()
         x.save()
    def load(self,begin,to,period="day"):
        for i in range(begin,to):
            repositorys=Repository(self.name[i])
            repositorys.create('2001-01-01','2015-03-30',period)
            repositorys.save()
        return(True)
