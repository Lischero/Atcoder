# -*- coding:utf-8 -*-
N, Q = map(int, input().split())
ans = [ 0 for tmp in range(N)]
l,r,t = ([], [], [])
for tmp in range(Q):
    L, R, T = map(int, input().split())
    l.append(L)
    r.append(R)
    t.append(T)
    for tmp2 in range (l[tmp]-1,r[tmp]):
        ans[tmp2] = t[tmp]
for tmp in range(N):
    print(ans[tmp])

