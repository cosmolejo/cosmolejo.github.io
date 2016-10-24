# /usr/bin/env python
import rutinas

L=input("ingrese el numero de elementos a combinar: ")
P=input("en grupos de cuanto desea combinarlos??: ")

combi=rutinas.combinatoria(L,P)

print"si se tienen %.0lf elementos combinados de a %.0lf elementos por grupo, se obietenen %.0lf grupos\n"%(L,P,combi)
