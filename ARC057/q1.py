# -*- coding:utf-8 -*-
A, K = map(int, input().split())
ans = 0
if K != 0:
    while True:
        if A >= 2*(10**12):
            break
        A = (K+1)*A+1
        ans += 1
else:
    ans = 2*(10**12)-A
print(ans)
