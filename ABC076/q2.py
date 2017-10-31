# -*- coding:utf-8 -*-
import itertools
N, K = (int(input()), int(input()))
num = 1
for tmp in range(N):
    a = 2*num
    b = num+K
    num = min(a,b)
print(num)
