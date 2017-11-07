# -*- coding:utf-8 -*-
import itertools
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = int(input())
ans = []
for tmp in itertools.product(a,b):
    if c in tmp:
        if tmp[0] != c:
            ans.append(tmp[0])
        elif tmp[1] != c:
            ans.append(tmp[1])
        else:
            ans.append(tmp[0])
    else:
        pass
ans = list(set(ans))
ans.sort()
print(len(ans))
for tmp in ans:
    print(tmp)
