# -*- coding:utf-8 -*-
n, l = map(int, input().split())
s = [ input() for tmp in range(n) ]
s.sort()
print(''.join(s))
