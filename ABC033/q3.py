# -*- coding:utf-8 -*-
import re
S = input()
num_index = [ tmp for tmp in range(0, len(S), 2) ]
ans = 0
iterator = re.finditer("[\d\*]+\d",S)
for tmp in iterator:
    start_end = tmp.span()
    if '0' not in list(S[start_end[0]:start_end[1]]):
        ans += 1
    for tmp2 in range(start_end[0], start_end[1], 2):
        num_index.pop(num_index.index(tmp2))
for tmp in num_index:
    if S[tmp] != '0':
        ans += 1
print(ans)

