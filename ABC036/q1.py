# -*- coding:utf-8 -*-
A, B = map(int, input().split())
if A <= B:
    tmp = B//A
    B -= A*tmp
    if B > 0:
        print(tmp+1)
    else:
        print(tmp)
else:
    print(1)

