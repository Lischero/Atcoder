# -*- coding:utf-8 -*-
#memo:a^p-1 mod p = 1
#memo:a^p-2 mod p = a^-1
import math
W, H = map(int, input().split())
mod = (10**9)+7
#ans = math.factorial(W+H-2) // (math.factorial(W-1) * math.factorial(H-1))
a = math.factorial(W+H-2) % mod
b = pow((math.factorial(W-1) * math.factorial(H-1)) % mod, mod-2, mod)
print((a*b)%mod)

