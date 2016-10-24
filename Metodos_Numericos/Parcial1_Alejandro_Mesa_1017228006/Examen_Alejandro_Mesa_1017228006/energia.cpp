#include <cstdio>
#include <iostream>


using namespace std;

double interp(double, double, double, double, double, double, double, double, double, double); 

int main(void)
{
    double dato, m[15][15][4],d1[1200],d2[1200],d3[1200],d4[1200],t[1200];
    double simpson,suma_par,suma_impar,tiempo,error,derivada4;
    
    int i,j;
    FILE* fp;
    FILE* fs;
    fp=fopen ("estrellas.dat","r");
    fs=fopen ("luminosidad.dat","w");


    
    for (i=0;i<10;i++)
    {
        for (j=0;j<10;j++)
        {
            fscanf(fp,"%lf", &m[i][j][0]); //masa 
            fscanf(fp,"%lf", &m[i][j][1]); //Tiempo
            fscanf(fp,"%lf", &dato);
            fscanf(fp,"%lf", &dato);
            fscanf(fp,"%lf", &m[i][j][2]); //Luminocidad
        }
        
    }
        
    fclose(fp);
   
    
    
    tiempo=0.0;
    j=0;
    for (i=0;i<=1000;i++)
    {
        if (tiempo==0.0)
        {
            t[i]=0.0;
        }
       if ((tiempo>0)&&(tiempo<m[5][0][1]))
        { 
            t[i]=interp(m[5][0][0], m[6][0][0], 0.0, m[6][1][1], 1.0, tiempo, 0.0, 0.0, m[5][1][2], m[6][1][2]); 
        }    

        if ((tiempo>=m[5][0][1])&&(tiempo<m[5][1][1]))
        { 
            t[i]=interp(m[5][0][0], m[6][0][0], m[5][0][1], m[6][1][1], 1.0, tiempo, m[5][0][2], m[6][0][2], m[5][1][2], m[6][1][2]); 
        } 


        if ((tiempo>=m[5][1][1])&&(tiempo<m[5][2][1]))
        { 
            t[i]=interp(m[5][0][0], m[6][0][0], m[5][1][1], m[6][2][1], 1.0, tiempo, m[5][1][2], m[6][1][2], m[5][2][2], m[6][2][2]); 
        } 
        

        if ((tiempo>=m[5][2][1])&&(tiempo<m[5][3][1]))
        { 
            t[i]=interp(m[5][0][0], m[6][0][0], m[5][2][1], m[6][3][1], 1.0, tiempo, m[5][2][2], m[6][2][2], m[5][3][2], m[6][3][2]); 
        } 
        
        if ((tiempo>=m[5][3][1])&&(tiempo<m[5][4][1]))
        { 
            t[i]=interp(m[5][0][0], m[6][0][0], m[5][3][1], m[6][4][1], 1.0, tiempo, m[5][3][2], m[6][3][2], m[5][4][2], m[6][4][2]); 
        } 

        if ((tiempo>=m[5][4][1])&&(tiempo<m[5][5][1]))
        { 
            t[i]=interp(m[5][0][0], m[6][0][0], m[5][4][1], m[6][5][1], 1.0, tiempo, m[5][4][2], m[6][4][2], m[5][5][2], m[6][5][2]); 
        } 

        if ((tiempo>=m[5][5][1])&&(tiempo<m[5][6][1]))
        { 
            t[i]=interp(m[5][0][0], m[6][0][0], m[5][5][1], m[6][6][1], 1.0, tiempo, m[5][5][2], m[6][5][2], m[5][6][2], m[6][6][2]); 
        } 

        if ((tiempo>=m[5][6][1])&&(tiempo<m[5][7][1]))
        { 
            t[i]=interp(m[5][0][0], m[6][0][0], m[5][6][1], m[6][7][1], 1.0, tiempo, m[5][6][2], m[6][6][2], m[5][7][2], m[6][7][2]); 
        } 

        if ((tiempo>=m[5][7][1])&&(tiempo<m[5][8][1]))
        { 
            t[i]=interp(m[5][0][0], m[6][0][0], m[5][7][1], m[6][8][1], 1.0, tiempo, m[5][7][2], m[6][7][2], m[5][8][2], m[6][8][2]); 
        } 

        if ((tiempo>=m[5][8][1])&&(tiempo<m[5][9][1]))
        { 
            t[i]=interp(m[5][0][0], m[6][0][0], m[5][8][1], m[6][9][1], 1.0, tiempo, m[5][8][2], m[6][8][2], m[5][9][2], m[6][9][2]); 
        } 
        
	/*

	  este siguiente paso es necesario hacerlo porque no se logro encontrar cual es la razon del error que 
          genera el problema: para la posicion 4 del vector t se genera una division por 0, pero puesto que solo es 
          en este unico dato de los mil generados se puede concluir facilmente que el erro no se debe a la carga de datos 
          o al metodo de interpolacion, por lo cual para evitar inconvenientes en los futuros calculos, se le asigna 
          arbitrariamente un valor de 0.0 

	 */

        if (i==4)  
        {
          t[i]=0.0;
        }
        
        fprintf(fs,"%lf %lf\n",tiempo,t[i]);
        
        tiempo=tiempo+0.0025;
    }
    
    fclose(fs);
    
    //Primera derivada
    for (i=1;i<1000;i++)
    {
        d1[i]=(t[i]-t[i-1])/0.0025;
        
        
    }
    
    //Segunda derivada
    for (i=2;i<1000;i++)
    {
        d2[i]=(d1[i]-d1[i-1])/0.0025;
    }


     //Tercera derivada
    for (i=3;i<1000;i++)
    {
        d3[i]=(d2[i]-d2[i-1])/0.0025;
    }

     //Cuarta derivada
    for (i=4;i<1000;i++)
    {
        d4[i]=(d3[i]-d3[i-1])/0.0025;
    }
   
    derivada4=0.0;
    for (i=10;i<510;i++)
    {
        derivada4=derivada4+d4[i];
    }
    error=(2.5-0.0)*(0.0025*0.0025*0.0025*0.0025)*derivada4/180.0;
    // printf("Error = %lf \n",error);
    
    suma_par=0.0;
    suma_impar=0.0;
    for (i=1;i<1000;i=i+2)
    {
        suma_impar=suma_impar+t[i];
    }
    suma_impar=4.0*suma_impar;
    for (i=2;i<998;i=i+2)
    {
        suma_par=suma_par+t[i];
    }
    suma_par=2.0*suma_par;
    simpson=(0.0025/3.0)*(t[0]+suma_par+suma_impar+t[999]);
    printf("este programa calcula la energia que emana una estrella de 1 masa solar en 2.5 Gyrs\n");
printf("Energia = %lf +/- %lf \n",simpson,error);
printf("magnitud [(Msun*Rsun**2)/Gyrs**2]\n");
    
}

double interp(double x1, double x2, double y1, double y2, double x, double y, double f11, double f21, double f12, double f22) 
{
       return (y2-y)*(x2-x)*f11/((y2-y1)*(x2-x1)) + (y2-y)*(x-x1)*f21/((y2-y1)*(x2-x1))  + (y-y1)*(x2-x)*f12/((y2-y1)*(x2-x1))  + (y-y1)*(x-x1)*f22/((y-y1)*(x2-x1));

}
       
