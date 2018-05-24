
print("==========1===========")

def Fib():
	a = 0
	b = 1
	while True:
		yield a
		a,b = b,a+b

def parz_niep(a, b):
	for i in a:
		if not b:
			if i%2:
				yield i
		else:
			if not i%2:
				yield i

def wieksza(a,b):
	for i in a:
		if i <= b:
			yield i
		else:
			return
		

print(sum(list(parz_niep(wieksza(Fib(),100),1))))
print(sum(list(parz_niep(wieksza(Fib(),100),0))))

print("=============2=============")

def myrange(s,koniec,krok = 1):
	if krok == 0:
		return
	elif krok > 0:
		while s < koniec:
			yield s
			s += krok
	else:
		while s > koniec:
			yield s
			s += krok

print(*list(myrange(-2,-10,0.5)))
print(list(range(-2,10)))

print("===============3==========")
from random import *
def warunek():
	x = random()
	y = x
	while x > 0.1:
		if x > y - 0.4 and x < y + 0.4:
			yield x
			y = x
		x = random()

print(list(warunek()))



print("=========4=========")

def ciag(a):
	ilosc = 0
	for i in a:
		if i == 0:
			ilosc += 1
		else:
			if ilosc:
				yield ilosc
			ilosc = 0
	if ilosc:
		yield ilosc


N = 10
l = [randrange(1,100)%2 for _ in range(N)]
print(l)
oddziel = list(ciag(l))
print(oddziel)
print(sum(oddziel)/len(oddziel))


print("===========5===========")

def rozmien(kwota):
	nom = [1,2,5,10,20,50,100,200]
	l = [100000 for i in range(kwota+1)]
	l[0] = 0
	for i in range(len(nom)):
		C = []
		for j in range(kwota+1):
			if(nom[i] > j):
				C.append(l[j])
			else:
				C.append(min(l[j], 1 + C[j-nom[i]]))
		l = C
		yield l



rozmien(100)
print(list(rozmien(5)))



