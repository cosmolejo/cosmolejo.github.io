set terminal png
set output "grafica 2.png"

set ylabel "Angulo (grados)"
set xlabel "t(s)"
set title "Elevacion en movimiento parabolico (parcial 3, Alejandro Mesa)

set xtics 0.2
set ytics 5

plot "./aux.csv" u1:2