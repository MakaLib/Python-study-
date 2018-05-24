print("========1===========")	
def odczyt(nazwa, n):
	with open(nazwa) as file:
		wiersze = file.readlines()
		print("n-ty wiersz")
		print(list(i.strip() for i in wiersze[:n]))
		print("n-konocywch")
		print(list(i.strip() for i in wiersze[-n:]))
		print("co n-ty wiersz")
		print(list(i.strip() for i in wiersze[::n]))
		print("n-te slowo")
		for i in wiersze:
			print(i.split(' ')[n])
		for i in wiersze:
			print(i[n])



odczyt("plik.txt", 4)

import keyword
from glob import glob

def dwa():
	pliki = glob("*.py")
	slowa = []
	key = keyword.kwlist
	for plik in pliki:
		with open(plik) as file:
			for number,line in enumerate(file.readlines()):
				for word in line.split(' '):
					if word in key:
						slowa.append((number,line.split()))
	print(slowa)

dwa()


print("==============3===========")

def histogram(litera, tryb = True):
	slowa = []
	start = []
	wszystkie_pliki = glob("*.py")
	for plik in wszystkie_pliki:
		with open(plik) as p:
			wiersze = p.readlines()
			for wiersz in wiersze:
				slowa.extend(wiersz.split(' '))
	for slowo in slowa:
		if slowo.startswith(litera):
			start.append(slowo)
	d = {i:start.count(i) for i in start}
	lista = list(d.items())

	if tryb:
		lista.sort()
	else:
		lista.sort(key = lambda x: x[1])
	return lista

print(histogram('a'))


print("=============4=============")

#def oblicz(zapis):


print("========5=========")
def gnuplot():
	pliki = '\''+'\', \''.join(glob('[a-c].dat')) + '\', \'mojoutput.dat\''
	wynik = '''set term pdf\nset out 'nazwa.pdf\nplot %s''' % pliki
	with open("gnuplot", 'w') as f:
		f.write(wynik) 