# -*- coding:utf-8 -*-
import re
S = input()
a = re.search("\d+", S)
print(a.group())
