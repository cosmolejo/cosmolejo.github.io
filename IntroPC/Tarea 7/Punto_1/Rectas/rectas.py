#!/usr/bin/env python 
import matplotlib.pyplot as plt
from numpy import *
plt.close("all")

x=linspace(-10,10)

r1=plt.plot(x,2*x+1)
r2=plt.plot(x,3*x+1)
r3=plt.plot(x,4*x+1)




plt.savefig("rectas_py.png")
plt.show()
