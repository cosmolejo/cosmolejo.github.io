set terminal png
set output "cuadrado_gp.png"

set xrange [-10:10]
set yrange [-1:20]
set ylabel "F(x)"
set xlabel "x"
set title "grafica x^2"
set grid
set xtics 1
set ytics 1


plot x*x

