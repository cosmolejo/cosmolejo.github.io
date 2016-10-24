#include <cstdio>
#include <cmath>
#include "Fperfecto.cpp"
using namespace std;

int main (void)
{
  int i,perf,num,sw;
  printf("ingrese el numero limite para caulcular numeros perfectos: ");
  scanf("%d",&num);
  for (i=num;i>=1;i--)
    {
      perf=Fperfecto(i);
      if (perf == 1)
	{
	  sw=1;
	  printf("numero perfecto inferior a %d: %d \n",num,i);
	}
    }
  if (sw==0)
    {
      printf("no existen numeros perfectos inferiores al numero %d \n",num);
    }
}
