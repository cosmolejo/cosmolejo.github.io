#!/usr/bin/env python



m1=input("ingrese la masa 1: ")
m2=input("ingrese la masa 2: ")
r=input("por ultimo ingresela distancia entre ambos cuerpos: ")
G=6.674E-11
grav=(G*((m1*m2)/r**2))
print"la fuerza de atraccion entre ambos cuerspos se de: %f",(grav)
