#!/usr/bin/env python3
from sys import argv

if(len(argv) == 1):
	print("Wpisz prawidlowa liczbe parametrow!")
else:
	our_string = ''.join(argv[1:])

print(our_string)

lowel = [el for el in our_string if el.islower()]
print(lowel)
highel = [el for el in our_string if el.isupper()]
print(highel)
digitel = [int(el) for el in our_string if el.isdigit()]
print(digitel)
notchar = [el for el in our_string if not el.isalpha()]
print(notchar)

norepeat = []
for el in lowel:
	if el not in norepeat:
		norepeat.append(el)
print(norepeat)

new_tuple = [(el,lowel.count(el)) for el in norepeat]
print(new_tuple)

def getSecond(elem):
	return elem[1]


new_tuple.sort(key = getSecond, reverse = True)
print(new_tuple)

a = len([el for el in our_string if el in "aeioyuAEIOUY"])
print(a)
b = len(our_string) - a - len(notchar)
print(b)

my_list = [(el,a*el+b) for el in digitel]
print(my_list)

x_sr = sum(el[0] for el in my_list)
y_sr = sum(el[1] for el in my_list)

x_sr = float(x_sr/len(my_list))
y_sr = float(y_sr/len(my_list))
print(x_sr,y_sr)
D = sum(((el[0] - x_sr)**2) for el in my_list)
temp = sum((el[1]*(el[0]-x_sr)**2) for el in my_list)


a = 1.0/D * temp
b = y_sr - a * x_sr
print(a,b)

print("Prawda" if 10>5 else "Falsz")
