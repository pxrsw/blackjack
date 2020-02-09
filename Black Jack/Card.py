#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:14:44 2020

@author: parsaahani
"""
import random
class Card():

 
    
    def __init__(self) :
        self.list = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
        self.tool_list = len(self.list)
        
    def get_barge(self):
        
        #print(tool_list)
        self.index = random.randint(0,self.tool_list - 1)
        self.meghdar_barge = self.list[self.index]
        self.list.pop(self.index)
        self.tool_list= self.tool_list-1
        return self.meghdar_barge
        