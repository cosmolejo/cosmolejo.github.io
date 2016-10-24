from visual import *
scene.width=600
scene.height=480

scene.center=vector(0,0,0)
scene.forward=vector(-0.5,-0.5,-0.5)

scene.ambient=1.0

tetamax=input("ingrese el angulo de inclinacion para soltar el pendulo (deg):")
tetamax=(tetamax*pi)/180

label(text="x",pos=vector(5,0,0),box=False,opacity=0.0)
ejex=curve(pos=[(0,0,0), (5,0,0)], radius=0.005)
label(text="y",pos=vector(0,5,0),box=False,opacity=0.0)
ejey=curve(pos=[(0,0,0), (0,5,0)], radius=0.005)
label(text="z",pos=vector(0,0,5),box=False,opacity=0.0)
ejez=curve(pos=[(0,0,0), (0,0,5)], radius=0.005)

teta=0
l=0.469
B=0.96
H=0.969
g=9.8
t=1

piso=box(pos=vector(0.95,0,-0.9),size=vector(1,0.05,1),color=color.red)

base=box(pos=vector(0.95,0.51,-0.9),size=vector(0.1,1,0.1),color=color.blue)

biga=box(pos=vector(0.95,0.969,-0.45),size=vector(0.1,0.1,0.9),color=color.green)

w= 2*pi*(sqrt(g/l))

teta=tetamax*cos(w*t)
x=(l*sin(teta))+B
y=(-l*cos(teta))+H
cuerda=curve(pos=[(0.96,0.969,0), (x,y,0)], radius=0.005)
bola=sphere(pos=vector(x,y,0), radius=0.05,color=color.yellow)

while True:
    teta=tetamax*cos(w*t)
    x=(l*sin(teta))+B
    y=(-l*cos(teta))+H
    bola.pos=vector(x,y,0)
    cuerda.pos[1]=(x,y,0)
    t+=0.01
    rate(5)
