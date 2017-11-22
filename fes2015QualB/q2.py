# -*- coding:utf-8 -*-
from collections import Counter
N, M = map(int, input().split())
a = list(map(int, input().split()))
b = Counter(a)
c = [ num[1] for num in b.most_common() ]
if b.most_common(1)[0][1] <= N/2 or (len(list(set(c))) == 1 and len(c) > 1):
    print('?')
else:
    print(b.most_common(1)[0][0])
