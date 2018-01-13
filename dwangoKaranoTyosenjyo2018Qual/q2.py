# -*- coding:utf-8 -*-
import re
s = input()
a = []
while len(re.findall('25', s)) > 0:
    a.append(''.join(re.findall('25', s)))
    s=re.sub('25','', s)

if len(s) != 0:
    print(-1)
else:
    print(len(a))
