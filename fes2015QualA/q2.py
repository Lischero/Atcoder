# -*- coding:utf-8 -*-
n = int(input())
a = list(map(int, input().split()))
ans = 0
for tmp in a:
    ans = tmp+2*ans
print(ans)
