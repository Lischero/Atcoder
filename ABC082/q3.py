# -*- coding:utf-8 -*-
from collections import Counter
n = int(input())
a = list(map(int, input().split()))
b = Counter(a)
ans = 0
for tmp in list(set(a)):
    if b[tmp] > tmp:
        ans += b[tmp]-tmp
    elif b[tmp] < tmp:
        ans += b[tmp]
    else:
        continue
else:
    print(ans)
