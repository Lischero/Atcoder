# -*- coding:utf-8 -*-
A, B, C = map(int, input().split())
if A == B and B == C:
    if A%2 != 0:
        print(0)
    else:
        print(-1)
else:
    ans = 0
    while A%2 == 0 and B%2 == 0 and C%2 ==0:
        a = (B+C)/2
        b = (A+C)/2
        c = (A+B)/2
        A = a
        B = b
        C = c
        ans += 1
    print(ans)
