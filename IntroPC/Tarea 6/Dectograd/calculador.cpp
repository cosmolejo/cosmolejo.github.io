#include <cstdio>
#include <cmath>
#include "dec2gsm.cpp"
using namespace std;

int main (void)
{
  double i,rad,grad, g,s,m;
  printf(" %-20s %-20s %-20s %-20s\n","cos(x)","x en radianes","x en grados","x en gsm");
  for (i=0;i<=1;i=i+0.1)
    {
      rad=acos(i);
      grad=(rad*180)/M_PI;
      dec2gsm(grad,g,m,s);
      printf(" %-20lf %-20lf %-20lf %-1.0lfg%.0lfm%.0lfs\n",i,rad,grad,g,m,s);  
      
      
    }

  return 0;


}
