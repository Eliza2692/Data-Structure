#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:04:04 2019

@author: elizabethalarcon
"""
def factorial (n):
    if n<=1:
        return 1
    
    return n * factorial(n-1)

def factorial2(n):
    if n<=1 :
        return 1
    factorial = 1
    for i in range (1,n+1):
        factorial *=i
    return factorial

print (factorial(5))
print (factorial2(5))

def fibonacci(n):
    if n==0:
        return 0
    elif n== 1: 
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def fibonacci2(n):
    a=0
    b=1
    for i in range(n):
        a,b = b,a+b
    return a

print (fibonacci(10))
print (fibonacci2(10))


def reverseString(s):
    if len(s)<=1:
        return s
    return reverseString(s[1:])+s[0]

print (reverseString('yoyo mastery'))
    
    
    
