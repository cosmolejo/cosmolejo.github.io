long double rutpi(long n)
{

  long i;
  double pi;
 
  pi=1.0;
  for (i=n;i>0;i--)
    {
      pi=2.0+double((2*i+1)*(2*i+1))/pi;
    }
  pi=1.0/pi;
  pi=pi+1.0;
  pi=4.0/pi;
  
  return pi;
}
