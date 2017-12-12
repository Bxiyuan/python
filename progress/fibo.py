# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:19:30 2017

@author: dell
"""

def fib(n):
    a,b=0,1
    while b<n:
        print(b,end=",")
        a,b=b,a+b
    print()
    
def fib2(n):
    result=[]
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result