#! /usr/bin/env python

def primo(f):
    i=2
    sw=0
    while i<=(f-1):
        comp=f%i
        if comp==0:
            sw=1
            return 0
            break
            
        i+=1
        
    if sw==0:
        return 1
        
    
    
