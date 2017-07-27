# -*- coding:utf-8 -*-
import re
S = input()
a = re.search('[a-z]*i[a-z]*c[a-z]*t[a-z]*', S, re.I)
if a:
    print("YES")
else:
    print("NO")
