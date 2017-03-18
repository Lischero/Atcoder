# -*- coding:utf-8 -*-
W, a, b = map(int, input().split())
a2 = a+W
b2 = b+W
if a2 < b:
    print(b - a2)
elif b2 < a:
    print(a - b2)
else:
    print(0)
