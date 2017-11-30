# -*- coding:utf-8 -*-
N, K = map(int, input().split())
factor = 0
ans = -1
for tmp in range(1,N+1):
    factor += int(input())
    if K <= factor and ans == -1:
        ans = tmp
print(ans)
