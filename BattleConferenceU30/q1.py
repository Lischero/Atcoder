# -*- coding:utf-8 -*-
n,k = map(int, input().split())
a = list(map(int, input().split()))
place = 0
for tmp in range(k):
    if place+a[tmp] > n:
        place = n-(place+a[tmp]-n)
    else:
        place += a[tmp]
    if place == n:
        break
print(place)
