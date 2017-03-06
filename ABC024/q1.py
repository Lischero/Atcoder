# -*- coding:utf-8 -*-
A, B, C, K = map(int, input().split())
S, T = map(int, input().split())
total = S+T
if total >= K:
    A -= C
    B -= C
print(A*S+B*T)
