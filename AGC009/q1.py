# -*- coding:utf-8 -*-
N = int(input())
A = []
B = []
ans = 0
for tmp in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)
for tmp in reversed(range(N)):
    factor = (A[tmp]+ans)
    if factor%B[tmp] != 0:
        ans += ((factor//B[tmp])+1)*B[tmp]-factor
print(ans)
