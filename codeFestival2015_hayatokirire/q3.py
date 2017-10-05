# -*- coding:utf-8 -*-
import math
N = int(input())
a = list(str(math.pi))
a.pop(1)
a = list(map(int, a))
for index, value in enumerate(a):
    if N == 0:
        print(32)
        break
    if value == N:
        print(index)
        break
