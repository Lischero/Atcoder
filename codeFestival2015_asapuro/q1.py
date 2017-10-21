# -*- coding:utf-8 -*-
import sys, math
N = int(input())
if math.sqrt(N) == int(math.sqrt(N)):
    print(0)
else:
    print((int(math.sqrt(N))+1)**2 - N)

