#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 04:39:02 2018

@author: davidlobe
"""

##Odd or even challenge

num = int(input("Enter a number: "))

if num % 4 == 0:
    print(num, " is a multiple of 4")

if num%2 == 0:
    print(num, " is an even number")
    
else:
    print(num, " is a odd  number")