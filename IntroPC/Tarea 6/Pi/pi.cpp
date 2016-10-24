#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include "rutinapi.cpp"
using namespace std;

int main()
{
  
  long  n,i,t,a,pi2;
  long double pi,pi3;
  cout<<"Numero de repeticiones: ";
  cin>>n;
  cout<<"numero de decimales MAXIMO 18: ";
  cin>>t;
  a=pow(10,t);
  pi=rutpi(n);
  pi2=(pi*a);
  pi3=pi2/a;
  pi2=pi2-(3*a);
  printf("pi con %ld cifras decimales es: 3.%ld\n",t,pi2);
  return 0;
}
