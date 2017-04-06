# -*- coding:utf-8 -*-
l = []
factor_num = 3
for tmp in range(4):
    tmp2 = list(input())
    l.append(tmp2)
while factor_num >= 0:
    l[factor_num].reverse()
    ans = ''.join(l[factor_num])
    print(ans)
    factor_num -= 1
