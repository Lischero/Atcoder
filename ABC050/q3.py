# -*- coding:utf-8 -*-
import sys, math
N = int(input())
A = sorted(list(map(int,input().split())))
ans = 1
factor = 0

while factor < N:
    tmp = A.count(A[factor])
    if tmp >= 1 and tmp <= 2:
        if A[factor] == 0 and tmp == 2:
            print(0)
            sys.exit()
        else:
            ans *= tmp
            factor += tmp
            continue
    else:
        print(0)
        sys.exit()

print(ans%((10**9)+7))
