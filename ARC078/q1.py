# -*- coding:utf-8 -*-
N = int(input())
a = list(map(int, input().split()))
b = sum(a)
c = 0
minimum = float('inf')
for tmp in range(0,N-1):
    c += a[tmp]    
    d = abs(c-(b-c))
    minimum = min(minimum, d)
print(minimum)
