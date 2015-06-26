# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:45:32 2015

@author: lywen
"""
from dataLogic.repository import *
import urllib.request as request
import re
import csv
class upload:
    def __init__(self,filename):
           url='http://quote.eastmoney.com/stocklist.html'
           self.symbols=[ i[0].replace('sh','ss') for i in get_symbol(url_get(url))]
           self.filename=filename
           self.notsymbol=[]
    def open(self):
           self.csvfile=open(self.filename,'a')
           self.writer=csv.writer(self.csvfile)
    def initial(self):
           self.write([['date','open','high','low','close','volume','adj_close','symbol']])
    def upload(self,begin,to):
        tick=to-begin
        for i in range(begin,to):
            ##(self,symbol='600000.ss',begin='2011-01-01',to='2012-01-01',period='day')
            try:            
               stocks=stock(symbol=self.symbols[i],begin='1990-01-01',to='2015-06-10',period='day')
               stocks.search_from_url()
               x=[da.append(self.symbols[i]) for da in stocks.data]
               self.write(stocks.data)
               print("symbol:%s ;长度：%d ;完成率：%.2f%%"%(self.symbols[i],len(stocks.data),(i-begin+1)/tick*100))
            except:
                print('%s failure\n'%self.symbols[i])
                self.notsymbol.append(self.symbols[i])
                continue
    def write(self,data):
            self.open()
            self.writer.writerows(data)
            self.save()
    def save(self):    
        self.csvfile.close()
        
        

 ##判断网页是否存在
def url_Exists(url):
     try:
         request.urlopen(url)
         return True
     except:
         return False
         
def url_get(url):
    ##http://quote.eastmoney.com/stocklist.html
    codes=['ASCII','UTF-8','GBK','GB2312']
    if url_Exists(url):
       s=request.urlopen(url).read()
       for code in codes:
           try:
              return s.decode(code)
           except:
               continue  
    else:
         return None
def str_index(S,s1,s2):
    if(S.find(s1)>=0):
        if(S.find(s2)>=S.find(s1)):
            return [S.find(s1),S.find(s2)]
            return [-1,-1]
    else:
        return [-1,-1]
        
def get_symbol(S):
    symbol=[];
    s1='<li><a target="_blank" href="http://quote.eastmoney.com/'
    s2='</a></li>'
    str_symbol=re.findall(s1+'(.*)'+s2,S)
    symbol=[[i.split('.html')[0],(i.split('>')[1]).split('(')[0]] for i in str_symbol]
    symbol=[[i[0][2:]+'.'+i[0][0:2],i[1]] for i in symbol]    
    return symbol
         

