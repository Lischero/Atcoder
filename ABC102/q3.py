# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    factors = [ factor-k for factor,k in zip(a, range(1,n+1)) ]
    factors.sort()
    index = (n//2)
    ans = sum([ abs(factor-factors[index]) for factor in factors ])
    print(ans)
