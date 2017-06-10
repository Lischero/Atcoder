# -*- coding:utf-8 -*-
N = int(input())
a = list(reversed(sorted(list(set(list(map(int, input().split())))))))
ans = 0
for tmp in range(len(a)-1):
    ans += a[tmp] - a[tmp+1]
print(ans)
