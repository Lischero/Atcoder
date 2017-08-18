# -*- coding:utf-8 -*-
import itertools
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(max([ (a[0]//tmp[0]) * (a[1]//tmp[1]) * (a[2]//tmp[2]) for tmp in itertools.permutations(b, 3) ]))
