# -*- coding:utf-8 -*-
N = int(input())
a = list(map(int,input().split()))
l = list(set(a))
s = []
ans = 0
for tmp in l:
    s.append(a.count(tmp))
num = l[s.index(max(s))] #最も多い割合を占める数。
for tmp in range(len(a)):
    ans += (tmp - num)**2
print(ans)
