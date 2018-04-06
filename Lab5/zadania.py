
print("========1=======")
from time import time
from sys import version
import random
from math import sqrt


powt = 1000
N = 1000

def tester(fun):
	t1 = time()
	for i in range(powt):
		fun(N)
	t2 = time()
	return t2-t1


def forStatement(n):
	l = []
	for i in range(n):
		l.append(i*i)

	

def listComprehension(n):
	l = [i*i for i in range(n)]

def mapFunction(n):
	x = list(map(lambda i: i*i, range(n)))

def generatorExpression(n):
	l = (i*i for i in range(n))



print(version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
	print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

print("========2========");

def funkcja(x):
	return 5*x+2

def metoda_trapezow(fun,xp,xk,n):
	dx = (xk-xp)/n
	wynik = 0
	wynik = sum(list(map(fun,(xp+ x*dx for x in range(n)))))
	return wynik 
	#temp = [x+1 for x in range(n)]
	#print(temp)
	#values = list(map(lambda x: xp + x *dx, temp))
	#print(values)
	#s = []
	#for i in values:
		#print(i,fun(i))
		#s.append(fun(i))
	#print(s);print(sum(s))
	#return (sum(s) + (fun(xp) + fun(xk)) /2) *dx

print("wynik = {:.3f}".format(metoda_trapezow(lambda x: 5*x+2,1,20,20)))


print("======3========")
print("Metoda Monte Carlo")
N = 10000
R = 4

x_t = [random.uniform(0,R) for i in range(N)]
y_t = [random.uniform(0,R) for i in range(N)] 

wyniki = list(map(lambda x,y: sqrt(x*x + y*y), x_t, y_t))

trafione = len(list(filter(lambda x: x<R,wyniki)))
print("PI: ", 4*trafione/N)


print("========4======5=====")
size = 4
matrix = [[random.randrange(50) for i in range(size)] for y in range(size)]
print(matrix)
najwieksza = list(map(lambda x: max(x), matrix))
print(najwieksza)

nowa = list(map(max,zip(*matrix)))
print(nowa)


matrix2 = [[random.randrange(50) for i in range(size)] for y in range(size)]
print(matrix2)
suma = [[matrix[i][j] + matrix2[i][j] for j in range(size)] for i in range(size)]
print(suma)

print("========6========")


from functools import reduce

def szosta(x,y):
	x_sr = sum(x)/len(x)
	y_sr = sum(y)/len(y)
	D = sum(list(map(lambda q: pow(q-x_sr,2),x)))
	print(D)
	a = 1/D * sum(list(map(lambda y,x: y*(x - x_sr),y,x)))
	print(a)
	


x = [1,2,3,4]
y = [3,7,1,8,7]
szosta(x,y)
