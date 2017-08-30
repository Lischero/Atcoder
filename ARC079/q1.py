# -*- coding:utf-8 -*-
import sys
N, M = map(int, input().split())
A = [ 0 for tmp in range(N) ]
B = [ 0 for tmp in range(N) ]
for tmp in range(M):
    a, b = map(int, input().split())
    if a == N or b == N:
        c = a if a != N else b
        B[c-1] = 1
    if a == 1 or b == 1:
        c = a if a != 1 else b
        A[c-1] = 1

for tmp in range(N):
    if A[tmp] and B[tmp]:
        print('POSSIBLE')
        sys.exit()
print('IMPOSSIBLE')
