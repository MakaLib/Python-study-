print("===============1=========")

class ZlaWartosc(Exception):
	pass

def Srodkowa(*a):
	for i in a:
		if not isinstance(i,(int,float)):
			raise ZlaWartosc("Parametr nie jest liczba")
	for i in range(len(a)-1):
		if a[i] > a[i+1]:
			raise ZlaWartosc("Zle posortowana")
	if len(a)%2:
		return a[len(a)//2]
	else:
		return (a[len(a)//2] + a[len(a)//2-1])/2

try:
	print(Srodkowa(1,2,3,4,5,6,7,8))
	print(Srodkowa(*(1,2,3,4,5)))
	print(Srodkowa(-4,-3,-2))
except ZlaWartosc as blad:
	print(blad)

print("==========2===========")

from types import FunctionType
def Metoda_Trapezow(fun,pocz,koniec,N):
	if not isinstance(pocz,(int, float)):
		raise ZlaWartosc("Zle typy")
	if not isinstance(koniec,(int, float)):
		raise ZlaWartosc("Zle typy")
	if not isinstance(N,(int, float)):
		raise ZlaWartosc("Zle typy")
	if pocz > koniec:
		raise ZlaWartosc("Zle posortowana")
	if not isinstance(fun,FunctionType):
		raise ZlaWartosc("Brak funkcji")
	s = 0
	dx = (koniec- pocz)/N
	i = pocz
	while i < koniec:
		s = s + fun(i) * dx
		i += dx
	return s

try:
	print(Metoda_Trapezow(lambda x: x**2 + 2*x,0,1,1000))
	print(Metoda_Trapezow(lambda x: x**2,3,2,1000))
except ZlaWartosc as blad:
	print(blad)








print("===============3============")

class Rozmiar(Exception):
	pass

def Pitagorejsa(lista, N):
	if len(lista)%N != 0:
		raise Rozmiar("Zly rozmiar listy")
	i = 0
	while i <= len(lista)- N:
		suma = 0;
		parzyste = 0
		nieparzyste = 0
		trojka = []
		for k in range(N-1):
			if lista[k+i] > lista[i+N-1]:
				raise ZlaWartosc("Ostatni element nie jest najwiekszy")
			trojka.append(lista[k+i])
			suma += lista[k+i]**2
		if suma == lista[i+N-1]**2:
			trojka.append(lista[i+N-1])
			print(trojka)
			for x in trojka:
				if x%2: nieparzyste +=1
				else: parzyste +=1	
			print(parzyste,nieparzyste)
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

try:
	#print(Pitagorejsa(l1,3),"\n") #Zly rozmiar
	#print(Pitagorejsa(l1,4),"\n") #Zly rozmiar
	#print(Pitagorejsa(l2,3),"\n") #Zly rozmiar
	print("2,4")
	print(Pitagorejsa(l2,4),"\n")  #False
	print("3,3")
	print(Pitagorejsa(l3,3),"\n")	#True
	#print("3,4")
	#print(Pitagorejsa(l3,4),"\n")	#False
	#print(Pitagorejsa(l4,3),"\n")	#Elemen
	print("4,4")
	print(Pitagorejsa(l4,4),"\n")	#False
except Rozmiar as blad:
	print(blad)
except ZlaWartosc as blad:
	print(blad)


print("===========4========")

from glob import glob
import os


def aver(nazwa):
	if os.access(nazwa, os.R_OK):
 		plik = open(nazwa)
 		kolumny = []
 		try:
 			linie = plik.readlines()
 			if len(linie) == 0:
 				raise ArithmeticError("Brak danych")
 			for linia in linie:
 				linia = linia.rstrip()
 				liczby = linia.split("\t")
 				for i in liczby:
 					if not i.isdigit():
 						raise ArithmeticError("Brak liczb")
 				if(len(liczby) != 2):
 					raise ArithmeticError("ZLa liczba kolumn")
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
 except ArithmeticError as blad:
 	print(blad)
