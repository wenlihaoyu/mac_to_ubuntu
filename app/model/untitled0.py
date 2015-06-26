# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:33:42 2015

@author: lywen
"""
from dataLogic.loading import *
from dataLogic.repository import *
from init.initagent import *
from model.account import *
### load the stock data from yahoo
class simulation:
    def __init__(self,database='db/finance.db'):
        self.database=database
    def initilation(self,begin="2000-01-01",to="2015-04-01",period="day"):
        initial=init(self.database)
        initial.create_table()
        initial.load_data(begin,to,period)
    def userJion(self,users):
        ###create account
        account=Account(users)
        accountrepository=AccountRepository(self.database)
        accountrepository.create(account)
        accountrepository.save()
    def simulation(self):
        