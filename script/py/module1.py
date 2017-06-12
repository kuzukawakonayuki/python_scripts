list1 = raw_input()
list2 = list1.split()
list = map(int, list2)
a = list[0] / list[1]
b = list[0] % list[1]
print str(a) + " " + str(b)