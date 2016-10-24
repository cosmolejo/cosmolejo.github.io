# *-* coding: utf-8 *-*

#### CARGA DE PAQUETES
from numpy import fabs,sin,sqrt,pi,linspace
#from pylab import plot,show,savefig



#### CARGA DE DATOS

print'este programa calcula la distancia recorrida por un cuerpo sobre una orbita eliptica en funcion de su anomalia excentrica'
print('NOTA: el metodo a implementar sera la regla de simpson con cuadratura adaptativa.')
print('NOTA2:EL PROGRAMA NO GENERA GRAFICAS.\n')


A=float(input('ingrese el semieje mayor de la elipse [u]: '))
B=float(input('ingrese el semieje menor de la misma [u] : '))
E=input('ingrese la anomalia excentrica [0≤E≤2π] si desea puede escribir "pi" : ')
TOL=input('ingrese el margen de error maximo permitido para la aproximacion: ')
e=sqrt(1.0-(B/A)**2.0) #Exentricidad de la elipse
a=0 #extremo inferior de la integral
h=fabs(E-a)/2.0

#### DECLARACION DE FUNCIONES

def funcion(x):
    f=sqrt(1-((e**2)*(sin(x)**2)))
    return f

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
intgauss=quad(funcion,0,E,rtol=TOL)              #devuelve una tupla, [0]=integral, [1]=error
gausseval=A*intgauss[0]                           #integral completa para gauss


## INTEGRAL SIMPSON/ADAPTATIVO
simpson= A*simpson_adapt(funcion,a,E,TOL)       #evaluacion de la integral

print('integral aproximada por simpson: %5.20f'%(simpson)),'±',TOL
print'integral aproximada por cuadratura gaussiana: ',gausseval,'±',intgauss[1],'\n'

print'IMPORTANTE: en este metodo el error es la tolerancia maxima permitida, de este modo el valor siempre va a estar entre el rango '
print'de error [',simpson-TOL,',',simpson+TOL,'] sin importar cuan grande sea esta'
