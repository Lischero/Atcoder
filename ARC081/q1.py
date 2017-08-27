# -*- coding:utf-8 -*-
import sys
from collections import Counter
N = int(input())
A = list(map(int, input().split()))
a = Counter(A)
width = -1
height = -1
candinate = []
for tmp in reversed(sorted(list(set(A)))):
    b = a[tmp]
    if b >= 4:
        if width == -1:
            width = tmp
        if height == -1:
            height = tmp
    elif b >= 2:
        if width == -1:
            width = tmp
            b = 0
        if height == -1 and b != 0:
            height = tmp
    else:
        pass
    if width != -1 and height != -1:
        print(width*height)
        sys.exit()
print(0)
