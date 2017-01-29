# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
f = list(set(A))
s = N - len(f) #重複枚数検出

if s%2 == 0:
    print(len(f)) #fが奇数 sが偶数。2枚ずつ取り出すから。
else:
    print(len(f) - 1)
