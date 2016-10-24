#include <cstdio>
#include <cmath>

using namespace std;

int main (void)
{
  float R,pi,area,peri;
  printf("ingrese el radio del circulo: ");
  scanf("%f",&R);
  pi=3.141592654;
  area=pi*pow(R,2);
  peri=2*pi*R;
  printf("el area de su circunferencia es: %f \n",area);
  printf("el perimetro de su circunferencia es: %f \n",peri);

  return 0;

}
