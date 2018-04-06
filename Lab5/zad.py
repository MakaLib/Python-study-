print("=========1========")

from time import time
from sys import version
from random import *

powt = 1000
N = 10000

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
	l = map(lambda i: i*i, range(n))

def generatorExpression(n):
	l = (i*i for i in range(n))

print(version)
test = (forStatement,listComprehension,mapFunction,generatorExpression)
for testFunction in test:
	print(testFunction.__name__.ljust(20), '=>',tester(testFunction))

print("===========2=========")
l1 = [randrange(0,20) for i in range(100)]
l2 = [randrange(0,20) for i in range(100)]
#l3 = list(zip(l1,l2))
k1 = list(filter(lambda x: sum(x)>3 and sum(x)<15,zip(l1,l2)))
print(k1)

print("==========3==========")
from math import sqrt

def trzecia(a,b):
	x_sr = sum(a)/len(a)
	y_sr = sum(b)/len(b)
	n = len(a)
	D = sum(list(map(lambda x: (x-x_sr)**2,a)))
	print(D)
	c = 1/D * sum(list(map(lambda y,x: y*(x-x_sr),b,a)))
	print(c)
	d = y_sr - c * x_sr
	print(d)
	dy = sqrt((sum(map(lambda y,x: (y - (c*x+d))**2,b,a)))/(n-2))
	print(dy)
	dc = dy/sqrt(D)
	print(dc)
	dd = dy*sqrt(1/n + (x_sr**2)/D)
	print(dd)
	return c,d,dy,dc,dd
	

a = [1,5,8,3]
b = [1,3,2,4]
print(trzecia(a,b))

print("==========4===========")

def myreduce(fun,a):
	x = a[0]
	for i in a[1:]:
		x = fun(x,i)
	return x

print(myreduce(lambda x,y: x+y,[1,2,3,4]))
print(myreduce(lambda x,y: x*y, [1,2,3,4]))

print("=========5============")
l5 = [[randrange(0,10),randrange(0,10)] for i in range(5)]
print(l5)
#lo = myreduce(lambda x,y: map(isinstance(l5[0],int) x.append(l5[0]),l5),l5)