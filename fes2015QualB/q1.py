# -*- coding:utf-8 -*-
S = list(input())
a = []
for tmp in list(set(S)):
    a.append(tmp+tmp)
print(''.join(a))
