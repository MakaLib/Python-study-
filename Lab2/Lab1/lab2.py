#!/usr/bin/env_python3.6

#metody działania na listach sort, diverse?,

l = [7,5,3,1]
print(l)
#to niżej nie ma sensu bo l ma none
#l = l.sort()
#print(l)
#w 2 jest cmp do sortowania tylko w 2.x
#cmp=lambda x,y : cmp(y,x)

key = lambda x: x[1]

l.sort()
print(l)

l1 = sorted(l)
print(l1)