#include <cstdio>
int primo (int f)
{
  int i,comp,sw=0;
 
  for(i=2;i<=(f-1);i++)
    {
      
      comp=f%i;
    
      if (comp==0)
	{

	  sw=1;
	  return 0;
	  break;
	  }
    }
  if (sw==0)
    {
      
	return 1;
    }
  
}
