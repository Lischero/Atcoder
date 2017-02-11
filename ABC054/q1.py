# -*- coding:utf-8 -*-
import sys
A, B = map(int, input().split())
if A == B:
    print("Draw")
    sys.exit()
if A > B:
    if B == 1:
        print("Bob")
    else:
        print("Alice")
else:
    if A == 1:
        print("Alice")
    else:
        print("Bob")
