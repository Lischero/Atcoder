# -*- coding:utf-8 -*-
s = list(input())
factor = [2,0,1,8]
for index in range(4):
    s[index] = str(factor[index])
print(''.join(s))
