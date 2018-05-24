import math
from scipy.misc import derivative

class Newton:
	def __init__(self,f,xs=1.5):
		self.f = f
		self.x = xs
	def __iter__(self):
		return self
	def __next__(self):
		if math.fabs(self.f(self.x)) < 10**(-5):
			raise StopIteration
		self.x = self.x - self.f(self.x)/derivative(self.f,self.x)
		return self.x

ff = Newton(lambda x: math.sin(x) - (0.5*x)**2)
for i in ff:
	print(i)