
class Automat:
	def __init__(self,rozmiar,wiel_kwa,liczba_iter):
		self.rozmiar = rozmiar
		self.wiel_kwadrat = wiel_kwa
		self.iteracje = liczba_iter
		self.kwadrat = [[0 for _ in range(rozmiar)] for i in range(rozmiar)]
		self.wypisz()
		print("\n")
		x = rozmiar//2 - wiel_kwa//2
		y = x
		for i in range(wiel_kwa):
			for j in range(wiel_kwa):
				self.kwadrat[x+i][y+j] = 1
		self.wypisz()

	
	def wypisz(self):
		for i in range(self.rozmiar):
			print(self.kwadrat[i])
	def wypisz_ewo(self):
		for i in range(self.rozmiar):
			print(self.kwadrat_2[i])


	def ewolucja(self):
		for iteracja in range(self.iteracje):
			self.kwadrat_2 = [[0 for _ in range(self.rozmiar)] for _ in range(self.rozmiar)]
			for i in range(self.rozmiar):
				for j in range(self.rozmiar):
					zycie = 0
					if(i != 0 and j != 0):
						if(self.kwadrat[i-1][j-1] == 1): zycie +=1
					if(i != 0):
						if(self.kwadrat[i-1][j] == 1): zycie +=1
					if(i != 0 and j != self.rozmiar-1):
						if(self.kwadrat[i-1][j+1] == 1): zycie +=1
					if(j != 0):
						if(self.kwadrat[i][j-1] == 1): zycie +=1
					if(j != self.rozmiar-1):
						if(self.kwadrat[i][j+1] == 1): zycie +=1
					if( i != self.rozmiar -1 and j != 0 ):
						if(self.kwadrat[i+1][j-1] == 1): zycie +=1
					if(i != self.rozmiar -1):	
						if(self.kwadrat[i+1][j] == 1): zycie +=1
					if(i != self.rozmiar -1  and j != self.rozmiar-1):
						if(self.kwadrat[i+1][j+1] == 1): zycie +=1
					if(self.kwadrat[i][j] == 1 and (zycie == 2)): pass
					elif(zycie == 3): self.kwadrat_2[i][j] = 1
					else: self.kwadrat_2[i][j] = 0
			print("\nIteracja ",iteracja+1,"\n")
			self.wypisz_ewo()
			self.kwadrat = self.kwadrat_2

print("\nA\n")
a = Automat(3,1,4)
a.ewolucja()
print("\n\nB\n")
b = Automat(5,3,4)
b.ewolucja()
print("\nC\n")
c = Automat(14,8,7)
c.ewolucja()
