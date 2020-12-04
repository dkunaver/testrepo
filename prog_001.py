# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:14:46 2020

@author: dkuna
"""

def mult_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result   

print (mult_add(4, 5, 10, 4))
