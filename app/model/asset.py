class asset(object):
    pass

class basicAsset(asset):

    def getOCHL(self, date):
        pass
    
    def getClose(self, date):
        pass

    def getOpen(self, date):
        pass

    def getHigh(self, date):
        pass

    def getLow(self, date):
        pass

class stock(basicAsset):
    pass


class future(basicAsset):
    pass


class option(basicAsset):
    pass

