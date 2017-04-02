# -*- coding:utf-8 -*-
A, B = map(int, input().split())
if A+B > 24:
    print(A+B-24)
elif A+B == 24:
    print(0)
else:
    print(A+B)
