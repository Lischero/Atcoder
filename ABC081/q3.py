# -*- coding:utf-8 -*-
from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(set(a))
c = Counter(a)
d = sorted(c.items(), key = lambda tmp: tmp[1])
ans = 0
if len(b) > k:
    e = len(b)
    for tmp in range(len(d)):
        if e == k:
            print(ans)
            break
        else:
            ans += (d[tmp])[1]
            e -= 1
else:
    print(ans)
