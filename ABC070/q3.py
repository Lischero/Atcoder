# -*- coding:utf-8 -*-
def euc(a,b):
    if b == 0:
        return a
    else:
        return euc(b, a%b)

N = int(input())
T = [ int(input()) for tmp in range(N) ]
if len(T) > 1:
    a = T.pop()
    b = T.pop()
    lcm = a*b//euc(a,b)
    for tmp in T:
        lcm = tmp*lcm//euc(tmp,lcm)
    print(lcm)
else:
    print(T.pop())
