# -*- coding:utf-8 -*-
n = int(input())
a = list(map(int, input().split()))
ans = []
for tmp in range(len(a)):
    b = a[tmp]
    c = 0
    while True:
        if b%2 != 0:
            ans.append(c)
            break
        else:
            b /= 2
            c += 1
print(min(ans))

