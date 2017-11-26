# -*- coding: utf-8 -*-
def square(cardinal, mod_num, num):
    if num == 0:
        return 1

    k = num-1 if num%2 else num//2
    if num%2:
        ans = square(cardinal, mod_num, k)*cardinal
    else:
        ans = square(cardinal, mod_num, k)**2

    return ans%mod_num

n,m,p = map(int, input().split())
print(square(n, m, p))
