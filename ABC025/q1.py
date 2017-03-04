# -*- coding:utf-8 -*-
import itertools
S, N = (list(input()), int(input()))
S2 = S
l = sorted(list(itertools.product(S,S2)))
print(l[N-1][0]+l[N-1][1])
