# *-* coding: utf-8 *-*

#### CARGA DE PAQUETES
from numpy import fabs,sin,sqrt,pi,linspace,loadtxt
from pylab import plot,show,savefig

print'este programa calcula la masa total de la tierra a partir de datos interpolados de densidad'
print('NOTA: el metodo a implementar sera la regla de simpson con cuadratura adaptativa.')
print('NOTA2:EL PROGRAMA NO GENERA GRAFICAS.\n')



#### CARGA DE DATOS
datos=loadtxt('densidad-tierra.dat')
radios=datos[:,0]
densidades=datos[:,1]
ndatos=radios.shape[0]
Rtierra=radios[-1]      #extremo superior de la integral
a=0                     #extremo inferior de la integral
h=fabs(Rtierra-a)/2.0
TOL=input('ingrese el margen de error maximo permitido para la aproximacion: ')

#### INTERPOLACION
"PUESTO QUE ESTE TEMA YA SE DESARROLLO EN LA PRACTICA PASADA, SE USARAN LIBRERIAS EXTERNAS PARA CALCULAR LOS DATOS DE FORMA MAS EFICIENTE"
from scipy.interpolate import interp1d

densidad_tierra=interp1d(radios,densidades)
rs=linspace(radios[0],radios[-1],10000000) #genera un arreglo con N puntos a partir de los radios
ds=densidad_tierra(rs) #la rutina crea un arreglo a partir de rs
'''
plot(rs,ds,'+')
show()
'''

#### DECLARACION DE FUNCIONES

def funcion(x):
    x=int(x)
    sigma=(ds[x])
    print x,sigma
    f=(x**2)*sigma
    
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
    return simpson_recurs(f,a,c,eps/2,izq)+simpson_recurs(f,c,b,eps/2,der)
    '''vuelve a llamar a la funcion recursiva con la mitad de tolerancia y 
    tomando como el todo a los intervalos izquierdos y derechos hasta que 
    se cumpla la condicion del if'''


def simpson_adapt(f,a,b,eps):                    #define el metodo adaptativo completo
    #                                            entra f(x),a,b y la tolerancia
    return simpson_recurs(f,a,b,eps,regla_simpson(f,a,b))

print 4.0*pi*simpson_adapt(funcion,a,Rtierra,TOL)

