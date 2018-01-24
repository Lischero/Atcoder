# -*- coding:utf-8 -*-
N = int(input())
change = 1000 - N
factors = [500, 100, 50, 10, 5, 1]
ans = 0
for factor in factors:
    while change >= factor:
        change -= factor
        ans += 1
print(ans)
