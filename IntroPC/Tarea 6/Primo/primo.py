sw=0
num=input("ingrese un numero: ")
i=2
while i<=(num-1):
    comp=num%i
    if comp==0:
        print"el numero no es primo\n"
        sw=1
        break
        
    i=i+1
if sw==0:
    print"el numero es primo\n"
    
