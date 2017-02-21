# -*- coding:utf-8 -*-
import math
W, H = map(int, input().split())
#l = [[0 for x in range(W)] for y in range(H)]
ans = math.factorial(W+H-2) // (math.factorial(W-1) * math.factorial(H-1))
print(ans%((10**9)+7))

