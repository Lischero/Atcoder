# -*- coding:utf-8 -*-
a,b,c,d = map(int, input().split())
if min(b,d) >= max(a,c):
    print(min(b,d)-max(a,c))
else:
    print(0)
