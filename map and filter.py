# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 21:42:38 2016

@author: YI
"""

#the usage of map and lambda
items = [1,2,3,4,5]
square= list(map(lambda x: x**2, items)) #elements in the list are x

#a list of functions
def multiply(x):
    return x*x
    
def add(x):
    return x+x

functions = [multiply, add]

for i in xrange(10):
    values = list(map(lambda x: x(i), functions))
    print values

#the usage of filter
numbers = range(-5,5)

negative = list(filter(lambda x: x<0, numbers))

print negative






