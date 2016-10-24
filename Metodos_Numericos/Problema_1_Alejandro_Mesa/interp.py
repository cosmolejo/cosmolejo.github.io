# *-* coding: utf-8 *-*
import os
from math import fabs
from numpy import loadtxt
from pylab import plot, show, legend

os.system('clear')
##### CARGA DE DATOS, r=radio, d=densidad
data=loadtxt('densidad-tierra.dat')
r=data[:,0]
d=data[:,1]
n=len(r)
X=[] #VECTOR PARA ALMACENAR LAS X DEL POLINOMIO
Xt=[] #Vector para almacenar las x teoricas
poli=[] #VECTOR DE POLINOMIOS
exper=[] #Densidad interpolada para puntos conocidos
xaux=[] #vector auxiliar para cnocer las x initerpoladas y teoricas
teor=[]




##### VALOR A INTERPOLAR Y GRADO MAXIMO DEL POLINOMIO
x=input('ingrese el radio [km] para hallar la densidad: ')
x*=1000
grado=input('ingrese el grado maximo de polinomios a interpolar: ')
grado+=1
#### CALCULO DE LA COTA PARA EL RADIO

for i in xrange(0,n):
    if r[i]<x and r[i+1]>x:
        for a in xrange(0,grado):
            X.append(r[i+a])

#### El programa puede calcular Polinomios de lagrange de distinto orden
#l=1 cociente interpolante
#p=0 polinomio de lagrange 
for k in xrange(1,grado):
    l=1
    p=0
    for i in xrange(0,k):
        for j in xrange(0,k):
            if j!=i:
                l*=((x-X[j])/(X[i]-X[j]))
            
        p+=(l*d[i])
    poli.append(p)

    print'la densidad para un radio de ',x,'[m] con un polinomio de lagrange de grado ',k,'es aproximadamente de ',p


print 'por las precision deseada para el ajuste se recomienda tomar el valor del polinomio de grado 1'
#### CALCULO DEL ERROR
for e in xrange(1,n-10):
    LT=1
    PT=0
    Xt=[]
    
    rad=r[e]#radio conocido a interpolar para hallar un rho exp.
    dens=d[e]
    Xt.append(r[e-1])
    Xt.append(r[e+1])
    Xt.append(r[e+2])
    
    for i in xrange(0,1):
        for j in xrange(0,1):
            if i!=j:
                LT*=((rad-Xt[j])/(Xt[i]-Xt[j]))
        PT+=(LT*dens)
        
    exper.append(PT)
    xaux.append(r[e])
    teor.append(d[e])

dim=len(exper)
media=0
for s in xrange(0,dim):
    media*=fabs(teor[s]-exper[s])
media/=n
print 'error estadistico del ajuste: ±', media


print 'cabe anotar que claramente no tiene sentido puesto que el ajuste no es 100% perfecto'

#######  GRAFICA
a=len(poli)
for i in xrange(0,a):
    plot(x,poli[i],'+',label=('polinomio grado: ',i+1))
plot(r,d,label='data')

legend(loc='upper right')
show()

