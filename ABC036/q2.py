# -*- coding:utf-8 -*-
N = int(input())
s = [ list(input()) for tmp in range(N)]
x, y = (0,N-1)
while x < N:
    ans = []
    y = N-1
    while y >= 0:
        ans.append(s[y][x])
        y -= 1
    print(''.join(ans))
    x += 1
