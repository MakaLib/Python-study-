from random import *

def MonteCarlo(f, xmin, xmax, n= 1000):
	c= 0
	ymin = -1000
	ymax = 1000
	step = xmin
	while step < xmax:
		if f(step) > ymax:
			ymax = f(step)
		if f(step) < ymin:
			ymin = f(step)
		step += 0.1
	for i in range(n):
		a = uniform(xmin,xmax)
		b = uniform(ymin,ymax)
		if b > 0 and b <= f(a): c = c+1
		elif b < 0  and b >= f(a): c = c-1

	return (xmax-xmin)*(ymax-ymin) *c /n


def pi(n):
	c = 0
	for _ in range(n):
		x = uniform(-1,1)
		y = uniform(-1,1)
		if x*x+y*y < 1: c +=1
	l = [c,4*c/n]
	return l