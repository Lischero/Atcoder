# -*- coding:utf-8 -*-
N,K = map(int,input().split())
ans = 0
for tmp in range (N):
    if tmp == 0:
        ans += K
    else:
        ans *= K - 1
print(ans)
