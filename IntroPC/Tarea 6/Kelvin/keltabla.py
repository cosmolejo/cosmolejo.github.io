#! /usr/bin/ env python
import k2cf

print"programa para convertir un rango de temperaturas K a C y F\n"
k1=input("ingrese una termperatura en kelvin: ")
k2=input("ingrese una termperatura menor a la inicial en kelvin: ")
if k1<0 or k2<0:
    print"los numeros deben ser mayores o iguales a 0, pues la escala kelvin es absoluta\n"
    
else:
    print"%-15s %-15s %-15s"%("Temperatura K","Temp. C","Temp. F\n")
    i=k2       
    while i<=k1:
        c,f=k2cf.k2cf(i)
        print"%-15d %-15lf %-15lf\n"%(i,c,f);
	i+=1


