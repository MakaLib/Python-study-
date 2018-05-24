from random import *
class Generator:
	def __init__(self):
		self.x = 1
		self.a = 7**5
		self.m = (2**31) - 1
		self.c = 0
		self.ilosc = 0
	def __iter__(self):
		return self
	def __next__(self):
		self.ilosc = self.ilosc + 1
		if self.ilosc >2* 10**5:
			raise StopIteration
		self.x = (self.a * self.x + self.c) % self.m
		return self.x/self.m

g = Generator()
n = uniform(1,10) + 1
print(n)
bok = 0.1 * n
print(bok)
ilosc_w_kwadracie = 0

for i in g:
	a = i
	b = next(g)
	if a <= bok and b <= bok:
		ilosc_w_kwadracie += 1

ilosc_zwykla = 0

for i in range(10**5):
	a = random()
	b = random()
	if a <= bok and b <= bok:
		ilosc_zwykla += 1
print(ilosc_w_kwadracie*100/(10**5),"   ", ilosc_zwykla*100/(10**5))
