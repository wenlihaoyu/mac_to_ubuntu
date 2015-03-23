

class DataManager(object):

    def create(self):
        pass
    
    def update(self):
        pass

    def delete(self):
        pass


class StockDataManager(DataManager):

    def create(self, symbol, name, market, comment):
        pass

    def update(self, symbol, period, from, to=None, dataset=None):
        pass

    def delete(self, symbol):
        pass
    
    



def DataManagerInstance(instance):
    global gdataManager
    try:
        gdataManager
    except:
        if instance == 'stock':
            gdataManager = StockDataManager()
    return gdataManager

