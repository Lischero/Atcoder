# -*- coding:utf-8 -*-
c = [ list(input()) for _ in range(2) ] 
a = list(reversed(c[1]))
b = list(reversed(c[0]))
if ''.join(c[0]) == ''.join(a) and ''.join(c[1]) == ''.join(b):
    print("YES")
else:
    print("NO")
