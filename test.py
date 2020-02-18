# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:45:26 2020

@author: toztel17
"""

import unittest
import Portfolio
#import Stock
#import MutualFund

class PortfolioTest(unittest.TestCase):
    def test_addCash(self):
        p = Portfolio.Portfolio()
        cash = p.cash
        self.assertEqual(p.addCash(10),cash+10)     # check if adds cash correctly
        
    def test_withdrawCash(self):
        p = Portfolio.Portfolio()
        cash = p.addCash(10) #add cash to the portfolio for test
        p.withdrawCash(3)
        cash_left = p.cash
        self.assertEqual(cash_left,cash-3) # check if withdraws cash correctly
        self.assertNotEqual(p.withdrawCash(3),cash) # check if withdraws cash correctly
         
    def test_sellStock(self):
        
        p = Portfolio.Portfolio()
        initial_cash = p.addCash(3000)
        s = Portfolio.Stock(20,"HFH") #making up an arbitrary stock of HFH
        p.buyStock(15,s) #we bought some stock
        initial_stock = p.stock_dict[s.s_symbol]
        p.sellStock("HFH",5) #we sell some of our stock
        decreased_stock = p.stock_dict[s.s_symbol]
        increased_cash = p.cash #cash should increase because we sold stuff..
        
        self.assertNotEqual(initial_cash, increased_cash) # increased vs initial cash should not be equal
        self.assertNotEqual(initial_stock, decreased_stock) # increased vs initial stock should not be equal

        
    def test_buyStock(self):
        
        p = Portfolio.Portfolio()
        initial_cash = p.addCash(3000) #amount of cash to add is arbitrarily chosen
        s = Portfolio.Stock(20,"HFH") #making up an arbitrary stock of HFH
        initial_stock = len(p.stock_dict) #ask if a key exists in the dictionary
        p.buyStock(5,s) #we bought stock
        increased_stock = p.stock_dict[s.s_symbol] #stock should increase here
        decreased_cash = p.cash # cash should decrease
        
        self.assertNotEqual(initial_cash,decreased_cash) #decreased vs initial cash should not be equal
        self.assertNotEqual(initial_stock, increased_stock) #increased vs initial cash should not be equal
        self.assertEqual(initial_stock, increased_stock -5)

        
    def test_sellMutualFund(self):
    
        p = Portfolio.Portfolio()
        initial_cash = p.addCash(3000) # we add cash
        mf = Portfolio.MutualFund("BRT") #making up an arbitrary stock of HFH
        p.buyMutualFund(15.2,mf) #we bought some stock
        initial_mf = p.mf_dict[mf.mf_symbol] 
        p.sellMutualFund("BRT",5)
        decreased_mf = p.mf_dict[mf.mf_symbol]
        increased_cash = p.cash
        
        self.assertNotEqual(initial_cash, increased_cash)#increased vs initial cash should not be equal
        self.assertNotEqual(initial_mf, decreased_mf)#increased vs initial mf should not be equal
        self.assertEqual(initial_mf, decreased_mf + 5)
        
    def test_buyMutualFund(self):
    
        p = Portfolio.Portfolio()
        initial_cash = p.addCash(3000) #amount of cash to add is arbitrarily chosen
        mf = Portfolio.MutualFund("BRT") #making up an arbitrary stock of HFH
        initial_mf = len(p.mf_dict)
        p.buyMutualFund(5.2,mf)
        increased_mf = p.mf_dict[mf.mf_symbol]
        decreased_cash = p.cash
        
        self.assertNotEqual(initial_cash,decreased_cash)#increased vs initial cash should not be equal
        self.assertNotEqual(initial_mf, increased_mf)#increased vs initial cash should not be equal
        self.assertEqual(initial_mf, increased_mf -5.2)
    
    
if __name__ == '__main__':
  unittest.main()