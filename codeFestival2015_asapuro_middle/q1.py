# -*- coding:utf-8 -*-
n,k,m,r = map(int, input().split())
a = [ int(input()) for tmp in range(n-1) ]
a.sort()
a.reverse()
factors = a[0:k]
average = sum(factors)/k

if average >= r:
    print(0)
else:
    factors.pop()
    ans = r*k-sum(factors)
    if ans <= m:
        print(ans)
    else:
        print(-1)
