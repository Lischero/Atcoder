# -*- coding:utf-8 -*-
import math
a, b = input().split()
factor = math.sqrt(int(a+b))
if factor == int(factor):
    print("Yes")
else:
    print("No")
