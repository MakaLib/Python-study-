class Fib:
	def __init__(self):
		self.a = 0
		self.b = 1
	def __iter__(self):
		return self
	def __next__(self):
		x = self.a
		y = self.b

		self.a = y
		self.b = x + y

		if self.b > 10000:
			raise StopIteration
		return self.b


F = Fib()
for i in F:
	print(i)