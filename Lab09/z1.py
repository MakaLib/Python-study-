from random import *

class IFS:
	def __init__(self,wsp):
		self.l = wsp
		self.x = [0]
		self.y = [0]

	def przeksztalc(self):
		for i in range(100000):
			los = randrange(len(self.l))
			a = self.l[los][0]*self.x[i] + self.l[los][1]*self.y[i] + self.l[los][2]
			b = self.l[los][3]*self.x[i] + self.l[los][4]*self.y[i] + self.l[los][5]
			self.x.append(a)
			self.y.append(b)
		with open("dane.dat","w") as plik:
			for i in range(len(self.x)):
				plik.write(str(self.x[i])+ ' ' + str(self.y[i]) + '\r\n')

			i 



zestaw = ((0,0,0,0.2,0.16,-0.04), (0.2,-0.26,0,0.23,0.22,0.1), (-0.15,0.28,0,0.26,0.24,0.1), (0.85,0.04,0,-0.04,0.84,0.1))
a = IFS(zestaw)
a.przeksztalc()
zestaw1 = ((0.255,0,0.3726,0,0.255,0.6714),(0.255,0,0.1146,0,0.255,0.2232),(0.255,0,0.6306,0,0.255,0.2232),(0.37,-0.642,0.6356,0.642,0.37,-0.00061))
b = IFS(zestaw1)
b.przeksztalc()