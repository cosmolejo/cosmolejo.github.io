from visual import *
from sys import exit
scene.width=600
scene.height=480

scene.center=vector(0,0,0)
scene.forward=vector(-1,-1,-1)

scene.ambient=1.0


label(text="x",pos=vector(5,0,0),box=False,opacity=0.0)
ejex=curve(pos=[(0,0,0), (5,0,0)], radius=0.005)
label(text="y",pos=vector(0,5,0),box=False,opacity=0.0)
ejey=curve(pos=[(0,0,0), (0,5,0)], radius=0.005)
label(text="z",pos=vector(0,0,5),box=False,opacity=0.0)
ejez=curve(pos=[(0,0,0), (0,0,5)], radius=0.005)

teta=pi/8
g=9.8
l=5
R=0.5
h=0.05
t=0


plano=box(pos=vector(2.22,1,0),size=vector(5,0.05,1),color=color.orange,material=materials.wood)
plano.rotate(axis=vector(0,0,1),angle=-teta)

r= g*sin(teta)*t
x=((l*cos(teta))-((l-r)*cos(teta))+((R+(h/2))*sin(teta)))
y=(((l-r)*sin(teta))+((R+(h/2))*cos(teta)))
alfa=(r/(2*pi*R))

bola=sphere(pos=vector(x,y,0), radius=0.5,color=color.white,material=materials.earth)


while True:
   r= g*sin(teta)*t
   x=((l*cos(teta))-((l-r)*cos(teta))+((R+(h/2))*sin(teta)))
   y=(((l-r)*sin(teta))+((R+(h/2))*cos(teta)))
   alfa=(r/(2*pi*R))
    
   bola.pos=vector(x,y,0)
   bola.rotate(axis=vector(1,0,0), angle=alfa)
    
   t+=0.1
   rate(2)
    
   if  y<R:
       break
    
    

