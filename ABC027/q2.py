# -*- coding:utf-8 -*-
N = int(input())
a = list(map(int, input().split()))
total = sum(a)
if total%N != 0:
    print(-1)
else:
    unit = total//N
    bridge = 0
    factor = 0
    for tmp in range(N):
        factor += a[tmp]
        if factor != unit*(tmp+1):
            bridge += 1
        else:
            pass
    print(bridge)
