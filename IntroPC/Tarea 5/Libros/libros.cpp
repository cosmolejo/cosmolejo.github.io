#include <cstdio>
#include <cmath>

using namespace std;

int main (void)

{
  float L1,L2,L3,p1,p2,p3,prom;
  printf("ingrese el numero de paginas del primer libro: ");
  scanf("%f",&L1);
  printf("ingrese el numero de palabras para este libro: ");
  scanf("%f",&p1);
  printf("ingrese el numero de paginas del segundo libro: ");
  scanf("%f",&L2);
  printf("ingrese el numero de palabras para este libro: ");
  scanf("%f",&p2);
  printf("ingrese el numero de paginas del tercer libro: ");
  scanf("%f",&L3);
  printf("ingrese el numero de palabras para este libro: ");
  scanf("%f",&p3);
  prom=(((p1/L1)+(p2/L2)+(p3/L3))/3);
  printf("el promedio de palabras por paginas de un libro (con base en sus libros) seria: %f\n",prom);
  return 0;
}
