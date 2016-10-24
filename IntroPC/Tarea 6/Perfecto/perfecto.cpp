#include <cstdio>
#include <cmath>
using namespace std;

int main (void)
{
  double div,sum,cond;
  int num,i;
  printf("ingrese un numero: ");
  scanf("%d",&num);
  for (i=1;i<=(num-1);i++)
    {
      cond=num%i;
      if (cond == 0)
	{
	  sum+=i;
	}
    }
  if (sum==num)
    {
      printf("el numero %d es perfecto \n",num);
    }
  else
    {
      printf("el numero %d es no perfecto \n",num);
    }
  return 0 ;

}
