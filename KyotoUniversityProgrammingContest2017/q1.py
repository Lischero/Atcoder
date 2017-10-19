# -*- coding:utf-8 -*-
import sys
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a.reverse()
count = 0
unit = 0
if sum(a) < k:
    print(-1)
    sys.exit()
for tmp in range(n):
    count += 1
    unit += a[tmp]
    if k <= unit:
        print(count)
        sys.exit()
