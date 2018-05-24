print("============1=======")

class ZlaWartosc(Exception):
	pass

class DzieleiePrzezZero(Exception):
	pass

from random import *
def jeden(a,b,c):
	if(a < 0 or b < 0 or c < 0):
		raise ZlaWartosc("Ujemne wartosci")
	if(a > b):
		raise ZlaWartosc("Zla wartosc pierwszego argumetnu")
	l = [randrange(a,b) for _ in range(c)]
	print(l)
	niep = len([x for x in l if x%2])
	print(niep)
	pa = len(l) - niep
	if niep == 0:
		raise DzieleiePrzezZero("Dzielenie przez 0")
	return pa/niep


try:
	print(jeden(1,8,4))
except ZlaWartosc as blad:
	print(blad)
except DzieleiePrzezZero as blad:
	print(blad)


print("============2==========")

class Nieokraslona(Exception):
	pass


from math import *
#def f1(x):
#	return x+1

#def f2(x):
#	if(x-1 == 0):
#		raise Nieokraslona("Funkcja nieokresolna")
#	return (x-2)*(x-2)/(x-1) - 2

def bisekcja(f,a,b):
	#if f(a) * f(b) > 0:
	#	raise Exception("Nie mozna zastosowac metody bisekcji")
	miejsca_zerowe = []
	#try:
	if(f(a) == 0): miejsca_zerowe.append(a)
	if(f(b) == 0): miejsca_zerowe.append(b)
	while fabs(b-a) > pow(10,-7):
		x = (a+b)/2
		if f(x) == 0:
			miejsca_zerowe.append(x)
		elif (f(x) * f(a) < 0):
			b = x
		else:
			a = x
	#except Nieokraslona as blad:
		#print(blad)
		#raise Nieokraslona("Funkcja nieokresolna")
	if len(miejsca_zerowe) == 0:
		raise ZlaWartosc("Brak miejsc zerowych")
	return miejsca_zerowe

try:
	#print(bisekcja(lambda x: x+1,-1,0))
	#print(bisekcja(lambda x: x+1,1,2))
	print(bisekcja(lambda x: (x-2)*(x-2)/(x-1)-2,0,2))
	#print(bisekcja(lambda x: (x-2)*(x-2)/(x-1)-2,4,6))
except ZlaWartosc as bald:
	print(blad)
except Exception as kazdy:
	print(kazdy)
#except Nieokraslona as blad:
	#print(blad)


print("============3===========")
class Rozmiar(Exception):
	pass


def Pitagorejsa(lista, N):
	if len(lista)%N != 0:
		raise Rozmiar("Zly rozmiar listy")
	i = 0
	while i < len(lista)- N - 1:
		suma = 0;
		for k in range(N-1):
			if lista[k+i] > lista[i+N-1]:
				raise ZlaWartosc("Ostatni element nie jest najwiekszy")
			suma += lista[k+i] **2
		if suma != lista[i+N-1]**2:
			return False
		i = i + N
	return True



l1=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,
12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,
21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,
23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2)

l2=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,
12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,
21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,
23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29)

l3=(3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)
l4=(3,4,5,5,13,12,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17) 
print(len(l1))
print(len(l2))
print(len(l3))
print(len(l4))
try:
	#print(Pitagorejsa(l1,3));
	#print(Pitagorejsa(l1,4))
	#print(Pitagorejsa(l2,3));
	print(Pitagorejsa(l2,4))
	print(Pitagorejsa(l3,3));
	print(Pitagorejsa(l3,4))
	#print(Pitagorejsa(l4,3));
	print(Pitagorejsa(l4,4))
except Rozmiar as blad:
	print(blad)
except ZlaWartosc as blad:
	print(blad)


print("===========5===========")

from glob import glob
import os

def aver(nazwa):
	if os.access(nazwa, os.R_OK):
 		plik = open(nazwa)
 		kolumny = []
 		try:
 			linie = plik.readlines()
 			if len(linie) == 0:
 				raise Rozmiar("Brak danych")
 			for linia in linie:
 				linia = linia.rstrip()
 				liczby = linia.split("\t")
 				#print(liczby)
 				for i in liczby:
 					if not i.isdigit():
 						raise Rozmiar("Brak liczb")
 				if(len(liczby) != 2):
 					raise Rozmiar("ZLa liczba kolumn")
 				kolumny.append(int(liczby[0]))
 				kolumny.append(int(liczby[1]))
 			with open("srednia.txt", "a") as zapis:
 				zapis.write(str(sum(kolumny)/len(kolumny)))
 				zapis.write("\r\n")



 		finally:
 			plik.close()



for plik in glob("*.dat"):
 try:
 	aver(plik)
 except Rozmiar as blad:
 	print(blad)
 #except ZlaWartosc as blad:
 #	print(blad)