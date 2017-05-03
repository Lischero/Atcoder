# -*- coding:utf-8 -*-
import math, sys
N = int(input())
S, P, total = ([], [], 0)
for tmp in range(N):
    s, l = input().split()
    S.append(s)
    P.append(int(l))
    total += P[tmp]
if total%2 != 0:
    comparison = math.ceil(total/2)
else:
    comparison = total/2+1
for tmp in range(N):
    if comparison <= P[tmp]:
        print(S[tmp])
        sys.exit()
    else:
        pass
print('atcoder')
