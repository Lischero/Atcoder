# -*- coding:utf-8 -*-
def isPrime(n):
    a = 2
    while n >= a*a:
        if n%a == 0:
            return False
        a += 1
    return True

n = int(input())
l = [ tmp for tmp in range(1,n+1) if isPrime(tmp) and tmp%2 == 0 ]
print(len(l))
