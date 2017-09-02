# -*- coding:utf-8 -*-
N, M = map(int, input().split())
template = [ tmp for tmp in range(1,N+1) ]
a = []
for tmp in range(M):
    b = int(input())
    a.append(b)
a.reverse()
a = sorted(set(a), key = a.index)
for tmp in a:
    template.pop(template.index(tmp))
template = a+template
for tmp in template:
    print(tmp)

