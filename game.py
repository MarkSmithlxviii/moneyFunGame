# -*- coding: utf-8 -*-
"""
A game for learning about coins.  
Provides a dollar and cents and a number of coins to make the value.
 
Created on Wed Aug 31 04:05:25 2016

@author: marka
"""

import random

toonie=0
loonie=0
quarter=0
dime=0
nickle=0
penny=0
atoonie = 0
aloonie = 0
aquarter =0
adime = 0
anickle = 0
apenny = 0
coinCheck = (toonie, loonie, quarter, dime, nickle, penny)
coinName = ('Toonies', 'Loonies', 'Quarters', 'Dimes', 'Nickles', 'Pennys')
answercheck = (atoonie, aloonie, aquarter, adime, anickle, apenny)

toonie = round(random.random())
loonie = round(2*random.random())
quarter = round(3*random.random())
dime = round(2*random.random())
nickle = round(random.random())
penny = round(4*random.random())

total = round(2*toonie + loonie + quarter/4 + dime/10 + nickle/20 + penny/100, 2)
coins = round(toonie + loonie + quarter + dime + nickle + penny)

print('Hi Jessie how are you today')
print('Can you find {0} coins that add up to {1:.2f}'.format(coins, total))

input('Press enter when you are ready to tell me what the coins are?')

atoonie = int(input('How many Toonies?'))
aloonie = int(input('How many Loonies?'))
aquarter = int(input('How many Quarters?'))
adime = int(input('How many Dimes?'))
anickle = int(input('How many Nickles?'))
apenny = int(input('How many Pennies?'))


usercontinue = input('That was great thanks for playing, would you like to check your answer? (y for yes)')
print (coinCheck, answercheck)
index = -1

if usercontinue == 'y':
    for coin in coinCheck:
        index += 1
        if coin != answercheck[index]:
            print ('There were actually {0} {1}'.format(coin, coinName[index]))
        else:
            print('{0} are correct'.format(coinName[index]))
