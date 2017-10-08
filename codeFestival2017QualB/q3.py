# -*- coding:utf-8 -*-
n,m = map(int, input().split())
l = [ [ 0 for x in range(n) ] for y in range(n) ]
for tmp in range(m):
    a, b = map(int, input().split())
    l[a-1][b-1] = 1
    l[b-1][a-1] = 1
for start in range(n):
    print(l[start])
