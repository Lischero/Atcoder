# -*- coding:utf-8 -*-
import math, itertools
N = int(input())
C = ( int(input()) for tmp in range(N) )
l = list(itertools.permutations(C))
a = [ True for tmp in range(N) ]
ans = 0
for tmp in range(len(l)):
    for tmp2 in range(N):
        for tmp3 in range(tmp2+1, N):
            if (l[tmp])[tmp3]%(l[tmp])[tmp2] != 0:
                pass
            else:
                a[tmp3] = not (a[tmp3])
    ans += a.count(True)
    a = [ True for tmp in range(N) ]
ans /= math.factorial(N)
print(ans)
