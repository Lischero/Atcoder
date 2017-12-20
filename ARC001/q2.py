# -*- coding:utf-8 -*-
import sys
a, b = map(int, input().split())
c = [(a, 0)]
if a == b:
    print(0)
    sys.exit()
else:
    ans = 0
    while True:
        tmp = c.pop(0)
        if tmp[0]+10 == b or tmp[0]-10 == b or tmp[0]+5 == b or tmp[0]-5 == b or tmp[0]+1 == b or tmp[0]-1 == b:
            ans = tmp[1]+1
            break
        c.append((tmp[0]+10,tmp[1]+1))
        c.append((tmp[0]-10,tmp[1]+1))
        c.append((tmp[0]+5,tmp[1]+1))
        c.append((tmp[0]-5,tmp[1]+1))
        c.append((tmp[0]+1,tmp[1]+1))
        c.append((tmp[0]-1,tmp[1]+1))
    print(ans)
