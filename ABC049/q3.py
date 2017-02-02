# -*- coding:utf-8 -*-
import re
S = input()
a = re.sub(r'eraser', '', S)
b = re.sub(r'erase', '', a)
c = re.sub(r'dreamer', '', b)
d = re.sub(r'dream', '', c)
if len(d) == 0:
    print("YES")
else:
    print("NO")
