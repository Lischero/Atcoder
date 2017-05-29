# -*- coding:utf-8 -*-
from functools import reduce
import sys, itertools
N, K = map(int, input().split())
T = []
for tmp in range(N):
    T.append(list(map(int, input().split())))
a = list(itertools.product(*(T)))
for tmp in a:
    if reduce(lambda x,y:x^y, tmp) == 0:
        print("Found")
        sys.exit()
    else:
        pass
print("Nothing")
