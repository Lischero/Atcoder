# -*- coding:utf-8 -*-
n = int(input())
S = []
ans = []
for factor in range(n):
    S.append(input())
for tmp in "abcdefghijklmnopqrstuvwxyz":
    l = []
    for tmp2 in range(n):
        l.append(S[tmp2].count(tmp))
    factor = min(l)
    for tmp3 in range(factor):
        ans.append(tmp)
s = ''.join(ans)
print(s)
