# -*- coding:utf-8 -*-
n,a,b = map(int, input().split())
if n >= a+b:
    print(0)
else:
    print((a+b)-n)
