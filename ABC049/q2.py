# -*- coding:utf-8 -*-
HW = list(map(int, input().split()))
c = [input() for i in range (HW[0])]
ans = []
for i in range( HW[0] ):
    ans.append(c[i])
    ans.append(c[i])
for i in range ( 2*HW[0] ):
    print(ans[i])

