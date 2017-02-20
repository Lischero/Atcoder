# -*- coding:utf-8 -*-
S = list(input())
T = int(input())
x, y = (0,0)
count = 0
for tmp in S:
    if tmp == 'U':
        y += 1
    elif tmp == 'D':
        y -= 1
    elif tmp == 'L':
        x -= 1
    elif tmp == 'R':
        x += 1
    else:
        count += 1

if T == 1:
    print(abs(x)+abs(y)+count)
else:
    print(max(len(S)%2, abs(x)+abs(y)-count))

