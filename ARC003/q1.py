# -*- coding:utf-8 -*-
N = int(input())
r = list(input())
ans = []
for tmp in [('A',4), ('B',3), ('C',2), ('D',1), ('F',0)]:
    a = len([ tmp2 for tmp2 in r if tmp2 == tmp[0] ])
    ans.append(a*tmp[1])
print(sum(ans)/N)
