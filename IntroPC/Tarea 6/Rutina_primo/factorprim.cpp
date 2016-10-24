#include <cstdio>
#include"rutinas_primo.cpp"
using namespace std;

int main(void)
{
  int n,i,f,j,comp,sw,p;
  printf("ingrese un numero: ");
  scanf("%d",&n);
  printf("factores primos: \n");
   for(i=1;i<=(n);i++)
    {
      
      
      comp=n%i; 
	  if (comp==0)
	    {
	     
	      p=primo(i);
	      if (p==1)
		{
		  printf(" %d \n",i);
		}
	    }

    }
}



 


