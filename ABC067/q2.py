# -*- coding:utf-8 -*-
N, K = map(int, input().split())
l = sorted(list(map(int, input().split())), reverse = True)
ans = 0
for tmp in range(K):
    ans += l[tmp]
print(ans)
