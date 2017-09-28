# -*- coding:utf-8 -*-
T = int(input())
rank = [ tmp for tmp in range(1, 200+1) ]
num = 0
ans = 0
for tmp in range(1,11):
    if tmp%2 != 0:
        a = list(rank[num:num+20])
    else:
        a = list(reversed(rank[num:num+20]))
    ans += a[T-1]
    num += 20
print(ans)
