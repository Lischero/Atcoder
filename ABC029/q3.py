# -*- coding:utf-8 -*-
import itertools
N = int(input())
factor = ['a','b','c']
candinate = sorted([ ''.join(list(tmp)) for tmp in itertools.product(factor, repeat = N) ])
for ans in candinate:
    print(ans)
