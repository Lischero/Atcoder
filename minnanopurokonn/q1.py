# -*- coding:utf-8 -*-
import sys
s = list(input())
a = [ 1,1,1,2 ]
b = []
for tmp in list('yaho'):
    b.append(s.count(tmp))
for tmp in range(4):
    if a[tmp] != b[tmp]:
        print("NO")
        sys.exit()
print("YES")
