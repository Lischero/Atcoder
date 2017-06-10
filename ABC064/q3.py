# -*- coding:utf-8 -*-
N = int(input())
a = list(map(int, input().split()))
rate = [ 0 for tmp in range(9) ]
factor = 0
empty = 0
for tmp in range(N):
    if 1 <= a[tmp] and  a[tmp] <= 399:
        rate[0] += 1
    elif 400 <= a[tmp] and a[tmp] <= 799:
        rate[1] += 1
    elif 800 <= a[tmp] and a[tmp] <= 1199:
        rate[2] += 1
    elif 1200 <= a[tmp] and a[tmp] <= 1599:
        rate[3] += 1
    elif 1600 <= a[tmp] and a[tmp] <= 1999:
        rate[4] += 1
    elif 2000 <= a[tmp] and a[tmp]<= 2399:
        rate[5] += 1
    elif 2400 <= a[tmp] and a[tmp] <= 2799:
        rate[6] += 1
    elif 2800 <= a[tmp] and a[tmp] <= 3199:
        rate[7] += 1
    else:
        rate[8] += 1
for tmp in range(len(rate)-1):
    if rate[tmp] > 0:
        factor += 1
    else:
        empty += 1
if rate[8] > 0:
    if factor == 0:
        print("1 "+str(rate[8]))
    else:
        print(str(factor)+' '+str(factor+rate[8]))
else:
    print(str(factor)+' '+str(factor)) 

