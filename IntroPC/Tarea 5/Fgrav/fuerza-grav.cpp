#include <cstdio>
#include <cmath>
using namespace std;

int main(void)
{
  float m1,m2,r,G,grav;
  printf("ingrese la masa 1: ");
  scanf("%e",&m1);
  printf("\n");
  printf("ingrese la masa 2: ");
  scanf("%f",&m2);
  printf("\n");
  printf("por ultimo ingresela distancia entre ambos cuerpos: ");
  scanf("%f",&r);
  printf("\n");
  G=6.674*pow(10.0,-11);
  grav=(G*((m1*m2)/(pow(r,2))));
  printf("la fuerza de atraccion entre ambos cuerspos se de: %e \n ",grav); 
  return 0;

}
