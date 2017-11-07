# -*- coding:utf-8 -*-
import sys
n = int(input())
h = list(map(int, input().split()))
x = int(input())
flag = True
if x < h[0]:
    print(1)
    sys.exit()
else:
    for tmp in range(n-1):
        if h[tmp] < x and x < h[tmp+1]:
            print(tmp+2)
            flag = False
            break
    else:
        if flag:
            print(n+1)
        else:
            pass
