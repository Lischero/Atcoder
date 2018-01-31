# -*- coding:utf-8 -*-
n, l ,r = map(int, input().split())
a = list(map(int, input().split()))
ans = []
for tmp in a:
    if tmp <= l:
        ans.append(str(l))
    elif tmp >= r:
        ans.append(str(r))
    else:
        ans.append(str(tmp))
print(' '.join(ans))
