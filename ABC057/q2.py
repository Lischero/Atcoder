# -*- coding:utf-8 -*-
N, M = map(int, input().split())
coordinate = []
checkpoint = []
tmplist = []
for tmp in range(N):
    a, b = map(int, input().split())
    coordinate.append((a,b))
for tmp in range(M):
    c, d = map(int, input().split())
    checkpoint.append((c,d))
for i in range(N):
    for j in range(M):
        tmplist.append(abs(coordinate[i][0]-checkpoint[j][0])+abs(coordinate[i][1]-checkpoint[j][1]))
    print(tmplist.index(min(tmplist))+1)
    tmplist = []
