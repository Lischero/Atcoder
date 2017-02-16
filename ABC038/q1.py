# -*- coding:utf-8 -*-
import re
S = input()
if re.search(r"T$", S):
    print("YES")
else:
    print("NO")
