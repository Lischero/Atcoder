# -*- coding:utf-8 -*-
n, k = map(int, input().split())
factors = [ list(map(int, input().split())) for _ in range(n) ]
ans = 0
for tmp in range(k):
    factors.sort(key = lambda tmp2: tmp2[0])
    ans += (factors[0])[0]
    (factors[0])[0] += (factors[0])[1]
else:
    print(ans)
