# -*- coding:utf-8 -*-
a, b = (int(input()), int(input()))
if a%b != 0:
    print(b - a%b)
else:
    print(0)
