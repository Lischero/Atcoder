# -*- coding:utf-8 -*-
n = int(input())
d = [ int(input()) for _ in range(n) ]
ans = sorted(list(set(d)))
print(len(ans))
