#! /usr/bin/env python
def rutpi(n):
    pi=1.0
    i=n
    while i>0:
        pi=2.0+(2*i+1)*(2*i+1)/pi
        i=i-1
    pi=1.0/pi
    pi=pi+1.0
    pi=4.0/pi
    return pi
