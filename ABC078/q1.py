# -*- coding:utf-8 -*-
d = { 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15 }
x, y = input().split()
if d[x] > d[y]:
    print(">")
elif d[x] < d[y]:
    print("<")
else:
    print("=")

