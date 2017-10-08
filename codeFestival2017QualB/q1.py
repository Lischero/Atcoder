# -*- coding:utf-8 -*-
S = list(input())
l = len(S)
for tmp in reversed(range(len(S))):
    S.pop(tmp)
    if tmp == l-8:
        break
print(''.join(S))
