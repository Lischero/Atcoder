# -*- coding:utf-8 -*-
N, K = map(int, input().split())
D = list(map(int, input().split()))
for tmp in range(N, 10*N+1):
    flag = True
    factor = list(map(int, str(tmp)))
    for num in D:
        if num in factor:
            flag = False
            break
    if flag:
        print(tmp)
        break
