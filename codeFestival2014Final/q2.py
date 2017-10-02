# -*- coding:utf-8 -*-
S = list(map(int, list(input())))
ans = S.pop(0)
for tmp in range(len(S)):
    if tmp%2 == 0:
        ans -= S[tmp]
    else:
        ans += S[tmp]
print(ans)
