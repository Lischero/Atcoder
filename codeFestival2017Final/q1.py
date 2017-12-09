# -*- coding:utf-8 -*-
import re
s = input()
factor = re.findall(r'^A{0,1}KIHA{0,1}BA{0,1}RA{0,1}$', s)
if len(factor) > 0:
    print("YES")
else:
    print("NO")
