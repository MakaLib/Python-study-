funckje:

zwroacanie wartosci
return a,b,c - zwracamy wtedy krotke (niejawnie), nie mozna zwrocic wiecej niz jedego obiektu
zawsze cos zwraca

def funkcja(a,*b,**c)   a - jeden parametr
						*b - zmienna liczba parametrow,wewnatrz funkcji b jest krotka
						**c - slownik

def fun(a=5,b=4)

mozna wywolac na wiele sposobo
fun(b=4,a=3) tak mozna(musimy znac nazwy parametrow)
fun()


def func():
	pass
nic nie zwracamy(chyba)

operator is zawsze prownuje referencje

funkcja moze odwolywac sie do zmiennych zewnetrznych(zle)

eval() oblicza wartosc wyrazenia ktore ma w srodku
x=7
eval('3*x+5')
x = {}.format(zmienna)
do {} mozemy wpisac
-index parametru
-formatowanie {1:3} 
				{mozna pominac:}