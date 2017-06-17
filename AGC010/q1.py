# -*- coding:utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
oddNum = [ tmp for tmp in A if tmp%2 != 0 ]
if len(oddNum)%2 == 0:
    print("YES")
else:
    print("NO")
