# -*- coding:utf-8 -*-
n, c = map(int, input().split())
l = [ int(input()) for _ in range(n) ]
l.sort()
ans = 0
while len(l) > 1:
    factor1 = l[0]
    factor2 = l[len(l)-1]
    if factor1+factor2+1 <= c:
        l.pop(0)
    l.pop()
    ans += 1
else:
    if len(l) == 1:
        ans += 1
print(ans)
