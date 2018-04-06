## Cwiczenia 2

# Zadanie 1

print ("\nZadanie 1")
from math import sqrt

def is_prime (a):
    for i in range(2, int(sqrt(a))+1):
        if a % i == 0:
            return False
    return True

print (is_prime(2))
print (is_prime(5))
print (is_prime(10))
print (is_prime(17))

# Zadanie 2
print ("\nZadanie 2")
import random
s = {}
i = 0
while i <50:
    k = random.randrange(0, 100)
    if k not in s:
        s[k] = is_prime(k)
        i+=1

print (s)

# Zadanie 3
print ("\nZadanie 3")
L = [ random.randrange(0,20) for i in range(100)]
print (L)
s1 = {}
s2 = {}
print (s1)
print (s2)
curren_index = 0
for j, i in enumerate(L):
    if not i%2:
            s1.setdefault(i, []).append(j)
    else:
            s2.setdefault(i, []).append(j)
print (s1, "\n")
print (s2, "\n")

      
s3 = { k : s1[k] if [j for j in s1[k] if j%3] else (min(s1[k]), max(s1[k])) for k in s1 }
print (s3, "\n")

# Zadanie 4
print ("\nZadanie 4")
from sys import argv

if len(argv) > 1:
    di = { i : random.randrange(2, 15) for i in range(int(argv[1]))}
    print (di)
    l = [(j, i) for i,j in di.items()]
    print (l)
    newdi = { di[i] : i for i in di}
    print (newdi)

# Zadanie 5
print ("\nZadanie 5")
newlist = [random.randrange(0, 11) for i in range(100)]
print (newlist)

newdi = { i : [] for i in range(0,11)}
print (newdi)
current_index = 0
for i in newlist:
    newdi[i].append(newlist.index(i, current_index))
    current_index+=1

print (newdi)

#Zadanie 6
print ("\nZadanie 6")
s1 = { k : random.randrange(1, 100) for k in range(1, 11) }
s2 = { k : random.randrange(1, 100) for k in range(1, 11) }
print (s1, "\n")
print (s2, "\n")

s1 = { s1[i] : i for i in s1}
s2 = { s2[i] : i for i in s2}
print (s1, "\n")
print (s2, "\n")


s3 = { k : (s1[k], s2[k]) for k in s1 if k in s2}
print (s3)



               
    
