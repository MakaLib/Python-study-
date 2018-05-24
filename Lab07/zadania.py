print("===========1==========")
def wypisz(nazwa, n):
	with open(nazwa) as plik:
		wiersze = plik.readlines()
		print("n poczatkowych wierszy")
		print(wiersze[:n])	
		print("n koncocyh wierszy")
		print(wiersze[-n:])
		print("co n-ty wiersz")
		print(wiersze[::n])
		print("n-te slowo w wierszu")
		for i in wiersze:
			print(i.split(' ')[n])
		print("n-ty znak")
		for i in wiersze:
			print(i[n])


wypisz("plik.txt", 3)

print("==============2=========")

def licz(nazwa, sprawdz, zastap):
	licznik = 0
	#open("licz.txt", "w")
	with open(nazwa) as plik, open("licz.txt", "w") as zapis:
			for linia in plik:
				if linia.startswith(sprawdz):
					licznik += 1
					print(linia)
					zapis.write(linia.replace(sprawdz,zastap))
					zapis.write('\r\n')
					#linia.replace(sprawdz, zastap)
					#print(linia,'\n')
	print(licznik)


licz("plik.txt","szosty","qwer")


print("==============3=========")
from glob import glob
pliki_in = glob("*.in")
lista_y = []
lista_x = []
slownik = {}
with open("wyniki.dat","w") as zapis:
	for pliki in pliki_in:
		with open(pliki) as plik:
			for linia in plik:
				linia = linia.split()
				slownik.setdefault(int(linia[0]), []).append(float(linia[1]))
			for key,value in slownik.items():
				zapis.write(str(key) + ' ' + str(sum(value)/len(value)) + ' ' + str(max(value) - min(value)) + '\r\n')




def plott(nazwa):
	print("==========4=========")
	with open("plot.p","w") as plot:
		plot.write('''set term png\r\nset out 'wynik.png'\r\nplot \'%s\' u 1:2 w l''' % nazwa)
		
plott("wyniki.dat")	



			







#print("==========4=========")
#	wynik_plik = '''set term png\r\nset out 'wynik.png'\r\nplot %s''' % zapis


print("===========5==========")

def znajdz():
	wszystkie = glob("*.py")
	slowa_w_pie = []
	with open(wszystkie[0]) as wiersze:
			for linie in wiersze:
				for slowo in linie.split(' '):
					if slowo not in slowa_w_pie:
				 		slowa_w_pie.append(slowo)
	#print(slowa_w_pie)
	temp = []
	for pliki in wszystkie[1:]:
		with open(pliki) as plik:
			wiersze = plik.readlines()
			for linie in wiersze:
				for slowo in linie.split(' '):
					if slowo not in temp:
						temp.append(slowo)
	wynik = []
	for i in temp:
		if i in slowa_w_pie:
			wynik.append(i)

	print(wynik)





znajdz()