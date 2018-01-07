# -*- coding:utf-8 -*-
import math
n, h = map(int, input().split())
l = []
ans = 0
for tmp in range(n):
    a, b = map(int, input().split())
    l.append((tmp,a,b))
while h > 0:
    factor = sorted(l, key= lambda tmp:tmp[1])
    factor2 = sorted(l, key= lambda tmp:tmp[2])
    max_a = factor.pop()
    max_b = factor2.pop()
    if max_b[2] >= h:
        h = h-max_b[2]
        l.pop(max_b[0])
        ans += 1
    elif math.ceil((h-max_b[2])/max_a[1]) < math.ceil(h/max_a[1]) and len(l) >= 2:
        h = h-max_b[2]
        l.pop(max_b[0])
        ans += 1
    else:
        ans += math.ceil(h/max_a[1])
        h = h - max_a[1]*(math.ceil(h/max_a[1]))
    print(ans)
