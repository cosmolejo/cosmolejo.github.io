#include <cstdio>
#include <cmath>

using namespace std;

int main (void)
{
  int a,b;
  double n,m,c,r;
  printf("ingrese el primer valor: ");
  scanf("%i",&a);
  printf("ingrese el segundo valor: ");
  scanf("%i",&b);
  n=a;
  m=b;
  c=(n/m);
  r=(a%b);
  printf("el cociente es: %f; su residuo es %f",c,r);   
  return 0;

}
