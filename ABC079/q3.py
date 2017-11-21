# -*- coding:utf-8 -*-
import itertools
a = list(map(int, list(input())))
factor = list(itertools.product(['+', '-'], repeat=3))
for tmp in factor:
    op1 = tmp[0]
    op2 = tmp[1]
    op3 = tmp[2]
    if op1 == '+':
        ans = a[0]+a[1]
    else:
        ans = a[0]-a[1]
    if op2 == '+':
        ans += a[2]
    else:
        ans -= a[2]
    if op3  == '+':
        ans += a[3]
    else:
        ans -= a[3]
    if ans == 7:
        print(str(a[0])+op1+str(a[1])+op2+str(a[2])+op3+str(a[3])+'=7')
        break
    else:
        pass
