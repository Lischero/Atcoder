# -*- coding:utf-8 -*-
N = int(input())
a = { int(input()):tmp for tmp in range(1,N+1) }
for tmp in range(1, N+1):
    if a[tmp] == 1:
        print("100000")
    elif a[tmp] == 2:
        print("50000")
    elif a[tmp] == 3:
        print("30000")
    elif a[tmp] == 4:
        print("20000")
    elif a[tmp] == 5:
        print("10000")
    else:
        print("0")
