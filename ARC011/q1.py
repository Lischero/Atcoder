# -*- coding:utf-8 -*-
m, n, N = map(int, input().split())
ans = N
mod = 0
while N+mod >= m:
    mod += N%m
    ans += n*(N//m)
    if mod >= m:
        ans += n*(mod//m)
        N = n*((N//m)+(mod//m))
        mod -= m*(mod//m)
    else:
        N = n*(N//m)
print(ans)
