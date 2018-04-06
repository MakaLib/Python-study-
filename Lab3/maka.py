print("========1=======")

from math import sqrt
def isPrime(a):
	for i in range(2,int(sqrt(a)) + 1):
		if a % i == 0:
			return False
	return True

print(isPrime(9))
print(isPrime(19))

print("==========2=========")
from random import *
direc = {}
i = 0
while i < 50:
	k = randrange(0,100)
	if k not in direc:
		direc[k] = isPrime(k)
		i = i+1
print(direc)

print("==========3=========")
lista = [randrange(0,20) for x in range(100)]
parzy = {}
nieparzy = {}
for i,j in enumerate(lista):
	if j%2:
		nieparzy.setdefault(j,[]).append(i)
	else:
		parzy.setdefault(j,[]).append(i)
print(nieparzy)
print(parzy)
weird = {k:parzy[k] if[i for i in parzy[k] if i%3==0] else (max(parzy[k]),min(parzy[k])) for k in parzy}
print(weird)

print("============4=======")
from sys import argv

if(len(argv[:]) > 1):
	my_dir  = {i:randrange(2,15) for i in range(int(argv[1]))}
	print(my_dir)
	my_list = [(j,i) for i,j in my_dir.items()]
	print(my_list)
	my_new_dir = {j:i for i,j in my_dir.items()}
	print(my_new_dir)

print("===========5=========")
new_list = [randrange(0,11) for i in range(100)]
dire = {i : [] for i in range(11)}
j = 0
for i in new_list:
	dire[i].append(new_list.index(i,j))
	j = j+1
print(dire)