# -*- coding:utf-8 -*-
import sys
T, N = (int(input()), int(input()))
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
soldout = 0
num = 0
for tmp in range(M):
    if soldout == N and tmp != M-1:
        print("no")
        sys.exit()
    for tmp2 in range(num,N):
        if B[tmp] <= A[tmp2]+T and B[tmp] - A[tmp] >= 0:
            soldout += 1
            num = tmp2+1
            break
        else:
            continue
    if soldout == N and tmp == M-1:
        print("yes")
        sys.exit()
if soldout != M: 
    print("no")
else:
    print("yes")
