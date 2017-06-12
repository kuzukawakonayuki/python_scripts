import csv

FILE = 'sample.csv'

title = ['a', 'b', 'c', 'd', 'e']
mylist = [[10, 68, 43, 25, 64],
          [42, 62, 34, 67, 36],
          [44, 41, 59, 77, 68],
          [90,  7, 24, 91, 82],
          [42, 64, 43,  6, 96],
          [76, 74, 62, 64, 66],
          [ 1, 96, 91,  0, 79]]

f = open(FILE, 'wb')

c = csv.writer(f)  # CSV??????????????
c.writerow(title)  # 1?????
c.writerows(mylist)  # ???????

f.close()