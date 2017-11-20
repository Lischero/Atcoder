# -*- coding:utf-8 -*-
n = int(input())
a = [ 2, 1 ]
for tmp in range(85):
    a.append(a[tmp]+a[tmp+1])
print(a[n])
