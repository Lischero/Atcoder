# -*- coding:utf-8 -*-
l,x,y,s,d = map(int, input().split())
if d >= s:
    rightDistance = d-s
else:
    rightDistance = d+l-s
leftDistance = l - rightDistance

if x < y:
    ans = min(leftDistance/(y-x), rightDistance/(y+x))
else:
    ans = rightDistance/(x+y)

print(ans)

