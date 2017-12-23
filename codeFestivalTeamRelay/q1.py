# -*- coding:utf-8 -*-
from decimal import *
import math
k,a,b = map(int, input().split())
if a >= k:
    print(1)
else:
    if a <= b:
        print(-1)
    else:
        print(2*math.ceil(Decimal(k-a)/Decimal(a-b))+1)
