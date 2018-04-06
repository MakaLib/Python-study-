
#1
print("\n1\n")
def palindrom(p):
	return str(p) == str(p)[::-1]

print(palindrom(14))
print(palindrom(55))
print(palindrom(678876))

#2
print("\n2\n")
import random
s1 = {}
i = 0
while i < 100:
	k = random.randrange(100,10000)
	if k not in s1:
		s1[k] = palindrom(k)
		i+=1
print(s1)

#3
print("\n3\n")
lista = [random.randrange(0,20) for i in range(100)]
print(lista)
parzy = {}
nieparz = {}
for i,j in enumerate(lista):
	if i%2:
		#setdefault(szukany KLUCZ, zwracana wartosc gdy nie ma danego klucza)
		parzy.setdefault(i,[]).append(j)
	else:
		nieparz.setdefault(i,[]).append(j)
print(parzy)
print(nieparz)

k = int(len(parzy)/2)
print(k)
mediana = parzy[k]
print(mediana)


#4
print("\n4\n")
from sys import argv

if len(argv) > 1:
	s2 = {k:random.randrange(2,15) for k in range(int(argv[1]))}
	print(s2)
	lista2 = [(j,i) for i,j in s2.items()]
	print(lista2)
	s2_odw={s2[k]:k for k in s2}
	print(s2_odw)

#5
print("\n5\n")
lista3 = [random.randrange(0,11) for k in range(100)]
s3 = {i:[] for i in range(0,11)}
num = 0
for k in lista3:
	s3[k].append(lista3.index(k,num))
	num += 1
print("\n",s3)



#6
print("\n6\n")
s4 = {k:random.randrange(1,100) for k in range(10)}
s5 = {k:random.randrange(1,100) for k in range(10)}
s4 = {w:k for k,w in s4.items()}
s5 = {w:k for k,w in s4.items()}
print(s4)
print(s5)

s6 = {k:(s4[k],s5[k]) for k in s4 if k in s5}
print(s6)
