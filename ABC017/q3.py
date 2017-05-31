# -*- coding:utf-8 -*-
import sys
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
for tmp in range(len(juwels)-1):
    juwels[tmp+1] += juwels[tmp]
lrs.sort(key = lambda x:x[2])
if 0 in juwels:
    print(ans)
    sys.exit()
else:
    minimum = min(juwels)
    for tmp in lrs:
        if minimum in juwels[tmp[0]-1:tmp[1]]:
            a = [ juwels[tmp2]-1 for tmp2 in range(tmp[0]-1, tmp[1]) ]
            juwels[tmp[0]-1:tmp[1]] = a
            ans -= tmp[2]
            minimum -= 1
        else:
            pass
        if minimum == 0:
            break
    print(ans)
