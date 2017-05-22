# -*- coding:utf-8 -*-
H, W = map(int, input().split())
a = []
b = []
for tmp in range(H):
    a.append(list(input()))
add = [ '#' for tmp in range(W+2) ]
b.append(add)
for tmp in range(H):
    c = ['#'] + a[tmp] + ['#']
    b.append(c)
b.append(add)
for tmp in range(H+2):
    print(''.join(b[tmp]))
