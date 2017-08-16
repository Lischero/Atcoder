# -*- coding:utf-8 -*-
import math
N = int(input())
c = []
for tmp in range(N):
    a, b = map(int, input().split())
    c.append(a*b)
print(math.floor(sum(c)*1.05))
