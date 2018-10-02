#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 04:50:58 2018

@author: davidlobe
"""
##### input challenge. Project to create a program that receices user name and age and 
#### tell at what he be 100 years old

name = input("Enter your name: ")

age = int(input("Enter your age: "))

year =  str((2018 - age) + 100)

print(name + " will be 100yrs in "+ year )
