# -*- coding:utf-8 -*-
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
for tmp in range(k):
    ans += a[tmp]+tmp
print(ans)
