# -*- coding:utf-8 -*-
s = list(input())
a = [ s[tmp] for tmp in range(len(s)) if tmp%2 == 0 ]
print(''.join(a))
