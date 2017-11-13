# -*- coding:utf-8 -*-
x,y,z = map(int, input().split())
ans = 0
while (y+z)*ans+z <= x:
    ans += 1
print(ans-1)
