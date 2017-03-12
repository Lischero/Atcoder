# -*- coding:utf-8 -*-
ABC = []
for tmp in range(3):
    ABC.append(int(input()))
S = sorted(ABC)
S.reverse()
for tmp in range(3):
    for tmp2 in range(3):
        if ABC[tmp] == S[tmp2]:
            print(tmp2+1)

