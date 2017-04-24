# -*- coding:utf-8 -*-
import re
s = input()
l = re.findall(r"((.)\2*)",s)
ans = []
for tmp in range(len(l)):
    ans.append(l[tmp][1])
    ans.append(str(len(l[tmp][0])))
ans = ''.join(ans)
print(ans)

