# -*- coding:utf-8 -*-
import math
def isPrime(num):
    if num == 2:
        return True
    if num < 2 or num%2 == 0:
        return False
    for tmp in range(3, math.floor(math.sqrt(num))+1, 2):
        if num%tmp == 0:
            return False
    return True

N = int(input())
if isPrime(N):
    print("YES")
else:
    print("NO")
