# -*- coding:utf-8 -*-
import math
from decimal import *
N = int(input())
A, B = (1, 1)
for tmp in range (N):
    t, a = map(int,input().split())
    n = Decimal(max([math.ceil(A/t),math.ceil(B/a)]))
    A = n*t
    B = n*a
print(A+B)

