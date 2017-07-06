# -*- coding:utf-8 -*-
N = int(input())
m = list(map(int, input().split()))
a = [ tmp for tmp in m if tmp < 80 ]
ans = 0
for tmp in a:
    ans += 80 - tmp
print(ans)
