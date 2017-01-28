# -*- coding: utf-8 -*-
import re
s = input()
ans = re.findall(r"A[A-Z]+Z", s)
print(len(ans[0]))
