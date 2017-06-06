# -*- coding:utf-8 -*-
S = list(input().split('+'))
ans = 0
for tmp in S:
    if '*' in list(tmp):
        if '0' not in list(tmp):
            ans += 1
    else:
        if tmp != '0':
            ans += 1
print(ans)
