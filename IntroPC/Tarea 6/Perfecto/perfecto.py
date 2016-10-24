num=input("ingrese un numero: ")
i=1
suma=0
while i<=(num-1):
    cond=num%i
    if cond == 0:
        suma+=i
    i+=1
    
if suma==num:
    print"el numero %d es perfecto \n"%(num)
    
else:
    print"el numero %d es no perfecto \n"%(num)
    
