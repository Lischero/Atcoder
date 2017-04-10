# -*- coding:utf-8 -*-
A = list(input())
w = A.pop()
if len(A) == 0:
    if w == 'a':
        print(-1)
    else:
        print(chr(ord(w)-1))
else:
    A = ''.join(A)
    print(A)
