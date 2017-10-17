# -*- coding:utf-8 -*-
import functools, math
N, K = map(int, input().split())
A = list(map(int, input().split()))
a = functools.reduce(math.gcd, A)
b = max(A)
if K%a == 0 and K <= b:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
