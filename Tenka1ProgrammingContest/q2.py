# -*- coding:utf-8 -*-
n = int(input())
l = [ tuple(map(int, input().split())) for _ in range(n) ]
result = sorted(l, key= lambda tmp:tmp[0], reverse = True)
print(result[0][0]+result[0][1])
