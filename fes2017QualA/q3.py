# -*- coding:utf-8 -*-
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
kind = len(table2)
#わからん．飛ばし．
