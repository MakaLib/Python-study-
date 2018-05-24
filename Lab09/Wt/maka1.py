from math import sqrt

class Wektor3D:
	def __init__(self,x = 0,y = 0,z = 0):
		self.x = x
		self.y = y
		self.z = z
	def __add__(self, wektor):
		if isinstance(wektor, Wektor3D):
			return Wektor3D(self.x + wektor.x, self.y + wektor.y,self.z + wektor.z)
		else:
			return None
	def __str__(self):
		return "({0} {1} {2})".format(self.x, self.y, self.z)
	def __sub__(self, wektor):
		if isinstance(wektor, Wektor3D):
			return Wektor3D(self.x - wektor.x, self.y - wektor.y, self.z - wektor.z)
		else: return None
	def __mul__(self,wektor):
		if isinstance(wektor, Wektor3D):
			wektorowe = Wektor3D((self.y * wektor.z - self.z * wektor.y), - (self.x * wektor.z - self.z * wektor.x)  ,(self.x * wektor.y - self.y * wektor.x))
			skalarne = self.x * wektor.x + self.y * wektor.y + self.z * wektor.z
			return (wektorowe,skalarne)
		elif isinstance(wektor, int):
			return Wektor3D(wektor*self.x, wektor*self.y, wektor*self.z)
		else: return None
	def len(self):
		return sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
	def __eq__(self,wektor):
		if not isinstance(wektor, Wektor3D): return None
		elif(self.x == wektor.x and self.y == wektor.y and self.z == wektor.z): return True
		return False






v1 = Wektor3D(1,5,4)
v2 = Wektor3D(3,5,1)
print(v1)
print(v2)
plus = v1 + v2
print(plus)
print(v1-v2)
print(*(v1*v2))
print(v1*3)
print(v1.len())
print(v1 == v2)
v1 = v2
print(v1 == v2)

