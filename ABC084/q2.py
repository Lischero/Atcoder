# -*- coding:utf-8 -*-
from collections import Counter
a, b = map(int, input().split())
s = list(input())
c = Counter(s)
if len(s) == a+b+1:
    if c['-'] == 1 and s[a] == '-':
        print("Yes")
    else:
        print("No")
else:
    print("No")
