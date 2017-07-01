# -*- coding:utf-8 -*-
from collections import deque
def odd(num):
    return True if num%2!=0 else False
n = int(input())
a = list(input().split())
b = deque()
for tmp in range(len(a)):
    if odd(n) == odd(tmp+1):
        b.appendleft(a[tmp])
    else:
        b.append(a[tmp])
print(' '.join(b))
'''
for tmp in range(1,len(a)):
    a[0:tmp+1] = reversed(a[0:tmp+1])
a = map(str,a)
print(" ".join(a))
'''
