# -*- coding:utf-8 -*-
import re
S = input()
b = re.findall('B+',S)
w = re.findall('W+',S)
ans = len(b)+len(w)-1
print(ans)
