# -*- coding:utf-8 -*-
import math
import sys
a, b, x = map(int,input().split())
"""
if a == b:
    if a%x == 0:
        print(1)
    else:
        print(0)
    sys.exit()
"""
if a%x == 0:
    ans= b // x - a // x + 1
else:    
    ans= b // x - a // x

print(ans)

"""
for tmp in range (a, b+1):
    if tmp % x == 0:
        ans += 1
"""
