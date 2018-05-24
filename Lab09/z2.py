class Wektor:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
	def __add__(self,wektor):
		if isinstance(wektor,Wektor):
			return Wektor(self.x + wektor.x, self.y + wektor.y, self.z + wektor.z)
		#return None
	def __str__(self):
		return "({0}, {1}, {2})".format(self.x,self.y,self.z)
	def __iadd__(self,wektor):
		if isinstance(wektor, Wektor):
			self.x += wektor.x
			self.y += wektor.y
			self.z += wektor.z
		return self
	def __getitem__(self, i):
		if(i == 0): return self.x
		elif(i == 1): return self.y
		elif(i == 2): return self.z
		#else: return None
	def __setitem__(self,i,wartosc):
		if(i == 0): self.x = wartosc
		elif(i == 1): self.y = wartosc
		elif(i == 2): self.z = wartosc
		return self
	def skalarny(self, wektor):
		if isinstance(wektor,Wektor):
			return (self.x *wektor.x + self.y*wektor.y + self.z*wektor.z)
		#else: return None
	def wektorowy(self, wektor):
		if isinstance(wektor,Wektor):
			return Wektor(self.y*wektor.z-self.z*wektor.y,self.z*wektor.x-self.x*wektor.z, self.x*wektor.y-self.y*wektor.x)
		#else: return None
	def mieszany(self, wektor1, wektor2):
		if isinstance(wektor1, Wektor) and isinstance(wektor2, Wektor):
			return self.skalarny(wektor1.wektorowy(wektor2))
		#else: return None





a = Wektor(4,6,7)
b = Wektor(1,1,1)
c = Wektor(2,2,4)
print(a)
print(a+b)
a += b
print(a)
print(a[1])
a[1] = 2
print(a[1])
a = Wektor(3,4,5)
b = Wektor(3,2,1)
c = Wektor(5,2,6)
print(a)
print(a.skalarny(b))
print(a.wektorowy(b))
print(a.mieszany(b,c))

