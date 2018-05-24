from math import *
class Pierwsze:
	def __init__(self,zakres):
		self.zakres = zakres
		self.pierwsza = 2
	def __iter__(self):
		return self
	def __next__(self):
		while True:
			if self.pierwsza == self.zakres:
				raise StopIteration
			czy_pie = True
			for j in range(2,int(sqrt(self.pierwsza)) + 1):
				if self.pierwsza % j == 0:
					czy_pie = False
					break
			self.pierwsza += 1
			if(czy_pie):
				return self.pierwsza - 1
		#self.pierwsza += 1


class B:
	def __init__(self,zakres):
		self.zakres = zakres
		self.pierwsza = 2
	def __next__(self):
		while True:
			if self.pierwsza == self.zakres:
				raise StopIteration
			czy_pie = True
			for j in range(2,int(sqrt(self.pierwsza)) + 1):
				if self.pierwsza % j == 0:
					czy_pie = False
					break
			self.pierwsza += 1
			if(czy_pie):
				return self.pierwsza - 1



class A:
	def __init__(self,zakres):
		self.zakres = zakres
	def __iter__(self):
		return B(self.zakres)

z = Pierwsze(18)
for i in z:
	for j in z:
		print(i,j)

print("Koniec\n")

q = A(18)
for i in q:
	for j in q:
		print(i,j)