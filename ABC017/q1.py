# -*- coding:utf-8 -*-
S, E = ([], [])
for tmp in range(3):
    s, e = map(int, input().split())
    S.append(s)
    E.append(e*0.1)
print(int(S[0]*E[0]+S[1]*E[1]+S[2]*E[2]))
