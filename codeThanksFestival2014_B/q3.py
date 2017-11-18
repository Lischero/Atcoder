# -*- coding:utf-8 -*-
n = int(input())
v = list(map(int, input().split()))
f = list(map(int, input().split()))
ans = 0
for tmp in range(n):
    if v[tmp]/2 < f[tmp]:
        ans += 1
    else:
        pass
print(ans)
