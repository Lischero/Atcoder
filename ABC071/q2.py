# -*- coding:utf-8 -*-
a = list('abcdefghijklmnopqrstuvwxyz')
S = list(input())
b = list(set(S))
for tmp in b:
    a.pop(a.index(tmp))
if len(a) == 0:
    print("None")
else:
    print(a.pop(0))
