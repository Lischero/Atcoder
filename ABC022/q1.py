# -*- coding:utf-8 -*-
N, S, T = map(int, input().split())
W = int(input())
A = [0]
s = W
ans = 0
for tmp in range(N-1):
    A.append(int(input()))

for tmp in range(N):
    if s + A[tmp] <= T and s+A[tmp] >= S:
        ans += 1
    s += A[tmp]
print(ans)
