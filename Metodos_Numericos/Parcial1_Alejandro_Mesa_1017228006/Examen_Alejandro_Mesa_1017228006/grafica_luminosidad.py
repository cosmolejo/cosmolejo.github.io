from numpy import loadtxt,linspace
from matplotlib import pyplot as plt
datos=loadtxt('luminosidad.dat')
time=datos[:,0]
lumi=datos[:,1]
plt.plot(time,lumi,'o')
print 'tiene 3 opciones: '
print '1: mostrar en pantalla  solamente'
print '2:guardar imagen'
print '3: mostrar en pantalla y guardar'
sw=0
while sw==0:
    a=input('ingrese la orden a ejecutar (1/2/3): ')
    if a==1:
        plt.show()
        sw=1
    elif a==2:
        plt.savefig('energia.png')
        sw=1
    elif a==3:
        plt.savefig('energia.png')
        plt.show()
        sw=1
    else:
        print'orden desconocida'
        sw=0
