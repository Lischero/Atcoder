# -*- coding:utf-8 -*-
N = int(input())
factor = 2025
a = factor - N
ans = []
for tmp in range(1,10):
    for tmp2 in range(1,10):
        if tmp*tmp2 == a:
            ans.append((tmp, tmp2))
        else:
            pass
ans.sort()
for tmp in range(len(ans)):
    print(str(ans[tmp][0])+" x "+str(ans[tmp][1]))
