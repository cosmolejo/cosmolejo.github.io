#include <cstdio>
#include <cmath>

using namespace std;

int main (void)
{
  int num,i,comp,sw;
  printf("ingrese un numero: ");
  scanf("%d",&num);
  for(i=2;i<=(num-1);i++)
    {
      comp=num%i;
      if (comp==0)
	{
	  printf("el numero no es primo\n");
	  sw=1;
	  break;
	  }
    }
  if (sw==0)
    {
        printf("el numero es primo\n");
    }
  return 0;

}
