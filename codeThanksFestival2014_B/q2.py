# -*- coding:utf-8 -*-
import itertools
a,b,c = (int(input()), int(input()), int(input()))
factors = list(itertools.product(['+','*'],['+','*']))
ans = float('-inf')
for tmp in factors:
    factor = 0
    if tmp[0] == '+':
        factor += a+b
    else:
        factor += a*b
    if tmp[1] == '+':
        factor += c
    else:
        factor *= c
    ans = max(ans, factor)
print(ans)
