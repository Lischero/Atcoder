# -*- coding:utf-8 -*-
x,a,b = map(int, input().split())
if a-b >= 0:
    print("delicious")
else:
    if abs(a-b) <= x:
        print("safe")
    else:
        print("dangerous")
