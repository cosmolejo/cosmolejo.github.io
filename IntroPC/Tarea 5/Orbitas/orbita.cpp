#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int main (void)

{
  float e;
  printf("ingrese la excentrisidad del cometa: ");
  scanf("%f",&e);
  if (e==1)
    {
      printf("el cometa tiene una orbita parabolica");
    }
  if (e<1)
    {
      printf("el cometa tiene una orbita eliptica");
    }  
  if (e>1)
    {
      printf("el cometa tiene una orbita hiperbolica\n");
    }
  cout<<endl;
  return 0;
}
