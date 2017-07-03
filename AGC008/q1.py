# -*- coding:utf-8 -*-
import sys
x, y = map(int, input().split())
factor = abs(abs(x)-abs(y))
a = [ x+factor, factor-x, (x+factor)*(-1), (factor-x)*(-1) ]
b = [ factor, factor+1, factor+1, factor+2 ]
for index,tmp in enumerate(a):
    if tmp == y:
        print(b[index])
        sys.exit()
