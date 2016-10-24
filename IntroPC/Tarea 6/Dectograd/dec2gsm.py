#! /usr/bin/env python  
import math
def dec2gsm(dec):
    
    grad= math.floor(dec)
    decimal=dec-grad
    g=grad
    a=decimal*60
    m=math.floor(a)
    b=a-m
    c=b*60
    s=c
    return g,m,s
