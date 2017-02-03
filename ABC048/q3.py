# -*- coding:utf-8 -*-
import math
N, x = map(int,input().split())
a = list(map(int, input().split()))
ans = 0
for tmp in range (0,N-1):
    if a[tmp] + a[tmp+1] <= x:
        continue
    else:
        tmp2 = (a[tmp]+a[tmp+1]) - x #差分を出す。
        if a[tmp+1] - tmp2 >= 0:
            a[tmp+1] -= tmp2
            ans += tmp2
        else: #足りない場合
            ans += tmp2
            a[tmp] += a[tmp+1] - tmp2 #足りない部分はa[tmp]から引く。
            tmp2 += a[tmp+1] - tmp2
            a[tmp+1] -= tmp2
print(ans)

