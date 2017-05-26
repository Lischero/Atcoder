# -*- coding:utf-8 -*-
N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())
L = [ 0 for tmp in range(N+1) ]
L[0] = H
ans = 0
for tmp in range(N):
    a,b,c = (L[tmp]+B, L[tmp]+D, L[tmp]-E)
    if c > 0:
        L[tmp+1] = c
    elif a > 0 or b > 0:
        L[tmp+1] = min(a,b)
        if L[tmp+1] == b:
            ans += C
        else:
            ans += A
print(L)
print(ans)
