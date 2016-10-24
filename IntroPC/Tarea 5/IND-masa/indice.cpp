#include <cstdio>
#include <cmath>
using namespace std;

int main(void)
{
  float IND,masa,altura;
  printf("ingrese la masa corporal de la persona: ");
  scanf("%f",&masa);
  printf("\n");
  printf("ingrese la estatura de la persona: ");
  scanf("%f",&altura);
  printf("\n");
  IND=(masa/pow(altura,2));
  printf("%f\n",IND);
  if (IND < 25.00 && IND > 18.50)
      {
	printf("la persona presenta un peso normal\n");	
      } 
  else
    {
      if (IND >= 25.000000)
	{
	  printf("la persona presenta sobrepeso\n");
	}  
      if (IND <= 18.500000)
	{
	  printf("la persona presenta desnutricion\n");
	}  
    }
	return 0;
}
