# -*- coding:utf-8 -*-
N, M = map(int, input().split())
if M > 0:
    if N*2 <= M:
        print((N+M//2)//2)
    else:
        print(M//2)
else:
    print(0)
