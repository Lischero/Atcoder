# -*- coding:utf-8 -*-
import itertools
N, M, R = map(int, input().split())
r = list(map(int, input().split()))
d = [[0 for x in range(N)] for y in range(N)]
ans = float("inf")
for y in range(N):
    for x in range(N):
        d[y][x] = 0 if x == y else float('inf')

for tmp in range(M):
    a,b,c = map(int, input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c

for k in range(N):
    for y in range(N):
        if d[y][k] == float('inf'):
            continue
        for x in range(N):
            if d[k][x] == float('inf'):
                continue
            d[y][x] = min(d[y][x], d[y][k]+d[k][x])

for tmp in list(itertools.permutations(r)):
    factor = 0
    for tmp2 in range(0, len(tmp)-1):
        if d[tmp[tmp2]-1][tmp[tmp2+1]-1] != 0 and d[tmp[tmp2]-1][tmp[tmp2+1]-1] != float('inf'):
            factor += d[tmp[tmp2]-1][tmp[tmp2+1]-1]
        else:
            break
    ans = min(ans, factor)
print(ans)
