#include <cstdio>
using namespace std;
int Fperfecto (int num)
{
  int div,sum=0;
  int i,cond;
  for (i=1;i<=(num-1);i++)
    {
      cond=num%i;
      if (cond == 0)
	{
	  sum+=i;
	}
    }
  if (sum==num)
    {
      return 1; 
    }
  else
    {
      return 0;
    }
}
