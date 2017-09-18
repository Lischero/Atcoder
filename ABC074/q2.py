# -*- coding:utf-8 -*-
N = int(input())
K = int(input())
x = list(map(int, input().split()))
ans = 0
for tmp in range(N):
    ans += min(x[tmp]*2, abs(K-x[tmp])*2)
print(ans)
