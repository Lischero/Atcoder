# -*- coding:utf-8 -*-
N, M = map(int, input().split())
list_a, list_b, ans = ( [], [], [] )
num = [ tmp for tmp in range(1,N+1) ]
for tmp in range(M):
    a, b = map(int, input().split())
    list_a.append(a)
    list_b.append(b)

for tmp in range(len(num)):
    x = list_a.count(num[tmp])
    y = list_b.count(num[tmp])
    ans.append(x+y)

for tmp in range(len(ans)):
    print(ans[tmp])
