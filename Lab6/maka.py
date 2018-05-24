from math import log
from math import sin
from math import factorial

print("=========1=========")

def naturalna():
	i = 0;
	while True:
		i = i + 1;
		yield i
		
def doskonala(a):
	for i in a:
		if i == sum(x for x in range(1,i//2 + 1) if i%x == 0):
			yield i

def mniejsze(a,b):
	for x in a:
		if x < b:
			yield x
		else:
			return

print(list(doskonala(mniejsze(naturalna(),10000))))

print("========2==========")



print("=========3==========")

def trzecie():
	u = 0
	x = 1
	a = 0.05
	while x < 1.5:
		u = u + a/x
		x = x + a
		yield x,u,log(x)

print(list(trzecie()))

print("========4=========")

def sumy(n):
	for i in range(1,n):
		q = n
		j = i
		l = []
		while (q != 0):
			if q - j >= 0:
				q = q - j
				l.append(j)
				#j = j - 1
			else:
				j = j -1
		yield l



def suma(n, l= []):
	if n == 1:
		yield (l,)
	else:
		q = n
		for i in range(2,n):
			for j in suma(q - 1, l):
				yield (l,) + j


print(list(sumy(4))) 
print(list(suma(4)))


print("========5=======")

def sinus(x):
	k = 0
	wartosc = 0
	while not ( sin(x) - 0.00000001 < wartosc and sin(x) + 0.00000001 > wartosc):
		wartosc = wartosc + (-1)**k*x**(1+2*k)/(factorial(1+2*k))
		k = k + 1
		yield wartosc,k

print(list(sinus(3.14/2)));
