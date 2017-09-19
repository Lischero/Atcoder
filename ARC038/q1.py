# -*- coding:utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
A.sort()
A.reverse()
ans = 0
for tmp in [ tmp2 for tmp2 in range(N) if tmp2%2 == 0 ]:
    ans += A[tmp]
print(ans)
