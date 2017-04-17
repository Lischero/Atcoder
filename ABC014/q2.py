# -*- coding:utf-8 -*-
n, X = map(int, input().split())
price = list(map(int, input().split()))
l = list(map(int,format(X,'b').zfill(n)))
ans = 0
l.reverse()
for tmp in range(len(l)):
    if l[tmp] == 1:
        ans += price[tmp]
print(ans)
