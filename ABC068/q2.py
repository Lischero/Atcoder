# -*- coding:utf-8 -*-
N = int(input())
a = [tmp for tmp in reversed(range(1,N+1)) if tmp%2 == 0]
ans = 0
for tmp in range(7):
    if N == 1:
        ans = 1
        break
    b = [tmp2//2 for tmp2 in a if tmp2%2 == 0]
    if len(b) != 0:
        ans += 1
    else:
        ans = (2**ans)*a.pop()
        break
    a = [tmp2 for tmp2 in b]
print(ans)
