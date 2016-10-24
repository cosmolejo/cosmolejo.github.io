# /usr/bin/env python

import Fperfecto

num=input("ingrese el numero limite para caulcular numeros perfectos: ")
sw=0
i=num
while i>=1:
    perf=Fperfecto.Fperfecto(i)
   
    if perf == 1:
        sw=1
        print"numero perfecto inferior a %d: %d \n"%(num,i)
          
    i=i-1
if sw==0:
    print"no existen numeros perfectos inferiores al numero %d \n"%(num)
    
