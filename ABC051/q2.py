# -*- coding:utf-8 -*-
K,S = map(int, input().split())
ans = 0

"""
for x in range (0, K+1):
    for y in range (0, K+1):
        for z in range (0, K+1):
            if S == x+y+z:
                ans += 1
"""

for x in range (0, K+1):
    for y in range (0, K+1):
        if 0 <= S-x-y and K >= S-x-y:
            ans += 1

print(ans)
