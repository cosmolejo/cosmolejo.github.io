#include <cstdio>
#include <cmath>

using namespace std;

int main (void)
{
  float v,d,t;
  printf("ingrese la distancia a la que se encuantra la estrella de la nave (km): ");
  scanf("%e",&d);
  printf("ingrese la velocidad a la que se desplaza la nave (m/s): ");
  scanf("%e",&v); 
  d*=1000;
  t=(d/v);
  /*if (t > 31557600) // si el tiempo supera un año...
    { 
      t*=(3600*24*365.25);
    }
  */
  printf("su nave tardara: %e segundos en llegar a la estrella en cuestion \n",t);

  return 0;

}
