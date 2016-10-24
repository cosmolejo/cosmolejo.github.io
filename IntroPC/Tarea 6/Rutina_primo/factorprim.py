#! /usr/bin/ env python
import rutinas_primo

n=input("ingrese un numero: ")
print"factores primos: \n"
i=1   
while i<=(n):
    comp=n%i 
    if comp==0:
        p=rutinas_primo.primo(i)
        if (p==1):
            print" %d \n"%(i)
            
    i=i+1


