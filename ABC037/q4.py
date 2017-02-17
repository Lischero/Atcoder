# -*- coding:utf-8 -*-
def check(y,x):
    global H, W, surplus, a
    sample = 1
    if surplus[y][x] > 0:
        return surplus[y][x]
    if y - 1 >= 0 and a[y][x] < a[y-1][x]:
        sample += check(y-1,x)
    if y + 1 < H and a[y][x] < a[y+1][x]:
        sample += check(y+1,x)
    if x - 1 >= 0 and a[y][x] < a[y][x-1]:
        sample += check(y,x-1)
    if x + 1 < W and a[y][x] < a[y][x+1]:
        sample + check(y,x+1)
    surplus[y][x] = sample % 10**9+7
    return surplus[y][x]

H,W = map(int, input().split())
a = [list(map, input().split()) for tmp in range(H)]
surplus = [[0 for tmp in range(W)] for tmp2 in range(H)]
ans = 0
for y in range(W):
    for x in range(H):
         check(y,x)


print(ans)
