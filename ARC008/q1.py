# -*- coding:utf-8 -*-
import math
N = int(input())
a = (N//10)*100
b = (N%10)*15
factor1 = a+b
a = math.ceil(N/10)*100
b = N*15
factor2 = min(a, b)
print(min(factor1,factor2))
