# -*- coding: utf-8 -*-
import math
def isPrime(n):
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

table = []
N = int(input())
for tmp in range(2,N+1):
    if isPrime(tmp):
        table.append(tmp)

table2 = [0 for i in range(len(table))]

factorial = 1
for num in range(2,N+1):
    factorial *= num
    factor = 0
    for i in table:
        while num >= i and num%i == 0:
            table2[factor] += 1
            num /= i
        factor += 1

ans = 1
for tmp2 in table2:
    ans *= tmp2+1

#for num in range (1, factorial+1):
#    if factorial % num == 0:
#       ans += 1 

ans = ans % ((10 ** 9) + 7)
print(ans)
