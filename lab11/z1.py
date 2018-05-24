

class Pascal():
	def __init__(self, zakres):
		self.zakres = zakres
		self.x = [1]
		self.ile = 0
	def __iter__(self):
		return self
	def __next__(self):
		self.ile += 1
		if self.ile == self.zakres:
			raise StopIteration
		if self.ile == 1: return 1
		l = [0 for _ in range(self.ile)]
		l[0] = 1
		l[self.ile -1] = 1
		if self.ile == 2:
			self.x = l
			return self.x
		for i in range(1,self.ile - 1):
			l[i] = self.x[i-1] + self.x[i]
		self.x = l
		return self.x


a = Pascal(10)
for i in a:
	print(i)

