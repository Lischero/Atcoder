# -*- coding:utf-8 -*-
N = int(input())
a = list(map(int, input().split()))
dp = [ 0 for tmp in range(N) ]
for tmp in range(1,N):
    if tmp-1 >= 0:
        if tmp-2 >= 0:
            dp[tmp] = min(dp[tmp-1]+abs(a[tmp]-a[tmp-1]), dp[tmp-2]+abs(a[tmp]-a[tmp-2]))
        else:
            dp[tmp] = dp[tmp-1]+abs(a[tmp]-a[tmp-1])
print(dp[N-1])
