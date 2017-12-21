# -*- coding:utf-8 -*-
n = int(input())
s = [ ''.join(reversed(list(input()))) for _ in range(n) ]
s.sort()
for tmp in range(n):
    print(''.join(reversed(list(s[tmp]))))
