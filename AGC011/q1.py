# -*- coding:utf-8 -*-
N, C, K = map(int, input().split())
T = sorted([ int(input()) for tmp in range(N) ])
minTime = T[0]
maxTime = T[0]+K
counter = 1
line = 0
for tmp in range(1,N):
    if counter == C:
        counter = 1
        line += 1
        maxTime = T[tmp]+K
        minTime = T[tmp]
    else:
        minTime = max(minTime, T[tmp])
    if maxTime < minTime:
        line += 1
        maxTime = T[tmp]+K
        minTime = T[tmp]
        counter = 1
        continue
    counter += 1
print(line+1)
