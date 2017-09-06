# -*- coding:utf-8 -*-
N  = int(input())
a = list(map(int, input().split()))
b = [ 0 for _ in range((10**5)+1) ]
ans = float('-inf')
for tmp in a:
    if tmp != 0:
        b[tmp-1] += 1
    b[tmp] += 1
    b[tmp+1] += 1
for tmp in b:
    ans = max(ans, tmp)
print(ans)
