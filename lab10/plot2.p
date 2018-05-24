set term jpeg
set out 'dane.jpg'
set xlabel 'X'
set ylabel 'Y(X)'
plot 'dane.dat' u 1:2 w p t '',\
			
set out 'wynik.jpg'
plot 'wynik.dat' u 1:2 w p t '',\
