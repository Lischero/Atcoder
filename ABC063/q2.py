# -*- coding:utf-8 -*-
S = list(input())
S.sort()
if ''.join(S) == ''.join(sorted(list(set(S)))):
    print("yes")
else:
    print("no")
