#coding: UTF-8
#式：(x-a)^2+(y-b)^2=>r^2
list1 = raw_input()
list2 = list1.split(" ")
a1 = int(list2[0])
b1 = int(list2[1])
r1 = int(list2[2])
N = int(raw_input())

roop = 0
while N > roop:
    roop += 1
    list3 = raw_input()
    list4 = list3.split(" ")
    x1 = int(list4[0])
    y1 = int(list4[1])
    ans1 = (x1-a1)**2
    ans2 = (y1-b1)**2
    ans = ans1 + ans2
    r = r1**2
    if ans < r:
        print "noisy"
    else:
        print "silent"



