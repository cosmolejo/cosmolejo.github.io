#include <cstdio>
#include"rutinas.cpp"

using namespace std;

int main (void)
{
  double L,P,combi;
  printf("ingrese el numero de elementos a combinar: ");
  scanf("%lf",&L);
  printf("en grupos de cuanto desea combinarlos??: ");
  scanf("%lf",&P);
  
  combi=combinatoria(L,P);
  
  printf("si se tienen %.0lf elementos combinados de a %.0lf elementos por grupo, se obietenen %.0lf grupos\n",L,P,combi);

  return 0;
}
