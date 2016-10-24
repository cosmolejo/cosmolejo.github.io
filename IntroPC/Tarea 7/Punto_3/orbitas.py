#!/usr/bin/env python 
import matplotlib.pyplot as plt
import matplotlib.patches as figuras
from numpy import *
plt.close("all")

fig = plt.figure()

grafica=fig.add_axes([0,0,1,1])
grafica.axhspan(-2,2,color='k')

xmer=[]
ymer=[]
xven=[]
yven=[]
xtie=[]
ytie=[]
xmar=[]
ymar=[]
for f in linspace(0,2*pi,1000):
    #mercurio
    r1= (0.38*(1-(0.206*0.206)))/(1-(0.206*cos(f-262.0)))
    x1 = r1*cos(f-262.0)
    y1 = r1*sin(f-262.0)
    xmer+=[x1]
    ymer+=[y1]
    
    #venus
    r2= (0.723*(1-(0.003*0.003)))/(1-(0.003*cos(f-71.2)))
    x2 = r2*cos(f-71.2)
    y2 = r2*sin(f-71.2)
    xven+=[x2]
    yven+=[y2]
    #tierra
    r3= (1.0*(1-(0.017*0.017)))/(1-(0.017*cos(f-286.0)))
    x3 = r3*cos(f-71.2)
    y3 = r3*sin(f-71.2)
    xtie+=[x3]
    ytie+=[y3]
    #marte
    r4= (1.524*(1-(0.100*0.100)))/(1-(0.100*cos(f-241.0)))
    x4 = r4*cos(f-71.2)
    y4 = r4*sin(f-71.2)
    xmar+=[x4]
    ymar+=[y4]

grafica.plot(xmer,ymer,color='w')
grafica.plot(xven,yven,color='g')
grafica.plot(xtie,ytie,color='b')
grafica.plot(xmar,ymar ,color='r')

#primitivos
grafica.add_patch(figuras.Circle((0,0),radius=0.18,color='y'))
plt.text(0.15,0.19,"Sol",color='w',fontsize=14)

grafica.add_patch(figuras.Circle((-0.12,-0.31),radius=0.06,color='w'))
plt.text(0.13,-0.20,"Mercurio",color='w',fontsize=12)

grafica.add_patch(figuras.Circle((-0.716895,-0.0837),radius=0.06,color='g'))
plt.text(-0.55,0.40,"Venus",color='g',fontsize=14)

grafica.add_patch(figuras.Circle((0.15,-0.98),radius=0.06,color='b'))
plt.text(0.41,-1.05,"Tierra",color='b',fontsize=14)

grafica.add_patch(figuras.Circle((1.28,1.02),radius=0.06,color='r'))
plt.text(0.76,1.08,"Marte",color='r',fontsize=14)

plt.text(0.15,1.74,"El sistema solar interior",color='w',fontsize=16)

plt.savefig("cancha.png")
plt.show()
