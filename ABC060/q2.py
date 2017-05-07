# -*- coding:utf-8 -*-
import sys
A, B, C = map(int, input().split())
for tmp in range(1, B+1):
    if A*tmp%B == C:
        print("YES")
        sys.exit()
    else:
        pass
print("NO")
