set terminal epslatex size 16cm, 8cm
set output 'external_field_at_surface.tex'

set xlabel '$\rho$'
set ylabel '$\dfrac{-H_{m,x}}{M_s}$'
unset key

set xrange [0:1]
set yrange [0:1]

set multiplot layout 1,2 rowsfirst

plot 0.5*(1 - exp(-2*pi*x)) with lines

set ylabel '$\dfrac{-H_{m,z}}{M_s}$'
plot 0.5*(1 + exp(-2*pi*x)) with lines
