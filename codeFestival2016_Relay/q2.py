# -*- coding:utf-8 -*-
import sys
S = list(input())
a = list(reversed(S))
for tmp in range(len(a)):
    if a[tmp] == 'b':
        a[tmp] = 'd'
    elif a[tmp] == 'd':
        a[tmp] = 'b'
    elif a[tmp] == 'p':
        a[tmp] = 'q'
    else:
        a[tmp] = 'p'

    if S[tmp] != a[tmp]:
        print("No")
        sys.exit()

print("Yes")
