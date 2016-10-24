# *-* coding: utf-8 *-*

#### CARGA DE PAQUETES
from numpy import fabs,exp,sqrt,pi,linspace
#from pylab import plot,show,savefig



#### CARGA DE DATOS

print'este programa calcula la funcion gamma de 2 y 0.5 respectivamente'
print('NOTA: el metodo a implementar sera la regla de simpson con cuadratura adaptativa.')
print('NOTA2:EL PROGRAMA NO GENERA GRAFICAS.\n')
TOL=input('ingrese el margen de error maximo permitido para la aproximacion: ')


b1=45 #extremo superior para G(2)
b2=5
a=0 #extremo inferior de la integral


#### DECLARACION DE FUNCIONES

def funcion1(x):                                  #Gamma para t=2
    t=2
    f=((x**(t-1))*exp(-x))
    return f
def funcion2(x):                                  #Gamma para t=1/2
    t=0.5
    return 1.0/((x**(1+t))*exp(x))


def regla_simpson(f,a,b):                         #defino simpson, entra f(x),a y b
    c = (a+b) / 2.0                               #valor medio entre a y b
    h3 = fabs(b-a) / 6.0                          #h de la regla de simpson*3 
    return h3*(f(a)+4.0*f(c)+f(b))                #regla de simpson para I=[a,b]
 

def simpson_recurs(f,a,b,eps,St): 
    #defino simpson de forma recursiva, dividiendo I en 2  entran f(x),a,b,la tolerancia(eps)
    #y simpson calculadp para todo I (St)
    c = (a+b) / 2.0
    izq = regla_simpson(f,a,c)                    #regla de simpson para el sun.I izq.
    der = regla_simpson(f,c,b)                    #regla de simpson para el sun.I der.
    if abs(izq + der - St) <= 15*eps:             #condicion de formula
        return izq + der + (izq + der - St)/15.0
    return simpson_recurs(f,a,c,eps/2.0,izq)+simpson_recurs(f,c,b,eps/2.0,der)
    
    
    '''vuelve a llamar a la funcion recursiva con la mitad de tolerancia y 
    tomando como el todo a los intervalos izquierdos y derechos hasta que 
    se cumpla la condicion del if'''


def simpson_adapt(f,a,b,eps):                    #define el metodo adaptativo completo
    #                                            entra f(x),a,b y la tolerancia
    return simpson_recurs(f,a,b,eps,regla_simpson(f,a,b))
 

####Calculo de la integral, error asociado y comparacion con librerias
from scipy.integrate import quadrature as quad 

##INTEGRAL Y ERROR CON CUADRATURA GAUSSIANA (LIBRERIAS)
intgauss1=quad(funcion1,0,b1,rtol=TOL)              #devuelve una tupla, [0]=integral, [1]=error
#intgauss2=quad(funcion2,0,b2,rtol=TOL)
#solgauss=intgauss2[0]*0.5

## INTEGRAL SIMPSON/ADAPTATIVO
simpson1= simpson_adapt(funcion1,a,b1,TOL)       #evaluacion de la integral
#simpson2= -0.5*simpson_adapt(funcion2,a,b2,TOL)


print('gamma(2) aproximada por simpson: %5.20f'%(simpson1)),'±',TOL
print'gamma(2) aproximada por cuadratura gaussiana: ',intgauss1[0],'±',intgauss1[1],'\n'
'''print('gamma(0.5) aproximada por simpson: %5.20f'%(simpson2)),'±',TOL
print'gamma(0.5) aproximada por cuadratura gaussiana: ',solgauss,'±',intgauss[1],'\n'
'''
