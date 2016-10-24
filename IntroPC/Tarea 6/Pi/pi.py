#! /usr/bin/env python 
import math
import rutinapi
n=input("numero de repeticiones")
t=input("numero de decimales MAXIMO 18: ")
a=math.pow(10,t)
pi=rutinapi.rutpi(n)
pi2=(pi*a)
pi3=pi2/a;
pi2=pi2-(3*a);
print" pi con %ld cifras decimales es: 3.%ld\n"%(t,pi2)
