# -*- coding:utf-8 -*-
ans = 0
for tmp in range(12):
    S = input()
    if S.count('r') >= 1:
        ans += 1
    else:
        pass
print(ans)
