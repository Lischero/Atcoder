# -*- coding:utf-8 -*-
import sys
N, K = map(int, input().split())
ans = []
for tmp in range(N):
    a, b = map(int, input().split())
    ans.append((a,b))
ans.sort()
s = 0
for tmp in range(len(ans)):
    s += (ans[tmp])[1]
    if s >= K:
        print((ans[tmp])[0])
        sys.exit()
