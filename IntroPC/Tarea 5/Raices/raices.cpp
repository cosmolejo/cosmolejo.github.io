#include <cstdio>
#include <cmath>
using namespace std;

int main(void)
{
  //declaracion de var.
  double discriminante,a,b,c,x1,x2,r;
 
  //obtencion de datos

  printf("tenemos la siguiente ecuacion ax^(2) +bx + c ... hallaremos sus raices\n");
  printf("ingrese el valor de a:");
  scanf("%lf",&a);
  printf("ingrese el valor de b:");
  scanf("%lf",&b);
  printf("ingrese el valor de c:");
  scanf("%lf",&c);


  //calculo discriminante
  discriminante=b*b-4*a*c;
  
  if(discriminante<0) // si el discrim. es <0 tenemos raices complejas
    {
      discriminante*=-1;
      r=sqrt(discriminante);
      x1=(-b+r)/(2*a);
      x2=(-b-r)/(2*a);
      printf("las raices de su polinomio son complejas\n");
      printf("las raices de su polinomio son x1= %lfi ; x2= %lfi \n",x1,x2); 
    }
 
  else // si no son reales
    {
      r=sqrt(discriminante);
      x1=(-b+r)/(2*a);
      x2=(-b-r)/(2*a);
      printf("las raices de su polinomio son reales\n");
      printf("las raices de su polinomio son x1= %lf ; x2= %lf \n",x1,x2);
    }
  return 0;

}
