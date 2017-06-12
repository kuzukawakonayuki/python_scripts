#coding: UTF-8
#式：r1=<(x-xc)^2+(y-yc)^2=<r2
list1 = raw_input()
list2 = list1.split(" ")
xc = int(list2[0])
yc = int(list2[1])
r1 = int(list2[2])
r2 = int(list2[3])
ans1 = r1**2
ans2 = r2**2
n = int(raw_input())
roop = 0
while n > roop:
    roop += 1
    list3 = raw_input()
    list4 = list3.split(" ")
    x = int(list4[0])
    y = int(list4[1])
    a = (x-xc)**2
    b = (y-yc)**2
    ans = a + b
    if ans1 <= ans <= ans2:
        print"yes"
    else:
        print"no"
