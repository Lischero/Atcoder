# -*- coding:utf-8 -*-
def search(y,x):
    global flag, h, w, c, a
    if y >= h or y < 0 or x >= w or x < 0:
        return
    if c[y][x] == '#':
        return
    if a[y][x]:
        return
    a[y][x] = True
    if c[y][x] == 'g':
        flag = True
    else:
        pass
    search(y-1,x)
    search(y+1,x)
    search(y,x-1)
    search(y,x+1)

flag = False
h, w = map(int, input().split())
c = [ list(input()) for _ in range(h) ]
a = [ [ False for _ in range(w) ] for _ in range(h) ]
for tmp in range(h):
    if 's' in c[tmp]:
        b = c[tmp].index('s')
        d = tmp
        search(d,b)
        break
    else:
        pass
if flag:
    print("Yes")
else:
    print("No")
