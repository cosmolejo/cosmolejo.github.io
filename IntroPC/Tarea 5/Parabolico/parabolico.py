#!/usr/bin/env python
import math
#recoleccion de informacion
vo=input("ingrese la velocidad inicial del cuerpo: ")
ang=input("ingrese el angulo con el cual es lanzado (formato deg): ")
g=9.8;
#calculos iniciales
ymax=(((vo**2)*(math.sin(ang)**2)))/(2*g)
xmax=(((vo*vo)*(math.sin(ang)*math.cos(ang)))/(g))
t=(((2*vo)*(math.sin(ang)))/g)
#si el angulo es igual a 90 distancia en x es 0 despreciando la friccion
if (ang==90):
    xmax=0
    print"el alcance horizontal  maximo es ",xmax
    print"el tiempo de vuelo es ",t
    print"la altura maxima es ",ymax     
#si el angulo esta entre 90 y 0 ....
else:
    if(ang<90 and ang>=0):
        print"el alcance horizontal  maximo es: ",xmax
        print"el tiempo de vuelo es ",t
        print"la altura maxima es: ",ymax  	
#si el angulo supera 90 grados los calculos serian negativos...
if (ang>90 and ang<360):
    ang=ang-90
    ymax=(((vo**2)*(math.sin(ang)**2)))/(2*g)
    xmax=((((vo**2)*(math.sin(ang)*math.cos(ang)))/(g)))*(-1)
    t=((((2*vo)*(math.sin(ang)))/g))*(-1)
    print"atencion!! su disparo fue realizado hacia el lado contrario..."
    print"el alcance horizontal  maximo es: ",xmax
    print"el tiempo de vuelo es: ",t
    print"la altura maxima es: ",ymax  
    
