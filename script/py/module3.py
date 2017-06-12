#coding: UTF-8
list1 = raw_input()
list = list1.split()
lista = map(int,list)
print lista
#生売れ残り
a = lista[0]

b = a / 100.0

d = lista[1]
c = b * d*1.0
a1 = lista[0]
a2 = a1 - c
print str(a2)
#惣菜売れ残り
a3 = a2
e = lista[2]
f = a2 / 100.0
g = f * e*1.0
a4 = a3 - g
#最終
print str(a4)

