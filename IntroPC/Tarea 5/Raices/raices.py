#!/usr/bin/env python
import math

#obtencion de datos

print"tenemos la siguiente ecuacion ax^(2) +bx + c ... hallaremos sus raices\n"
a=input("ingrese el valor de a:")
b=input("ingrese el valor de b:")
c=input("ingrese el valor de c:");

#calculo discriminante
discriminante=b*b-4*a*c;
  
if(discriminante<0): # si el discrim. es <0 tenemos raices complejas
   
    discriminante*=-1;
    r=math.sqrt(discriminante);
    x1=(-b+r)/(2*a);
    x2=(-b-r)/(2*a);
    print"las raices de su polinomio son complejas\n"
    print"las raices de su polinomio son x1=",x1,"i ; x2= ",x2,"i \n" 
    
else:  #si no son reales
   
    r=math.sqrt(discriminante);
    x1=(-b+r)/(2*a);
    x2=(-b-r)/(2*a);
    print"las raices de su polinomio son reales\n"
    print"las raices de su polinomio son x1= ",x1," ; x2= ",x2," \n"
