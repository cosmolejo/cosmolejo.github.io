from visual import *
from sys import exit
scene.width=600
scene.height=480

scene.center=vector(0,0,0)
scene.forward=vector(-3,-3,-3)

scene.ambient=1.0


label(text="x",pos=vector(5,0,0),box=False,opacity=0.0)
ejex=curve(pos=[(0,0,0), (5,0,0)], radius=0.005)
label(text="y",pos=vector(0,5,0),box=False,opacity=0.0)
ejey=curve(pos=[(0,0,0), (0,5,0)], radius=0.005)
label(text="z",pos=vector(0,0,5),box=False,opacity=0.0)
ejez=curve(pos=[(0,0,0), (0,0,5)], radius=0.005)


#caja
piso=box(pos=vector(0,0,0),size=vector(5,0.05,5),color=color.white, material=materials.wood)
muro1=box(pos=vector(0,2.5,-2.48),size=vector(5,5,0.05),color=color.white, material=materials.wood)
muro2=box(pos=vector(0,2.5,2.48),size=vector(5,5,0.05),color=color.orange, material=materials.wood,opacity=0.1)
muro3=box(pos=vector(2.48,2.5,0),size=vector(0.05,5,5),color=color.orange, material=materials.wood,opacity=0.1)
muro2=box(pos=vector(-2.48,2.5,0),size=vector(0.05,5,5),color=color.white, material=materials.wood)
techo=box(pos=vector(0,5,0),size=vector(5,0.05,5),color=color.yellow, material=materials.wood,opacity=0.1)

#posiciones
xo=0
yo=4
zo=0
rad=0.5 #radio

#velocidad, aceleracion y variables
vox=0
voy=10
voz=0
g=(-9.8)
t=0.1
aux=-1

#bola
bola=sphere(pos=vector(xo,yo,zo), radius=rad,color=color.red, material=materials.rough)
bola.velocity=vector(vox,voy,voz)
while True:
   
    x=xo+vox*t
    y=yo+voy*t+((g*t*t)/2)
    z=zo+voz*t

   
    print 't: %lf x: %lf y: %lf z: %lf | vox: %lf voy: %lf voz: %lf\n'%(t,x,y,z,vox,voy,voz)

    if (y < bola.radius):
        
        xo=x
        yo=y
        z0=z
        
        vox=vox*0.9
        voy=abs(voy)*0.9
        voz=voz*0.9
        if y<=0:
            y=abs(y)
        print '**** en condicion!!: t: %.lf x: %.lf y: %lf z: %lf | vox: %lf voy: %lf voz: %lf \n'%(t,x,y,z,vox,voy,voz)   
 
    if (x>=1.7):
        xo=x
        vox=(-0.9)*vox        
    
    if (x<=-1.7):
        xo=x
        vox=(-0.9)*vox
        
    if (z<=-1.7):
        zo=z
        voz=(-0.9)*voz 
       
    if (z>=1.7):
        zo=z
        voz=(-0.9)*voz        
        
    if (y>5):
        yo=y
        voy=(-0.9)*voy
        if y>9:
            y=-y
    bola.pos=vector(x,y,z)
    t+=0.1
    rate(5)

    if y<0:
        print'abortando\n'
        break
