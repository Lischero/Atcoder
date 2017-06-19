# -*- coding:utf-8 -*-
import math, itertools, operator
ABC = list(map(int,input().split()))
itr = list(itertools.accumulate(ABC, operator.mul))
if itr[len(itr)-1] == 0:
    print(0)
else:
    maximum = max(max(ABC[0],ABC[1]), ABC[2])
    ABC.remove(maximum)
    a = math.floor(maximum/2)
    b = maximum-a
    c = list(itertools.accumulate(ABC, operator.mul))
    print(abs( (c[len(c)-1]*a) - (c[len(c)-1]*b)) )
