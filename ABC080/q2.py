# -*- coding:utf-8 -*-
N = list(input())
total = sum(list(map(int, N)))
if int(''.join(N))%total != 0:
    print("No")
else:
    print("Yes")
