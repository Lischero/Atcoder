# -*- coding:utf-8 -*-
N = int(input())
L = sorted(list(map(int, input().split())), reverse = True)
ans = 0
for tmp in range(0, len(L), 2):
    ans += min(L[tmp],L[tmp+1])
print(ans)
