#coding: UTF-8
li1 = raw_input()
li2 = raw_input()
li1s = li1.replace(" ", ",")
li2s = li1.replace(" ", ",")
li1s.split()
li2s.split()
list1 = map(int,li1s)
list2 = map(int,li2s)
from operator import mul
combined1 = [x * y for (x, y) in zip(list1, list2)]
print str(combined1)
