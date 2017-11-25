# -*- coding:utf-8 -*-
a = list(input())
b = int(input())
length = len(a)
c = { tmp:a.pop(0) for tmp in range(1,length) }
c[0] = a.pop()
ans = b%length
print(c[ans])
