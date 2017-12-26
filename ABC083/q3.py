# -*- coding:utf-8 -*-
x, y = map(int, input().split())
ans = []
index = 0
for tmp in range(x, y+1):
    factor = (2**index)*x
    if x <= factor and factor <= y:
        ans.append(factor)
        index += 1
    else:
        break
print(len(ans))
