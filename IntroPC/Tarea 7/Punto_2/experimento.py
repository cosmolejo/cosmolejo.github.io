#!/usr/bin/env python 
import matplotlib.pyplot as plt
from numpy import *
plt.close("all")


datos=loadtxt("experimento.dat")
x=datos[:,0]
y=datos[:,1]
plt.grid(True)


xlin=linspace(0.0,1.2)

exp=plt.plot(x,y,'+',color='r',markersize=5)
linea=plt.plot(xlin,9.8*xlin+0.5,'-',color='b')
plt.text(0.6211,5.10204,"v(t)=9.8t + vo",fontsize=14)

plt.xlabel("t (segundos)")
plt.ylabel("v(m/s)")
plt.title("Datos experimento de caida libre")


plt.savefig("experimento_py.png")
plt.show()
