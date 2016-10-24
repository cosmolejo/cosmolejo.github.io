#!/usr/bin/env python 
import matplotlib.pyplot as plt
from numpy import *
plt.close("all")

x=linspace(-4*pi,4*pi)

seno=plt.plot(x,sin(x)/x)
plt.setp(seno,color='r')
plt.setp(seno,linewidth=3)
plt.setp(seno,linestyle='--')


plt.xlim((-10,10))
plt.ylim((-1.1,1.1))


plt.savefig("seno_py.png")
plt.show()
