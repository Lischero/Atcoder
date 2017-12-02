# -*- coding:utf-8 -*-
n = int(input())
if n%2 == 0:
    even = n//2
    odd = n//2
else:
    even = (n-1)//2
    odd = ((n-1)//2)+1
print(3*odd-2*even)
