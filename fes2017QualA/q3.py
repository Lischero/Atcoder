# -*- coding:utf-8 -*-
import math, sys
h,w = map(int, input().split())
a = [ list(input()) for y in range(h) ]
table = {}
table2 = []
for y in range(h):
    for x in range(w):
        if a[y][x] in table:
            table[a[y][x]] += 1
        else:
            table[a[y][x]] = 1
            table2.append(a[y][x])

size2 = math.floor(h/2)+math.floor(w/2)
size4 = math.floor(h/2)*math.floor(w/2)

for tmp in table2:
    if table[tmp]%4 == 1 or table[tmp]%4 == 3:
        table[tmp] -= 1
        break

for tmp in table2:
    if table[tmp]%4 == 2:
        table[tmp] -= 2
        size2 -= 1
        if size2 == 0:
            break

for tmp in table2:
    if table[tmp]%4 == 0 and table[tmp] != 0:
        table[tmp] -= 4
        size4 -= 1
        if size4 == 0:
            break

for tmp in table2:
    if table[tmp] != 0:
        print("No")
        sys.exit()
else:
    print("Yes")
