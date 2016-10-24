#! /usr/bin/env python

def gms2dec(g,m,s):
    sdec=(s/3600);
    mdec=(m/60);
    gdec=sdec+mdec+g;
    
    return gdec
