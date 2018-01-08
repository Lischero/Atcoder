# -*- coding:utf-8 -*-
import math
n, h = map(int, input().split())
l = []
ans = 0

for tmp in range(n):
    a, b = map(int, input().split())
    l.append((a,b))

factor = sorted(l, key=lambda tmp:tmp[1])
max_a = max(l, key=lambda tmp:tmp[0])
while h > 0:
    if len(factor) != 0:
        max_b = factor[-1]
    else:
        max_b = (-1,-1)
    if max_a[0] < max_b[1]:
        h -= max_b[1]
        factor.pop()
        ans += 1
    else:
        ans += math.ceil(h/max_a[0])
        h -= max_a[0]*math.ceil(h/max_a[0])
print(ans)
