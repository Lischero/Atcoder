# -*- coding:utf-8 -*-
ans_list = []
while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    x = list(map(int, input().split()))
    x.sort()
    ans = 0
    for tmp in range(k):
        ans += x[tmp]
    ans_list.append(ans)

for tmp in range(len(ans_list)):
    print(ans_list[tmp])
