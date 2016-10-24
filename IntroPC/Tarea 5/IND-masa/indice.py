#!/usr/bin/env python
import math

masa=input("ingrese la masa corporal de la persona: ")
altura=input("ingrese la estatura de la persona: ")
IND=(masa/altura**2)
if (IND < 25.00 and IND > 18.50):
    print("la persona presenta un peso normal\n");	 
else:
    if (IND >= 25.000000):
        print("la persona presenta sobrepeso\n");  
    if (IND <= 18.500000):
        print("la persona presenta desnutricion\n");
	  
