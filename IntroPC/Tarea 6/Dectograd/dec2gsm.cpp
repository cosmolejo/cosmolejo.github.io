#include <cmath>

void dec2gsm(double dec, double& g, double& m, double& s)
{
  double grad,decimal,a,b,c;
  grad= floor(dec);
  decimal=dec-grad;
  g=grad;
  a=decimal*60;
  m=floor(a);
  b=a-m;
  c=b*60;
  s=c;
}
