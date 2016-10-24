#! /usr/bin/env python

def Fperfecto(num):
    i=1
    suma=0
    while i<=(num-1):
        cond=num%i
        if cond == 0:
            suma+=i
        i=i+1   				 
        
    if (suma==num):
        return 1 
        
    else:
        return 0
    
