

class DataManager(object):

    def create():
        pass
    
    def update():
        pass

    def delete():
        pass



def DataManagerInstance():
    global gdataManager
    try:
        gdataManager
    except:
        gdataManager = DataManager()
    return gdataManager

