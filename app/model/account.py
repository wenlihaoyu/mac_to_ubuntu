
class Account:
    def __init__(self, uid, passwd, items):
        self.uid = uid
        self.passwd = passwd
        self.items = items
        
    def __str__(self):
        string = "User id: %s\nSymbol: %s\n" %(self.uid, self.name)
        for item in self.items:
            string += item.__str__()
        return string

class AccountItem:
    def __init__(self, uid, symbol, avgcost, num):
        self.uid = uid
        self.symbol = symbol
        self.num = num
        
    def __str__(self):
        return "User id: %s\nSymbol: %s\nAverage Cost: \s\nNum: %s\n" %(self.uid, self.symbol, self.avgcost, self.num)
