# -*- coding:utf-8 -*-
n = int(input())
a = list(map(int, input().split()))
ans = 0
for tmp in range(n-1):
    ans += a[tmp+1] - a[tmp]
print(ans/(n-1))
