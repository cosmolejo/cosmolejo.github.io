# *-* coding: utf-8 *-*
import os
from math import fabs
from numpy import loadtxt,linspace
from pylab import plot, show, legend,savefig

os.system('clear')
##### CARGA DE DATOS, r=radio, d=densidad
data=loadtxt('densidad-tierra.dat')
r=data[:,0]
d=data[:,1]
n=len(r)
X=[] #VECTOR PARA ALMACENAR LAS X DEL POLINOMIO
D=[] #vector para almacenar las densidades asociadas a X
Xt=[] #Vector para almacenar las x teoricas
poli=[] #VECTOR DE POLINOMIOS
exper=[] #Densidad interpolada para puntos conocidos
xaux=[] #vector auxiliar para cnocer las x initerpoladas y teoricas
teor=[] #vector auxiliar, datos "teoricos"
rt=r[-1] #radio terrestre
media=0 #variable para almacenar el error medio


##### VALOR A INTERPOLAR Y GRADO MAXIMO DEL POLINOMIO
x=input('ingrese el radio [km] para hallar la densidad: ')
x*=1000
inter=(rt-x) #dato a interpolar
grado=input('ingrese el grado maximo de polinomios a interpolar: ')
grado+=1


#### CALCULO DE LA COTA PARA EL RADIO
for i in xrange(0,n):
    if r[i]<inter and r[i+1]>inter:
        for a in xrange(0,grado):
            X.append(r[i+a])
            D.append(d[i+a])

#### El programa puede calcular Polinomios de lagrange de distinto orden
#l=1 cociente interpolante
#p=0 polinomio de lagrange 
for k in xrange(1,grado):
    l=1
    p=0
    for i in xrange(0,k+1):
        l=1
        for j in xrange(0,k+1):
            if j!=i:
                l*=((inter-X[j])/(X[i]-X[j]))
        p+=(l*D[i])
    poli.append(p)

    print'la densidad para un radio de ',x/1000,'[km] con un polinomio de lagrange de grado ',k,'es aproximadamente de ',p
print 'por las precision deseada para el ajuste se recomienda tomar el valor del polinomio de grado 1'


#### CALCULO DEL ERROR
e=1
while e<26:
    LT=1
    PT=0
    Xt=[]
    Dt=[]
    rad=r[e]#radio conocido a interpolar para hallar un rho exp.
    dens=d[e]
    Xt.append(r[e-1])
    Xt.append(r[e+1])
    Dt.append(d[e-1])
    Dt.append(d[e+1])
    for i in xrange(0,2):
        LT=1
        for j in xrange(0,2):
            if i!=j:
                LT*=((rad-Xt[j])/(Xt[i]-Xt[j]))
        PT+=(LT*Dt[i])
    exper.append(PT)
    xaux.append(r[e])
    teor.append(d[e])
    err=fabs(exper[-1]-teor[-1])
    media+=err
    e+=1
media/=e
print 'error estadistico del ajuste: ±', media


#######  GRAFICA

##barras de error
EM=poli[0]+media
Em=poli[0]-media
Ebarr=linspace(Em,EM,100)
b=Ebarr.shape[0]
for i in xrange(0,b):
    plot(inter,Ebarr[i],'+',c='k')
##polinomios
a=len(poli)
for i in xrange(0,a):
    plot(inter,poli[i],'o',label=('polinomio grado: ',i+1))
##datos
plot(r,d,label='data')
legend(loc='upper right')

savefig('interpolacion(interp.py).png')
show()

