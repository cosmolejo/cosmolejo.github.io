set terminal png
set output "rectas_gp.png"

plot 2*x+1 t "2*x+1" w lp  lw 3 lc rgb"blue", 3*x+1 t "3*x+1" w l lw 3 lc rgb"red", 4*x+2 t "4*x+1" w l  lw 3 lc rgb"green"
