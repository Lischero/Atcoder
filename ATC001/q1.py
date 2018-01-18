# -*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(1000000)
def search(y,x):
    global flag, h, w, c, a
    a[y][x] = True
    if c[y][x] == 'g':
        flag = True
        return
    if y-1 >= 0 and not a[y-1][x]:
        search(y-1,x)
    if y+1 < h and not a[y+1][x]:
        search(y+1,x)
    if x-1 >= 0 and not a[y][x-1]:
        search(y,x-1)
    if x+1 < w and not a[y][x+1]:
        search(y,x+1)



if __name__ == "__main__":
    flag = False
    h, w = map(int, input().split())
    c = [ list(input()) for _ in range(h) ]
    a = [ [ c[y][x] == '#' for x in range(w) ] for y in range(h) ]
    for tmp in range(h):
        if 's' in c[tmp]:
            b = c[tmp].index('s')
            d = tmp
            search(d,b)
            break
    if flag:
        print("Yes")
    else:
        print("No")
