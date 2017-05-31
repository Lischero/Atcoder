# -*- coding:utf-8 -*-
import sys, itertools, operator
N, M = map(int, input().split())
juwels = [ 0 for tmp in range(M) ]
lrs, ans = ( [], 0 )
for tmp in range(N):
    l, r, s = map(int, input().split())
    lrs.append((l,r,s))
    ans += s
    juwels[l-1] += 1
    if r != M:
        juwels[r] -= 1
    else:
        pass
juwels = list(itertools.accumulate(juwels, operator.add))
if 0 in juwels:
    print(ans)
    sys.exit()
else:
    minimum = min(juwels)
    lrs.sort(key = lambda x:x[2])
    for tmp,tmp2,tmp3 in lrs:
        if minimum in juwels[tmp-1:tmp2]:
            a = [ juwels[tmp4]-1 for tmp4 in range(tmp-1, tmp2) ]
            juwels[tmp-1:tmp2] = a
            ans -= tmp3
            minimum -= 1
            if minimum == 0:
                break
        else:
            pass
    print(ans)
