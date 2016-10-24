#include <cstdio>
#include <cmath>

using namespace std;

int main(void)
{
  // declaracion variables
  double vo,t,seno,coseno,g,ang,ymax,xmax;
  //recoleccion de informacion
  printf("ingrese la velocidad inicial del cuerpo: ");
  scanf("%lf",&vo);
  printf("ingrese el angulo con el cual es lanzado (formato deg): ");
  scanf("%lf",&ang);
  g=9.8;
  //calculos iniciales
  ymax=(((vo*vo)*(sin(ang)*sin(ang)))/(2*g));
  xmax=(((vo*vo)*(sin(ang)*cos(ang)))/(g));
  t=(((2*vo)*(sin(ang)))/g);
  //si el angulo es igual a 90 distancia en x es 0 despreciando la friccion
  if (ang==90)
    {
      xmax=0;
      printf("el alcance horizontal  maximo es:%lf \n",xmax);
      printf("el tiempo de vuelo es:%lf \n",t);
      printf("la altura maxima es:%lf \n",ymax);  
    }
  //si el angulo esta entre 90 y 0 ....
  else
    {
      if(ang<90 && ang>=0)
	{
	  printf("el alcance horizontal  maximo es:%lf \n",xmax);
	  printf("el tiempo de vuelo es:%lf \n",t);
	  printf("la altura maxima es:%lf \n",ymax);  
	}
    }
  //si el angulo supera 90 grados los calculos serian negativos...
  if (ang>90 && ang<360)
    {
      ang=ang-90;
       ymax=(((vo*vo)*(sin(ang)*sin(ang)))/(2*g));
       xmax=abs((((vo*vo)*(sin(ang)*cos(ang)))/(g)));
       t=abs((((2*vo)*(sin(ang)))/g));
       printf("atencion!! su disparo fue realizado hacia el lado contrario...\n");
       printf("el alcance horizontal  maximo es:%lf \n",xmax);
       printf("el tiempo de vuelo es:%lf \n",t);
       printf("la altura maxima es:%lf \n",ymax);  
    }
  
  return 0;
}
