
class Account:
    def __init__(self, uid, passwd, items=None):
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
        self.avgcost=avgcost
    def __str__(self):
        return "User id: %s\nSymbol: %s\nAverage Cost: \s\nNum: %s\n" %(self.uid, self.symbol, self.avgcost, self.num)
def cumpute(data):
    i=0
    j=0
    m_average=0
    m_total=0
    m_data=data
    while (i<=len(m_data)-1 and j<=len(m_data)-1):
        ## find the next lable is buy
        while m_data[i][3]=="sell" and i<=len(m_data)-1:
            i+=1
            if i==len(m_data):
                break
        ## find the next lable is sell
        while m_data[j][3]=="buy" and j<=len(m_data)-1:
            j+=1
            if j==len(m_data):
                break
        if i <len(m_data) and j< len(m_data):
            if m_data[i][2]>m_data[j][2]:
                m_average+=m_data[j][2]*(m_data[j][1]-m_data[i][1])
                m_total+=m_data[j][2]
                m_data[i][2]-=m_data[j][2]
                j+=1
            
            elif m_data[i][2]<m_data[j][2]:
                m_average+=m_data[i][2]*(m_data[j][1]-m_data[i][1])
                m_total+=m_data[i][2]
                m_data[j][2]-=m_data[i][2]
                i+=1
            else:
                m_average+=m_data[i][2]*(m_data[j][1]-m_data[i][1])
                m_total+=m_data[i][2]
                i+=1
                j+=1
    #print m_average
    #print m_total
    return  m_average/1.0/m_total