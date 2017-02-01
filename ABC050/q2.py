# -*- coding:utf-8 -*-
N = int(input())
T = list(map(int,input().split()))
M = int(input())
P = [ list(map(int,input().split())) for i in range (M) ]

for tmp in range (M):
    ans = P[tmp][1]
    for tmp2 in range (N):
        if tmp2 == P[tmp][0] - 1:
            continue
        else:
            ans += T[tmp2]
    print(ans)
