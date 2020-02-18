# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 13:47:24 2020

@author: toztel17
"""

 # HOMEWORK 1 INTL550
import numpy
class Portfolio:
    def __init__(self):
        self.cash = 0 #we store cash here
        self.mf_dict = {} #mutual funds dictionary: we store the mf symbol and the amount of mf here
        self.stock_dict = {} #stock dictionary: we store the stock symbol and stock amount here
        self.stock_price = {} #stock price
        self.transHistory = [] #transaction history
        
    def __repr__(self): #print(portfolio) will print the portfolio info.
        
        s_info = [] 
        mf_info = []
        
        s_keys = list(self.stock_dict.keys())
        mf_keys = list(self.mf_dict.keys())
        
        for item in range(0,len(s_keys)):
            s_info.append(str(self.stock_dict[s_keys[item]])+' ' +s_keys[item])
            
        for item in range(0,len(mf_keys)):
            mf_info.append(str(self.mf_dict[mf_keys[item]])+' ' + mf_keys[item])
        return ('cash: $' +str(self.cash) + '\nstock: '+ str(s_info) + '\nmutual funds: ' + str(mf_info))
           
        
    def addCash(self,x): 
        if type(x) == str: #check if input arg is an integer
            raise TypeError('Cash input should be a numerical value')
        else:
            self.cash = self.cash + x #add x amount of cash to the existing cash
            self.transHistory.append('$'  + str(x)+ ' ' + 'amount of cash is added') #create transaction history
        return self.cash
    def withdrawCash (self, amount):
        if type(amount) == str: #check if input arg is an integer
            raise TypeError('Cash input should be a numerical value')
        else:
            if amount <= self.cash: # if the amount is smaller than the existing cash, then withdraw that amount successfully
                self.cash = self.cash - amount
                self.transHistory.append('$' + str(amount)  + ' ' +  'amount of cash is withdrawn')
            else: # if there is not enough amount of money in the cash, raise error
                raise Exception('Not enough cash in the portfolio to withdraw! Sell some of your stock or mutual fund or add at least' + ' ' + '$' + str(amount-self.cash) + ' ' + 'of cash to the portfolio')
    
    
    def buyStock(self,s_share,s_stock): #s_Share should be integer, s_stock should be a stock
        if type(s_share) != int: #check if the input is provided in a correct type
            raise TypeError('Share amount should be provided in integer.') 
        else:
            if s_share != int(s_share): #check if share is in fraction unit. if so,raise error
                raise Exception('Share input can not be in fraction unit while purchasing a stock')
            else:
                if s_stock.price <= self.cash: # if we have enough money to buy that stock, put the stock symbol and amount of stock in the stock dictionary
                    sym_var = s_stock.s_symbol
                    if sym_var in self.stock_dict: #if we already have that stock symbol, then increase its amount in the dictionary
                       self.stock_dict[sym_var] = self.stock_dict[sym_var] + s_share
                    else:
                        self.stock_dict[sym_var] = s_share
                    self.cash = self.cash-(s_share*s_stock.price) #after all, we spent money buy buying something. our money should decrease as the amount of stock we bought multiplied by its price 
                    self.stock_price['stock_price'] = s_stock.price 
                    self.transHistory.append(str(s_share) + sym_var + ' ' + 'shares of stock is bought for $' + str(s_stock.price)) #create transaction history for this operation
                else: # if we dont have money in the cash to afford the stock, raise error
                    raise Exception('Not enough cash in the portfolio! Sell some of your stock or mutual fund or add at least' + ' ' + '$' + str(s_stock.price-self.cash) + 'of cash to the portfolio')
    
    def sellStock(self,s_symbol,s_share):
        if type(s_symbol) != str or type(s_share) != int: #check if the input args are provided in correct types
            raise TypeError('Either of the input arguments is not provided in correct type:\n<s_symbol> should be string, <s_share> should be integer')
        else:
            if self.stock_dict[s_symbol] < s_share: #if we do not have enough stock in the portfolio, we cant sell it
                raise Exception('Not enough product in the stock!')
            else:
                coeff_mult = self.stock_price['stock_price'] 
                self.stock_rand_price = numpy.random.uniform(low=0.5*coeff_mult, high=1.5*coeff_mult, size=None) # draw a random value from a uniform distribution and specify the stock price boundaries
                self.cash = self.cash + self.stock_rand_price # we sold, so it should add to our cash
                self.stock_dict[s_symbol] = self.stock_dict[s_symbol] - s_share #we sold, so our stock should decrease
                self.transHistory.append(str(s_share) + s_symbol + ' ' + 'shares of stock is sold for $' + str(self.stock_rand_price)) #transaction history for this operation
            
            
    def buyMutualFund(self,mf_share,mf_symbol):
        if type(mf_share) != float: #check the inout argument type
            raise TypeError('Share input should be provided in float type')
        else:
            if mf_share == int(mf_share): #check if the share is given as a fraction. if the input is in fraction type, then do the following operations
                raise Exception('Share input can not be in whole unit while purchasing a mutual fund')
            else:
                if mf_share <= self.cash: #since the price of mf is amount of mf * 1, we check if we have enough amount in the cash by asking if the wanted share is smaller than the existing cash. if we have enough money, we can go on
                    mf_sym_var = mf_symbol.mf_symbol
                    if mf_sym_var in self.mf_dict: #if we already have that mf, we should add the amount on it
                       self.mf_dict[mf_sym_var] = self.mf_dict[mf_sym_var] + mf_share
                    else:
                       self.mf_dict[mf_sym_var] = mf_share #store in the mf dictionary
                    self.cash = self.cash-(mf_share*1) #we decrease the cash by the amount of mf we bough since the price of mf is 1$ per mf
                    self.transHistory.append(str(mf_share) + mf_symbol.mf_symbol + ' ' + 'shares of mutual fund is bought for $' +str(mf_share)) #transaction history for this operation
                else:
                    raise Exception('Not enough cash in the portfolio! Sell some of your stock or mutual fund or add at least' + ' ' + '$' + str(mf_share-self.cash) + ' ' +'of cash to the portfolio') # if we do not have enough money, it will warn us

    def sellMutualFund(self,mf_symbol,mf_share):
        if type(mf_symbol) != str or type(mf_share) != int: # check if input args are provided in correct type
            raise TypeError('Either of the input arguments is not provided in correct type:\n<mf_symbol> should be string, <mf_share> should be integer')
        else:
            if self.mf_dict[mf_symbol] < mf_share: #check if we have enough mf in the portfolio (e.g., we have, say, 10 BRT of mf but do we have enough HTF (or smth.. which is asked to be bought))
                raise Exception('Not enough product in the mutual fund!')
            else:
                self.mf_rand_price = numpy.random.uniform(low=0.9, high=1.2, size=None)
                self.cash = self.cash + self.mf_rand_price #if we sell, we earn money. so add that money to the cash
                self.mf_dict[mf_symbol] = self.mf_dict[mf_symbol] - mf_share # we decrease in that type of mf in our portfolio
                self.transHistory.append(str(mf_share) + mf_symbol + ' ' + 'shares of mutual fund is sold for $' + str(self.mf_rand_price)) #transaction history for this operation
                
    def history(self): #print the transaction history
        for item in range(0,len(self.transHistory)):
            print ('Transaction' + ' ' + str(item+1)+ ':' + ' ' +self.transHistory[item])



class Stock: #create a stock
    def __init__(self,price,s_symbol):
        if type(price) != int or type(s_symbol) != str: # check if input args are provided in correct type
            raise TypeError('Either of the input arguments is not provided in correct type:\nPrice should be integer, <s_symbol> should be string')
        else:
            self.price = price #stock price
            self.s_symbol = s_symbol #stock symbol
class MutualFund: #the price of the mutual fund is 1 $ for each share
    def __init__(self,mf_symbol):
        if type(mf_symbol) != str: #check if input arg is provided in a correct type
            raise TypeError('Input should be provided in string type')
        else:
            self.mf_symbol = mf_symbol # mf symbol
            self.mf_price = 1 #mf price
        
        
