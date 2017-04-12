# -*- coding:utf-8 -*-
N = int(input())
A = []
for tmp in range(N):
    A.append(int(input()))
print(sorted(list(set(A)))[-2])
