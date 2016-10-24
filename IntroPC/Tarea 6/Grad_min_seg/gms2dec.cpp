#include <cstdio>

using namespace std;

double gms2dec(double g, double m, double s)
{
  double gdec,mdec,sdec;
  sdec=(s/3600);
  mdec=(m/60);
  gdec=sdec+mdec+g;
  
  return gdec;






}
