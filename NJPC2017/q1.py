# -*- coding:utf-8 -*-
L = int(input())
S = list(input())
if len(S) < L:
    print(''.join(S))
else:
    print(''.join(S[0:L]))
