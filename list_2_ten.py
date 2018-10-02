#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 05:06:23 2018

@author: davidlobe
"""

#List less than 10 create a sublist of numbers less than or equal 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

s = []

for x in a:
    if x <= 5:
        s.append(x)
        
print(s)

        
