# -*- coding:utf-8 -*-
import sys
n = int(input())
l = [ tmp for tmp in range(1,200, 20)]
d = { tmp:tmp for tmp in range(1,21) }
d2 = { 21-tmp:tmp for tmp in reversed(range(1,21)) }
for index in range(len(l)):
    if n <= l[index]+19 and n >= l[index]:
        if index%2:
            print(d2[n-20*index])
            sys.exit()
        else:
            print(d[n-20*index])
            sys.exit()
    else:
        pass
