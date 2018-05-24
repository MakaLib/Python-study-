
class Pseudo:
	def __init__(self):
		self.x = 1;
		self.c = 0
		self.a = 44485709377909
		self.m = 2 **48
	def __iter__(self):
		return self
	def __next__(self):
		self.x = (self.a * self.x + self.c) % self.m
		return self.x/self.m




def f(x):
	return x*x + 2* x


a = Pseudo()
xs = 0
xk = 20
ymax = f(xs)
ymin = f(xs)
step = xs
while step < xk:
	if f(step) > ymax:
		ymax = f(step)
	if f(step) < ymin:
		ymin = f(step)
	step += 0.1
dokladna = 3066.668
print(ymin,ymax)
c = 0
n = 0
calka = 0
while True:
	x = next(a) *(xk - xs) + xs
	y = next(a) * (ymax - ymin) + ymin
	n += 1
	if 0 < y and f(x) >= y:
		c += 1
	elif 0 > y and f(x) <= y:
		c -= 1
	calka = (ymax - ymin) * (xk - xs) * c / n
	print(calka)
	if abs(calka -dokladna) < 10**(-3): break
print(c)
print(n)
print(calka)


