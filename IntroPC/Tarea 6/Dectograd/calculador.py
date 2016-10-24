#! /usr/bin/env python 

import math
import dec2gsm
print" %-20s %-20s %-20s %-20s\n"%("cos(x)","x en radianes","x en grados","x en gsm")
i=0.0
while i<=1 :

    rad=math.acos(i)
    grad=(rad*180)/math.pi
    g,m,s=dec2gsm.dec2gsm(grad)
    print" %-20lf %-20lf %-20lf %-1.0lfg%.0lfm%.0lfs\n"%(i,rad,grad,g,m,s)
    i=i+0.1
    
    
