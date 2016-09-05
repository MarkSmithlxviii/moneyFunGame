# -*- coding: utf-8 -*-
"""
A game for learning about coins.  
Provides a dollar and cents and a number of coins to make the value.
 
Created on Wed Aug 31 04:05:25 2016

@author: marka
"""

import random

coins = 0
value = 0
coinName = ('Toonies', 'Loonies', 'Quarters', 'Dimes', 'Nickles', 'Pennies')
coinValue = {'Toonies': 2, 'Loonies' : 1, 'Quarters' : 0.25, 'Dimes' : 0.1, 'Nickles' : 0.05, 'Pennies' : 0.01}


questionCoin = {}
for name in coinName:
    questionCoin [name] = round(2*random.random())   
for name in coinName:
    coins = coins + questionCoin[name]
for name in coinName:
    value = value + questionCoin[name] * coinValue[name]    
    
print('Hi Jessie how are you today')
print('Can you find {0} coins that add up to {1:.2f}'.format(coins, value))

input('Press enter when you are ready to tell me what the coins are?')

answerCoin = {}
for name in coinName:
    answerCoin[name] = int(input('How many {0} '.format(name)))

usercontinue = input('That was great thanks for playing, would you like to check your answer? (y for yes) ')

for name in coinName:
    if questionCoin[name] == answerCoin[name]:
        print('{0} {1} is correct'.format(questionCoin[name], name))
    else:
        print('{0} {1} was the correct answer'.format(questionCoin[name], name))