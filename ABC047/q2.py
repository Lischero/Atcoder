# -*- coding:utf-8 -*-
import sys
W, H, N = map(int,input().split())
xya = []
W1, W2, H3, H4 = (0, W, 0, H)

for tmp in range(0, N):
    xya.append(list(map(int,input().split())))

for y in range(0, N):

    if xya[y][2] == 1:
        W1 = max(W1, xya[y][0])
    elif xya[y][2] == 2:
        W2 = min(W2, xya[y][0])
    elif xya[y][2] == 3:
        H3 = max(H3, xya[y][1])
    else:
        H4 = min(H4, xya[y][1])

    if W1 >= W2 or H3 >= H4:
        print(0)
        sys.exit()

print((W2 - W1)*(H4 - H3))

