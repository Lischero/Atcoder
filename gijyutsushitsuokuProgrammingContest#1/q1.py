# -*- coding:utf-8 -*-
N = int(input())
ans = [ sum(list(map(int, input().split()))) for tmp in range(N) ]
for tmp in range(N):
    print(ans[tmp])
