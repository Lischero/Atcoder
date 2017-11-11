# -*- coding:utf-8 -*-
N = int(input())
a = [ int(input()) for _ in range(2**N) ]
while len(a) != 1:
    b = []
    for tmp in range(0,len(a)-1,2):
        if a[tmp] > a[tmp+1]:
            b.append(a[tmp]-a[tmp+1])
        elif a[tmp] == a[tmp+1]:
            b.append(a[tmp])
        else:
            b.append(a[tmp+1]-a[tmp])
    a = b
print(a[0])
