#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:08:48 2020

@author: parsaahani
"""

# besmellah
meghdar_nahaii = 0
asghar = 0

from Person import person
from Card import Card
import random
import os
import sys


def check_howmuch_bet(bet_price_check):
    if (int(bet_price_check) > int(Person_1.balance) or int(bet_price_check) > int(Person_2.balance)):
        
        print ("DAII ZIADE , ZIADE ...\n")
        howmuch_bet(input("DADA CHEGHAD MIKHAY BET KONI BA MA ?\n"))
    else:
       # print("megdhare nahaii " + str(bet_price))
       # meghdar_nahaii = bet_price
        global asghar
        asghar = bet_price_check
        return bet_price_check
    
        

def howmuch_bet(bet_price):
    meghdar_nahai = check_howmuch_bet(bet_price)
    #print("megdhare nahaii " + str(meghdar_nahai))
    return meghdar_nahai

        
 
def play_game():
    howmuch_bet(input("DADA CHEGHAD MIKHAY BET KONI BA MA ?\n"))
    card = Card()
    ## barge gerefaten bazikone aval 
    while(int(input("barge mikhay "+Person_1.name+"?\n"))):
        Person_1.meghdar = Person_1.meghdar + int(card.get_barge())
        if(Person_1.meghdar > 21):
            print("POKIDI BABA")
            print(Person_2.name + " BORDI")
            play_game()
            break
            
            
        else:    
            print("jamet ta alan shode = " + str(Person_1.meghdar))
            
    while(int(input("barge mikhay "+Person_2.name+"?\n"))):
        Person_2.meghdar = Person_2.meghdar + int(card.get_barge())
        if(Person_2.meghdar > 21):
            print("POKIDI BABA")
            print(Person_1.name + " BORDI")
            play_game()
            break
            
            
        else:    
            print("jamet ta alan shode = " + str(Person_2.meghdar))
            
            
            
    if(Person_1.meghdar > Person_2.meghdar   ):
        print(Person_1.name+" BORDIIIIIIII")
            
    else:
        print(Person_2.name+" BORDIIIIIIII")   
            



Person_1 = person(input("HI \nWHAT IS YOUR NAME ?\n"), int(input("AND HOW MUCH IS YOUR BALANCE\n")))
Person_2 = person(input("HI \nWHAT IS YOUR NAME ?\n"), int(input("AND HOW MUCH IS YOUR BALANCE\n")))

print ("WELCOME TO OUR GAME "+Person_1.name + " AND " + Person_2.name )

howmuch_bet(input("DADA CHEGHAD MIKHAY BET KONI BA MA ?\n"))

card = Card()
## barge gerefaten bazikone aval 
while(int(input("barge mikhay "+Person_1.name+"?\n"))):
    Person_1.meghdar = Person_1.meghdar + int(card.get_barge())
    if(Person_1.meghdar > 21):
        print("POKIDI BABA")
        print(Person_2.name + " BORDI")
        Person_2.balance = int(Person_2.balance) + asghar
        asghar = 0 
        if(input("mikhay dobare bazi koni??\n")):
            play_game()
            break
        
        
    else:    
        print("jamet ta alan shode = " + str(Person_1.meghdar))
        
while(int(input("barge mikhay "+Person_2.name+"?\n"))):
    Person_2.meghdar = Person_2.meghdar + int(card.get_barge())
    if(Person_2.meghdar > 21):
        print("POKIDI BABA")
        print(Person_1.name + " BORDI")
        Person_1.balance = int(Person_1.balance) + asghar
        asghar = 0 
        if(input("mikhay dobare bazi koni??\n")):
            play_game()
            break
        
        
    else:    
        print("jamet ta alan shode = " + str(Person_2.meghdar))
        
        
        
if(Person_1.meghdar > Person_2.meghdar   ):
    print(Person_1.name+" BORDIIIIIIII")
    Person_1.balance = int(Person_1.balance) + asghar
    asghar = 0 
        
else:
    print(Person_2.name+" BORDIIIIIIII")  
    Person_2.balance = int(Person_2.balance) + asghar
    asghar = 0 
    
    

     
    

