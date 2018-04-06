
## bez nawiasow dziala w python2 
print ("Hello")

s = "1"

# type - podaje typ danej zmiennej
print(type(s))

"""
To nie jest komentarz wielowierszowy
tylko bardzo dlugi obiekt typu string,
ktory jest normalnie przechowywany w pamieci!
"""
s = 1			#typ int (w python2 istnieje int i long dla calkowitych)
print(type(s))
s = 1.			#typ float
print(type(s))

#importujemu modul o nazwie keyword
import keyword
#print(keyword.kwlist)

import math
math.sqrt(9)		#przed import sqrt uzywamy tak
from math import sqrt	#teraz mozemy juz bez math.
sqrt(9)
#from math import sqrt as csqrt	#as umozliwia zmiane nazwy danej importowanej funkcji


#print(dir(math))		#dir funckja wyswiatlajaca nazwy funkcji w math
#print(help(math.modf)) 
#tuple - krotka
print(2/3)	# w python3 0.6666 w python2 0
print(2//3) #0 i 0

#abs - zwaraca wartosc bezw liczby
#fabs - float abs - w module math(math.fabs)
#sum - sumuje
#hypot(a,b) - zwraca odleglosc miedzy punktami
#pow - podnosi do potegi pow(a,b) podnosi a do potegi b
#pow(a,b,c) - a do potegi b modulo c
print(pow(5,3,4))

a,*b = 7, 3, 5, 'a', 3	#a = 7 *b = reszta
print(a,b)

a,b = b,a 		#swap, dziala dla dowolnej liczby parametrow
print(a,b)
print(type((1,)))	#() - krotka(nie mozna modyfikowac), [] - lista(mozna modyfikowac)

k = (1,2,'a',[1,2,3])
#k[3] = 5 - blad, nie mozna modyfikowac 
k[3][2] = 5	#mozna modyfikowac element krotki ktory jest modyfikowalny np. lista
print(k)

k = [1,2,'a',[1,2,3]]
print(type(k))
k[2] = 'Q'
print(k)
k.append([4,5,6])	#append dodajemy na koniec listy
print(k)
#k.extend([7,8,9])	#extend dodajemy na koniec listy ale jako osobne elementy
#print(k)

print(len(k)) #len - dlugosc 
#l = k #przypisujemy oryginal
#l = k[0:] 	#kopiujemy [element startowy: element koncowy(bez niego)]
l = k[:]
l[0] = 7
l[-1][0] ='b'	#slaba kopia
print(l,k) 

from copy import deepcopy
l = deepcopy(k)
l[-1][0] = 'z'	#dobra kopia
print(l,k)

l = [0] * 10 #lista 10 0, kopiujemy warotsci
print(l)
l[5] = 'a'
print(l)

l = [[]] * 20	#kopiujemy referencje
l[3].append('a')
print(l)

l = [[] for _ in range(10)] #[obiekt_dodany petla] _ - konwencja kiedy nie kozystamy z licznika petli


#instrukcje sterujace
# a = war ? T : F inne jzeyki
# a = T if war else F python


#if warunek:
#
#elif warunek2:
#
#else:
from sys import argv	#sys - modul wiersza polecen
print(type(argv))		#typ lista
print(argv)				

import cmath
#a = float(input("a: "))
#b = float(input("b: "))
#c = float(input("c: "))
a = float(argv[1])
b = float(argv[2])
c = float(argv[3])
delta = (b*b - 4*a*c)
if delta != 0:
	pier = cmath.sqrt(delta)
	print("Rozw rownania to: ", (-b-pier)/(2*a), "lub", (-b+pier)/(2*a))
elif delta == 0:
	print("Rozw rownania to", b/(2*a))


k = [1,2,3,4,5]
for i in k:
	i+=3	#tak naprawde nie zmieniamy wartosci
print(k)

for i in range(len(k)):
	k[i] += 3	#teraz modyfikujemy
print(k)

k = [[3,2],[3,4],[6,4]]
#for i,j in k:
#	print(i,j)

for i,j in k:
	if i < j:
		break
else:
	print(i,j)

#range(a)
#range(a,b) poczatek,koniec
#range(a,b,c) poczatek,koniec,krok
#range(10,2,-1) tak tylko gdy chcemy w dol