# -*- coding:utf-8 -*-
num = list(map(int, input().split()))
if num[0]*num[1] >= num[2]*num[3]:
    print(num[0]*num[1])
else:
    print(num[2]*num[3])
