#!/usr/bin/env_python3

#importujemy wszystko z biblioteki random
from random import *

#sto = [randrange(0,20) if not x%2 else x+1 for i in range(10)]
#funkcja zwracajaca slownik 
def slownik(a):
	#towrzymy slownik
	s={}
	#losujemy ilosc elementow w slowniku
	x = randrange(0,20)
	print(x)
	for i in range(x):
		#losujemy liczbe od 0 do 1
		k = random()
		#uzupelniamy
		s[k] = '{0:.3f}'.format(eval('{}+{}'.format(a,k)))
	return s
	



def dowolna(*a):
	lista = []
	for i in a[0]:
		for j in a[1:]:
			if i not in j:
				break
		else:
			lista.append(i)
	return lista


def min(a,b):
	if a < b:
		return a
	return b

def max(a,b):
	if a > b:
		return a
	return b

def min_max(funkcja, *a):
	temp = a[0]
	for i in a[1:]:
		temp = funkcja(temp,i)
	return temp

def reszta(kwota, a=(10,5,2)):
	resz = []
	for i in a:
		while True:
			if kwota-i>=0:
				resz.append(i)
				kwota = kwota-i
			else:
				break
	return resz


def losuj (a,b,c, tryb = 'r'):
	while True:
		n = randrange(b,c) if tryb == 'r' else (b+c)//2
		if n == a:
			return n
		b = n+1 if n < a else b
		c = n-1 if n > a else c

def sekwencja(a,b, tryb = True):
	if(len(a) < len(b)):
		roznica  = len(b) - len(a)
		l = [(a[x],b[x]) for x in range(len(a))]
	else:
		roznica = len(a) - len(b)
		l = [(a[x],b[x]) for x in range(len(b))]
	if tryb:
		return l
	else:
		for x in range(roznica):
			l.append('None')
	return l

		



print("Zadnie1\n")	
s1 = slownik(5)
print(s1)

print("Zadnie 2")
my_list = dowolna('qwer','qetyu','qedfga')
print(my_list)

 
print("Zadanie 3")
jeden = [1,3,5,7,9,11]
dwa = [0,2,4,6,8]
dziala = sekwencja(jeden,dwa,False)
print(dziala)

print("Zadanie 4")
min_value = min_max(min,1,2,3,4,5,6,7,8,9)
print(min_value)
max_value = min_max(max,1,2,3,4,5,6,7,8,9)
print(max_value)

print("Zadanie 5")
reszzta = reszta(148)
print(reszzta)

print("Zadanie 6")
print(losuj(89,0,100,'z'))