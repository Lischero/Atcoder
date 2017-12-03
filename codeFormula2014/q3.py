# -*- coding:utf-8 -*-
import re
s = input()
ans_list = list(set(re.findall(r'@[a-z]+', s)))
ans = [ src.replace("@","") for src in ans_list ]
ans.sort()
if len(ans) != 0:
    for tmp in ans:
        print(tmp)
else:
    print('')
