#coding: UTF-8
n = int(raw_input())
nm = 0
y = [0,0,0,0]
while n > nm:
    nm += 1
    x = map(int, raw_input().split())
    while nm == 1:
        y = x
        ans0 = x[0]
        break
    while y[3] > x[3]:
        ans3 = x[3]
        y[3] = x[3]
        break
    while y[2] < x[2]:
        ans2 = x[2]
        y[2] = x[2]
        break
ans1 = x[1]
print str(ans0) +" "+ str(ans1) +" "+ str(ans2) +" "+ str(ans3)




