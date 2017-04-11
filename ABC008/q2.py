#-*- coding:utf-8 -*-
N = int(input())
S = []
for tmp in range(N):
    S.append(input())
l = list(set(S))
c = []
for tmp in range(len(l)):
    c.append(S.count(l[tmp]))
print(l[c.index(max(c))])
