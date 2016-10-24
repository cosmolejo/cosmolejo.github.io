set terminal png
set output "experimento_gp.png"
set grid
set xlabel "t (segundos)"
set ylabel "v(m/s)"
set title "Datos experimento de caida libre"
set label "v(t)=9.8t + vo" at 0.6,5
plot [0.0:1.2] [0:14]"./experimento.dat" u 1:2 t "" w p lc rgb"red" , 9.8*x+0.5 t "" w l lc rgb"blue"
