#include <cstdio>
#include "gms2dec.cpp"
using namespace std;

int main (void) 
{
  double g1,m1,s1,g2,s2,m2,lat,lon;
  printf("ingrese la latitud (formato: grad  m' s'')\n");
  printf("angulo (grad): ");
  scanf("%lf",&g1);
  printf("minutos (m'): ");
  scanf("%lf",&m1);
  printf("segundos (s''): ");
  scanf("%lf",&s1);

  lat=gms2dec(g1,m1,s1);
  printf("ingrese la longitud (formato: grad  m' s'')\n");
  printf("angulo (grad): ");
  scanf("%lf",&g2);
  printf("minutos (m'): ");
  scanf("%lf",&m2);
  printf("segundos (s''): ");
  scanf("%lf",&s2);

  lon=gms2dec(g2,m2,s2);
  printf("su latitud en formato decimal es: %lf \n",lat);
  printf("su longitud en formato decimal es: %lf \n",lon);

  return 0;



}
