# -*- coding:utf-8 -*-
N = int(input())
a = sorted(list(map(int, input().split())))
ans = 0
for tmp in range(N, 3*N, 2):
    ans += a[tmp]
print(ans)
