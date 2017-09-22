# -*- coding:utf-8 -*-
q,h,s,d = map(int, input().split())
n = int(input())
s = min(s, 2*min(h, 2*q))
if 2*s >= d:
    print(d*(n//2)+s*(n%2))
else:
    print(s*n)
