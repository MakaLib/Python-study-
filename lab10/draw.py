
from random import *
from math import *
def przeksztalc(l):
	x = [0]
	y = [0]
	for i in range(10000):
		los = randrange(100)
		if los < 85 : los = 3
		elif los >= 85 and los < 92: los = 2
		elif los >=92 and los < 99: los = 1
		else: los = 0
		a = l[los][0] * x[i] + l[los][1] * y[i] + l[los][2]
		b = l[los][3] * x[i] + l[los][4] * y[i] + l[los][5]
		x.append(a)
		y.append(b)
	with open("dane.dat","w") as plik:
		for i in range(len(x)):
			plik.write(str(x[i]) + " "+ str(y[i]) + "\r\n")


def drugie(n=5):
	napis = 'F'
	for _ in range(n):
		napis = napis.replace('F','F+F-F-F+F')
	print(napis)
	x = [0]
	y = [0]
	kat = 0
	for i in napis:
		if i == 'F':
			x.append(x[-1] + cos(kat*pi/180))
			y.append(y[-1] + sin(kat*pi/180))
		elif i == '+':
			kat -= 90
			kat %= 360
		else:
			kat += 90
			kat %= 360
	with open("wynik.dat", "w") as plik:
		for i in range(len(x)):
			plik.write(str(x[i]) + " " + str(y[i]) + "\r\n")
