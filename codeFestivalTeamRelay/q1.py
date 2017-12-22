# -*- coding:utf-8 -*-
import math
k,a,b = map(int, input().split())
if a >= k:
    print(1)
else:
    if a <= b:
        print(-1)
    else:
        print((2*math.floor((k-a)/(a-b)))+1)
