from numpy import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint

###################################
###CONSTANTES
###################################

G=6.673E-11     #[N*(m/kg)^2] costante gravitacional
C=299792458.0   #[m/s] velocidad de la luz
M=1.989E30      #[kg] masa del sol
Rs=2*G*M/(C**2) #radio schwarzchild
E=0.9*C**2

##################################
###SISTEMA DE ECUACIONES
##################################

#fo=dt/dlam f1=dphi/dlam f2=dr/dlam
def f(y,lam):
    ri = y[0]
    phi= y[1]
    L=(E/C**2)*ri*sin(phi)
   
    f1=L/ri**2
    f2=sqrt(fabs(((E/C**2)**2)-((L**2/ri**2)*(1-(Rs/ri)))))
    return [f1,f2]


##################################
###VALORES INICIALES
##################################

ro  =  2.5*Rs                 #radio inicial
phio=  pi/3.0                 #angulo inicial
yo  =  [ro,phio]              #verctor inicial
lam =  linspace(0,1.0E5,6.0E5)  #grid de integracion

##################################
###SOLUCION DEL SISTEMA
##################################

sol=odeint(f,yo,lam)
PHI   =sol[:,0]
R     =sol[:,1]
'''
for i in xrange(len(PHI)):
    if R[i]==nan:
        R[i]=0.
        print' nan R'
    if PHI[i]==nan:
        PHI[i]=0.
        print' nan PHI'
'''
'''
print PHI
print R
'''
#plt.polar(array(PHI),array(R))
#plt.plot(array(R*cos(PHI)),array(R*sin(PHI)))
plt.plot(array(R),array(PHI))
plt.show()

