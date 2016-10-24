double factorial(int n)
{
  int i;
  double factorial;

  factorial=1;

  for(i=n;i>=1;i=i-1)
    {
      factorial=factorial*i;
    }
  
  return factorial;
}
double combinatoria(double L,double P)
{
  double aux,fac1,fac2;
  fac1=factorial(L);
  fac2=factorial((L-P));
  aux=fac1/fac2;
  return aux;
}
