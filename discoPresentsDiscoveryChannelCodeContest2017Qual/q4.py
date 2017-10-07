# -*- coding:utf-8 -*-
h,w = map(int, input().split())
a, b = map(int, input().split())
m = [ list(input()) for y in range(h) ]
d = {}
for y in range(h/2):
    for x in range(w/2):
        if m[y][x] != m[y][w-1-x]:
            if m[y][x] == 'S':
                d[(y,x)] = 1
            else:
                d[(y, w-1-x)] = 1
        else:
            pass
for x in range(w/2):
    for y in range(h/2):
        if m[y



'''
H = [ tmp for tmp in range(h) ]
W = [ tmp for tmp in range(w) ]
d = []
e = []
ans = 0
flag = True
while len(H) > 0:
    d.append((H.pop(0), H.pop()))
while len(W) > 0:
    e.append((W.pop(0), W.pop()))
for tmp in d:
    for x in range(w):
        if m[tmp[0]][x] != m[tmp[1]][x]:
            if m[tmp[0]][x] == 'S':
                m[tmp[0]][x] = '.'
            else:
                m[tmp[1]][x] = '.'
        else:
            flag = False

if flag:
    pass
else:
    ans += a

for tmp in e:
    for y in range(h):
        if m[y][tmp[0]] != m[y][tmp[1]]:
            if m[y][tmp[0]] == 'S':
                m[y][tmp[0]] = '.'
            else:
                m[y][tmp[1]] = '.'

if flag:
    ans += a+b
else:
    ans += b

print(ans)
'''
