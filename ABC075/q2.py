# -*- coding:utf-8 -*-
import itertools
H, W = map(int, input().split())
s = [ list(input()) for h in range(H) ]
for y in range(H):
    for x in range(W):
        if s[y][x] == '#':
            continue
        y1 = [ tmp for tmp in [ y-1, y, y+1 ] if tmp >= 0 and tmp < H ]
        x1 = [ tmp for tmp in [ x-1, x, x+1 ] if tmp >= 0 and tmp < W ]
        bomb = 0
        for pair in itertools.product(y1,x1):
            if pair[0] == y and pair[1] == x:
                continue
            if s[pair[0]][pair[1]] == '#':
                bomb += 1
            else:
                pass
        s[y][x] = str(bomb)
for y in range(H):
    print(''.join(s[y]))
