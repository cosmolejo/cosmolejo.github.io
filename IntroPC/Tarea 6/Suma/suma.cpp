#include <cstdio>
using namespace std;

int main (void)
{
  double num,sum,i;
  printf("ingrese un numero: ");
  scanf("%lf",&num);
  for (i=1;i<=num;i++)
    {
      sum+=i;

    }
  printf("la suma de todos los numeros anteriores a %.0lf es: %.0lf \n",num,sum);

  return 0;

}
