# -*- coding:utf-8 -*-
import sys
n, y = map(int, input().split())
for a in range(n+1):
    for b in range(n+1-a):
        if 5000*a+9000*b == 10000*n-y and n-a-b >= 0:
            print(str(n-a-b)+' '+str(a)+' '+str(b))
            sys.exit()
        else:
            pass
'''
for a in range(n+1):
    for b in range(n-a+1):
        for c in range(n-a-b+1):
            if 10000*a+5000*b+1000*c == y:
                print(str(a)+' '+str(b)+' '+str(c))
                sys.exit()
            else:
                pass
'''
print("-1 -1 -1")
