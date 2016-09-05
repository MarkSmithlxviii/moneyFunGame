# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:51:32 2016

@author: marka
"""
import random

coinNames = ('Toonie', 'Loonies', 'Quarters', 'Dimes', 'Nickles', 'Pennys')
questionCoins ={}
for name in coinNames:
    questionCoins [name] = round(2*random.random())
print (questionCoins)    