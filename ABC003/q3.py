# -*- coding:utf-8 -*-
N, K = map(int, input().split())
R = list(map(int, input().split()))
C1 = C2 = 0
sorted_R = sorted(R)
reversed_R = list(reversed(sorted_R))
for tmp in range(N-K,N):
    C1 = (C1+sorted_R[tmp])/2
for tmp in range(K):
    C2 = (C2+reversed_R[tmp])/2
print(max(C1,C2))
