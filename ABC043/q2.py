# -*- coding:utf-8 -*-
s = list(input())
ans = []
for tmp in range (len(s)):
    if s[tmp] == '0' or s[tmp] == '1':
        ans.append(s[tmp])
    elif len(ans) > 0:
        ans.pop()
print(''.join(ans))
