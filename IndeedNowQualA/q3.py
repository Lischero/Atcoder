# -*- coding:utf-8 -*-
N = int(input())
s = []
k = []
for tmp in range(N):
    a = int(input())
    if a != 0:
        s.append(a)
    else:
        pass
else:
    s.sort()
    s.reverse()

Q = int(input())
for tmp in range(Q):
    k.append(int(input()))

for tmp in k:
    if len(s) > tmp:
        print(s[tmp]+1)
    else:
        print(0)
