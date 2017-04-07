# -*- coding:utf-8 -*-
N = int(input())
T = []
for tmp in range(N):
    T.append(int(input()))
print(min(sorted(T)))
