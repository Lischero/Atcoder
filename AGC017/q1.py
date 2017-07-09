# -*- coding:utf-8 -*-
import itertools, math
N, P = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
odd = [ tmp for tmp in a if tmp%2 != 0]
even = [ tmp for tmp in a if tmp%2 == 0]
d = math.factorial(len(odd))
e = math.factorial(len(even))
if P == 0:
    ans += 1
    b = sum([ (d//math.factorial(len(odd)-tmp))//math.factorial(tmp) for tmp in range(2, len(odd)+1, 2) ])
else:
    b = sum([ (d//math.factorial(len(odd)-tmp))//math.factorial(tmp) for tmp in range(1, len(odd)+1, 2) ])
c = [ (e//math.factorial(len(even)-tmp))//math.factorial(tmp) for tmp in range(1, len(even)+1) ]
for tmp in c:
    ans += tmp*b
else:
    if P == 0:
        ans += b+sum(c)
    else:
        ans += b
print(ans)
