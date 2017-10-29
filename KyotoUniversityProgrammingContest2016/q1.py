# -*- coding:utf-8 -*-
N, A, B = map(int, input().split())
t = []
for tmp in range(N):
    t.append(int(input()))
print(len([tmp for tmp in t if tmp < A or B <= tmp]))
