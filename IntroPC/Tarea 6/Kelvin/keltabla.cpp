#include <cstdio>
#include <cmath>
#include "k2cf.cpp"
int main (void)
{
  int k1,k2,i;
  double c,f;
  printf("programa para convertir un rango de temperaturas K a C y F\n");
  printf("ingrese una termperatura en kelvin: ");
  scanf("%d",&k1);
  printf("ingrese una termperatura menor a la inicial en kelvin: ");
  scanf("%d",&k2);
  if (k1<0 || k2<0)
    {
      printf("los numeros deben ser mayores o iguales a 0, pues la escala kelvin es absoluta\n");
      return 0;
    }
  else
    {
      printf("%-15s %-15s %-15s","Temperatura K","Temp. C","Temp. F\n");
      for (i=k2;i<=k1;i++)
	{
	  k2cf(i,c,f);
	  printf("%-15d %-15lf %-15lf\n",i,c,f);
	}
    }
}
