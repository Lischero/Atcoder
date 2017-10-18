# -*- coding:utf-8 -*-
N = int(input())
ans = 0
before = 1
factor = 0
for tmp in range(1,N+1):
    ans += tmp
    factor = tmp
    if before < N and N <= ans:
        break
    before = ans
difference = ans - N
if difference != 0:
    for tmp in range(1,factor+1):
        if difference != tmp:
            print(tmp)
        else:
            pass
else:
    for tmp in range(1,factor+1):
        print(tmp)
